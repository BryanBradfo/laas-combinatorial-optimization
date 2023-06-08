# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from .utils import get_figsize, get_font_size, \
     get_value_or_domain, \
     print_domain_in_square


def kakuro(problem, solution=None, figsize=10):

    """ Display a Kakuro problem with its solution (if specified).

    Parameters:
      - problem Instance of data.kakuro.problem.
      - solution Either None (no solution), or a dictionary mapping
        position (row, col) to value (int) or variable (CpoIntVarSolution).
      - figsize Size of the figure (width, height) in inches, or a single
        value representing the width.

    """

    # retrieve n rows / columns from problem
    nrows, ncols = problem.nrows, problem.ncolumns

    # custom figsize
    figsize = get_figsize(figsize, (nrows, ncols))

    def get_position(cell):
        if type(cell) is not tuple:
            cell = cell.position
        return np.array([cell[1], nrows - cell[0] - 1])

    fig, ax = plt.subplots(figsize=figsize)

    bg_color = '#1f77b4'

    isizes = fig.get_size_inches()
    fontsize = min(
        get_font_size(isizes[0], problem.nrows),
        get_font_size(isizes[1], problem.ncolumns)
    )

    kargs = {
        'color': bg_color,
        'fontsize': fontsize / 2
    }

    for row in problem:
        for cell in row:
            pos = get_position(cell)
            if cell.is_black():
                ax.add_patch(plt.Rectangle(pos, 1, 1, color=bg_color))
            elif cell.is_empty():
                pass
            else:
                bottri = None
                if cell.bottom:
                    ax.text(pos[0] + 0.35, pos[1] + 0.25,
                            str(cell.bottom[0]),
                            va='center', ha='center',
                            **kargs)
                else:
                    bottri = np.array([
                        pos, (pos[0], pos[1] + 1), (pos[0] + 1, pos[1])
                    ])
                if cell.right:
                    ax.text(pos[0] + 0.75, pos[1] + 0.65,
                            str(cell.right[0]),
                            va='center', ha='center',
                            **kargs)
                else:
                    bottri = np.array([
                        (pos[0], pos[1] + 1), pos + 1, (pos[0] + 1, pos[1])
                    ])
                if bottri is not None:
                    ax.add_patch(plt.Polygon(bottri, color=bg_color))
                else:
                    ax.plot([pos[0], pos[0] + 1], [pos[1] + 1, pos[1]],
                            color=bg_color, linestyle='-', linewidth=1)

    kargs = {
        'color': 'k',
        'fontsize': fontsize
    }
    if solution:
        for (i, j), v in solution.items():

            pos = get_position((i, j))
            v = get_value_or_domain(v)

            if isinstance(v, list):
                print_domain_in_square(ax, nrows, (i, j), v)
            else:
                ax.text(pos[0] + 0.5, pos[1] + 0.5,
                        str(v), va='center', ha='center',
                        **kargs)

    # Remove ticks, etc.
    ax.set(xticks=np.arange(ncols),
           yticks=np.arange(nrows))
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(which='both', bottom='off', left='off')

    ax.grid(b=True, which='major', color=[.7, .7, .7])

    # Display
    plt.show()
