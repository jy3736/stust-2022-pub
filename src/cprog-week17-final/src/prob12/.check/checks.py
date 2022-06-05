import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def expected():
    dat = [randint(-5, 15),randint(-5, 15)]
    idat = f"{dat[0]} {dat[1]}"
    if dat[0]<1: dat[0]=1
    if dat[1]<1: dat[1]=1
    if dat[0]>9: dat[0]=9
    if dat[1]>9: dat[1]=9
    odat = ""
    for r in range(1,dat[0]+1):
        for c in range(1,dat[1]+1):
            odat+=f"{r*c:4}"
        odat+="\n"
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
