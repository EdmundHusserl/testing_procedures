#! /usr/bin/python3

def method(*args):
    import logging
    try:
        if not args:
            raise Exception("You haven't provided any parameters.")
        return list(map(lambda x: x, args))
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    import sys
    from pprint import pprint as pp
    pp(method(*sys.argv[1:]))
