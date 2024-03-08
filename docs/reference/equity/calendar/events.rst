Events
======

Get historical events of a company.

Example:

Use ``equity.calendar.events()`` with default parameters: ``provider`` (TCBS), ``limit`` (100)

.. code-block:: python

    from vietfin import vf
    
    # Get 100 most recent events of company SSI
    vf.equity.calendar.events(symbol="ssi")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 limit        int               - The number of data entries to return.      100             FALSE
                                - ``0`` will return all available records.         
 provider     Literal["tcbs"]   The provider to use for the query            tcbs            FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ==================== ========== ======================================================= 
         field_name           type       description                                            
        ==================== ========== ======================================================= 
         event_code           str        Code of the event.                                     
         event_name           str        Name of the event.                                     
         event_desc           str        Description of the event.                              
         price                float      Price of the stock.                                    
         price_change         float      Price change of the stock.                             
         price_change_ratio   datetime   Price change ratio of the stock.                       
         date_notify          datetime   Date of the notification sent to the public.           
         date_execute         datetime   Execution date of the event.                           
         date_register        datetime   Registration date of the event.                        
         date_ex_right        datetime   Ex-right date of the event.                            
         symbol               str        Symbol representing the entity requested in the data.  
        ==================== ========== ======================================================= 
