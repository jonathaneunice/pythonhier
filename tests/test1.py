import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from app.model import BigModel

b = BigModel

assert b.size == "l"
print "tests done!"
