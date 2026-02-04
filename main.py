from __future__ import annotations

import config
from scale import ScaleEngine
from mapper import NoteMapper
from midi_backend import MidoBackend
from keyboard import KeyboardListener

# key -> midi_note mapping for correct NOTE_OFF
ACTIVE_KEYS: dict[str, int] = {}

SCALE_HOTKEYS = {
    "1": "major",
    "2": "minor",
    "3": "dorian",
    "4": "phrygian",
    "5": "lydian",
    "6": "mixolydian",
    "7": "locrian",
    "8": "harmonic_minor",
    "9": "melodic_minor",
    "0": "blues",
}

def banner(engine: ScaleEngine, mapper: NoteMapper):
    print("=== Virtual Keyboard → MIDI (v3.1) ===")
    print(f"Root note: {config.ROOT_NOTE} (C4=60)")
    print(f"Scale: {engine.scale_name} -> {engine.intervals}")
    print("")
    print("Play blocks (degree chaining):")
    print("  1) ", "".join(config.ROW3))
    print("  2) ", "".join(config.ROW2))
    print("  3) ", "".join(config.ROW1))
    print("")
    print("Hotkeys:")
    print(f"  {config.OCTAVE_DOWN_KEY} / {config.OCTAVE_UP_KEY}: global octave down/up")
    print("  1..9,0: change scale")
    print("  ESC: quit")
    print("")

def main():
    engine = ScaleEngine(root_note=config.ROOT_NOTE, scale_name=config.DEFAULT_SCALE)
    mapper = NoteMapper(engine)
    backend = MidoBackend()

    banner(engine, mapper)
    print("MIDI output port: VirtualKeyboard")

    def on_press(k: str):
        # Exit
        if k == config.EXIT_KEY:
            backend.close()
            raise SystemExit

        # Octave shift
        if k == config.OCTAVE_DOWN_KEY:
            mapper.shift_global_octave(-1)
            print(f"Global octave shift: {mapper.global_octave_shift}")
            return
        if k == config.OCTAVE_UP_KEY:
            mapper.shift_global_octave(1)
            print(f"Global octave shift: {mapper.global_octave_shift}")
            return

        # Scale switching
        if k in SCALE_HOTKEYS:
            engine.set_scale(SCALE_HOTKEYS[k])
            print(f"Scale changed to: {engine.scale_name} -> {engine.intervals}")
            return

        # Notes
        if k in ACTIVE_KEYS:
            return

        note = mapper.key_to_midi(k)
        if note is None:
            return

        ACTIVE_KEYS[k] = note
        backend.note_on(note, velocity=config.VELOCITY)

    def on_release(k: str):
        if k not in ACTIVE_KEYS:
            return

        note = ACTIVE_KEYS.pop(k)
        backend.note_off(note)

    listener = KeyboardListener(on_press, on_release)
    listener.start()
    listener.join()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
