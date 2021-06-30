#!/user/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from thinkdsp import Chirp
from thinkdsp import normalize, unbias

PI2 = 2 * np.pi
class SawtoothChirp(Chirp):
     
     def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys



