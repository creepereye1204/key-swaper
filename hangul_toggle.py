import ctypes
import json
import os
import sys
import threading

import keyboard
import pystray

from icon import build_icon

CONFIG_DIR = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), "HanYoungToggle")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
DEFAULT_HOTKEY = "alt+space"

VK_HANGUL = 0x15
KEYEVENTF_KEYUP = 0x0002

RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"
APP_NAME = "HanYoungToggle"

current_hotkey = None
hotkey_handle = None
lock = threading.Lock()


def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_config(cfg):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def toggle_ime():
    # VK_HANGUL is the virtual key most IMEs (MS IME, 새나루, 구름 등) treat
    # as the 한/영 language-toggle key, regardless of which physical key fired it.
    ctypes.windll.user32.keybd_event(VK_HANGUL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_HANGUL, 0, KEYEVENTF_KEYUP, 0)


def register_hotkey(hotkey):
    global hotkey_handle, current_hotkey
    with lock:
        if hotkey_handle is not None:
            keyboard.remove_hotkey(hotkey_handle)
        hotkey_handle = keyboard.add_hotkey(hotkey, toggle_ime, suppress=True)
        current_hotkey = hotkey


def capture_new_hotkey(icon, item):
    def _capture():
        icon.notify("새 단축키 조합을 눌러주세요...", "한/영 전환기")
        new_hotkey = keyboard.read_hotkey(suppress=False)
        register_hotkey(new_hotkey)
        cfg = load_config()
        cfg["hotkey"] = new_hotkey
        save_config(cfg)
        icon.notify(f"단축키가 '{new_hotkey}' 로 설정되었습니다.", "한/영 전환기")
        icon.menu = build_menu()

    threading.Thread(target=_capture, daemon=True).start()


def get_exe_path():
    if getattr(sys, "frozen", False):
        return sys.executable
    return os.path.abspath(__file__)


def set_startup_enabled(enabled):
    import winreg

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_SET_VALUE) as key:
        if enabled:
            winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, f'"{get_exe_path()}"')
        else:
            try:
                winreg.DeleteValue(key, APP_NAME)
            except FileNotFoundError:
                pass


def ensure_startup_default():
    cfg = load_config()
    if "startup" not in cfg:
        cfg["startup"] = True
        save_config(cfg)
    set_startup_enabled(cfg["startup"])


def toggle_startup(icon, item):
    cfg = load_config()
    new_state = not cfg.get("startup", True)
    cfg["startup"] = new_state
    save_config(cfg)
    set_startup_enabled(new_state)
    icon.menu = build_menu()


def is_startup_enabled(item=None):
    return load_config().get("startup", True)


def quit_app(icon, item):
    icon.stop()
    os._exit(0)


def build_menu():
    return pystray.Menu(
        pystray.MenuItem(f"현재 단축키: {current_hotkey}", None, enabled=False),
        pystray.MenuItem("단축키 변경", capture_new_hotkey),
        pystray.MenuItem("Windows 시작 시 자동 실행", toggle_startup, checked=is_startup_enabled),
        pystray.MenuItem("종료", quit_app),
    )


def main():
    if sys.platform != "win32":
        print("이 프로그램은 Windows 전용입니다.")
        sys.exit(1)

    ensure_startup_default()
    register_hotkey(load_config().get("hotkey", DEFAULT_HOTKEY))

    icon = pystray.Icon("han_young_toggle", build_icon(64), "한/영 전환기", build_menu())
    icon.run()


if __name__ == "__main__":
    main()
