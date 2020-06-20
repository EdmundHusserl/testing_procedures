from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import logging
import os

__PARAMS__ = ["hola", "hello", "bonjour"]
__file__ = "Execution_Etapes.py"

try:
    os.system(f'touch {__file__}')
except Exception as e:
    logging.exception(e)
    pass

libPath = os.path.abspath(__file__)

@keyword(name="Test")
def main():
    create_fn(__PARAMS__)
    try:
        BuiltIn().run_keyword("Import Library", libPath)
        for m in __PARAMS__:
            BuiltIn().run_keyword(m, *[el for el in range(10)])
    except Exception as e:
        logging.exception(e)
    finally:
        clean_up()

def clean_up():
    try:
        os.remove(__file__)
    except FileNotFoundError:
        pass

def create_fn(kws:list):
    with open(__file__, 'a', encoding="utf8") as file:
        file.write("from robot.api.deco import keyword\n")
        for k in kws:
            file.write("@keyword\n")
            file.write(f"def {k}(*params):\n")
            file.write(" print(params)\n")
            file.write("\n")
        file.close()
