@echo off
title Cellab cleanup - move old demo files to _archive
cd /d "%~dp0"

echo.
echo ============================================================
echo   Cellab workspace cleanup
echo ============================================================
echo.
echo This will move OLD demo HTML files to _archive\ folder.
echo Active files (index, pump, tubing, syringe, pumphead, fitting,
echo other, admin, product_curated) stay in place.
echo.
echo Press any key to continue, or close this window to cancel.
pause > nul

if not exist _archive mkdir _archive

echo.
echo Moving old demo files...

if exist tubing_curated_demo.html (
    move /Y tubing_curated_demo.html _archive\ > nul
    echo   - tubing_curated_demo.html
)
if exist tubing_shop_demo.html (
    move /Y tubing_shop_demo.html _archive\ > nul
    echo   - tubing_shop_demo.html
)
if exist tubing_16_sample.html (
    move /Y tubing_16_sample.html _archive\ > nul
    echo   - tubing_16_sample.html
)
if exist tubing_catalog_hybrid_demo.html (
    move /Y tubing_catalog_hybrid_demo.html _archive\ > nul
    echo   - tubing_catalog_hybrid_demo.html
)
if exist compatibility_matrix_sample.html (
    move /Y compatibility_matrix_sample.html _archive\ > nul
    echo   - compatibility_matrix_sample.html
)
if exist series_bt101s_sample.html (
    move /Y series_bt101s_sample.html _archive\ > nul
    echo   - series_bt101s_sample.html
)

echo.
echo Done. Old demo files are now in _archive\
echo Active files in workspace root (unchanged):
echo   index.html, pump.html, tubing.html, syringe.html,
echo   pumphead.html, fitting.html, other.html,
echo   admin.html, product_curated.html
echo.
echo If you want to undo, just move files back from _archive\ to root.
echo.
pause
