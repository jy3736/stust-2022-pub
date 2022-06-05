# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/kJqu0q" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/kJqu0q</a>

### [問題 11]：運用兩層迴圈存取(write/read)二維陣列

- 從終端機讀取`row`參數
- 將`row x 5`陣列依序填滿連續的數字
    - 以行(row)為基準填入 1 ~ (row x 5)整數
        - row=4 => 1 ~ 20 
        - row=6 => 1 ~ 30 
        - row=8 => 1 ~ 40 
- 參考`簡易測試`印出填滿資料的二維陣列

### 簡易測試
```powershell
prob11> g++ -o main .\main.cpp
prob11> 3 | .\main.exe
   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15

prob11> 5 | .\main.exe
   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20
  21  22  23  24  25

prob11> 7 | .\main.exe
   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20
  21  22  23  24  25
  26  27  28  29  30
  31  32  33  34  35
```

### 隨機自動檢測
```powershell
prob11> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 6
Test Data : 10
Test Data : 5
Test Data : 15
Test Data : 15
Test Data : 7
Test Data : 5
Test Data : 10
Test Data : 8
Test Data : 7

測試通過!

   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20
  21  22  23  24  25
  26  27  28  29  30
  31  32  33  34  35
```