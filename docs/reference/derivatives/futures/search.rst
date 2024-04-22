Search
======

Search for a futures contract. An empty query (by default) returns the full list of currently available futures contracts from the selected provider.

Examples:

.. code-block:: python
    :caption: Search for futures contract VN30F2409 using default provider (SSI)

    from vietfin import vf

    vf.derivatives.futures.search(symbol="vn30f2409")

.. code-block:: python
    :caption: Retrieve the full list of currently available futures contracts using default provider (SSI)

    vf.derivatives.futures.search()

Parameters
----------

============ ================= ============================================ =============== ============= 
 param_name   type              description                                  default_value   is_required  
============ ================= ============================================ =============== ============= 
 symbol       str               Symbol to get data for.                      ""              FALSE         
 provider     Literal           The provider to use for the query.           ssi             FALSE         
============ ================= ============================================ =============== ============= 

Data Model
----------

.. tab-set::

    .. tab-item:: SSI

        ================= ======= =========================================================================================================================== 
         field_name        type    description                                                                                                                
        ================= ======= =========================================================================================================================== 
         symbol            str     Symbol of the futures contract.                                                                                            
         expiration_date   date    Expiration (a.k.a maturity or expiry date) refers to the last trading day of the futures contract. Ngày đáo hạn hợp đồng.  
         initial_date      date    Refers to the first trading day of the futures contract. Ngày giao dịch đầu tiên.                                          
         price             float   Matched price. Giá khớp lệnh.                                                                                              
         volume            int     Matched volume. Khối lượng khớp lệnh.                                                                                      
         asset             str     Underlying asset. Tài sản cơ sở của hợp đồng tương lai.                                                                    
        ================= ======= =========================================================================================================================== 
 

Data Sources
------------

- SSI: `iboard.ssi.com.vn <https://iboard.ssi.com.vn/>`_

Misc
----

- `Infographic of futures contract. From SSI. Vietnamese. <https://www.ssi.com.vn/khach-hang-ca-nhan/tong-quan-ve-chung-khoan-phai-sinh>`_
- `Basic terminologies of a futures contract. From Vietstock. Vietnamese. <https://finance.vietstock.vn/chung-khoan-phai-sinh/VN30F1M/hdtl-tong-quan.htm>`_