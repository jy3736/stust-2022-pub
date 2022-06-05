### [課堂練習 03]：二維陣列以列(column)為基準的操作


```c++
#include <iostream>
#include <iomanip>

using namespace std;
```

### 6 x 6 二維陣列輸出函數
- d   ：二維陣列

#### 將二維陣列傳遞給函數，陣列的`列(column)必須固定`。


```c++
void dump66(int d[6][6]) {
    for(int r=0; r<6; r++) {
        for(int c=0; c<6; c++) {
            cout<<setw(4)<<d[r][c];
        }
        cout<<endl;
    }
    cout<<endl;
}
```

#### 利用迴圈把二維陣列全部填入0


```c++
int a[6][6];

for(int r=0; r<5; r++) {
    for(int c=0; c<5; c++) {
        a[r][c] = 0;
    }
}

dump66(a);
```

       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
    


#### 把填入0的程式片段變成函數


```c++
void zero66(int d[6][6]) {
    for(int r=0; r<6; r++) {
        for(int c=0; c<6; c++) {
            d[r][c] = 0;
        }
    }
}
```


```c++
int a[6][6];

zero66(a);
dump66(a);
```

       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
       0   0   0   0   0   0
    


#### 把填入0的函數再次進化成填入特定數值的函數


```c++
void fill66(int d[6][6], int val) {
    for(int r=0; r<6; r++) {
        for(int c=0; c<6; c++) {
            d[r][c] = val;
        }
    }
}
```


```c++
int a[6][6];

fill66(a,3);
dump66(a);
```

       3   3   3   3   3   3
       3   3   3   3   3   3
       3   3   3   3   3   3
       3   3   3   3   3   3
       3   3   3   3   3   3
       3   3   3   3   3   3
    


### 將特定數列填入 6 x 6 二維陣列的第 5 列


```c++
int a[6][6];

zero66(a);

int start = 2;
int step = 2;
for(int r=0; r<6; r++) {
    a[r][4] = start;
    start+=step;
}

dump66(a);

```

       0   0   0   0   2   0
       0   0   0   0   4   0
       0   0   0   0   6   0
       0   0   0   0   8   0
       0   0   0   0  10   0
       0   0   0   0  12   0
    


### 將特定數列填入 6 x 6 二維陣列的第 c 列函數
- d    ：二維陣列
- r    ：陣列第 r 行(row)
- start：數列的起始值
- step ：數列的步階(間距)


```c++
void seq_col(int d[6][6], int c, int start, int step) {
    for(int r=0; r<6; r++) {
        d[r][c] = start;
        start+=step;
    }
}
```


```c++
int a[6][6];

zero66(a);
seq_col(a,4,2,2);
dump66(a);
```

       0   0   0   0   2   0
       0   0   0   0   4   0
       0   0   0   0   6   0
       0   0   0   0   8   0
       0   0   0   0  10   0
       0   0   0   0  12   0
    


#### 使用 `seq_col(...)` 函數把每一列(column)填上特定數列


```c++
int a1[6][6];

seq_col(a1,0,1,0);
seq_col(a1,1,2,0);
seq_col(a1,2,3,0);
seq_col(a1,3,4,0);
seq_col(a1,4,5,0);
seq_col(a1,5,6,0);

dump66(a1);
```

       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
    


#### 使用迴圈簡化填滿陣列的動作


```c++
int a2[6][6];

for(int i=0; i<6; i++)
    seq_col(a2,i,i+1,0);

dump66(a2);
```

       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
       1   2   3   4   5   6
    


#### 利用迴圈變化填入有趣的數列


```c++
int a2[6][6];

for(int i=0; i<6; i++)
    seq_col(a2,i,i+1,1);

dump66(a2);
```

       1   2   3   4   5   6
       2   3   4   5   6   7
       3   4   5   6   7   8
       4   5   6   7   8   9
       5   6   7   8   9  10
       6   7   8   9  10  11
    


#### 利用迴圈變化填入 6 x 6 乘法表


```c++
int a2[6][6];

for(int i=0; i<6; i++)
    seq_col(a2,i,i+1,i+1);

dump66(a2);
```

       1   2   3   4   5   6
       2   4   6   8  10  12
       3   6   9  12  15  18
       4   8  12  16  20  24
       5  10  15  20  25  30
       6  12  18  24  30  36
    

