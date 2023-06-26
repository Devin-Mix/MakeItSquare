import numpy as np
import soundfile as sf
from sys import argv

def main(filename: str, outname: str="./out.wav", threshold: float=0.0) -> int:
    inframes = sf.read(filename)
    stereo = True
    if inframes[0].ndim == 1:
        lframes = inframes[0]
        stereo = False
    else:
        lframes = inframes[0][:, 0]
        rframes = inframes[0][:, 1]
    lframes_new = lframes.copy()
    lframes_new.fill(1.)
    if stereo:
        rframes_new = rframes.copy()
        rframes_new.fill(1.)
    last_mark_l = 1.
    last_mark_r = 1.
    for ii in range(np.size(lframes)):
        if ii > 0:
            if last_mark_l < lframes[ii] - threshold:
                lframes_new[ii] = 1.
                last_mark_l = lframes[ii]
            elif last_mark_l > lframes[ii] + threshold:
                lframes_new[ii] = -1.
                last_mark_l = lframes[ii]
            else:
                lframes_new[ii] = lframes_new[ii - 1]
            if stereo:
                if last_mark_r < rframes[ii] - threshold:
                    rframes_new[ii] = 1.
                    last_mark_r = rframes[ii]
                elif last_mark_r > rframes[ii] + threshold:
                    rframes_new[ii] = -1.
                    last_mark_r = rframes[ii]
                else:
                    rframes_new[ii] = rframes_new[ii - 1]
    if stereo:
        sf.write(outname, np.transpose(np.stack([lframes_new, rframes_new])), inframes[1])
    else:
        sf.write(outname, lframes_new, inframes[1])
    return 1


if __name__ == "__main__":
    if len(argv) == 2:
        main(argv[1])
    elif len(argv) == 3:
        main(argv[1], argv[2])
    else:
        main(argv[1], argv[2], float(argv[3]))
