@echo off

echo 📦 Installing Python dependencies...
pip install -r ..\requirements.txt

echo 📁 Copying .env.example to .env...
copy ..\env.example ..\env > nul

echo ✅ Setup complete!
echo 🛠  Please edit the .env file to add your GitHub token and settings.

pause
