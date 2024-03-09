:description: VietFin is a Python package which fetch Vietnam stock market data.

======================
VietFin Documentation
======================

VietFin is an open-source tool to web scrape Vietnam stock market data. This package provides a Python interface for publicly available APIs from multiple brokerage firms. It is intended for personal use, research and educational purposes.

Installation
============

VietFin is available on `PyPI <https://pypi.org/>`_. To use the package:

Install VietFin in your project's virtual environment using `Poetry <https://python-poetry.org/>`_.

.. code-block:: shell

   poetry add vietfin

Or using `pip`.

.. code-block:: shell
   
   pip install vietfin

Import the package.

.. code-block:: python

   from vietfin import vf

Use the package.

.. code-block:: python

   vf.equity.search()

.. toctree::
    :caption: Getting Started
    :hidden:

    usage/index
    reference/index

.. toctree::
    :caption: Development
    :hidden:

    development/index