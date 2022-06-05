# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/hPEJJc" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/hPEJJc</a>

### [問題 3]：加總由終端機輸入且『可被 m 整除』的任意個隨機整數

### 簡易測試
```powershell
prob03> g++ -o main .\main.cpp
prob03> 1,$(1..100) | .\main.exe
5050

prob03> 2,$(1..100) | .\main.exe
2550

prob03> 3,3,6,9,12 | .\main.exe 
30
```

### 隨機自動檢測
```powershell
prob03> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 7 63 2 29 56 76 54 79 54 20 10 38 75 95 61
Test Data : 7 34 98 72 15 68 2 50 53
Test Data : 9 42 21 92 62 16 49
Test Data : 5 74 30 1 76 6 97 47 34 25 97 47 41 11 60
Test Data : 3 87 15 13 50 78 100
Test Data : 4 94 41 72 47 30
Test Data : 7 47 64 21 21 19 11 5 56
Test Data : 10 93 65 8 69 38 83 16 35 68 61 84
Test Data : 6 77 59 9 51 56 12 23 63 80 7 89 88
Test Data : 8 96 45 68 99 29 84

測試通過!

96
```