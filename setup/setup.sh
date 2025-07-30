#!/bin/bash

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Copying .env.example to .env"
cp .env.example .env
echo "Edit the .env file to add your GitHub information."

echo "Installation complete!"
