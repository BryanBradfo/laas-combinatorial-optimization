# -*- encoding: utf-8 -*-

import matplotlib
matplotlib.use('module://ipykernel.pylab.backend_inline')

from .kakuro import kakuro      # noqa: F401
from .n_queens import n_queens  # noqa: F401
from .sudoku import sudoku      # noqa: F401
from .golomb import golomb      # noqa: F401
