Major Holders
=============

Get data about major holders of a given company over time.

Example:

Use ``equity.ownership.major_holders()`` with default parameters: ``provider`` (TCBS).

.. code-block:: python

    from vietfin import vf
    
    # Get 100 most recent insider trading of company BVH
    vf.equity.ownership.major_holders(symbol="bvh")

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                                      TRUE         
 provider     Literal           The provider to use for the query            tcbs            FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        =============== ======= ======================================= 
         field_name      type    description                            
        =============== ======= ======================================= 
         investor_name   str     Investor name of the stock ownership.  
         weight          float   Weight of the stock ownership.         
        =============== ======= ======================================= 
