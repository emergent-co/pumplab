@echo off
chcp 65001 > nul
title 셀렙 크롤러 - 외부 제품 정보 수집

echo.
echo ============================================================
echo   셀렙 크롤러 - 시그마/코랩샵/올포랩 외부 제품 수집
echo ============================================================
echo.

cd /d "%~dp0"

REM Python 설치 확인
python --version > nul 2>&1
if errorlevel 1 (
    echo [!] Python이 설치되어 있지 않습니다.
    echo.
    echo Python 3.10 이상을 설치해 주세요:
    echo   https://www.python.org/downloads/
    echo.
    echo 설치 시 "Add Python to PATH" 체크 필수
    echo.
    pause
    exit /b 1
)

REM 의존성 설치 확인
python -c "import requests, bs4" > nul 2>&1
if errorlevel 1 (
    echo [!] 의존성 미설치. 자동 설치 시작...
    echo.
    pip install requests beautifulsoup4 lxml
    if errorlevel 1 (
        echo.
        echo [!] 자동 설치 실패. 수동 실행 필요:
        echo     pip install requests beautifulsoup4 lxml
        pause
        exit /b 1
    )
    echo.
    echo 설치 완료.
    echo.
)

REM 크롤러 실행
python crawl.py

REM 완료 후 결과 폴더 자동 열기 (선택)
REM explorer .

pause
