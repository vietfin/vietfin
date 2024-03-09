Ratios
======

Get the key financial ratios data of a company over time.

Example:

Use ``equity.fundamental.ratios()`` with default parameters: ``provider`` (TCBS), ``period`` (annual).

.. code-block:: python

    from vietfin import vf
    
    # Get the key financial ratios data of company MWG
    vf.equity.fundamental.ratios(symbol="mwg")

Parameters
----------

============ ============================== ==================================== =============== ============= 
 param_name   type                           description                          default_value   is_required  
============ ============================== ==================================== =============== ============= 
 symbol       str                            Symbol to get data for.                              TRUE         
 period       Literal["annual", "quarter"]   Time period of the data to return.   annual          FALSE         
 provider     Literal["tcbs"]                The provider to use for the query.   tcbs            FALSE         
============ ============================== ==================================== =============== =============

Data Model
----------

.. tab-set::

    .. tab-item:: TCBS

        ========================= ====== ======================================================= 
         field_name                type   description                                            
        ========================= ====== ======================================================= 
         symbol                    str    Symbol representing the entity requested in the data.  
         period                    str    Time period of the data to return.                     
         fiscal_year               int    Fiscal year.                                           
         fiscal_quarter            int    Fiscal quarter.
         priceToEarning             
         priceToBook             
         valueBeforeEbitda             
         dividend             
         roe             
         roa             
         daysReceivable             
         daysInventory             
         daysPayable             
         ebitOnInterest             
         earningPerShare             
         bookValuePerShare             
         equityOnTotalAsset             
         equityOnLiability             
         currentPayment             
         quickPayment             
         epsChange             
         ebitdaOnStock             
         grossProfitMargin             
         operatingProfitMargin             
         postTaxMargin             
         debtOnEquity             
         debtOnAsset             
         debtOnEbitda             
         shortOnLongDebt             
         assetOnEquity             
         capitalBalance             
         cashOnEquity             
         cashOnCapitalize             
         cashCirculation             
         revenueOnWorkCapital             
         capexOnFixedAsset            
         revenueOnAsset             
         postTaxOnPreTax             
         ebitOnRevenue             
         preTaxOnEbit             
         payableOnEquity             
         ebitdaOnStockChange             
         bookValuePerShareChange                                                     
        ========================= ====== ======================================================= 
        