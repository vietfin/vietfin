Active
======

Get the most actively traded stocks based on trading volume.

Example:

Use ``equity.discovery.active()`` with default parameters: ``provider`` (vndirect), ``exchange`` (hose).

.. code-block:: python

    from vietfin import vf
    
    # Get the most actively traded stocks based on trading volume, in HOSE exchange, from provider VnDirect
    vf.equity.discovery.active()

.. inclusion-marker-do-not-remove

Parameters
----------

============ ========= =================================================== =============== ============= 
 param_name   type      description                                         default_value   is_required  
============ ========= =================================================== =============== ============= 
 exchange     Literal   The stock exchange for retrieving the top movers.   hose            FALSE         
 provider     Literal   The provider to use for the query.                  vndirect        FALSE         
============ ========= =================================================== =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: VnDirect

        ================ ========== ======================================================== 
         field_name       type       description                                             
        ================ ========== ======================================================== 
         symbol           str        Symbol representing the stock satisfying the criteria.  
         price            float      Last price of the stock.                                
         change           float      Change in price value.                                  
         percent_change   float      Percent change in price value.                          
         volume           float      Trading volume averaged over 20 days.                   
         trading_value    float      Trading value, i.e. price * volume, unit VND.           
         updated_at       datetime   Date and time of the last data update.                       
        ================ ========== ======================================================== 

Data Sources
------------

- VnDirect: `banggia.vndirect.com.vn <https://banggia.vndirect.com.vn/thong-tin-thi-truong/tieu-diem-thi-truong>`_
