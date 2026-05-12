# 절대 규칙 — 사이트 손상 방지

## 1. AI/에이전트가 절대 하면 안 되는 것

- Python `re.sub` 또는 sed로 **여러 HTML 파일 일괄 변경** → 후반부 잘림 사고 다수
- HTML 안 JS template literal에 `</script>`, `</style>` 문자열 포함
- 변경 후 검증 없이 commit/push

## 2. 매 작업 후 의무 검증

```bash
for f in *.html blog/*.html; do
  last=$(tail -1 "$f" | tr -d '[:space:]')
  if [ "$last" != "</html>" ]; then
    echo "JEOLLIM: $f ($(wc -l < $f)줄)"
  fi
done
```

이 출력에 한 줄이라도 나오면 **즉시 commit 중단** + 정상 commit에서 복원.

## 3. 외부 도구 의심 신호

- 작업한 적 없는데 파일이 modified로 뜸
- HTML 줄수가 갑자기 줄어듦
- `grep`이 `binary file matches` 출력
- 브라우저 콘솔 "Unexpected end of input"

## 4. 손상 발견 시 복원 절차

```powershell
# 1. 정상 commit 찾기
git log --oneline -10

# 2. 정상 commit에서 파일 복원
git show <정상해시>:<파일경로> > <파일경로>

# 3. git index 손상 시
Remove-Item .git/index
git reset
```

## 5. 환경 정리 (작업 전 1회)

- OneDrive 동기화 일시 중지 (작업 표시줄 아이콘 → 일시 중지)
- 메모장(notepad.exe)으로 절대 HTML/MD 열지 말 것
- VS Code 등 에디터 동시 작업 시 충돌 주의

## 6. AI 에이전트와 작업 시 절대 규칙

- AI는 Edit 도구로 한 파일씩 정확히 수정만
- 여러 파일 헤더/푸터 공통 작업 시 — Python 일괄 처리 금지, Edit 한 번씩
- 변경 직후 항상 `wc -l` + `tail -3` 검증
- commit 메시지에 변경 파일 줄수 명시 (예: `leadfluid.html: 0→432줄`)

---

자세한 사례·해결법은 `OPERATIONS.md` 2장 "발생 사례 + 재발 방지" 참조.
