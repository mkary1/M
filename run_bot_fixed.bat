@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found: .venv
    echo Create it and install requirements before running this file.
    pause
    exit /b 1
)

if not exist "main.py" (
    echo ERROR: main.py was not found in this folder.
    pause
    exit /b 1
)

echo Starting Qureo bot...
".venv\Scripts\python.exe" "main.py"
set "EXIT_CODE=%ERRORLEVEL%"
echo.
echo Bot process exited with code %EXIT_CODE%.
pause
exit /b %EXIT_CODE%
