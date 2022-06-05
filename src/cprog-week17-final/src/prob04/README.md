# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/VIvafK" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/VIvafK</a>

### [問題 4]：依據給定的條件過濾輸出由終端機輸入的任意個整數

- 過濾條件：
    - 0 : 輸出全部數字
    - 1 : 輸出奇數
    - 2 : 輸出偶數  

### 簡易測試
```powershell
prob04> g++ -o main .\main.cpp
prob04> 0,$(1..10) | .\main.exe
    1    2    3    4    5    6    7    8    9   10

prob04> 2,$(1..10) | .\main.exe
    2    4    6    8   10

prob04> 1,$(1..10) | .\main.exe
    1    3    5    7    9
```

### 隨機自動檢測
```powershell
prob04> .\test.ps1    
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 1 31 99 67 45 8 18 29 7 53 33 10
Test Data : 0 68 96 15 89 4 53 36 28 100 75 87 53 54 24
Test Data : 1 15 17 39 78 60 85 80 97 74
Test Data : 1 24 38 15 93 35 96 41 25 95
Test Data : 1 79 92 2 23 42 76 35 1 2 93 48 48
Test Data : 1 17 73 28 61 73 38 28 22 52 48
Test Data : 1 11 34 80 76 86 68 75 76 98
Test Data : 2 42 51 71 51 4 29 44 24 60 99
Test Data : 2 42 23 10 45 32 46 44 11 76 30 15 68 55 59 88
Test Data : 2 65 74 48 28 50

測試通過!

   74   48   28   50
```