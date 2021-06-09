#!/user/bin/python
# -*- coding: utf-8 -*-
import os

import numpy as np

from thinkdsp import Sinusoid, PI2, normalize, unbias
from thinkdsp import decorate


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