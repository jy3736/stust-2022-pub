import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def expected():
    m = randint(0,2)
    dat = [randint(1,100) for _ in range(randint(5,15))] 
    idat = f"{m} " + " ".join([str(_) for _ in dat])
    odat = " ".join([str(_) for _ in dat])
    if m==1:
        odat = " ".join([str(_) for _ in filter(lambda x:x%2==1,dat)])
    elif m==2:
        odat = " ".join([str(_) for _ in filter(lambda x:x%2==0,dat)])
    print(f"Test Data : {idat}")
    return idat, odat


chk_template.expected = expected

if __name__ == "__main__":
    # print(f"cur = {sys.argv[0]}")
    root = sys.argv[0].replace(".check\checks.py", "")
    root = root.replace(".check/checks.py", "")
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 0, loops)
