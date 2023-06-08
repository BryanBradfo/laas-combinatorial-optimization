# -*- encoding: utf-8 -*-

import matplotlib.pyplot
import os
import string

from docplex.cp.solution import CpoIntVarSolution


IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'images')


def read_image(name, folder=IMAGE_DIR):
    """ Read an image from the given filename. """
    return matplotlib.pyplot.imread(os.path.join(folder, name))


def get_figsize(figsize, nrows_and_cols):
    """ If `figsize` is a tuple (w, h), returns (w, h), otherwize
    consider figsize as the width and returns corresponding (w, h)
    depending on nrows and ncols. """
    nrows, ncols = nrows_and_cols
    try:
        w, h = figsize
    except:
        w = figsize
        h = figsize / ncols * nrows
    return w, h


def get_font_size(w, N):
    """ Return an appropriate font size to print number in a figure
    of width / height `width` with NxN cells. """
    return 0.4 * w * 72 / N


def get_value_or_domain(v):
    """ Retrieve the domain associated with v.

    Parameters:
      - v CpoIntVarSolution or int.

    Return: d where d is the value of v if v is fully instantiated,
    or the domain of v (i.e. a list of int). If v is not a CpoVarSolution,
    returns v.
    """
    if not isinstance(v, CpoIntVarSolution):
        return v
    v = v.get_value()
    if isinstance(v, tuple):
        u = []
        for d in v:
            if isinstance(d, tuple):
                u.extend(range(d[0], d[1] + 1))
            else:
                u.append(d)
        v = u
    return v


def print_domain_in_square(ax, nRows, pos, v, nbym=(3, 3),
                           numbers=string.digits, padding=0.2,
                           **kargs):

    # retrive line / column
    l, c = pos

    kargs.setdefault('fontsize',
                     get_font_size(min(ax.figure.get_size_inches()),
                                   nRows) / nbym[0])
    kargs.setdefault('color', 'r')

    gap_num = (1 - 2 * padding) / (nbym[0] - 1)
    in_coords = [
        [(padding + gap_num * y,
          padding + gap_num * x) for x in range(nbym[0])]
        for y in range(nbym[1])
    ]

    for ll in range(nbym[0]):
        for cc in range(nbym[1]):
            d = nbym[0] * ll + cc + 1
            s = " "
            if d in v:
                s = numbers[d]
            ax.text(c + in_coords[ll][cc][1],
                    nRows - l - in_coords[ll][cc][0],
                    s, va='center', ha='center',
                    **kargs)
