import os

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề ôn thi giữa kì 1 - Môn Toán 12 (Đề số 02)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 10mm;
  margin-bottom: 12mm;
  margin-left: 14mm;
  margin-right: 14mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 102";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #000;
  margin: 0;
  padding: 0;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2px;
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
  font-size: 11.5pt;
  font-weight: bold;
  text-transform: uppercase;
}

.author-title {
  font-size: 10.5pt;
  font-style: italic;
  margin-top: 1px;
}

.exam-title {
  font-size: 10.5pt;
  font-weight: bold;
}

.subject-title {
  font-size: 10.5pt;
  font-weight: bold;
  margin-top: 1px;
}

.time-title {
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 1px;
}

.left-box {
  border: 1.2px solid #000;
  padding: 2px 6px;
  text-align: center;
  width: 160px;
  margin: 4px auto 0 auto;
}

.left-box .bold-text {
  font-size: 9pt;
  font-weight: bold;
}

.left-box .sub-text {
  font-size: 8.5pt;
}

.right-box {
  border: 1.3px solid #000;
  padding: 3px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 4px;
}

.solid-divider {
  border-top: 1px solid #000;
  margin: 6px 0 5px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 5px 0 8px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 10.5pt;
  font-style: italic;
  margin-bottom: 3px;
}

.section-title {
  font-weight: bold;
  font-size: 11pt;
  margin-top: 6px;
  margin-bottom: 6px;
  text-align: justify;
}

.question {
  margin-bottom: 7px;
  text-align: justify;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 2.5px;
  margin-bottom: 2.5px;
  padding-left: 4px;
}

.grid-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.grid-2 {
  grid-template-columns: 1fr 1fr;
}

.sub-item {
  margin-left: 18px;
  margin-bottom: 1.8px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 8px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9pt;
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
      <div class="subject-title">Môn: TOÁN - Lớp 12 (ĐỀ SỐ 02)</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 102</div>
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
  <div style="text-align: center; margin: 3px 0;">
    <img src="assets/de2_bbt_cau1.png" style="width: 130mm; max-width: 95%;">
  </div>
  Hàm số đã cho nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-\infty; 0)$.</div>
    <div><b>B.</b> $(-1; 3)$.</div>
    <div><b>C.</b> $(-2; 0)$.</div>
    <div><b>D.</b> $(0; +\infty)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Điểm cực tiểu của hàm số $y = x^3 - 3x^2 + 2$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = 0$.</div>
    <div><b>B.</b> $x = 2$.</div>
    <div><b>C.</b> $x = -2$.</div>
    <div><b>D.</b> $x = 1$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Tiệm cận ngang của đồ thị hàm số $y = \dfrac{3x + 2}{1 - x}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = -3$.</div>
    <div><b>B.</b> $y = 3$.</div>
    <div><b>C.</b> $x = 1$.</div>
    <div><b>D.</b> $y = 2$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Tiệm cận xiên của đồ thị hàm số $y = \dfrac{2x^2 + 3x - 1}{x + 2}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = 2x + 1$.</div>
    <div><b>B.</b> $y = 2x + 7$.</div>
    <div><b>C.</b> $y = x - 1$.</div>
    <div><b>D.</b> $y = 2x - 1$.</div>
  </div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 1; padding-right: 15px;">
      <span class="question-title">Câu 5:</span> Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-2" style="margin-top: 8px;">
        <div><b>A.</b> $y = -x^3 + 3x + 1.$</div>
        <div><b>B.</b> $y = x^4 - 2x^2 + 1.$</div>
        <div><b>C.</b> $y = x^3 - 3x + 1.$</div>
        <div><b>D.</b> $y = x^3 - 3x^2 + 1.$</div>
      </div>
    </div>
    <div style="width: 140px; text-align: center;">
      <img src="assets/de2_dothi_cau5.png" style="width: 130px;">
    </div>
  </div>
</div>

<!-- ==================== TRANG 2 ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 6:</span> Cho dãy số $(u_n)$ được xác định bởi hệ thức truy hồi: $\begin{cases} u_1 = 2 \\ u_{n+1} = u_n + 3, \quad \forall n \ge 1 \end{cases}$. Công thức số hạng tổng quát của dãy số $(u_n)$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_n = 3n - 1$.</div>
    <div><b>B.</b> $u_n = 3n + 2$.</div>
    <div><b>C.</b> $u_n = 2n + 1$.</div>
    <div><b>D.</b> $u_n = 3n - 2$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 7:</span> Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 5$ và công sai $d = -3$. Số hạng thứ 6 của cấp số cộng đó là
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_6 = -10$.</div>
    <div><b>B.</b> $u_6 = -13$.</div>
    <div><b>C.</b> $u_6 = 20$.</div>
    <div><b>D.</b> $u_6 = -7$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8:</span> Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 3$ và công bội $q = 2$. Số hạng thứ 4 của cấp số nhân đó là
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_4 = 24$.</div>
    <div><b>B.</b> $u_4 = 48$.</div>
    <div><b>C.</b> $u_4 = 18$.</div>
    <div><b>D.</b> $u_4 = 54$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 9:</span> Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $A'B$ và $B'C$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $60^\circ$.</div>
    <div><b>C.</b> $90^\circ$.</div>
    <div><b>D.</b> $45^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = a\sqrt{2}$. Góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $45^\circ$.</div>
    <div><b>C.</b> $60^\circ$.</div>
    <div><b>D.</b> $90^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11:</span> Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông tại $A$ với $AB = a, AC = a\sqrt{3}$. Chiều cao hình lăng trụ $AA' = 2a$. Khoảng cách từ điểm $A'$ đến mặt phẳng đáy $(ABC)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $a$.</div>
    <div><b>B.</b> $a\sqrt{3}$.</div>
    <div><b>C.</b> $2a$.</div>
    <div><b>D.</b> $2a\sqrt{3}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 12:</span> Cho hình chóp $S.ABC$ có cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và đáy $ABC$ là tam giác đều cạnh $a$. Gọi $M$ là trung điểm của cạnh $BC$. Khoảng cách từ điểm $A$ đến đường thẳng $BC$ bằng độ dài đoạn thẳng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $AB$.</div>
    <div><b>B.</b> $AM$.</div>
    <div><b>C.</b> $SM$.</div>
    <div><b>D.</b> $AC$.</div>
  </div>
</div>

<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = \dfrac{x^2 + 2x + 2}{x + 1}$ có đồ thị $(C)$. Gọi $I$ là giao điểm hai đường tiệm cận của $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có tiệm cận đứng $x = -1$ và tiệm cận xiên $y = x + 1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho nghịch biến trên khoảng $(-2; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Có đúng hai giá trị nguyên của tham số $m$ để đường thẳng $y = m$ không có điểm chung với $(C)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tiếp tuyến tại điểm $M$ bất kỳ thuộc $(C)$ cắt tiệm cận đứng và tiệm cận xiên lần lượt tại $A$ và $B$. Khi đó diện tích tam giác $IAB$ luôn bằng $2$.</div>
</div>

<!-- ==================== TRANG 3 ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 2:</span> Một cốc cà phê vừa pha có nhiệt độ $95^\circ\text{C}$ được đặt trên bàn trong một căn phòng có nhiệt độ không đổi $25^\circ\text{C}$. Theo định luật làm nguội của Newton, nhiệt độ $T(t)$ (đơn vị: $^\circ\text{C}$) của cà phê sau $t$ phút là $T(t) = 25 + 70e^{-kt}$ ($t \ge 0$), với $k$ là hằng số dương. Đo thực tế, sau 10 phút nhiệt độ cà phê còn $60^\circ\text{C}$.
  <div style="text-align: center; margin: 3px 0;">
    <img src="assets/de2_hinh_cafe.png" style="width: 82mm; max-width: 80%;">
  </div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Giá trị của hằng số $k$ là $k = \dfrac{\ln 2}{10}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Nếu để cốc cà phê đủ lâu thì nhiệt độ của cà phê sẽ xuống thấp hơn $25^\circ\text{C}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tốc độ giảm nhiệt độ của cà phê ngay khi vừa pha xong lớn gấp 4 lần tốc độ giảm nhiệt độ tại thời điểm $t = 20$ phút.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Cà phê ngon nhất khi uống ở nhiệt độ từ $50^\circ\text{C}$ đến $70^\circ\text{C}$. Khoảng thời gian cà phê ở nhiệt độ ngon nhất dài hơn 9 phút.</div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Một kỹ sư công nghệ ký hợp đồng làm việc với một tập đoàn phần mềm trong 8 năm. Mức lương khởi điểm trong năm đầu tiên là $240\text{ triệu đồng/năm}$. Kể từ năm thứ hai trở đi, sau mỗi năm làm việc, mức lương của kỹ sư đó sẽ được tăng thêm $10\%$ so với mức lương của năm liền trước đó. Ký hiệu $u_n$ là mức lương của kỹ sư đó ở năm thứ $n$ ($1 \le n \le 8$).
  <div class="sub-item"><span class="sub-item-label">a)</span> Dãy số $(u_n)$ là một cấp số nhân có số hạng đầu $u_1 = 240$ và công bội $q = 1,1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Số hạng tổng quát biểu diễn mức lương của kỹ sư đó ở năm thứ $n$ là $u_n = 240 \cdot (1,1)^{n-1}\text{ (triệu đồng)}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Mức lương của kỹ sư đó ở năm thứ 4 vượt quá $330\text{ triệu đồng}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng thu nhập mà kỹ sư đó nhận được sau toàn bộ 8 năm làm việc tại tập đoàn vượt quá $2,8\text{ tỷ đồng}$ ($2800\text{ triệu đồng}$).</div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Cho hình chóp tứ giác đều $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $2a$, tâm $O$. Chiều cao của hình chóp là $SO = a\sqrt{3}$. Gọi $M$ là trung điểm của cạnh $CD$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đoạn thẳng $SO$ vuông góc với mặt phẳng đáy $(ABCD)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Góc giữa cạnh bên $SA$ và mặt phẳng đáy $(ABCD)$ bằng $60^\circ$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Góc giữa mặt bên $(SCD)$ và mặt phẳng đáy $(ABCD)$ bằng $60^\circ$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách từ điểm $A$ đến mặt phẳng $(SCD)$ bằng $2a$.</div>
</div>

<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $f(x) = x^3 - 3x^2 + 2$. Phương trình $f(f(x)) = 0$ có bao nhiêu nghiệm thực phân biệt?
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Một công ty khoan giếng đưa ra giá dịch vụ như sau: giá của mét khoan đầu tiên là $100.000$ đồng, kể từ mét khoan thứ hai trở đi, giá của mỗi mét khoan tăng thêm $20.000$ đồng so với mét khoan ngay trước đó. Một hộ gia đình cần khoan một giếng sâu $25\text{ m}$. Hỏi tổng số tiền mà gia đình đó phải trả cho công ty là bao nhiêu triệu đồng?
</div>

<!-- ==================== TRANG 4 ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 3:</span> Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có đáy $ABCD$ là hình vuông cạnh $a$. Biết khoảng cách từ điểm $A$ đến mặt phẳng $(A'BD)$ bằng $\dfrac{a\sqrt{10}}{5}$. Tính số đo góc giữa đường thẳng $A'C$ và mặt phẳng $(ABB'A')$ (đơn vị: độ).
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Có ba ngôi nhà $A, B, C$ mà khoảng cách giữa từng cặp ngôi nhà đều bằng $4\text{ km}$. Một ngôi nhà thứ tư $D$ ở bên ngoài vùng tam giác $ABC$, mà góc nhìn của $D$ đối với hai ngôi nhà $A, B$ là $120^\circ$ và khoảng cách từ $D$ đến $A$ và $B$ bằng nhau (như hình vẽ bên dưới). Người ta muốn chọn điểm $M$ nằm giữa $B$ và $C$, để làm con đường đi từ $C$ đến $M$ rồi từ $M$ đến $D$. Biết giá tiền làm đường trên đoạn $BC$ là $200\text{ triệu đồng/km}$ và trên đoạn $MD$ là $400\text{ triệu đồng/km}$. Hỏi tổng chi phí nhỏ nhất để làm con đường đó là bao nhiêu triệu đồng?
  <div style="text-align: center; margin: 4px 0;">
    <img src="assets/de2_hinh_ngoinha.png" style="width: 76mm; max-width: 82%;">
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = 3\text{ cm}, BC = 4\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = 4\text{ cm}$. Gọi $G$ là trọng tâm của tam giác đáy $ABC$. Tính khoảng cách từ điểm $G$ đến mặt phẳng $(SBC)$ (kết quả ghi theo đơn vị cm dưới dạng số thập phân).
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Nhà ông An ở gần bờ kênh, ông dự định thiết kế một ao nuôi vịt như sau: ông bắc một chiếc cầu thứ nhất từ nhà tại điểm $A$ đến điểm $M$ trên bờ kênh. Tại điểm $M$ ông rào một ao hình tròn có đường kính bằng $MC$ và bắc thêm một cây cầu thứ hai từ $M$ đến một điểm $D$ trên bờ ao. Hằng ngày ông đi từ nhà ra kênh trên cái cầu thứ nhất rồi từ đó đi qua cái cầu thứ hai rồi đi theo cung tròn của ao đến chuồng vịt tại $C$ để cho vịt ăn (như hình vẽ bên dưới). Hỏi độ dài của cây cầu thứ nhất là bao nhiêu km biết ông đi quãng đường dài nhất với góc $\widehat{AMD} = 120^\circ$, nhà ông cách bờ kênh $200\text{ m}$ và $HC = 1\text{ km}$ (kết quả làm tròn đến hàng phần trăm).
  <div style="text-align: center; margin: 4px 0;">
    <img src="assets/de2_hinh_ao_vit.png" style="width: 88mm; max-width: 90%;">
  </div>
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

with open('exam_de2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("exam_de2.html created successfully!")
