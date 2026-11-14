import os
import subprocess

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề ôn thi giữa kì 1 - Môn Toán 12</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 13mm;
  margin-bottom: 16mm;
  margin-left: 15mm;
  margin-right: 15mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 101";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 11.5pt;
  line-height: 1.55;
  color: #000;
  margin: 0;
  padding: 0;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 3px;
}

.header-table td {
  vertical-align: top;
  padding: 0;
}

.left-header {
  width: 44%;
  text-align: center;
}

.right-header {
  width: 56%;
  text-align: center;
}

.title-main {
  font-size: 12pt;
  font-weight: bold;
  text-transform: uppercase;
}

.author-title {
  font-size: 11pt;
  font-style: italic;
  margin-top: 1px;
}

.exam-title {
  font-size: 11pt;
  font-weight: bold;
}

.subject-title {
  font-size: 11pt;
  font-weight: bold;
  margin-top: 1px;
}

.time-title {
  font-size: 10pt;
  font-style: italic;
  margin-top: 1px;
}

.left-box {
  border: 1.2px solid #000;
  padding: 3px 6px;
  text-align: center;
  width: 165px;
  margin: 5px auto 0 auto;
}

.left-box .bold-text {
  font-size: 9.5pt;
  font-weight: bold;
}

.left-box .sub-text {
  font-size: 9pt;
}

.right-box {
  border: 1.5px solid #000;
  padding: 4px 16px;
  font-weight: bold;
  font-size: 11.5pt;
  display: inline-block;
  margin-top: 5px;
}

.solid-divider {
  border-top: 1px solid #000;
  margin: 7px 0 5px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 5px 0 10px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 11pt;
}

.section-title {
  font-weight: bold;
  font-size: 11.5pt;
  margin-top: 8px;
  margin-bottom: 8px;
}

.question {
  margin-bottom: 12px;
  text-align: justify;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 5px;
  margin-bottom: 3px;
  row-gap: 5px;
}

.grid-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.grid-2 {
  grid-template-columns: 1fr 1fr;
}

.sub-item {
  margin-left: 20px;
  margin-bottom: 4px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 16px;
  margin-bottom: 4px;
  font-weight: bold;
  font-size: 11.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 10pt;
}

.page-break {
  page-break-before: always;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1 ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN THI GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 101</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 4px 0;">
    <img src="assets/bbt_cau1.png" style="width: 135mm; max-width: 95%;">
  </div>
  Hàm số đã cho nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-1; 2)$.</div>
    <div><b>B.</b> $(-\infty; -1)$.</div>
    <div><b>C.</b> $(2; +\infty)$.</div>
    <div><b>D.</b> $(-1; 3)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 1)^2(x + 2)^3$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Đạo hàm của hàm số $y = \dfrac{2x - 1}{x + 1}$ trên từng khoảng xác định là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y' = \dfrac{3}{(x + 1)^2}$.</div>
    <div><b>B.</b> $y' = \dfrac{1}{(x + 1)^2}$.</div>
    <div><b>C.</b> $y' = \dfrac{-3}{(x + 1)^2}$.</div>
    <div><b>D.</b> $y' = \dfrac{3}{x + 1}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{x + 2}{x^2 - 4}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $0$.</div>
  </div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 1; padding-right: 15px;">
      <span class="question-title">Câu 5:</span> Đường cong trong hình bên là đồ thị của hàm số nào sau đây?
      <div class="options-grid grid-2" style="margin-top: 10px;">
        <div><b>A.</b> $y = -x^3 + 3x.$</div>
        <div><b>B.</b> $y = x^3 - 3x + 1.$</div>
        <div><b>C.</b> $y = x^3 - 3x.$</div>
        <div><b>D.</b> $y = x^4 - 2x^2.$</div>
      </div>
    </div>
    <div style="width: 145px; text-align: center;">
      <img src="assets/dothi_cau5.png" style="width: 135px;">
    </div>
  </div>
</div>

<!-- ==================== TRANG 2 ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 6:</span> Cho dãy số $(u_n)$ với số hạng tổng quát $u_n = \dfrac{2n - 1}{n + 1}$. Giá trị của số hạng $u_3$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $\dfrac{5}{4}$.</div>
    <div><b>B.</b> $\dfrac{3}{4}$.</div>
    <div><b>C.</b> $1$.</div>
    <div><b>D.</b> $\dfrac{1}{2}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 7:</span> Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 3$ và công sai $d = 4$. Số hạng thứ 5 của cấp số cộng đó là
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_5 = 15$.</div>
    <div><b>B.</b> $u_5 = 19$.</div>
    <div><b>C.</b> $u_5 = 23$.</div>
    <div><b>D.</b> $u_5 = 12$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8:</span> Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 2$ và công bội $q = 3$. Tổng của 4 số hạng đầu tiên của cấp số nhân đó bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $S_4 = 80$.</div>
    <div><b>B.</b> $S_4 = 40$.</div>
    <div><b>C.</b> $S_4 = 26$.</div>
    <div><b>D.</b> $S_4 = 54$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 9:</span> Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $AB$ và $A'C'$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $45^\circ$.</div>
    <div><b>C.</b> $60^\circ$.</div>
    <div><b>D.</b> $90^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = a$. Góc giữa đường thẳng $SB$ và mặt phẳng $(ABC)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $45^\circ$.</div>
    <div><b>C.</b> $60^\circ$.</div>
    <div><b>D.</b> $90^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = a$, $AD = 2a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = 3a$. Khoảng cách từ điểm $S$ đến mặt phẳng $(ABCD)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $a$.</div>
    <div><b>B.</b> $2a$.</div>
    <div><b>C.</b> $3a$.</div>
    <div><b>D.</b> $a\sqrt{14}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 12:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$. Kẻ $AH \perp SB$ tại $H$. Khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ bằng độ dài đoạn thẳng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $AB$.</div>
    <div><b>B.</b> $SA$.</div>
    <div><b>C.</b> $AH$.</div>
    <div><b>D.</b> $SB$.</div>
  </div>
</div>

<!-- ==================== TRANG 3 ==================== -->
<div class="page-break"></div>

<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Một hội trường nhà hát được thiết kế có 25 hàng ghế xếp theo hình bậc thang từ thấp lên cao. Hàng ghế đầu tiên có 20 ghế, mỗi hàng sau có nhiều hơn hàng liền trước nó 3 ghế. Ký hiệu $u_n$ là số ghế ở hàng thứ $n$ ($1 \le n \le 25$).
  <div class="sub-item"><span class="sub-item-label">a)</span> Dãy số $(u_n)$ lập thành một cấp số cộng với số hạng đầu $u_1 = 20$ và công sai $d = 3$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàng ghế thứ 15 của hội trường có 65 ghế.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tổng số ghế của toàn bộ 25 hàng ghế trong hội trường là 1400 ghế.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Ban tổ chức phát hành vé xem ca nhạc với giá 200.000 đồng/vé cho 10 hàng ghế đầu và 120.000 đồng/vé cho 15 hàng ghế còn lại. Khi bán hết toàn bộ số vé, tổng số tiền thu được là 208.700.000 đồng.</div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 6}{x - 2}$ có đồ thị là $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có đường tiệm cận đứng là đường thẳng $x = 2$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho nghịch biến trên khoảng $(0; 4)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Điểm cực đại của đồ thị hàm số là $M(0; -3)$ và điểm cực tiểu của đồ thị hàm số là $N(4; 5)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đường tiệm cận xiên của $(C)$ cùng với hai trục tọa độ tạo thành một tam giác có diện tích bằng $1$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Một hộ gia đình dự định xây dựng một bể chứa nước sinh hoạt hình hộp chữ nhật không có nắp với thể tích $V = 36\text{ m}^3$. Đáy bể là hình chữ nhật có chiều dài gấp đôi chiều rộng. Biết rằng chi phí vật liệu xây dựng đáy bể là $400.000\text{ đồng/m}^2$, chi phí xây dựng bốn mặt bên (thành bể) là $300.000\text{ đồng/m}^2$. Gọi $x$ (m) là chiều rộng của đáy bể ($x > 0$), $h$ (m) là chiều cao của bể và $C(x)$ (đồng) là tổng chi phí xây dựng bể.
  <div class="sub-item"><span class="sub-item-label">a)</span> Chiều cao của bể nước được biểu diễn theo $x$ là $h = \dfrac{18}{x^2}\text{ (m)}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tổng diện tích của bốn mặt bên xung quanh bể là $S_{xq} = \dfrac{108}{x}\text{ (m}^2\text{)}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tổng chi phí xây dựng bể nước biểu diễn theo $x$ là hàm số $C(x) = 800.000x^2 + \dfrac{32.400.000}{x}\text{ (đồng)}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Để chi phí xây dựng bể là nhỏ nhất thì gia đình cần xây dựng đáy bể có chiều rộng $x = 3\text{ m}$, và khi đó chi phí nhỏ nhất là $21.600.000$ đồng.</div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = a\sqrt{3}$. Gọi $O$ là giao điểm của $AC$ và $BD$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đoạn thẳng $AC$ là hình chiếu vuông góc của đoạn thẳng $SC$ lên mặt phẳng $(ABCD)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ bằng $60^\circ$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khoảng cách từ điểm $A$ đến mặt phẳng $(SBD)$ bằng $\dfrac{a\sqrt{21}}{7}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách giữa hai đường thẳng chéo nhau $SC$ và $BD$ bằng $\dfrac{a\sqrt{21}}{14}$.</div>
</div>

<!-- ==================== TRANG 4 ==================== -->
<div class="page-break"></div>

<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho cấp số nhân $(u_n)$ có tất cả các số hạng đều là số thực dương, thỏa mãn hệ thức:
  $$\begin{cases} u_2 + u_4 = 20 \\ u_3 + u_5 = 40 \end{cases}$$
  Tìm số hạng thứ 7 ($u_7$) của cấp số nhân đó.
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$, $AB = BC = 2a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = 2a\sqrt{2}$. Tính số đo góc giữa đường thẳng $SC$ và mặt phẳng $(SAB)$ (đơn vị: độ).
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = 3\text{ cm}$, $BC = 4\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = 4\text{ cm}$. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ (kết quả ghi dưới dạng số thập phân).
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Tìm giá trị nhỏ nhất của hàm số $f(x) = \dfrac{x^2 + 3}{x - 1}$ trên đoạn $[2; 4]$.
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Một giàn khoan dầu khí ngoài khơi đặt tại điểm $A$ cách bờ biển thẳng một khoảng $AH = 6\text{ km}$. Một nhà máy lọc dầu đặt tại vị trí $B$ trên bờ biển cách $H$ một khoảng $HB = 16\text{ km}$. Người ta cần lắp đặt một đường ống dẫn dầu từ giàn khoan $A$ đến một vị trí $M$ trên bờ biển (nằm giữa $H$ và $B$), rồi từ $M$ nối tiếp đường ống trên bờ biển về nhà máy lọc dầu $B$ (như hình vẽ bên dưới).
  <div style="text-align: center; margin: 6px 0;">
    <img src="assets/hinh_cau5_part3.png" style="width: 125mm; max-width: 95%;">
  </div>
  Biết rằng chi phí lắp đặt mỗi kilômét đường ống dưới biển là $100.000\text{ USD}$, chi phí lắp đặt mỗi kilômét đường ống trên bờ biển là $60.000\text{ USD}$. Để tổng chi phí lắp đặt toàn bộ hệ thống đường ống dẫn dầu là nhỏ nhất thì vị trí $M$ cần cách $H$ một khoảng bằng bao nhiêu kilômét?
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Một công ty du lịch tổ chức một tour tham quan với số lượng khách tối đa cho một chuyến đi là 60 người. Khi giá vé là 2 triệu đồng/người thì có đủ 60 khách đăng ký tham gia. Cứ mỗi lần công ty tăng giá vé thêm 100.000 đồng (0,1 triệu đồng) cho mỗi người thì lượng khách đăng ký sẽ giảm đi 2 người. Chi phí tổ chức cố định của chuyến đi là 15 triệu đồng và chi phí phục vụ trực tiếp cho mỗi khách tham gia tour là 800.000 đồng (0,8 triệu đồng). Hỏi công ty cần định giá bán mỗi vé tour là bao nhiêu triệu đồng mỗi người để lợi nhuận thu được từ chuyến đi là lớn nhất?
</div>

<div class="end-exam">----------------------- HẾT -----------------------</div>
<div class="end-note">Học sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

<script>
  renderMathInElement(document.body, {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '$', right: '$', display: false}
    ]
  });
</script>

</body>
</html>
"""

with open('exam.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("exam.html updated with diagram for Câu 5 Phần III!")
