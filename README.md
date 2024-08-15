# 使用
直接使用 密碼生成器.exe  
開啟程式會在同一目錄下生成一個 密碼文件(如: New password.txt)  

# pwg.conf
可在同一目錄下創建一個 pwg.conf 文件，用於配置可用參數
可配置參數:
* password_length : 設定生成的密碼長度，不少於12位，當設定少於12，程式將生成12位密碼
* output_filename : 設定生成的密碼文件名稱，不包含副案名。

### 例子:
```
password_length = 20
output_filename = New password
```

# python源代碼 編譯成exe執行檔
`pyinstaller main.py --onefile --icon=pwg_icon.ico`


