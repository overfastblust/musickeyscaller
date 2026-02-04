"""MIDI backend using mido + python-rtmidi (v3.1)."""

import mido

class MidiBackend:
    def note_on(self, note: int, velocity: int): ...
    def note_off(self, note: int): ...
    def close(self): ...

class MidoBackend(MidiBackend):
    def __init__(self, port_name: str = "VirtualKeyboard"):
        self.port = mido.open_output(port_name, virtual=True)

    def note_on(self, note: int, velocity: int = 100) -> None:
        self.port.send(mido.Message("note_on", note=int(note), velocity=int(velocity)))

    def note_off(self, note: int) -> None:
        self.port.send(mido.Message("note_off", note=int(note), velocity=0))

    def close(self) -> None:
        try:
            self.port.close()
        except Exception:
            pass
