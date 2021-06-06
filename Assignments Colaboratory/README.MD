# Bài tập colab số 01. sklearn hand-written digits recognition

Yêu cầu code: tạo một notebook colab với các đoạn code và chú thích cần thiết để thực hiện công việc sau:
- Train model cho bài toán hand-written digits recognition theo example của sklearn: https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py
- Truy cập webcam của máy tính từ colab.
- Chụp ảnh một tờ giấy đang được giơ ra trước webcam
- Nhận dạng xem chữ số đang viết trên tờ giấy là số mấy.

**Yêu cầu phân tích: Thông qua thực nghiệm chạy thử nhiều lần trả lời các câu hỏi sau**

1. Kết quả chạy thực tế với webcam của laptop và giấy viết tay của các bạn có tốt không?
2. Ủa mà nhìn vào đâu để kết luận là tốt hay không?
3. Nếu không tốt thì lý do tại sao?
4. Nếu tốt thì tiếp theo có thể dùng model digits recognition này vào các bài toán phức tạp hơn như nhận dạng biển số nhà không?

 - [x] [RECOGNIZING HAND-WRITTEN DIGITS](https://github.com/trong-khanh-1109/CS114.L22.KHCL/blob/d4386fcfc8a0a3e993da1ca53e63c52165e33ed1/Assignments%20Colaboratory/Colab_01.ipynb) - [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jpcB2WAmeKvAs0XwsEX3pF_yhfPQngJZ)
 
 # Bài tập colab số 02. PREDICT EXECUTION TIME OF A PROGRAM WITH GIVEN THE NUMBERS OF INPUT

- Dữ liệu train: https://cs.uit.edu.vn/data2.txt
- Dữ liệu test: https://cs.uit.edu.vn/data3.txt

- [x] [PREDICT EXECUTION TIME OF A PROGRAM WITH GIVEN THE NUMBERS OF INPUT](https://github.com/trong-khanh-1109/CS114.L22.KHCL/blob/1254a56d76ad8c7afee4dd086ef7577ea8d1d1b9/Assignments%20Colaboratory/Colab_02.ipynb) - [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18_nQt37VcN7FEk1NqGiFPHV4Ea6ZOImX?authuser=1&hl=en#scrollTo=gLFe_OFDlpxm)

# Bài tập colab số 03. PREDICT FINAL SCORE OF IT001

- Cho dataset gồm 02 file. Là kết quả thực hành của hơn 1500 sinh viên IT001 và kết quả môn học IT001 của hơn 900 sinh viên trong các sinh viên này. 
Hãy tìm cách dự đoán điểm thi cuối kỳ cho các sinh viên IT001 còn thiếu.
- File wecode.csv gồm các thông tin: 

     "id"            : id của lần nộp bài
     "assignment_id" : id của assignment
     "problem_id"    : id của problem
     "user_id"       : id của user **cái này quan trọng nè**
     "is_final"      : đây có phải là lần
     "status"        : submission này đang dược chấm (PENDING), đã được chấm (SCORE) hay bị compilation-error
     "pre_score"     : Số phần trăm test đúng, làm tròn đến 2 chữ số thập phân và nhân cho 100.
     "coefficient"   : Hệ số nộp bài trễ
     "file_name"     : không quan trọng
     "language_id"   : language_id sẽ luôn là C++
     "created_at"    : Thời điểm nộp bài
     "updated_at"    : Thời điểm hệ thống cập nhật kết quả chấm cho bài nộp đó

- File score_training.csv gồm các thông tin
     id  : user id sẽ tương ứng với user id của file wecode.csv
     QT  : Điểm quá trình
     GK  : Điểm giữa kỳ
     TH  : Điểm thực hành
     CK  : Điểm cuối kỳ
     TBM : Trung bình môn it001
     TBTL: Trung bình tích lũy

- [wecode.csv](https://drive.google.com/file/d/1X5pBfb94tpaCUGtB7gHDFXPzXv4L8Gnr/view?usp=sharing)
- [score_training](https://drive.google.com/file/d/1dsiSt6TuPpgr1imkvvHzWfBJU7-RGT4X/view?usp=sharing)

- [x] [Scatter plot vẽ mối liên hệ giữa những thông số có thể tính được từ dữ liệu wecode.csv đến điểm thi cuối kỳ của sinh viên](https://github.com/trong-khanh-1109/CS114.L22.KHCL/blob/a81062ee166814347e2b3adbd531bffe28635af6/Assignments%20Colaboratory/Colab_03.ipynb) - [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12WlmSzp9KTUJKILNtQ02GWLIN9rniNNW?authuser=1)
- [x] [Dự đoán điểm thi cuối kỳ IT001 từ quá trình nộp bài wecode](https://github.com/trong-khanh-1109/CS114.L22.KHCL/blob/a81062ee166814347e2b3adbd531bffe28635af6/Assignments%20Colaboratory/Colab_03_1.ipynb) - [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N1SUiSd9rbLtclEAQ3kQjuJ_ZQjs2xof?authuser=1)
