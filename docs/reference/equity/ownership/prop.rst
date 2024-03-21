Proprietary Trading
===================

Get the trading data of domestic proprietary trading firms of a given stock ticker over time.

Vietnamese: Lịch sử giao dịch khối tự doanh (bộ phận tự doanh của các doanh nghiệp chứng khoán trong nước).

Example:

Use ``equity.ownership.prop_trading()`` with default parameters: ``provider`` (cafef), ``start_date`` (None), ``end_date`` (None).

.. code-block:: python

    from vietfin import vf
    
    # Get the proprietary trading data of stock ticker BVH
    vf.equity.ownership.prop_trading(symbol="bvh")

Parameters
----------

============ ========== =============================================== =============== ============= 
 param_name   type       description                                     default_value   is_required  
============ ========== =============================================== =============== ============= 
 symbol       str        Symbol to get data for.                                         TRUE         
 start_date   str        Start date of the data, in YYYY-MM-DD format.   None            FALSE        
 end_date     str        End date of the data, in YYYY-MM-DD format.     None            FALSE        
 provider     Literal    The provider to use for the query               cafef           FALSE        
============ ========== =============================================== =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: CafeF

        ============ ====== ====================================================================== 
         field_name   type   description                                                           
        ============ ====== ====================================================================== 
         date         date   The date of the data.                                                 
         bid_volume   int    Bid volume. Khối lượng mua bởi khối tự doanh của các cty chứng khoán  
         bid_value    int    Bid value. Giá trị mua bởi khối tự doanh của các cty chứng khoán      
         ask_volume   int    Ask volume. Khối lượng bán bởi khối tự doanh của các cty chứng khoán  
         ask_value    int    Ask value. Giá trị bán bởi khối tự doanh của các cty chứng khoán      
         symbol       str    The stock ticker                                                      
        ============ ====== ====================================================================== 

Data Sources
------------

- CafeF: `s.cafef.vn <https://s.cafef.vn/lich-su-giao-dich-vnindex-4.chn#data>`_