"""Maps keys to scale degrees and then to MIDI notes (v3.1)."""

import config
from scale import ScaleEngine

KEY_TO_DEGREE: dict[str, int] = {k: i for i, k in enumerate(config.PLAY_KEYS)}

class NoteMapper:
    def __init__(self, engine: ScaleEngine):
        self.engine = engine
        self.global_octave_shift = 0

    def shift_global_octave(self, delta: int) -> None:
        self.global_octave_shift += int(delta)

    def key_to_midi(self, key: str) -> int | None:
        if key not in KEY_TO_DEGREE:
            return None
        degree = KEY_TO_DEGREE[key]
        return self.engine.degree_to_midi(degree, extra_octaves=self.global_octave_shift)
