Search
======

Search for ETF. An empty query (by default) returns the full list of ETFs available on selected provider.

Example:

.. code-block:: python
    :caption: Search for an ETF ticker E1VFVN30 using default provider (SSI)

    from vietfin import vf

    vf.etf.search(symbol="E1VFVN30")

.. code-block:: python
    :caption: Retrieve the full list of ETFs available on provider SSI

    vf.etf.search()

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 provider     Literal           The provider to use for the query.           ssi             FALSE         
============ ================= ============================================ =============== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: SSI

        ============ ======= ================================================================================================== 
         field_name   type    description                                                                                       
        ============ ======= ================================================================================================== 
         symbol       str     Symbol of the ETF.                                                                                
         short_name   str     Short name of the ETF.                                                                            
         inav         float   Intraday indicative value of an ETF, giá trị tài sản ròng tham chiếu trên một chứng chỉ quỹ ETF.  
         open         float   Today open price.                                                                                 
         high         float   Today high price.                                                                                 
         low          float   Today low price.                                                                                  
         volume       int     Today trading volume.                                                                             
         exchange     str     Name of the exchange where the ETF is listed.                                                     
        ============ ======= ================================================================================================== 
