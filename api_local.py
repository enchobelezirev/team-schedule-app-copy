from app import *

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9002, app)