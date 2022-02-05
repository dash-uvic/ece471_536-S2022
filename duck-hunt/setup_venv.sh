#!/bin/bash

if [ $1 == "-h" ]; then
    echo "USAGE: bash setup_venv.sh <name of environment>"
    exit 0
fi

env_name="$1"
py_ver="python3.7"

if [ -z "$env_name" ]; then
    echo "Usage: need virtualenv name"
    exit 1
fi

$py_ver -m pip install virtualenv
$py_ver -m virtualenv $env_name
source $env_name/bin/activate

pip install --upgrade pip

if [ -e requirements.txt ]; then
    pip install -r requirements.txt
fi

echo ""
echo "To activate your $env_name virtual environment: source $env_name/bin/activate"
echo "To deactivate: deactivate"
