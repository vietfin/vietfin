Balance
=======

Get the balance sheet of a company.

Example:

Use ``equity.fundamental.balance()`` with default parameters: ``provider`` (TCBS), ``period`` (annual).

.. code-block:: python

    from vietfin import vf
    
    # Get the balance sheet of company ACB
    vf.equity.fundamental.balance(symbol="acb")

.. inclusion-marker-do-not-remove

Parameters
----------

============ ============================== ==================================== =============== ============= 
 param_name   type                           description                          default_value   is_required  
============ ============================== ==================================== =============== ============= 
 symbol       str                            Symbol to get data for.                              TRUE         
 period       Literal["annual", "quarter"]   Time period of the data to return.   annual          FALSE         
 provider     Literal["tcbs", "ssi"]         The provider to use for the query.   tcbs            FALSE         
============ ============================== ==================================== =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ================ ======= ======================================================= 
         field_name       type    description                                            
        ================ ======= ======================================================= 
         fiscal_year      int     Fiscal year.                                           
         fiscal_quarter   int     Fiscal quarter.                                        
         period           str     Time period of the data to return.                     
         items            str     Line item in the financial statement.                  
         values           float   Value of the line item.                               
         symbol           str     Symbol representing the entity requested in the data.  
        ================ ======= ======================================================= 

    .. tab-item:: SSI

        ================ ======= ======================================================= 
         field_name       type    description                                            
        ================ ======= ======================================================= 
         fiscal_period    str     Fiscal period. E.g. "2023", "Q1 2021"                                           
         period           str     Time period of the data to return.                     
         items            str     Line item in the financial statement.                  
         values           float   Value of the line item.                               
        ================ ======= ======================================================= 
