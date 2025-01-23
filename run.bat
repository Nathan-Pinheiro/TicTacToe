@echo off

:: Install the required packages and log the output
echo Installing required packages...
pip install -r requirements.txt

cd ./src

:: Run the main GUI application and log the output
echo Running the main GUI application...
python ./mainGUI.py
