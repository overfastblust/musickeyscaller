# Virtual Keyboard → MIDI (v3.1)

## v3.1 Fix
- Correct NOTE_OFF handling: the exact MIDI note started on key press is stored
  and always turned off on key release, even if scale/octave changes while holding.

## Layout (degree chaining)

Keys are chained into a single degree line:
1) zxcvbnm,./
2) asdfghjkl;'
3) qwertyuiop[]

Each next key advances to the next scale degree.

## Install

```bash
pip install mido python-rtmidi pynput
```

## Linux: FluidSynth / QSynth

```bash
sudo apt update
sudo apt install fluidsynth qsynth
sudo modprobe snd-virmidi
```

Connect MIDI port **VirtualKeyboard** to FluidSynth/QSynth.

## Run

```bash
python main.py
```

## Controls

- Play: zxcvbnm,./ asdfghjkl;' qwertyuiop[]
- Octave: `-` down / `=` up
- Scale: `1..9,0`
- Exit: Esc
