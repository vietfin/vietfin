Historical
==========

Get the historical price data of a futures contract.

Example:

Use ``equity.futures.historical()`` with default parameters: ``provider`` (TCBS), ``end_date`` (None), ``start_date`` (None).

.. code-block:: python

    from vietfin import vf
    
    # Get the historical price data of futures contract VN30F1M
    vf.equity.futures.historical(symbol="VN30F1M")

Parameters
----------

============ ====== =============================================== =============== ============= 
 param_name   type   description                                     default_value   is_required  
============ ====== =============================================== =============== ============= 
 symbol       str    Symbol to get data for.                                         TRUE         
 start_date   str    Start date of the data, in YYYY-MM-DD format.   None            FALSE        
 end_date     str    End date of the data, in YYYY-MM-DD format.     None            FALSE        
 provider     str    The provider to use for the query               tcbs            FALSE        
============ ====== =============================================== =============== ============= 

Data Model
----------

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
         volume       Union[int, float]   The trading volume.    
        ============ =================== =======================