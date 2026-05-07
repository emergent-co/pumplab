@echo off
chcp 65001 > nul
title 셀렙 크롤러 - 미니 웹 서버

echo.
echo ============================================================
echo   셀렙 크롤러 - 미니 웹 서버
echo ============================================================
echo.

cd /d "%~dp0"

REM Python 설치 확인
python --version > nul 2>&1
if errorlevel 1 (
    echo [!] Python이 설치되어 있지 않습니다.
    echo Python 3.10 이상을 설치해 주세요.
    pause
    exit /b 1
)

REM 의존성(Flask 포함) 확인
python -c "import requests, bs4, flask" > nul 2>&1
if errorlevel 1 (
    echo [!] 의존성 미설치 또는 Flask 없음. 자동 설치 시작...
    pip install requests beautifulsoup4 lxml flask
    if errorlevel 1 (
        echo.
        echo [!] 자동 설치 실패. 수동 실행:
        echo     pip install requests beautifulsoup4 lxml flask
        pause
        exit /b 1
    )
)

REM 브라우저 자동 열기 (1초 후)
start "" /min cmd /c "timeout /t 2 /nobreak > nul & start http://localhost:5000/tubing_curated_demo.html"

REM 서버 실행
python server.py

pause
