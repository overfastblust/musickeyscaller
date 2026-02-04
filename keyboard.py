"""Keyboard listener using pynput (v3.1)."""

from pynput import keyboard

class KeyboardListener:
    def __init__(self, on_press, on_release):
        self._on_press_cb = on_press
        self._on_release_cb = on_release
        self._listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)

    @staticmethod
    def _normalize_key(key) -> str:
        if hasattr(key, "char") and key.char is not None:
            return key.char
        return str(key)

    def _on_press(self, key):
        self._on_press_cb(self._normalize_key(key))

    def _on_release(self, key):
        self._on_release_cb(self._normalize_key(key))

    def start(self):
        self._listener.start()

    def join(self):
        self._listener.join()
