#!/bin/bash
echo "Syncing host /output directory with S3... This may take a while depending on your network speed"
aws s3 sync  --exclude "*" --include "*.png" --include "*.json" /output s3://renderbus