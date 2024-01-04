@echo off

rem 切换到脚本所在目录
cd %~dp0

echo "=== Starting Script ==="

echo "Current Directory: %CD%"

echo "Activating Virtual Environment"
call .\miniconda3\Scripts\activate.bat .\venv

echo "=== Start API + WebUI ==="
python startup.py -a

echo "=== Script Execution Completed ==="

rem 保持命令提示符窗口打开
cmd /k