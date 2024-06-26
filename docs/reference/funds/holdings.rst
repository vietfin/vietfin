Holdings
========

Get the holdings of a mutual fund.

Example:

Get the holdings of fund VESAF, using default parameters: ``provider`` (Fmarket).

.. code-block:: python

    from vietfin import vf

    vf.funds.holdings(symbol="vesaf")

Parameters
----------

============ ========= =============================================== =============== ============= 
 param_name   type      description                                     default_value   is_required  
============ ========= =============================================== =============== ============= 
 symbol       str       Symbol to get data for.                                         TRUE         
 provider     Literal   The provider to use for the query               fmarket         FALSE        
============ ========= =============================================== =============== =============

Data Model
----------

.. tab-set::

    .. tab-item:: Fmarket

        ================ ========== ===================================================== 
         field_name       type       description                                          
        ================ ========== ===================================================== 
         stock_code       str        The code string of the holding.                      
         industry         str        The industry category of the holding.                
         weight           float      The weight of the holding, as a normalized percent.  
         asset_category   str        The asset category of the holding.                   
         update_at        datetime   The date when the data was updated.                  
        ================ ========== ===================================================== 

Data Sources
------------

- Fmarket: `fmarket.vn <https://fmarket.vn/home>`_