source $HOME/.bash_profile
echo "Running tests..."
python3 -m pip install -r ./requirements.txt
python3 -m pytest ./tests/unittest.py
echo "Compiling..."
python3 -m PyInstaller -F ./exec.py
