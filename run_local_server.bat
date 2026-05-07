@echo off
title Cellab admin server - http://localhost:8000
cd /d "%~dp0"

python --version > nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is required. Install Python 3.10+ from python.org
    pause
    exit /b 1
)

REM Check Flask
python -c "import flask" > nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing Flask...
    pip install flask
    if errorlevel 1 (
        echo [ERROR] Flask installation failed.
        pause
        exit /b 1
    )
)

echo.
echo ============================================================
echo   Cellab admin server (Flask)
echo   http://localhost:8000
echo ============================================================
echo.
echo Open in browser:
echo   http://localhost:8000/admin.html       (admin dashboard)
echo   http://localhost:8000/index.html       (home)
echo   http://localhost:8000/pump.html        (pump catalog)
echo   http://localhost:8000/tubing.html      (tubing catalog)
echo.
echo In admin.html click "Save + Build" to:
echo   1) Save products.json
echo   2) Auto-rebuild ALL 6 category pages
echo.
echo Stop: Ctrl+C or close this window
echo ============================================================
echo.

start "" cmd /c "timeout /t 1 /nobreak > nul && start http://localhost:8000/admin.html && start http://localhost:8000/index.html"

python _build\admin_server.py
