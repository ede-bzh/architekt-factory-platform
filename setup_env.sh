#!/bin/bash
# Setup environment for Software Factory
# Source this file before running factory commands

# Add parent directory to PYTHONPATH so we can import _FACTORY_CORE
export PYTHONPATH="/Users/sylvain/_ARCHITEKT_FACTORY:$PYTHONPATH"

echo "✅ Environment configured"
echo "PYTHONPATH: $PYTHONPATH"

export SF_LOCAL=1
