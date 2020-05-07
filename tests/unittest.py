import os
os.environ["PYTHONPATH"]=os.path.abspath(os.getcwd())

def test_w_params():
    from exec import method
    assert method("Hola", "ql", "como", "estai") == ["Hola", "ql", "como", "estai"]

def test_wo_params():
    from exec import method
    assert method() == None
