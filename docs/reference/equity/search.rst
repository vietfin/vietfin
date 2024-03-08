Search
======

Search for stock symbol. An empty query (by default) returns the full list of listed companies from selected provider.

Example:

.. code-block:: python
    :caption: Search for ticker MSN using default provider (SSI)

    from vietfin import vf

    vf.equity.search(symbol="msn")

.. code-block:: python
    :caption: Retrieve the full list of listed companies using provider WiFeed

    vf.equity.search(provider="wifeed")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 provider     Literal           The provider to use for the query.           ssi             FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: SSI

        ============ ====== =================================================== 
         field_name   type   description                                        
        ============ ====== =================================================== 
         symbol       str    Symbol of the stock ticker.                        
         name         str    Legal name of the company.                         
         short_name   str    Common name of the company.                         
         organ_code   str    Organization code of the company in SSI database.  
        ============ ====== =================================================== 

    .. tab-item:: WiFeed

        ============ ====== ==================================================== 
         field_name   type   description                                         
        ============ ====== ==================================================== 
         symbol       str    Symbol of the stock ticker.                         
         name         str    Common name of the company.                                
         exchange     str    The code of exchange where the stock is listed on.  
        ============ ====== ==================================================== 
