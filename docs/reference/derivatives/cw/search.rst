Search
======

Search for a covered warrant. An empty query (by default) returns the full list of currently available covered warrants from the selected provider.

Examples:

.. code-block:: python
    :caption: using default provider (SSI)

    from vietfin import vf

    # Search for the covered warrant CACB2304
    vf.derivatives.cw.search(symbol="CACB2304")

    # Retrieve the full list of currently available covered warrants
    vf.derivatives.cw.search()

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

        =================== ======= =============================================================================== 
         field_name          type    description                                                                    
        =================== ======= =============================================================================== 
         symbol              str     Symbol of the covered warrant. Mã chứng quyền có đảm bảo.                      
         expiration_date     date    The expiry (a.k.a maturity) date of the covered warrant. Ngày đáo hạn.         
         last_trading_date   date    The last trading day of the covered warrant. Ngày giao dịch cuối cùng.         
         issuer              str     Identification code of the issuer (financial institution). Tổ chức phát hành.  
         underlying_asset    str     Underlying asset of the covered warrant. Chứng khoán cơ sở.                    
         strike_price        float   Strike price. Giá thực hiện.                                                   
         close_price         float   Close price. Giá chứng quyền.                                                  
         price_change        float   Price change compared to the previous trading day. Giá thay đổi.               
         price_change_pct    float   Price change percentage. Giá thay đổi theo phần trăm.                          
         volume              int     Matched volume. Khối lượng khớp lệnh.                                          
         conversion_ratio    str     Conversion ratio of the covered warrant. Tỷ lệ chuyển đổi.                     
        =================== ======= =============================================================================== 

Data Sources
------------

- SSI: `iboard.ssi.com.vn <https://iboard.ssi.com.vn/>`_

Misc
----

- `Basics of covered warrant. From SSI. Vietnamese. Thông tin cơ bản thị trường Chứng quyền có đảm bảo <https://www.ssi.com.vn/khach-hang-ca-nhan/kien-thuc-chung-quyen-co-bao-dam>`_