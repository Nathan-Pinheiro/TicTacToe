#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed."
    echo "Please install the latest version of Python to continue."
    exit 1
fi

# Install the required packages and log the output
echo "Installing required packages..."
pip install -r requirements.txt

cd ./src

# Run the main GUI application and log the output
echo "Running the main GUI application..."
python ./mainGUI.py