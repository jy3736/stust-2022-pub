#include <iostream>
#include <iomanip>

using namespace std;

string toLG(int g)
{
    if (g >= 90)
        return "A+";
    if (g >= 85)
        return "A";
    if (g >= 80)
        return "A-";
    if (g >= 77)
        return "B+";
    if (g >= 73)
        return "B";
    if (g >= 70)
        return "B-";
    if (g >= 67)
        return "C+";
    if (g >= 63)
        return "C";
    if (g >= 60)
        return "C-";
    if (g >= 50)
        return "D";
    if (g >= 1)
        return "E";
    return "X";
}

float toGP(int g)
{
    if (g >= 90)
        return 4.3;
    if (g >= 85)
        return 4;
    if (g >= 80)
        return 3.7;
    if (g >= 77)
        return 3.3;
    if (g >= 73)
        return 3.0;
    if (g >= 70)
        return 2.7;
    if (g >= 67)
        return 2.3;
    if (g >= 63)
        return 2.0;
    if (g >= 60)
        return 1.7;
    if (g >= 50)
        return 1.0;
    if (g >= 1)
        return 0;
    return 0;
}

// ==============================================
// -----^^----- 不得修改『以上』的程式 -----^^-----
// ==============================================

// 1. 你所寫的程式碼只能在這個段落以下。
// 2. 請依照題目說明完成欠缺的程式碼。
