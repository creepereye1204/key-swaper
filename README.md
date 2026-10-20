<div align="center">

# ⌨️ key-swaper

**직접 지정한 단축키 하나로 한글 ↔ 영문 입력을 전환하는 Windows 트레이 유틸리티**

[![Release](https://img.shields.io/github/v/release/creepereye1204/key-swaper?style=flat-square&label=release)](https://github.com/creepereye1204/key-swaper/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/creepereye1204/key-swaper/total?style=flat-square)](https://github.com/creepereye1204/key-swaper/releases)
[![Platform](https://img.shields.io/badge/platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](#)

</div>

---

## ✨ 특징

- 🎹 **원하는 키 조합을 직접 지정** — 트레이 메뉴에서 "단축키 변경"을 누르고 원하는 키를 누르면 그대로 등록됩니다.
- 🫥 **콘솔 창 없이 백그라운드 실행** — 시스템 트레이 아이콘 하나로만 존재합니다.
- 🚀 **Windows 시작 시 자동 실행** — 트레이 메뉴에서 언제든 켜고 끌 수 있습니다.
- 🪶 **가볍고 단순함** — 텍스트를 가로채지 않고, 실제 `한/영` 키(`VK_HANGUL`)를 대신 눌러주는 방식이라 모든 IME와 호환됩니다.

## 📥 다운로드

[**➡ 최신 릴리즈에서 `key-swaper-windows-x64-*.exe` 다운로드**](https://github.com/creepereye1204/key-swaper/releases/latest)

설치가 따로 필요 없는 단일 실행 파일입니다. 다운로드 후 그냥 실행하면 트레이에 아이콘이 나타납니다.

## 🖱️ 사용법

1. 실행하면 시스템 트레이(우측 하단 시계 옆)에 아이콘이 생깁니다.
2. 트레이 아이콘을 우클릭합니다.
3. **단축키 변경**을 누르고 원하는 키(조합)를 누르면 즉시 해당 키로 등록됩니다.
4. 이후 그 키를 누르면 현재 입력 언어가 한글 ↔ 영문으로 전환됩니다.
5. **Windows 시작 시 자동 실행** 항목을 체크/해제해 부팅 시 자동 실행 여부를 설정할 수 있습니다.
6. **종료**를 누르면 프로그램이 완전히 종료됩니다.

설정(단축키, 자동 실행 여부)은 `%APPDATA%\HanYoungToggle\config.json`에 저장됩니다.

## 🎮 ESC 대체키 (`esc-remap`)

Moonlight 모바일 등으로 원격 접속하면 폰 키보드의 `ESC`가 안드로이드 **뒤로가기**로 처리돼 앱이 종료되는 문제가 있습니다.
`esc-remap`은 지정한 다른 키 조합을 누르면 PC에 `ESC`를 대신 입력해주는 별도의 트레이 앱입니다.

- 기본 대체키는 **`Ctrl+[`** (vim 등에서 쓰는 표준 ESC 대체 조합)입니다.
- 트레이 메뉴 **대체키 변경**으로 원하는 키로 바꿀 수 있습니다.
- PC(스트리밍 호스트) 쪽에서 실행하면 됩니다. 릴리즈에서 `esc-remap-windows-x64-*.exe` 를 받으세요.
- 설정은 `%APPDATA%\EscRemap\config.json`에 저장됩니다.

## 🛠️ 소스에서 직접 빌드하기

Windows + Python 3.11 환경에서:

```bash
pip install -r requirements.txt
python generate_ico.py
pyinstaller --onefile --noconsole --name key-swaper --icon=app_icon.ico hangul_toggle.py
pyinstaller --onefile --noconsole --name esc-remap --icon=esc_icon.ico esc_remap.py
```

빌드 결과물은 `dist/key-swaper.exe`, `dist/esc-remap.exe` 에 생성됩니다.

## 📦 릴리즈 배포

`v*` 형태의 태그를 push하면 GitHub Actions가 Windows 환경에서 자동으로 빌드하고, 실행 파일을 첨부한 릴리즈를 생성합니다.

```bash
git tag v0.1.0
git push origin v0.1.0
```

## ⚠️ 참고

- Windows 전용입니다 (IME 제어에 Windows API를 사용).
- 관리자 권한으로 실행 중인 다른 프로그램(게임 등)에서도 단축키가 동작하게 하려면, 이 프로그램도 관리자 권한으로 실행해야 합니다.
