import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..', 'tools'))
from mylibs import chk_template
from random import randint
from decimal import Decimal

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"

def toLG(g):
    if (g >= 90):
        return "A+"
    if (g >= 85):
        return "A"
    if (g >= 80):
        return "A-"
    if (g >= 77):
        return "B+"
    if (g >= 73):
        return "B"
    if (g >= 70):
        return "B-"
    if (g >= 67):
        return "C+"
    if (g >= 63):
        return "C"
    if (g >= 60):
        return "C-"
    if (g >= 50):
        return "D"
    if (g >= 1):
        return "E"
    return "X"

def toGP(g):
    if (g >= 90):
        return 4.3
    if (g >= 85):
        return 4
    if (g >= 80):
        return 3.7
    if (g >= 77):
        return 3.3
    if (g >= 73):
        return 3.0
    if (g >= 70):
        return 2.7
    if (g >= 67):
        return 2.3
    if (g >= 63):
        return 2.0
    if (g >= 60):
        return 1.7
    if (g >= 50):
        return 1.0
    if (g >= 1):
        return 0
    return 0


def expected():
    dat = []
    odat = ""
    gpa = 0.0
    tc=0
    for _ in range(randint(1,5)) : 
        dat.append(randint(40,100))
        dat.append(randint(1,4))  
        odat+=f"{toLG(dat[-2])} "
        odat+=f"{dat[-1]} "
        gpa+=toGP(dat[-2])*dat[-1]
        tc+=dat[-1]
    gpa/=tc
    odat+=f"{gpa:.2f}"               
    idat = " ".join([str(_) for _ in dat])
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
    chk_template.main(root, 2, loops)
