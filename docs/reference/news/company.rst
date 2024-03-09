Company
=======

Get the news related to a company via its stock ticker.

Example:

Get the news related to stock ticker VNM, using default parameters: ``provider`` (tcbs), ``limit`` (100).

.. code-block:: python

    from vietfin import vf

    vf.news.company(symbol="vnm")

Company
-------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 limit        int               - The number of data entries to return.      100             FALSE
                                - ``0`` will return all available records.         
 provider     Literal           The provider to use for the query            tcbs            FALSE         
============ ================= ============================================ =============== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: TCBS

        ==================== ========== ======================================================= 
         field_name           type       description                                            
        ==================== ========== ======================================================= 
         date_published       datetime   Date and time when the news article was published.     
         title                str        Title of the news article.                             
         source               str        Source of the news article.                            
         price                float      Price of the stock at that moment.                     
         price_change         float      Price change of the stock.                             
         price_change_ratio   float      Price change ratio of the stock.                       
         symbol               str        Symbol representing the entity requested in the data.  
        ==================== ========== ======================================================= 
