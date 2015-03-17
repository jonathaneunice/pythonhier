

from stuf import stuf

from helpers.helper1 import helper_fn1
from helpers.helper2 import helper_fn2

BigModel = stuf(size="l")
SmallModel = stuf(size="s")

if __name__ == '__main__':
    print "model.py"
    helper_fn2()