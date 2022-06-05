#include <iostream>
#include <iomanip>

using namespace std;

const int ROW = 9;
const int COL = 9;

// ==============================================
// -----^^----- 不得修改『以上』的程式 -----^^-----
// ==============================================

// 1. 你所寫的程式碼只能在這個段落。
// 2. 請依照題目說明完成欠缺的程式設計。

// ==============================================
// -----vv----- 不得修改『以下』的程式 -----vv-----
// ==============================================

int main()
{
    int a[ROW][COL];
    int row;
    int col;

    cin >> row;
    cin >> col;

    row = (row < 1) ? 1 : (row > 9) ? 9
                                    : row;
    col = (col < 1) ? 1 : (col > 9) ? 9
                                    : col;

    fill(a, row, col);
    dump(a, row, col);

    return 0;
}