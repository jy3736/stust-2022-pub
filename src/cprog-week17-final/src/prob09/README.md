# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/e84TnR" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/e84TnR</a>

### [問題 9]：複製一維陣列指定段落的內容

- Week 13 作業。
- 完成主程式中使用的`copy(...)`函數。
- 函數原型及參數說明：
    - 從`src`陣列的`sp`索引位置，複製`n`筆資料到目的陣列`des`。
```c++
void copy(int src[], int des[], int sp, int n);
```
    - src  : 資料來源
    - des  : 複製目的
    - sp   : 來源陣列的起始索引
    - n    : 要複製的資料筆數


### 簡易測試
```powershell
prob09> g++ -o main .\main.cpp
prob09> 1..100 | Get-Random -Count 10 | .\main.exe
a1 =   3  40  22  73  69  71  44  58  88  78
a1[3] ~ a1[7] =  73  69  71  44  58
a1[0] ~ a1[5] =   3  40  22  73  69  71

prob09> 1..100 | Get-Random -Count 10 | .\main.exe
a1 =  24  58  59  11  89  13  48  47  50  68
a1[3] ~ a1[7] =  11  89  13  48  47
a1[0] ~ a1[5] =  24  58  59  11  89  13

prob09> 1..100 | Get-Random -Count 10 | .\main.exe
a1 =  29  28  30  49 100  36  17  75  69  46
a1[3] ~ a1[7] =  49 100  36  17  75
a1[0] ~ a1[5] =  29  28  30  49 100  36
```

### 隨機自動檢測
```powershell
prob09> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 50 26 74 45 22 36 51 77 57 80 70 14
Test Data : 61 87 12 96 6 42 14 33 23 94 60 60 43 31
Test Data : 31 60 35 97 34 47 17 19 30 49 91 86
Test Data : 85 86 85 75 86 73 11 47 67 61 8 73 80 71
Test Data : 15 96 84 22 82 65 27 23 76 72 18 38 95
Test Data : 89 59 68 45 2 95 52 35 46 100
Test Data : 67 77 41 60 17 83 2 15 20 39 17 18 26 48
Test Data : 75 31 86 73 41 21 28 20 54 54 54 18 40
Test Data : 26 62 27 46 21 60 50 26 4 41 43
Test Data : 7 83 91 93 58 61 92 34 16 57 93 56 95

測試通過!

a1 =   7  83  91  93  58  61  92  34  16  57  93  56  95
a1[3] ~ a1[7] =  93  58  61  92  34
a1[0] ~ a1[5] =   7  83  91  93  58  61
```