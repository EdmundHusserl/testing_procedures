import logging
logging.basicConfig(level=20)

def execute_test_steps(test:dict, retry:int) -> bool:
    steps = (el for el in test.get("steps"))
    for step in steps:
        for i in range(retry):
            try:
                if get_step_results(step) == step.get("result"):
                    logging.info(f"Step {step.get('name')} was completed successfully after {i+1} try.")
                    break
                else:
                    logging.warning(f"Step {step.get('name')} didn't generate expected result {step.get('result')} with params {step.get('params')}.")
            except Exception as e:
                logging.warning(f"Step {step.get('name')} generated the following exception:\n")
                logging.exception(e)
                continue
        else:
            logging.critical(f"Test failed at step {step.get('name')} after {retry} unsucessful tries.")
            return False
    logging.info("All tests' steps were completed successfully.")
    return True

def get_step_results(step:dict) -> object:
    method = step.get("method")
    logging.info(f"Executing {method.__name__} with params {step.get('params')}")
    return method.__call__(step.get("params"))

def is_equal(t:tuple) -> True:
    return t[0] == t[1]

if __name__ == '__main__':
    test = {
        "steps": [
            {
                "name": "sum",
                "method": sum,
                "params": [1,2,3,4],
                "result": 10
            },
            {
                "name": "evaluation",
                "method": eval,
                "params": "14",
                "result": 14
            },
            #{
            #    "name": "I'm supposed to fail.",
            #    "method": sum,
            #    "params": [1,2,3],
            #    "result": 7,
            #}
            {
                "name": "Is equal",
                "method": is_equal,
                "params": (0,0),
                "result": True
            }
        ]
    }
    #import pdb;pdb.set_trace()
    execute_test_steps(test, 3)
