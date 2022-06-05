### [課堂練習 02]：二維陣列以行(row)為基準的操作


```c++
#include <iostream>
#include <iomanip>

using namespace std;
```

### 5 x 5 二維陣列輸出函數
- d   ：二維陣列

#### 將二維陣列傳遞給函數，陣列的`列(column)必須固定`。


```c++
void dump55(int d[5][5]) {
    for(int r=0; r<5; r++) {
        for(int c=0; c<5; c++) {
            cout<<setw(4)<<d[r][c];
        }
        cout<<endl;
    }
    cout<<endl;
}
```

#### 利用迴圈把二維陣列全部填入0


```c++
int a[5][5];

for(int r=0; r<5; r++) {
    for(int c=0; c<5; c++) {
        a[r][c] = 0;
    }
}

dump55(a);
```

       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
    


#### 把填入0的程式片段變成函數


```c++
void zero55(int d[5][5]) {
    for(int r=0; r<5; r++) {
        for(int c=0; c<5; c++) {
            d[r][c] = 0;
        }
    }
}
```


```c++
int a[5][5];

zero55(a);
dump55(a);
```

       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
    


#### 把填入0的函數再次進化成填入特定數值的函數


```c++
void fill55(int d[5][5], int val) {
    for(int r=0; r<5; r++) {
        for(int c=0; c<5; c++) {
            d[r][c] = val;
        }
    }
}
```


```c++
int a[5][5];

fill55(a,7);
dump55(a);
```

       7   7   7   7   7
       7   7   7   7   7
       7   7   7   7   7
       7   7   7   7   7
       7   7   7   7   7
    


### 將特定數列填入 5 x 5 二維陣列的第 3 行


```c++
int a[5][5];

zero55(a);

int start = 1;
int step = 2;
for(int c=0; c<5; c++) {
    a[2][c] = start;
    start+=step;
}

dump55(a);

```

       0   0   0   0   0
       0   0   0   0   0
       1   3   5   7   9
       0   0   0   0   0
       0   0   0   0   0
    


### 將特定數列填入 5 x 5 二維陣列的第 r 行函數
- d    ：二維陣列
- r    ：陣列第 r 行(row)
- start：數列的起始值
- step ：數列的步階(間距)


```c++
void seq_row(int d[5][5], int r, int start, int step) {
    for(int c=0; c<5; c++) {
        d[r][c] = start;
        start+=step;
    }
}
```


```c++
int a[5][5];

zero55(a);
seq_row(a,2,1,2);
dump55(a);
```

       0   0   0   0   0
       0   0   0   0   0
       1   3   5   7   9
       0   0   0   0   0
       0   0   0   0   0
    


#### 使用 `seq_row(...)` 函數把每一行(row)填上特定數列


```c++
int a1[5][5];

seq_row(a1,0,1,0);
seq_row(a1,1,2,0);
seq_row(a1,2,3,0);
seq_row(a1,3,4,0);
seq_row(a1,4,5,0);

dump55(a1);
```

       1   1   1   1   1
       2   2   2   2   2
       3   3   3   3   3
       4   4   4   4   4
       5   5   5   5   5
    


#### 使用迴圈簡化填滿陣列的動作


```c++
int a2[5][5];

for(int i=0; i<5; i++)
    seq_row(a2,i,i+1,0);

dump55(a2);
```

       1   1   1   1   1
       2   2   2   2   2
       3   3   3   3   3
       4   4   4   4   4
       5   5   5   5   5
    


#### 利用迴圈變化填入有趣的數列


```c++
int a2[5][5];

for(int i=0; i<5; i++)
    seq_row(a2,i,i+1,1);

dump55(a2);
```

       1   2   3   4   5
       2   3   4   5   6
       3   4   5   6   7
       4   5   6   7   8
       5   6   7   8   9
    


#### 利用迴圈變化填入 5 x 5 乘法表


```c++
int a2[5][5];

for(int i=0; i<5; i++)
    seq_row(a2,i,i+1,i+1);

dump55(a2);
```

       1   2   3   4   5
       2   4   6   8  10
       3   6   9  12  15
       4   8  12  16  20
       5  10  15  20  25
    


### 利用 `seq_row(...)` 函數設計把 5 x 5 二維陣列填滿特定數字的函數


```c++
void fill55(int d[5][5], int val) {
    for(int r=0; r<5; r++) {
        seq_row(d,r,val,0);
    }
}
```


```c++
int a2[5][5];

fill55(a2,0);
dump55(a2);
```

       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
       0   0   0   0   0
    



```c++
int a2[5][5];

fill55(a2,63);
dump55(a2);
```

      63  63  63  63  63
      63  63  63  63  63
      63  63  63  63  63
      63  63  63  63  63
      63  63  63  63  63
    

