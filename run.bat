@echo off

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed.
    echo Please install the latest version of Python to continue.
    pause
    exit /B 1
)

REM Install the required packages and log the output
echo Installing required packages...
pip install -r requirements.txt

cd ./src

REM Run the main GUI application and log the output
echo Running the main GUI application...
python ./mainGUI.py
