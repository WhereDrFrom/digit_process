#!/user/bin/python
# -*- coding: utf-8 -*-
import os

import numpy as np

from thinkdsp import Sinusoid, PI2, normalize, unbias
from thinkdsp import decorate


def ChangeSpectrum(spectrum):
    spectrum.hs[0]=0
    for i in range(len(spectrum.hs)):
        if spectrum.fs[i]!=0:
            spectrum.hs[i]=spectrum.hs[i]/spectrum.fs[i]
    return spectrum


class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""

    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times

        returns: float wave array
        """
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys