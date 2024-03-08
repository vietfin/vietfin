Management
==========

Get the key executive management team data of a company.

Example:

Use ``equity.fundamental.management()`` with default parameters: ``provider`` (TCBS).

.. code-block:: python

    from vietfin import vf
    
    # Get the key executives data of company BIDV
    vf.equity.fundamental.management(symbol="bid")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 provider     Literal["tcbs"]   The provider to use for the query            tcbs            FALSE         
============ ================= ============================================ =============== =============

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ============ ======= ======================================================= 
         field_name   type    description                                            
        ============ ======= ======================================================= 
         name         str     Name of the key executive.                             
         title        str     Designation of the key executive.                      
         weight       float   Weight of the stock ownership.                         
         symbol       str     Symbol representing the entity requested in the data.  
        ============ ======= ======================================================= 
