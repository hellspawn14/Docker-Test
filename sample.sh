# Initiate venv 
python3 -m venv /usr/local/Script/venv 

# Activate venv 
. /usr/local/Script/venv/bin/activate

# Update pip 
python3 -m pip install --upgrade pip

# Install requirements.txt
python3 -m pip install -r /usr/local/Script/requirements.txt

# Run Script 
python3 /usr/local/Script/sample.py
