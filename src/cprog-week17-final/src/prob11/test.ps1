$cdir = Split-Path -leaf -path (Get-Location)
if (test-path main.exe) {
    Remove-Item main.exe
}
if (test-path main.cpp) {
    Write-Output "g++ -o main ./main.cpp"
    g++ -o main ./main.cpp
    if ($?) {
        py -3 .check/checks.py $args[0]
    } else {
        Write-Output "`nError while compiling ./main.cpp!`n" 
    }
} else {
    Write-Output "`nmain.cpp: No such file!`n"
}

