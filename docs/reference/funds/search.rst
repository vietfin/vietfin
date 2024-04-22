Search
========

Search for a mutual fund. An empty string (by default) will return all available funds on a provider.

Example:

Get the list of all available funds, using default parameters: ``provider`` (Fmarket), ``symbol`` ("", an empty string).

.. code-block:: python

    from vietfin import vf

    vf.funds.search()

Parameters
----------

============ ========= =============================================== =============== ============= 
 param_name   type      description                                     default_value   is_required  
============ ========= =============================================== =============== ============= 
 symbol       str       Symbol to get data for.                         ""              FALSE         
 provider     Literal   The provider to use for the query               fmarket         FALSE        
============ ========= =============================================== =============== =============

Data Model
----------

.. tab-set::

    .. tab-item:: Fmarket

        ================ ========== ========================================================== 
         field_name       type       description                                               
        ================ ========== ========================================================== 
         fund_id          int        ID of a fund in Fmarket database.                         
         short_name       str        Common name of a fund.                                    
         name             str        Legal official name of a fund.                            
         inception_date   datetime   Date of inception of a fund.                              
         management_fee   float      Annual management fee of a fund. Unit: percent per year.  
         nav              float      Current Net Asset Value of a fund.                        
         fund_owner       str        Name of the Organization issuing the fund.                
         fund_type        str        Type of fund. E.g. "stock", "bond", "balanced".            
        ================ ========== ========================================================== 

Data Sources
------------

- Fmarket: `fmarket.vn <https://fmarket.vn/home>`_