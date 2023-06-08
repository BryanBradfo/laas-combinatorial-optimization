# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import string

from .utils import get_figsize, get_font_size, \
     get_value_or_domain, \
     print_domain_in_square


def sudoku(problem, solution=None, figsize=(8, 8)):
    """ Display a sudoku grid with the given (partial) solution.

    Parameters:
      - problem Instance of data.sudoku.problem.
      - solution Either None (no solution), or a 2-dimensional object
        (list of list, ndarray, etc.) containing either value (int) or
        variable (CpoIntVarSolution).
      - figsize Size of the figure (width, height) in inches, or a single
        value representing the width.
    """

    N = problem.N
    K = problem.K

    figsize = get_figsize(figsize, (N, N))

    fig, ax = plt.subplots(figsize=figsize)

    if N < 10:
        numbers = string.digits
    elif N < 26:
        numbers = ' ' + string.ascii_uppercase

    kargs = {
        'color': 'k',
        'fontsize': get_font_size(figsize[0], N)
    }

    for l in range(N):
        for c in range(N):

            v = problem[l][c]
            s = " "
            if v > 0:
                s = numbers[v]
                ax.text(c + 0.5, N - 0.5 - l, s,
                        va='center', ha='center',
                        **kargs)

    kargs['color'] = 'b'
    if solution:
        for l in range(N):
            for c in range(N):
                if problem[l][c] == 0:
                    v = get_value_or_domain(solution[l][c])
                    if isinstance(v, list):
                        print_domain_in_square(ax, N, (l, c), v,
                                               numbers=numbers)
                    else:
                        s = numbers[v]
                        ax.text(c + 0.5, N - 0.5 - l, s,
                                va='center', ha='center',
                                **kargs)

    # Draw grids, hide ticks, etc.
    mj_ticks = range(0, N + 1, K)
    mn_ticks = [i for i in range(N) if i % K != 0]
    ax.set_xticks(mj_ticks)
    ax.set_xticks(mn_ticks, minor=True)
    ax.set_yticks(mj_ticks)
    ax.set_yticks(mn_ticks, minor=True)

    ax.grid(b=True, which='minor', color=[.7, .7, .7])
    ax.grid(b=True, which='major', color='k')
    ax.tick_params(which='both', bottom='off', left='off',
                   labelbottom='off', labelleft='off')

    # Display
    plt.show()
