CSS Colors
==========

CSS Colors is a simple module for defining CSS 3 compatible colors.

The complete list of named colors is provided in the ``colors`` module.
``Color``, a ``namedtuple`` class in the ``color`` module provides conversion
functions. The ``parse`` module parses string representations of colors. The
``color`` function is designed to support ``argparse``, e.g.:

.. code-block:: python

    from csscolor import colors, parse
    parser.add_argument('-c', '--color', type=parse.color, default=colors.black)


Contents:

.. toctree::
   :maxdepth: 2

   color
   colors
   parse

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

