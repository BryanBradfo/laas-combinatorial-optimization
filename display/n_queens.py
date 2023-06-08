# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from .utils import read_image, \
     get_value_or_domain


def n_queens(queens, ax=None):
    """ Display a chessboard with the given queens.

    Parameters:
      - queens List of value (int) or variable (CpoIntVarSolution)
        representing the columns for the N queens. Columns start at 0 and
        end at (N - 1).
      - ax If None, a new axes will be created, otherwized will be used
        as the main axes for drawings.
    """

    # Retrieve the number of queens
    n = len(queens)

    # Fill chessboard without queens
    chess_board = np.zeros((n, n, 3))
    for l in range(n):
        for c in range(n):
            if l % 2 == c % 2:
                chess_board[l, c, :] = 1
            else:
                chess_board[l, c, :] = 0

    # Plot chessboard
    show = False
    if ax is None:
        show = True
        _, ax = plt.subplots(figsize=(n / 2, n / 2))

    ax.imshow(chess_board, interpolation='none')

    wq = read_image('WQueen.png')
    bq = read_image('BQueen.png')
    rc = read_image('redcross.png')

    for y, x in enumerate(queens):
        v = get_value_or_domain(x)
        if isinstance(v, list):
            for x_ in range(n):
                if x_ not in v:
                    ax.imshow(rc, extent=[x_ - 0.35, x_ + 0.35,
                                          y - 0.35, y + 0.35],
                              alpha=0.6)
        else:
            if y % 2 == v % 2:
                q = bq
            else:
                q = wq
            ax.imshow(q, extent=[v - 0.4, v + 0.4, y - 0.4, y + 0.4])
            if v is not x:
                for x_ in range(n):
                    if x_ != v:
                        ax.imshow(rc, extent=[x_ - 0.35, x_ + 0.35,
                                              y - 0.35, y + 0.35],
                                  alpha=0.3)

    # Remove ticks, etc.
    ax.set(xticks=np.arange(n),
           yticks=np.arange(n))
    ax.set_xticklabels([
        chr(ord('A') + k) for k in ax.get_xticks()
    ])
    ax.set_yticklabels([
        str(i) for i in range(n)
    ])
    ax.tick_params(which='both', bottom='off', left='off')
    ax.axis('image')

    # Display everything
    if show:
        plt.show()
