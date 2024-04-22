Foreign Trading
===============

Get the trading data of foreign entities of a given stock ticker over time.

Vietnamese: Lịch sử giao dịch khối ngoại (nhà đầu tư nước ngoài).

Example:

Use ``equity.ownership.foreign_trading()`` with default parameters: ``provider`` (cafef), ``start_date`` (None), ``end_date`` (None).

.. code-block:: python

    from vietfin import vf
    
    # Get foreign trading data of stock ticker BVH
    vf.equity.ownership.foreign_trading(symbol="bvh")

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

        ==================== ======= =============================================================================== 
         field_name           type    description                                                                    
        ==================== ======= =============================================================================== 
         date                 date    The date of the data.                                                          
         net_trading_volume   int     Net trading volume. Khối lượng giao dịch ròng.                                 
         net_trading_value    int     Net trading value. Giá trị giao dịch ròng.                                     
         bid_volume           int     Bid volume. Khối lượng mua bởi nhà đầu tư nước ngoài.                          
         bid_value            int     Bid value. Giá trị mua bởi nhà đầu tư nước ngoài.                              
         ask_volume           int     Ask volume. Khối lượng bán bởi nhà đầu tư nước ngoài.                          
         ask_value            int     Ask value. Giá trị bán bởi nhà đầu tư nước ngoài.                              
         remaining_room       int     Remaining room. Khối lượng còn lại mà nhà đầu tư nước ngoài có thể sở hữu.     
         weight               float   Current Ownership Percent. Tỷ lệ % sở hữu hiện tại của nhà đầu tư nước ngoài.  
         close_price          float   Current daily close price of the stock ticker.                                 
         percent_change       float   Percent change of the stock ticker compared to previous session.               
        ==================== ======= =============================================================================== 

Data Sources
------------

- CafeF: `s.cafef.vn <https://s.cafef.vn/lich-su-giao-dich-vnindex-3.chn#data>`_