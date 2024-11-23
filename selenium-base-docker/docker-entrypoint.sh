#!/bin/bash
set -e
echo "***** SeleniumBase Docker Machine *****"

# Check if config.yaml is mounted; if so, copy it into /script/
if [ -f "/mounted/config.yaml" ]; then
    echo "Copying config.yaml to /script/"
    cp /mounted/config.yaml /script/config.yaml
else 
    echo "No config.yaml found in /mounted"
fi

# Run the provided command or fall back to default CMD
exec "$@"