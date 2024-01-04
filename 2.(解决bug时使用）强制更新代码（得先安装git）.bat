@echo off
chcp 65001

REM 检查系统中是否安装 Git 客户端
where git > nul 2>&1
if %errorlevel% neq 0 (
    echo Git 命令没找到，请先安装 Git 客户端.
    pause
    exit /b
)

echo 正在从远程仓库拉取最新内容并将本地分支重置到远程的 dev 分支...
git fetch --all
git reset --hard origin/dev

REM 打印最新提交的信息
echo 最新提交的信息：
git log -1

echo 拉取完毕（如果没报错的话）.
rem 保持命令提示符窗口打开
cmd /k
