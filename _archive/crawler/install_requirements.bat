@echo off
chcp 65001 > nul
title 크롤러 의존성 설치 (최초 1회만)

echo.
echo ============================================================
echo   크롤러 의존성 설치 (최초 1회만 실행)
echo ============================================================
echo.

REM Python 설치 확인
python --version
if errorlevel 1 (
    echo.
    echo [!] Python이 설치되어 있지 않습니다.
    echo Python 3.10 이상을 먼저 설치해 주세요:
    echo   https://www.python.org/downloads/
    echo 설치 시 "Add Python to PATH" 체크 필수
    pause
    exit /b 1
)

echo.
echo 설치 중: requests beautifulsoup4 lxml flask
echo.

pip install --upgrade pip
pip install requests beautifulsoup4 lxml flask

echo.
echo ============================================================
echo   설치 완료.
echo   - 크롤만 돌리려면: run_crawl.bat
echo   - 웹 서버 띄우려면: run_server.bat
echo ============================================================
pause
