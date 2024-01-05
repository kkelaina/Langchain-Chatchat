@echo off
chcp 65001

venv\python.exe -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo 如果有失败的，请手动补装
cmd /k