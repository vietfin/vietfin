Quote
==========

Get the latest quote of a stock ticker.

Example:

Use ``equity.price.quote()`` with default parameters: ``provider`` (TCBS), ``limit`` (100).

.. code-block:: python

    from vietfin import vf
    
    # Get the most recent 100 quote data of company CTG
    vf.equity.price.quote(symbol="ctg")

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

        =================== ======= ============= 
         field_name          type    description  
        =================== ======= ============= 
         time                time                 
         price               float                
         volume              int                  
         average_price       float                
         order_type          str                  
         order_count         int                  
         investor_type       str                  
         prev_price_change   float                
        =================== ======= ============= 

.. dropdown:: Explain data column's value

    Khi 1 lệnh lớn (từ Cá mập, tay to, tổ chức....) mua chủ động (hoặc bán chủ động) được đưa vào Sàn, thường thì nó sẽ được khớp với nhiều lệnh nhỏ đang chờ bán (hoặc chờ mua). Nếu chỉ nhìn realtime theo từng lệnh khớp riêng lẻ, thì sẽ không thể phát hiện được các lệnh to (của Cá mập, tay to...) vừa được đẩy vào Sàn. Vì vậy, chúng tôi "cộng dồn" các lệnh khớp này lại (phát sinh bởi 1 lệnh lớn chủ động vào sàn trong 1 khoảng thời gian rất nhanh) để giúp nhà đầu tư (a.k.a NĐT) phát hiện các lệnh lớn (của Cá mập, tay to....) chính xác hơn. Lệnh Cá mập sẽ được tô xanh (cho Mua chủ động) và đỏ (cho Bán chủ động).

    - ``investor_type``

        a. SHARK: nhà đầu tư tay to, tổ chức, đầu tư lớn, dẫn dắt thị trường. Giá trị 1 lệnh đặt > 1 tỷ đồng/lệnh đặt. Đồ thị 1N dùng số liệu 1 phút cho 60’ gần nhất; 1W là tổng mỗi 15’ cho 1 tuần; 1M là tổng hàng ngày cho 1 tháng.
        b. WOLF: nhà đầu tư kinh nghiệm, giá trị lệnh đặt cao. Giá trị 1 lệnh đặt từ 200 tr đến 1 tỷ đồng/lệnh đặt.
        c. SHEEP: nhà đầu tư nhỏ lẻ, giá trị giao dịch và mua bán chủ động thấp. Giá trị 1 lệnh đặt Mua hoặc Bán chủ động < 200 triệu đồng/lệnh đặt vào.
    
    - ``order_type``

        a. BU (Buy Up / Mua chủ động): là khi NĐT thực hiện chủ động mua lên qua việc đặt lệnh mua với giá bằng giá dư bán gần nhất để có thể khớp luôn. Như thế, giá khớp cho lệnh này thường sẽ đẩy giá khớp lên cao hơn thị giá trước đó.
        b. SD (Sell Down / Bán chủ động) là khi NĐT thực hiện chủ động Bán dưới giá hiện tại (hay thị giá) của cổ phiếu bằng việc đặt lệnh bán với giá bán bằng giá dư mua gần nhất để khớp ngay. Và như thế, thị giá sẽ bị kéo xuống thấp hơn so với thị giá trước đó. Thống kê khối lượng giao dich theo Mua CĐ và Bán CĐ dùng để đánh giá tương quan giữa cung (Bán CĐ) và cầu (Mua CĐ) trên giao dịch khớp lệnh thực tế, nhằm nhận định tương đối về sự vận động của xu hướng dòng tiền. Khi tỷ lệ % Mua CĐ trên (Tổng Mua và Bán CĐ) lớn hơn 50%, đồng nghĩa với việc thị trường đang có xu hướng mua vào nhiều hơn bán ra và ngược lại, qua đó xác định được dòng tiền vào/ra với mỗi cổ phiếu. Khi tỷ lệ này cao đột biến (>70% hay <30%) so với điểm cân bằng (50%) , đó là tín hiệu của việc mua hoặc bán bất chấp của thị trường.
    
    source: `vnstock <https://docs.vnstock.site/functions/technical/#du-lieu-khop-lenh-trong-ngay-giao-dich>`_