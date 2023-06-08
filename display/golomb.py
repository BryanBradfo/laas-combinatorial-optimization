# -*- encoding: utf-8 -*-

import math
import matplotlib.pyplot as plt


def golomb(ms, figsize=None):
    """ Display a golomb ruler solution.

    Parameters:
      - ms List of marks (values).
      - figsize Size of the figure. """

    ms = sorted(ms)
    d = [(ms[j] - ms[i], ms[i])
         for i in range(len(ms)) for j in range(i + 1, len(ms))]
    d = sorted(d)

    if figsize is None:
        figsize = (16, 5 + len(ms) * math.log(len(ms)))

    fig, ax = plt.subplots(figsize=figsize)

    ax.plot([0, max(ms)], [0, 0])
    for m in ms:
        ax.plot([m, m], [-0.1, 0.1], 'k')
        ax.text(m, 0.2, str(m), horizontalalignment='center')

    c = -0.15
    for di, mi in d:
        ax.arrow(mi + 0.1, c, di - 0.2, 0, head_width=0.03,
                 head_length=0.1)
        ax.arrow(mi + 0.2, c, -0.1, 0, head_width=0.03,
                 head_length=0.1)
        ax.text(mi + di / 2, c + 0.02, str(di), horizontalalignment='center')
        c -= 0.1

    ax.axis([-1, max(ms) + 1, c, 0.3])
    ax.tick_params(which='both', bottom='off', left='off',
                   labelbottom='off', labelleft='off')

    plt.show()
