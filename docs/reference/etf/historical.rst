Historical
==========

Get historical price of an ETF.

Example:

Get historical price of an ETF ticker E1VFVN30, using default parameters: ``provider`` (SSI), ``start_date`` (None), ``end_date`` (None), ``interval`` (1d), 

.. code-block:: python

    from vietfin import vf

    vf.etf.historical(symbol="E1VFVN30")

Parameters
----------

============ ====== =============================================== =============== ============= 
 param_name   type   description                                     default_value   is_required  
============ ====== =============================================== =============== ============= 
 symbol       str    Symbol to get data for.                                         TRUE         
 start_date   str    Start date of the data, in YYYY-MM-DD format.   None            FALSE        
 end_date     str    End date of the data, in YYYY-MM-DD format.     None            FALSE        
 interval     str    Time interval of the data to return.            1d              FALSE        
 provider     str    The provider to use for the query               ssi             FALSE        
============ ====== =============================================== =============== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: SSI

        ============ =================== ======================= 
         field_name   type                description            
        ============ =================== ======================= 
         date         date                The date of the data.  
         open         float               The open price.        
         high         float               The high price.        
         low          float               The low price.         
         close        float               The close price.       
         volume       int                 The trading volume.    
        ============ =================== =======================