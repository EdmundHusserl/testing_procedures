source $HOME/.bash_profile
pytest ./tests/unittest.py
python3 -m PyInstaller -F ./exec.py 
