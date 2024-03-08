Search
======

Search for an index. An empty string (by default) will return all available indices on a provider.

Example:

Get the list of all available indices, using default parameters: ``provider`` (SSI), ``symbol`` ("", an empty string).

.. code-block:: python

    from vietfin import vf

    vf.index.search()

Parameters
----------

============ ========= ==================================== ================== ============= 
 param_name   type      description                          default_value      is_required  
============ ========= ==================================== ================== ============= 
 symbol       str       Symbol to get data for.              "" (empty string)  FALSE        
 provider     Literal   The provider to use for the query.   ssi                FALSE        
============ ========= ==================================== ================== ============= 

Returns
-------

.. tab-set::

    .. tab-item:: SSI

        ================ ========== ========================================================== 
         field_name       type       description                                               
        ================ ========== ========================================================== 
         index_symbol     str        Symbol of an index.                                        
         group_by_index   str        The parent index from which the given index is derived.    
        ================ ========== ========================================================== 
