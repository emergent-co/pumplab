@echo off
chcp 65001 >nul
setlocal

REM ============================================
REM  LeadFluid MF106 영상 다운로드 스크립트
REM  실행: 이 파일을 더블클릭
REM ============================================

cd /d "%~dp0"

set "YTDLP=%~dp0yt-dlp.exe"
set "VIDEO_URL=https://www.youtube.com/watch?v=RuCpezl-SxA"
set "OUTNAME=MF106_original.mp4"

echo.
echo  [1/2] yt-dlp 준비 중...
echo.

if exist "%YTDLP%" (
    echo       이미 있습니다. 최신 버전으로 업데이트합니다.
    "%YTDLP%" -U
) else (
    echo       yt-dlp.exe 를 내려받습니다...
    powershell -NoProfile -Command ^
      "try { Invoke-WebRequest -Uri 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe' -OutFile '%YTDLP%' -UseBasicParsing; exit 0 } catch { Write-Host $_.Exception.Message; exit 1 }"
    if errorlevel 1 (
        echo.
        echo  [오류] yt-dlp 다운로드 실패. 인터넷 연결 또는 백신 차단을 확인하세요.
        pause
        exit /b 1
    )
)

echo.
echo  [2/2] 영상 다운로드 중...
echo.

"%YTDLP%" -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b" ^
          --merge-output-format mp4 ^
          --write-subs --write-auto-subs --sub-langs "en.*,zh.*" --convert-subs srt ^
          -o "%OUTNAME%" ^
          "%VIDEO_URL%"

if errorlevel 1 (
    echo.
    echo  [오류] 영상 다운로드 실패.
    pause
    exit /b 1
)

echo.
echo  ============================================
echo   완료!  저장 위치: %~dp0%OUTNAME%
echo   Claude 에게 "영상 받았어" 라고 알려주세요.
echo  ============================================
echo.
pause
