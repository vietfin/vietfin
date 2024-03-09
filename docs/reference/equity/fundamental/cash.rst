Cash
====

Get the cash flow statement of a company.

Example:

Use ``equity.fundamental.cash()`` with default parameters: ``provider`` (TCBS), ``period`` (annual).

.. code-block:: python

    from vietfin import vf
    
    # Get the cash flow statement of company HAG
    vf.equity.fundamental.cash(symbol="hag")

.. include:: balance.rst
    :start-after: inclusion-marker-do-not-remove