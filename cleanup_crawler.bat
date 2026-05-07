@echo off
title Cellab cleanup - archive crawler folder
cd /d "%~dp0"

echo.
echo ============================================================
echo   Move crawler folder (old Stage 2 work) to _archive
echo ============================================================
echo.
echo The crawler/ folder contains old Stage 2 server work that
echo is no longer used. Moving it to _archive/ reduces workspace
echo size and OneDrive sync load.
echo.
echo Decision saved in memory: B-pipeline (offline) for sigma crawl.
echo Restoring is just a folder move from _archive/.
echo.
echo Press any key to continue, or close to cancel.
pause > nul

if not exist _archive mkdir _archive

if exist crawler (
    move /Y crawler _archive\ > nul
    echo Done. crawler/ moved to _archive\crawler\
) else (
    echo crawler/ folder not found - already archived?
)

echo.
pause
