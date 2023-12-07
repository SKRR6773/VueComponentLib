import os



__DIR__ = os.path.dirname(__file__)


with open(os.path.join(__DIR__, "log.yxy"), 'w')as f:
    f.write("Hello World!")