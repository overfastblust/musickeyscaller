"""Scale definitions and a scale-degree based note engine (v3.1)."""

SCALES = {
    "major":            [0, 2, 4, 5, 7, 9, 11],
    "minor":            [0, 2, 3, 5, 7, 8, 10],
    "dorian":           [0, 2, 3, 5, 7, 9, 10],
    "phrygian":         [0, 1, 3, 5, 7, 8, 10],
    "lydian":           [0, 2, 4, 6, 7, 9, 11],
    "mixolydian":       [0, 2, 4, 5, 7, 9, 10],
    "locrian":          [0, 1, 3, 5, 6, 8, 10],

    "harmonic_minor":   [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor":    [0, 2, 3, 5, 7, 9, 11],

    "major_pent":       [0, 2, 4, 7, 9],
    "minor_pent":       [0, 3, 5, 7, 10],
    "blues":            [0, 3, 5, 6, 7, 10],

    "hungarian_minor":  [0, 2, 3, 6, 7, 8, 11],
    "byzantine":        [0, 1, 4, 5, 7, 8, 11],
    "spanish_phrygian": [0, 1, 4, 5, 7, 8, 10],
    "persian":          [0, 1, 4, 5, 6, 8, 11],
    "arabic":           [0, 2, 4, 5, 6, 8, 10],
    "enigmatic":        [0, 1, 4, 6, 8, 10, 11],
    "neapolitan_minor": [0, 1, 3, 5, 7, 8, 11],
    "neapolitan_major": [0, 1, 3, 5, 7, 9, 11],
    "romanian_minor":   [0, 2, 3, 6, 7, 9, 10],
    "ukrainian_dorian": [0, 2, 3, 6, 7, 9, 10],
    "hirajoshi":        [0, 2, 3, 7, 8],
    "iwato":            [0, 1, 5, 6, 10],
    "kumoi":            [0, 2, 3, 7, 9],
    "egyptian":         [0, 2, 5, 7, 10],
    "whole_tone":       [0, 2, 4, 6, 8, 10],
    "diminished":       [0, 2, 3, 5, 6, 8, 9, 11],
}

class ScaleEngine:
    def __init__(self, root_note: int = 60, scale_name: str = "major"):
        self.root_note = int(root_note)
        self.set_scale(scale_name)

    def set_scale(self, name: str) -> None:
        if name not in SCALES:
            raise ValueError(f"Unknown scale: {name}")
        self.scale_name = name
        self.intervals = sorted({int(x) % 12 for x in SCALES[name]})

    def degree_to_midi(self, degree: int, extra_octaves: int = 0) -> int:
        degree = int(degree)
        scale_len = len(self.intervals)
        octave_shift = degree // scale_len
        idx = degree % scale_len
        return self.root_note + self.intervals[idx] + 12 * (octave_shift + int(extra_octaves))
