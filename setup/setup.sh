#!/bin/bash

echo "📦 Installing Python dependencies..."
pip install -r ../requirements.txt

echo "📁 Copying .env.example to .env"
cp ../.env.example ../.env

echo "✅ Setup complete!"
echo "🛠  Now edit the .env file to configure your GitHub credentials."
