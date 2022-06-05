# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/IyAx6r" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/IyAx6r</a>

### [問題 10]：回傳參數資料在陣列中的索引位置

- 如果`val`參數資料存在於陣列中，回傳該資料的`索引`位置。
- 如果`val`參數資料不存在，回傳 `-1`。
- 建議的函數原型：
```C++
int index(float arr[],  int len, int val);
```
    - arr 一維陣列
    - len 陣列長度
    - val 要回傳索引的資料

### 簡易測試
```powershell
prob10> g++ -o main .\main.cpp
prob10> 1..10 | .\main.exe
-1 0 1 2 3 4 5 6 7 8 
prob10> 1,2,3,6,7,8,9 | .\main.exe
-1 0 1 2 -1 -1 3 4 5 6 
prob10> 5..10 | .\main.exe        
-1 -1 -1 -1 -1 0 1 2 3 4 
```

### 隨機自動檢測
```powershell
prob10> .\test.ps1    
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 1 9 15 14 3 11 8 2 14 11 7 2 14 11 9 7 2 14 8 2
Test Data : 1 7 15 10 9 8 9 11 13 6
Test Data : 15 11 8 5 4 2 15 15 6 4 11 3 3 9
Test Data : 6 15 6 2 12 9 15 3 5 10 5 7 13 7 4 14 10 8
Test Data : 15 2 4 2 4 11 7 1 10 2 6 5 14 4 15 2 10 8 9 6
Test Data : 5 2 14 13 5 13 5 5 13 11 12 11 11 10
Test Data : 15 4 9 5 7 2 9 4 6 1 2 9 13 3 9 11
Test Data : 1 5 13 15 15 11 2 8 1 7 9 6 8 6 1 4 14
Test Data : 7 6 12 13 12 3 1 9 14 11 2 9 1
Test Data : 13 12 9 11 2 1 3 9 4 1

測試通過!

-1 5 4 6 8 -1 -1 -1 -1 2
```