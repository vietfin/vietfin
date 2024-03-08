Income
======

Get the income statement of a company.

Example:

Use ``equity.fundamental.income()`` with default parameters: ``provider`` (TCBS), ``period`` (annual).

.. code-block:: python

    from vietfin import vf
    
    # Get the income statement of company VPB
    vf.equity.fundamental.income(symbol="vpb")

.. include:: balance.rst
    :start-after: inclusion-marker-do-not-remove