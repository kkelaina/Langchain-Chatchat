@echo off
chcp 65001

REM 检查系统中是否安装 Git 客户端
where git > nul 2>&1
if %errorlevel% neq 0 (
    echo Git 命令没找到，请先安装 Git 客户端.
    pause
    exit /b
)

REM 从远程仓库拉取最新内容并将本地分支重置到远程的 dev 分支
git fetch --all
git reset --hard origin/dev

REM 打印最新提交的信息
echo 最新提交的信息：
git log -1 --pretty=format:"%h - %s (%an, %ad)"

REM 等待一段时间后关闭（示例中等待 10 秒）
timeout /nobreak /t 10 > nul

REM 最后输出一条消息
