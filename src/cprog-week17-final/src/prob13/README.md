# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/eg6rWy" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/eg6rWy</a>

### [問題 13]：對調二維矩陣中的兩行資料

- 從終端機讀取 `R1` 和 `R2` 兩個參數。
- `R1` 和 `R2` 是介於`0`到`ROW-1`的整數。
- 對調二維矩陣中的`第R1行`跟`第R2行`的資料。
- 參考`簡易測試`輸出對調後的二維矩陣。

### 簡易測試
```powershell
prob13> g++ -o main .\main.cpp
prob13> 0,8 | .\main.exe
   8   8   8   8   8   8   8   8   8
   1   1   1   1   1   1   1   1   1
   2   2   2   2   2   2   2   2   2
   3   3   3   3   3   3   3   3   3
   4   4   4   4   4   4   4   4   4
   5   5   5   5   5   5   5   5   5
   6   6   6   6   6   6   6   6   6
   7   7   7   7   7   7   7   7   7
   0   0   0   0   0   0   0   0   0

prob13> 5,6 | .\main.exe
   0   0   0   0   0   0   0   0   0
   1   1   1   1   1   1   1   1   1
   2   2   2   2   2   2   2   2   2
   3   3   3   3   3   3   3   3   3
   4   4   4   4   4   4   4   4   4
   6   6   6   6   6   6   6   6   6
   5   5   5   5   5   5   5   5   5
   7   7   7   7   7   7   7   7   7
   8   8   8   8   8   8   8   8   8

prob13> -5,6 | .\main.exe
   6   6   6   6   6   6   6   6   6
   1   1   1   1   1   1   1   1   1
   2   2   2   2   2   2   2   2   2
   3   3   3   3   3   3   3   3   3
   4   4   4   4   4   4   4   4   4
   5   5   5   5   5   5   5   5   5
   0   0   0   0   0   0   0   0   0
   7   7   7   7   7   7   7   7   7
   8   8   8   8   8   8   8   8   8
```

### 隨機自動檢測
```powershell
prob13> .\test.ps1       
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 5 4
Test Data : 1 5
Test Data : 12 4
Test Data : 9 6
Test Data : 7 12
Test Data : 11 5
Test Data : 5 0
Test Data : 1 1
Test Data : -1 3
Test Data : 9 5

測試通過!

   0   0   0   0   0   0   0   0   0
   1   1   1   1   1   1   1   1   1
   2   2   2   2   2   2   2   2   2
   3   3   3   3   3   3   3   3   3
   4   4   4   4   4   4   4   4   4
   8   8   8   8   8   8   8   8   8
   6   6   6   6   6   6   6   6   6
   7   7   7   7   7   7   7   7   7
   5   5   5   5   5   5   5   5   5
```