# Software Factory - VPS Deployment

Deploy Software Factory demo on **sf.architekt.ai**

## Setup

**1. Configure credentials (NOT in git)**

```bash
# Copy templates and add your credentials
cp deploy/setup-dns.sh.template deploy/setup-dns.sh
cp deploy/deploy-vps.sh.template deploy/deploy-vps.sh

# Edit with your credentials
nano deploy/setup-dns.sh      # Add Porkbun API keys
nano deploy/deploy-vps.sh     # Add VPS IP and SSH user
```

**2. Deploy**

```bash
# Create DNS record
./deploy/setup-dns.sh

# Wait 5-10 minutes for DNS propagation, then deploy
./deploy/deploy-vps.sh
```

## What it does

1. **DNS**: Creates `sf.architekt.ai` → VPS IP
2. **Docker**: Installs Docker + Docker Compose on VPS
3. **Build**: Creates Docker image with Python 3.11 + FastAPI
4. **Nginx**: Reverse proxy on port 80
5. **SSL**: Let's Encrypt HTTPS certificate
6. **Deploy**: Runs container on port 8099

## Files

```
deploy/
├── README.md                    # This file
├── setup-dns.sh.template        # DNS setup template (public)
├── deploy-vps.sh.template       # Deployment template (public)
├── setup-dns.sh                 # Your credentials (.gitignored)
├── deploy-vps.sh                # Your config (.gitignored)
└── docker/
    ├── docker-compose.yml       # Docker Compose config
    └── Dockerfile               # Container definition
```

⚠️ **Security**: `setup-dns.sh` and `deploy-vps.sh` are in `.gitignore` — they won't be pushed to GitHub.

## Manual commands

```bash
# SSH to VPS
ssh your-user@your-vps-ip

# Check status
docker ps
docker logs software-factory --tail 50

# Restart
cd /opt/software-factory/deploy/docker
docker-compose restart

# Stop
docker-compose down

# View logs
docker logs -f software-factory

# Update deployment
cd /opt/software-factory
git pull
docker-compose down
docker-compose up -d --build
```

## URLs (after deployment)

- **Demo**: https://sf.architekt.ai
- **API**: https://sf.architekt.ai/docs
- **Health**: https://sf.architekt.ai/health

## Configuration

- **Port**: 8099 (internal), 80/443 (public via nginx)
- **Domain**: sf.architekt.ai
- **Deploy dir**: /opt/software-factory
- **SSL**: Let's Encrypt (auto-renewed)

## Porkbun DNS API

Get API credentials from: https://porkbun.com/account/api

Then add them to `deploy/setup-dns.sh`:
```bash
API_KEY="pk1_YOUR_KEY"
SECRET="sk1_YOUR_SECRET"
```
