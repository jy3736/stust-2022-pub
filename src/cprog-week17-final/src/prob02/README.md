# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/oPSNlU" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/oPSNlU</a>


### [問題 2]：加總由終端機輸入的任意個隨機整數

### 簡易測試
```powershell
prob02> g++ -o main .\main.cpp
prob02> 1,2,3,4,5 | .\main.exe
15

prob02> 1..100 | .\main.exe   
5050

prob02> 3,5,7,9,1,3,5,7 | .\main.exe
40
```

### 隨機自動檢測
```powershell
prob02> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 66 33 72 6 31 17 41 17 89
Test Data : 50 12 97 62 60 53 60 58 90
Test Data : 43 10 31 25 85 88 91 39 30 69 15 56 76 63 76
Test Data : 22 88 83 56 26 6 21 41 74 83
Test Data : 50 95 91 7 51 70 63 9 8 32 5 34 30 84
Test Data : 57 67 84 34 73 79 81 10 92 31 49 63 24 83 96
Test Data : 45 73 73 34 14 88 78 84 36 38
Test Data : 28 95 90 10 45 59 47 92 78 60 48
Test Data : 52 76 11 89 33 57 8 51 69
Test Data : 5 1 74 84 48 30

測試通過!

242
```