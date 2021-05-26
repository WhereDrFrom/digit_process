import matplotlib.pyplot as plt
import numpy as np
import thinkdsp

def stretch(sign,ts,framerate):
    sign.ts+=ts
    sign.framerate*=framerate
    return sign
