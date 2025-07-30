@echo off

echo Installing Python dependencies...
pip install -r requirements.txt

echo Copying .env.example to .env...
copy .env.example .env

echo Open the .env file in a text editor and fill in your information.

echo Installation complete!
pause
