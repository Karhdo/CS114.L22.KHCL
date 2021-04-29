# Ứng dụng thực tế sử dụng Regression

**Bài toán 1: Dự đoán điểm chuẩn ngành Khoa Học Máy Tính của trường Đại học Công Nghệ Thông Tin vào năm 2021 dựa vào điểm thi đại học.**
- Input: Điểm trung bình của các tổ hợp (Toán Văn Anh, Toán Lý Hoá, ...) của các năm trước.
- Output: Điểm chuẩn ngành Khoa học máy tính của trường Đại học Công Nghệ Thông Tin vào năm đó.
- Thu thập đata: 
  + Lấy dữ liệu trên các trang mạng đã thống kê sẵn dưới dạng biểu đồ( Ví dụ [Phổ điểm thi THPT quốc gia 2020](https://hoatieu.vn/pho-diem-thi-thpt-quoc-gia-203316#:~:text=sinh%20(kh%E1%BB%91i%20B)-,K%E1%BA%BFt%20qu%E1%BA%A3%20ph%C3%A2n%20t%C3%ADch%20%C4%91i%E1%BB%83m%20thi%20theo%20t%E1%BB%95%20h%E1%BB%A3p%203,%C4%91%E1%BA%A1t%20nh%E1%BA%A5t%20l%C3%A0%2022%20%C4%91i%E1%BB%83m.))
  + Lấy dữ liệu trên các trang báo online có uy tín (Ví dụ [Phổ điểm các môn thi tốt nghiệp THPT 2020](https://tuoitre.vn/pho-diem-cac-mon-thi-tot-nghiep-thpt-2020-tap-trung-o-khoang-5-5-7-5-diem-20200808195948919.htm))
- Xử lí dữ liệu:
  + Loại bỏ các điểm dữ liệu bị trống có thể do bỏ thi hoặc do lý do nào khác.
  + Tổng hợp các điểm trung bình của từng môn theo từng năm.
  + Tính trung bình các tổ hợp mà ngành Khoa học máy tính xét.

**Bài toán 2: Bài toán dự đoán số người có nguy cơ tử vong cao vì dịch covid tại Việt Nam.**
- Input:
  + Số lượng người bị nhiễm covid tại Việt Nam (int).
  + Số tuổi của người bị nhiễm covid (int).
- Output:
  + Số lượng người có nguy cơ cao tử vong vì covid (int). (Ứng với số tuổi nhập vào, những người có độ tuổi từ 80 trở lên thì nguy cơ tử vong rất cao).
- Thu thâp data:
  + Xin dữ liệu, thông tin của những người bị nhiễm covid từ các bệnh viện tại mỗi tỉnh trong nước.
  + Dựa vào thông tin, dữ liệu của các bệnh nhân bị nhiễm covid đã được bệnh viện cung cấp, tạo file csv để gom nhóm các thuộc tính lại như số lượng 
  người bị nhiễm(int), tên(string), tuổi(int),giới tính(string).
- Xử lí dữ liệu:
  + Xóa các dòng mà thuộc tính không mang giá trị.
  + Loại bỏ các thông tin mà không làm ảnh hưởng tới output (tên, giới tính).

**Bài toán 3: Dự đoán doanh thu phim.**
- Input: Doanh thu và ngân sách của các bộ phim.
- Output: Doanh thu của bộ phim khi biết chi phí sản xuất
- Cách thu thập data: 
  + Từ trang web: https://www.the-numbers.com/movie/budgets -> Movies -> Budgets and Finances
  + Lấy 2 cột: Production Budget( Ngân sách của phim) và Domestic Gross(Doanh thu của phim trong nội địa)
- Xử lý data: 
	+ Làm sạch dữ liệu, có những phim có ngân sách nhưng lại không có doanh thu (Doanh tu = 0) vì nhiều vấn đề khác nhau như phim chưa phát hành hay đã hoàn thành nhưng chưa được công chiếu,… Vì vậy chúng ta cần loại bỏ những dữ liệu này để không làm dữ liệu của ta bị thiếu sót.
	+ Phân tách những dữ liệu cần thiết cũng như trực quan hóa chúng thông qua các biểu đồ.

**Bài toán 4: Dự đoán giá tiền khi đi Grab.**
- Input: Số km người dùng đi.
- Output: Số tiền tương ứng với input.
- Cách thu thập data: Dựa trên số km và giá tiền tương ứng của các chuyến trước đó.
- Xử lý data: 
	+ Tạo một file csv chứa các dữ liệu: cột đầu tiên là số km, cột thứ 2 là số tiền tương ứng.
	+ Tạo một hàm biểu thị mối liên hệ giữa hai đại lượng đó.

