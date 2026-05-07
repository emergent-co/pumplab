"""
Cellab admin mini-server (Flask)
============================================================
정적 파일 서빙 + admin.html에서 호출하는 자동 저장/빌드 API

라우트:
  GET  /                       → index.html
  GET  /<file>                 → 워크스페이스 루트 정적 파일
  POST /api/save-and-build     → products.json 저장 + build.py 실행
  POST /api/save-products      → products.json만 저장 (빌드 안 함)
  POST /api/build              → build.py만 실행
============================================================
"""

import json
import os
import subprocess
import sys
from flask import Flask, request, send_from_directory, jsonify

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
PRODUCTS_JSON = os.path.join(SCRIPT_DIR, 'products.json')
BUILD_PY = os.path.join(SCRIPT_DIR, 'build.py')

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory(ROOT_DIR, 'index.html')


@app.route('/<path:filename>')
def static_file(filename):
    """워크스페이스 루트의 모든 정적 파일 서빙."""
    if filename.startswith('_build/') or filename.startswith('crawler/'):
        return ('Forbidden', 403)
    return send_from_directory(ROOT_DIR, filename)


@app.route('/_build/<path:filename>')
def build_file(filename):
    """_build/ 내부 일부 파일은 admin.html이 read 용도로 접근 (products.json 등)."""
    allowed = {'products.json', 'categories.json'}
    if filename not in allowed:
        return ('Forbidden', 403)
    return send_from_directory(SCRIPT_DIR, filename)


@app.route('/api/save-products', methods=['POST'])
def save_products():
    try:
        data = request.get_json()
        if not data or 'products' not in data:
            return jsonify({'ok': False, 'error': 'invalid JSON (no products field)'}), 400
        with open(PRODUCTS_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({'ok': True, 'count': len(data['products']), 'path': PRODUCTS_JSON})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/api/build', methods=['POST'])
def run_build():
    try:
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        result = subprocess.run(
            [sys.executable, BUILD_PY],
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            cwd=ROOT_DIR, timeout=30, env=env
        )
        return jsonify({
            'ok': result.returncode == 0,
            'returncode': result.returncode,
            'stdout': (result.stdout or '')[-3000:],
            'stderr': (result.stderr or '')[-3000:]
        })
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/api/save-and-build', methods=['POST'])
def save_and_build():
    """JSON 저장 후 즉시 빌드 — admin.html '저장 + 빌드' 버튼이 호출."""
    try:
        data = request.get_json()
        if not data or 'products' not in data:
            return jsonify({'ok': False, 'error': 'invalid JSON (no products field)'}), 400

        # 1) Save
        with open(PRODUCTS_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # 2) Build
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        result = subprocess.run(
            [sys.executable, BUILD_PY],
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            cwd=ROOT_DIR, timeout=30, env=env
        )

        return jsonify({
            'ok': result.returncode == 0,
            'count': len(data['products']),
            'returncode': result.returncode,
            'stdout': (result.stdout or '')[-3000:],
            'stderr': (result.stderr or '')[-3000:]
        })
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


if __name__ == '__main__':
    print('=' * 60)
    print('  Cellab admin server')
    print('  http://localhost:8000')
    print('=' * 60)
    print('  Open in browser:')
    print('    http://localhost:8000/admin.html  (admin sheet)')
    print('    http://localhost:8000/index.html  (home)')
    print('    http://localhost:8000/pump.html   (pump catalog)')
    print('=' * 60)
    print('  Stop: Ctrl+C or close window')
    print('=' * 60)
    print()
    app.run(host='127.0.0.1', port=8000, debug=False)
