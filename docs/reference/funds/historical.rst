Historical
==========

Get historical price of a mutual fund.

Example:

Get historical price of ticker VESAF, using default parameters: ``provider`` (Fmarket), ``start_date`` (None), ``end_date`` (None).

.. code-block:: python

    from vietfin import vf

    vf.funds.historical(symbol="vesaf")

Parameters
----------

============ ====== =============================================== =============== ============= 
 param_name   type   description                                     default_value   is_required  
============ ====== =============================================== =============== ============= 
 symbol       str    Symbol to get data for.                                         TRUE         
 start_date   str    Start date of the data, in YYYY-MM-DD format.   None            FALSE        
 end_date     str    End date of the data, in YYYY-MM-DD format.     None            FALSE        
 provider     str    The provider to use for the query               fmarket         FALSE        
============ ====== =============================================== =============== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: Fmarket

        ============ =================== ======================= 
         field_name   type                description            
        ============ =================== ======================= 
         date_nav     date                The date of the data.  
         open         float               The open price.        
         high         float               The high price.        
         low          float               The low price.         
         close        float               The close price.       
         volume       int                 The trading volume.    
        ============ =================== =======================