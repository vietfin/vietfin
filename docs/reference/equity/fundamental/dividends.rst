Dividends
=========

Get the historical dividends data of a company.

Example:

Use ``equity.fundamental.dividends()`` with default parameters: ``provider`` (TCBS), ``limit`` (100).

.. code-block:: python

    from vietfin import vf
    
    # Get the historical dividends data of company FPT
    vf.equity.fundamental.dividends(symbol="fpt")

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

        ========================== ========== ======================================================= 
         field_name                 type       description                                            
        ========================== ========== ======================================================= 
         symbol                     str        Symbol representing the entity requested in the data.  
         dividend_type              str        Type of the dividend, i.e. "cash", "stock".                
         payment_date               datetime   The payment date of the dividend.                      
         cash_dividend_percentage   float      NOTE: I don't know the description of this field.      
        ========================== ========== ======================================================= 
