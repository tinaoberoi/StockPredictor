#!/bin/bash
echo "Creating a virtual env for you."
python3 -m venv env

echo -ne '#####                     (33%)\r'
sleep 1

echo "Activating virtual environment env."
source env/bin/activate
echo -ne '#############             (66%)\r'
sleep 10

echo "Installed required packages."
pip3 install -r requirements.txt
echo "Building your model."
echo -ne '#######################   (100%)\r'
echo -ne '\n'

python3 create_model.py

