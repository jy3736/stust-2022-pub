# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/7mLB11" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/7mLB11</a>

### [問題 8]：設計`nth(...)`函數回傳『隨機』整數陣列中第 n 個元素

- 完成主程式中使用的`nth(...)`函數。
- 函數`nth(...)`的設計不可使用任何排序演算法。
- 隨機陣列中不會出現重複的整數。

### 簡易測試
```powershell
prob08> g++ -o main .\main.cpp
prob08> 1,4,2,5,3,7 | .\main.exe
Min  :    1
Max  :    7
Sort :    1   2   3   4   5   7

prob08> 1,6,8,9,5,4,2,3,7 | .\main.exe
Min  :    1
Max  :    9
Sort :    1   2   3   4   5   6   7   8   9

prob08> 1..100 | Get-Random -Count 10 | .\main.exe
Min  :    3
Max  :  100
Sort :    3  17  34  35  61  63  66  71  97 100
```

### 隨機自動檢測
```powershell
prob08> .\test.ps1 
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 37 83 64 68 81 13 62
Test Data : 96 90 28 63 1 91 23 31 100 99 87 16
Test Data : 68 77 7 40 94 42 41 63 13 90
Test Data : 87 65 71 73 98 38 56 33 74 76 10 49
Test Data : 62 90 19 76 77 92 14 15 31 38 59
Test Data : 49 40 87 75 29 53 5 11 28
Test Data : 53 96 27 76 74 23 21 89 35 16 37 56 64 52 78
Test Data : 29 92 69 91 85 3 21
Test Data : 17 1 52 11 44 41 45 39 97 48 19 6 95 34
Test Data : 3 18 34 68 48 10 87 7

測試通過!

Min  :    3
Max  :   87
Sort :    3   7  10  18  34  48  68  87
```