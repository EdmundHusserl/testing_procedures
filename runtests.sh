source $HOME/.bash_profile
echo "Running tests..."
pytest ./tests/unittest.py
echo "Compiling..."
python3 -m PyInstaller -F ./exec.py
