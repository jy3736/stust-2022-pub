# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/xfIc9z" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/xfIc9z</a>

### [問題 12]：將矩形乘法表填入 R x C 二維陣列

- 從終端機讀取 `R` 和 `C` 兩個參數。
- `R` 和 `C` 是介於`1`到`9`的整數。
- 參考`簡易測試`的輸出結果，將`R x C` 二維陣列填入乘法表。

### 簡易測試
```powershell
prob12> g++ -o main .\main.cpp
prob12> 3,3 | .\main.exe
   1   2   3
   2   4   6
   3   6   9

prob12> 5,7 | .\main.exe
   1   2   3   4   5   6   7
   2   4   6   8  10  12  14
   3   6   9  12  15  18  21
   4   8  12  16  20  24  28
   5  10  15  20  25  30  35

prob12> 10,100 | .\main.exe
   1   2   3   4   5   6   7   8   9
   2   4   6   8  10  12  14  16  18
   3   6   9  12  15  18  21  24  27
   4   8  12  16  20  24  28  32  36
   5  10  15  20  25  30  35  40  45
   6  12  18  24  30  36  42  48  54
   7  14  21  28  35  42  49  56  63
   8  16  24  32  40  48  56  64  72
   9  18  27  36  45  54  63  72  81
```

### 隨機自動檢測
```powershell
prob12> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : -2 3
Test Data : 15 11
Test Data : 13 13
Test Data : -1 7
Test Data : 8 4
Test Data : 5 12
Test Data : 3 5
Test Data : -5 0
Test Data : -3 10
Test Data : 10 5

測試通過!

   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
   6  12  18  24  30
   7  14  21  28  35
   8  16  24  32  40
   9  18  27  36  45
```