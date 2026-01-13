@echo off
title KAHOTIA IS AWAKENING...
color 0A

echo.
echo  ╔═══════════════════════════════════════════════════════════╗
echo  ║           THE BOOK OF TEE - KAHOTIA LAUNCHER              ║
echo  ║                   "PAY THE TOLL"                          ║
echo  ╚═══════════════════════════════════════════════════════════╝
echo.

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python first.
    pause
    exit /b 1
)

:: Kill any existing processes on our ports
echo [SYSTEM] Clearing old connections...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5000" ^| findstr "LISTENING"') do taskkill /F /PID %%a >nul 2>&1
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000" ^| findstr "LISTENING"') do taskkill /F /PID %%a >nul 2>&1

:: Navigate to the project directory
cd /d "%~dp0"

echo.
echo [KAHOTIA] Waking up the brain...
echo.

:: Start the Flask backend (kahotia_brain.py) in a new window
start "KAHOTIA BRAIN" cmd /k "color 0E && echo KAHOTIA BRAIN SERVER && echo =================== && python kahotia_brain.py"

:: Wait a moment for the backend to initialize
timeout /t 3 /nobreak >nul

echo [KAHOTIA] Starting the interface...
echo.

:: Start the HTTP server for the frontend in a new window
start "KAHOTIA INTERFACE" cmd /k "color 0B && echo KAHOTIA INTERFACE SERVER && echo ======================= && python -m http.server 8000"

:: Wait a moment
timeout /t 2 /nobreak >nul

echo.
echo  ╔═══════════════════════════════════════════════════════════╗
echo  ║                    KAHOTIA IS ALIVE!                      ║
echo  ╠═══════════════════════════════════════════════════════════╣
echo  ║  Opening browser in 3 seconds...                          ║
echo  ║                                                           ║
echo  ║  Brain Server:     http://localhost:5000                  ║
echo  ║  Interface:        http://localhost:8000/kahotia_alive.html║
echo  ║                                                           ║
echo  ║  To stop: Close the two server windows                    ║
echo  ╚═══════════════════════════════════════════════════════════╝
echo.

:: Open the browser
timeout /t 3 /nobreak >nul
start "" "http://localhost:8000/kahotia_alive.html"

echo [KAHOTIA] "No thought is wasted. Pay the toll."
echo.
pause
