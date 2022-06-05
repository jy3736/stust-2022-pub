# 計算機程式及實習 (2022 Spring) 期末測驗

#### <a href="https://sndn.link/cprog2022s/xhYphw" target="_blank">[Podcast 說明] : https://sndn.link/cprog2022s/xhYphw</a>

### [問題 6]：主程式會依參數的(奇/偶)特性，使用(*/#)繪製直角三角形圖

- 完成主程式中使用的劃線函數 `drawLine(...)`。

### 簡易測試
```powershell
prob06> g++ -o main .\main.cpp
prob06> 5 |  .\main.exe
*
**
***
****
*****

prob06> 8 |  .\main.exe
#
##
###
####
#####
######
#######
########

prob06> 3 |  .\main.exe
*
**
***
```

### 隨機自動檢測
```powershell
prob06> .\test.ps1
g++ -o main ./main.cpp

********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 6
Test Data : 8
Test Data : 8
Test Data : 1
Test Data : 2
Test Data : 8
Test Data : 5
Test Data : 1
Test Data : 6
Test Data : 9

測試通過!

*
**
***
****
*****
******
*******
********
*********
```