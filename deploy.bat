@echo off
title Cellab GitHub Pages 배포
cd /d "%~dp0"

REM PowerShell 실행 정책 우회로 deploy.ps1 실행
REM 인자 전체를 그대로 PowerShell에 전달

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0deploy.ps1" %*
