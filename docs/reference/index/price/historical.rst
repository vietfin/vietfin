Historical
==========

Get the historical price data of an index.

Example:

Get the historical price data of the index VN30 using default parameters: ``provider`` (tcbs), ``start_date`` (None), ``end_date`` (None), ``interval`` (1d).

.. code-block:: python

    from vietfin import vf

    vf.index.price.historical(symbol="vn30")

Parameters
----------

============ ========== =============================================== =============== ============= 
 param_name   type       description                                     default_value   is_required  
============ ========== =============================================== =============== ============= 
 symbol       str        Symbol to get data for.                                         TRUE         
 start_date   str        Start date of the data, in YYYY-MM-DD format.   None            FALSE        
 end_date     str        End date of the data, in YYYY-MM-DD format.     None            FALSE        
 interval     str        Time interval of the data to return.            1d              FALSE        
 provider     Literal    The provider to use for the query               tcbs            FALSE        
============ ========== =============================================== =============== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: TCBS

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

    .. tab-item:: DNSE

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
