#!/bin/bash
# Deploy CLI fix and module conflict fix to Azure production

set -e

AZURE_HOST="${AZURE_VM_IP:?Set AZURE_VM_IP in .env}"
AZURE_USER="appuser"
CONTAINER_NAME="deploy-platform-1"

echo "🚀 Deploying CLI fix to Azure production..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if we can reach the server
echo "📡 Checking connection to Azure VM..."
if ! curl -s -m 5 http://${AZURE_HOST}/ > /dev/null; then
    echo "❌ Cannot reach Azure VM at ${AZURE_HOST}"
    exit 1
fi
echo "✅ Azure VM is reachable"

# Test if SSH works
echo ""
echo "🔐 Testing SSH connection..."
if ssh -o ConnectTimeout=5 -o BatchMode=yes ${AZURE_USER}@${AZURE_HOST} "echo 'SSH OK'" 2>/dev/null | grep -q "SSH OK"; then
    echo "✅ SSH connection works!"
    
    echo ""
    echo "📦 Method 1: Git pull inside container (recommended)"
    echo "────────────────────────────────────────────────────"
    
    # Try to pull latest code
    ssh ${AZURE_USER}@${AZURE_HOST} << 'ENDSSH'
        echo "Entering container..."
        docker exec deploy-platform-1 bash -c "
            cd /app && 
            echo '📥 Pulling latest code...' &&
            git fetch origin &&
            git status &&
            echo '' &&
            echo '🔄 Current commit:' &&
            git log -1 --oneline &&
            echo '' &&
            read -p '⚠️  Pull latest changes? [y/N] ' -n 1 -r &&
            echo &&
            if [[ \$REPLY =~ ^[Yy]$ ]]; then
                git pull origin master &&
                echo '✅ Code updated!' &&
                echo '' &&
                echo '🔄 Restarting container...' &&
                exit 0
            else
                echo '❌ Pull cancelled'
                exit 1
            fi
        "
        
        if [ $? -eq 0 ]; then
            echo "Restarting container..."
            docker restart deploy-platform-1
            echo "✅ Container restarted"
            echo ""
            echo "⏳ Waiting 10 seconds for startup..."
            sleep 10
        fi
ENDSSH
    
else
    echo "❌ SSH connection failed"
    echo ""
    echo "📦 Method 2: Manual file upload"
    echo "────────────────────────────────────────────────────"
    echo "Since SSH doesn't work, you'll need to deploy manually:"
    echo ""
    echo "Option A: Azure Portal Web Console"
    echo "1. Go to Azure Portal → Virtual Machine → Connect → Native SSH"
    echo "2. Run:"
    echo "   docker exec -it deploy-platform-1 bash"
    echo "   cd /app"
    echo "   git pull origin master"
    echo "   exit"
    echo "   docker restart deploy-platform-1"
    echo ""
    echo "Option B: Azure CLI"
    echo "1. Install Azure CLI: https://aka.ms/azure-cli"
    echo "2. Run:"
    echo "   az vm run-command invoke -g RG-ARCHITEKT -n vm-architekt \\"
    echo "     --command-id RunShellScript \\"
    echo "     --scripts 'docker exec deploy-platform-1 bash -c \"cd /app && git pull origin master\" && docker restart deploy-platform-1'"
    echo ""
    exit 1
fi

# Verify deployment
echo ""
echo "🧪 Verifying deployment..."
echo "────────────────────────────────────────────────────"

sleep 5

echo "Testing SF commands endpoint..."
if curl -s -X POST http://${AZURE_HOST}/api/sf/execute \
    -H "Content-Type: application/json" \
    --data '{"command":"help","args":[]}' | grep -q "success.*true"; then
    echo "✅ SF commands working"
else
    echo "⚠️  SF commands not responding yet"
fi

echo ""
echo "Testing CLI endpoint..."
if curl -s -X POST http://${AZURE_HOST}/api/cli/execute \
    -H "Content-Type: application/json" \
    --data '{"command":"help","args":[]}' | grep -q "Available CLI Commands"; then
    echo "✅ CLI endpoint working"
else
    echo "⚠️  CLI endpoint not found (may need more time)"
fi

echo ""
echo "Testing platform status..."
RESULT=$(curl -s -X POST http://${AZURE_HOST}/api/sf/execute \
    -H "Content-Type: application/json" \
    --data '{"command":"platform status","args":[]}')

if echo "$RESULT" | grep -q '"success":true'; then
    echo "✅ Platform status command working"
    echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"   Agents: {d['data']['agents']}, Missions: {d['data']['missions']}, Skills: {d['data']['skills']}\")"
elif echo "$RESULT" | grep -q "not a package"; then
    echo "❌ Module conflict error still present"
    echo "   Error: $RESULT"
    echo ""
    echo "🔧 Additional fix needed for module conflict:"
    echo "   The platform/__init__.py fix needs to be deployed"
else
    echo "⚠️  Unexpected response: $RESULT"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Deployment Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Files updated:"
echo "  • platform/web/routes/cli.py"
echo "  • platform/web/routes/sf_commands.py"
echo "  • platform/__init__.py (module conflict fix)"
echo ""
echo "Test in browser:"
echo "  1. Go to: http://${AZURE_HOST}/toolbox"
echo "  2. Click CLI tab"
echo "  3. Type: platform status"
echo "  4. Should see platform stats (no 'Unknown error')"
echo ""
echo "✅ Deployment complete!"
