#!/bin/bash

if command -v nginx &> /dev/null; then
    echo "[INFO] Nginx is already installed"
    exit 0
fi

echo "[INFO] Installing Nginx..."
sudo apt-get update
sudo apt-get install -y nginx

if [ $? -eq 0 ]; then
    echo "[INFO] Nginx installation completed."
else
    echo "[ERROR] Failed to install Nginx."
    exit 1
fi