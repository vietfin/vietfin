Constituents
============

Get the list of constituents of an index.

Example:

Get the list of the index VN30 using default parameters: ``provider`` (SSI).

.. code-block:: python

    from vietfin import vf

    vf.index.constituents(symbol="vn30")

Parameters
----------

============ ========= ==================================== ================== ============= 
 param_name   type      description                          default_value      is_required  
============ ========= ==================================== ================== ============= 
 symbol       str       Symbol to get data for.              "" (empty string)  FALSE        
 provider     Literal   The provider to use for the query.   ssi                FALSE        
============ ========= ==================================== ================== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: SSI

        ============ ======= =============================================== 
         field_name   type    description                                    
        ============ ======= =============================================== 
         symbol       str     Symbol representing the stock ticker.          
         name         str     Name of the constituent company in the index.  
         open         float   The open price.                                
         high         float   The high price.                                
         low          float   The low price.                                 
         volume       int     The trading volume.                            
         prev_close   float   The previous close price.                      
         exchange     str     The exchange where the stock is listed.        
        ============ ======= =============================================== 

Data Sources
------------

- SSI: `iboard.ssi.com.vn <https://iboard.ssi.com.vn/>`_