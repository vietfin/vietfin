Quote
=====

Get the latest quote of a futures contract.

Example:

Use ``equity.futures.quote()`` with default parameters: ``provider`` (SSI), ``limit`` (100).

.. code-block:: python

    from vietfin import vf
    
    # Get the latest quote data of futures contract VN30F2404
    vf.equity.futures.historical(symbol="VN30F2404")

Parameters
----------

============ ======== =============================================== =============== ============= 
 param_name   type     description                                     default_value   is_required  
============ ======== =============================================== =============== ============= 
 symbol       str      Symbol to get data for.                                         TRUE         
 limit        int      The number of records to return.                100             FALSE        
 provider     Literal  The provider to use for the query               ssi             FALSE        
============ ======== =============================================== =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: SSI

        ====================== ======= ============================================================================================= 
         field_name             type    description                                                                                  
        ====================== ======= ============================================================================================= 
         date_session           date    Date of the session of the quote.                                                            
         time                   time    Time of the quote execution.                                                                 
         symbol                 str     Unique identifier representing the futures contract.                                         
         volume                 int     Volume of contracts in the quote.                                                            
         price                  float   Price of the quote.                                                                          
         status                 str     Buy / Sell / Unfilled. Convey the idea that the order has been fulfilled (executed) or not.  
         price_change           float   Change in price from the session's reference price, in absolute value.                       
         price_change_percent   float   Change in price from the current reference price, in percent.                                
         ref_price              float   Reference or opening price for the trading session.                                          
         id                     str     Unique identifier representing the quote.                                                    
        ====================== ======= ============================================================================================= 

.. NOTE: 2024-04-22 removed VDSC from available data providers since v0.2.0 release. But keep the table below as archives, in case it will be needed in the future.
.. .. tab-item:: VDSC

..     =================== ======= ==================================================================================== 
..      field_name          type    description                                                                         
..     =================== ======= ==================================================================================== 
..      time                time    Time of the latest trade execution                                                  
..      symbol              str     Unique identifier representing the futures contract                                 
..      exchange            str     Unique identifier representing the trading floor or exchange                        
..      ref_price           float   Reference or opening price for the trading session                                  
..      high_price          float   Highest price reached during the current trading session                            
..      low_price           float   Lowest price reached during the current trading session                             
..      matched_vol         int     Volume of contracts traded in the last match                                        
..      matched_price       float   Price at which the last trade occurred                                              
..      matched_change      float   Change in price from the last matched trade                                         
..      avg_price           float   Average price of the contracts traded                                               
..      matched_total_vol   int     Total volume of contracts traded                                                    
..      bid_price_1         float   Best bid price                                                                      
..      bid_vol_1           int     Best bid volume                                                                     
..      bid_price_2         float                                                                              
..      bid_vol_2           int      
..      bid_price_3         float                                                                              
..      bid_vol_3           int
..      offer_price_1       float   Best offer (ask) price                                                              
..      offer_vol_1         int     Best offer (ask) volume   
..      offer_price_2       float                                                                 
..      offer_vol_2         int                      
..      offer_price_3       float                                                                 
..      offer_vol_3         int                                                      
..      ceil_price          float   Closing price of the previous trading day                                           
..      floor_price         float   The lowest price level at which a futures contract or security is allowed to trade  
..      am_pm               str     Indicates whether it is the morning (AM) or afternoon (PM) trading session          
..     =================== ======= ==================================================================================== 

Data Sources
------------

- SSI: `iboard.ssi.com.vn <https://iboard.ssi.com.vn/>`_
- VDSC Rong Viet: `livedragon.vdsc.com.vn <https://livedragon.vdsc.com.vn/fos/fos.rv>`_