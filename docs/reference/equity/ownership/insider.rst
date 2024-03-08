Insider Trading
===============

Get data about trading made by a company's management team and board of directors.

Example:

Use ``equity.ownership.insider_trading()`` with default parameters: ``provider`` (TCBS), ``limit`` (100).

.. code-block:: python

    from vietfin import vf
    
    # Get 100 most recent insider trading of company BVH
    vf.equity.ownership.insider_trading(symbol="bvh")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 limit        int               - The number of data entries to return.      100             FALSE
                                - ``0`` will return all available records.         
 provider     Literal["tcbs"]   The provider to use for the query            tcbs            FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ============================ ======= ============================================================================= 
         field_name                   type    description                                                                  
        ============================ ======= ============================================================================= 
         filing_date                  date    Filing date of the trade.                                                    
         acquisition_or_disposition   str     Acquisition or disposition of the shares. e.g. "Mua", "Bán"                  
         transaction_price            float   Price at which the transaction was executed.                                 
         securities_transacted        float   Number of securities transacted by the reporting individual.                 
         owner_type                   str     Type of the owner. e.g. "Cổ đông lớn", "Cổ đông sáng lập", "Cổ đông nội bộ"  
         symbol                       str     Ticker of the company.                                                       
        ============================ ======= ============================================================================= 
