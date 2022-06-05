import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def expected():
    dat = [randint(-2, 12),randint(-2, 12)]
    idat = f"{dat[0]} {dat[1]}"
    if dat[0]<0: dat[0]=0
    if dat[1]<0: dat[1]=0
    if dat[0]>8: dat[0]=8
    if dat[1]>8: dat[1]=8
    odat = ""
    for r in range(9):
        for c in range(9):
            if r==dat[0]:
                odat+=f"{dat[1]:4}"
            elif r==dat[1]:
                odat+=f"{dat[0]:4}"
            else:
                odat+=f"{r:4}"
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
