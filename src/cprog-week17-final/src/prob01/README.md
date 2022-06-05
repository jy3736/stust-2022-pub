# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/ty6pvo" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/ty6pvo</a>


### [問題 1]：輸出 1 ~ n 中所有可以被 m 整除的整數

### 簡易測試
```powershell
prob01> g++ -o main .\main.cpp
prob01> 10,2 | .\main.exe
    2    4    6    8   10

prob01> 30,3 | .\main.exe
    3    6    9   12   15   18   21   24   27   30

prob01> 5,1 | .\main.exe 
    1    2    3    4    5
```

### 隨機自動檢測
```powershell
prob01> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 39 4
Test Data : 63 9
Test Data : 1 3
Test Data : 80 10
Test Data : 15 5
Test Data : 54 3
Test Data : 49 8
Test Data : 6 2
Test Data : 2 2
Test Data : 78 6

測試通過!

    6   12   18   24   30   36   42   48   54   60   66   72   78
```