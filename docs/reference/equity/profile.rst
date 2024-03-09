Profile
=======

Get general information about a company via its stock ticker.

Example:

Get info about company VPBank via its stock ticker VPB, using default ``provider`` (TCBS).

.. code-block:: python

    from vietfin import vf

    vf.equity.profile(symbol="vpb")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 provider     Literal           The provider to use for the query.           tcbs            FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ================== ====== ======================================================= 
         field_name         type   description                                            
        ================== ====== ======================================================= 
         symbol             str    Symbol representing the entity requested in the data.  
         name               str    Common name of the company.                            
         legal_name         str    Official legal name of the company.                    
         exchange           str    Stock exchange where the stock ticker is traded.       
         long_description   str    Long description of the company.                       
         company_url        str    URL of the company's website.                          
         employees          int    Number of employees working for the company.           
         industry           str    Category of industry in which the company operates.    
        ================== ====== ======================================================= 
