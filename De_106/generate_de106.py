import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề thi thử giữa kì 1 - Môn Toán 12 (ĐỀ SỐ 04 - Mã đề: 106)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 7mm;
  margin-bottom: 7.5mm;
  margin-left: 13.5mm;
  margin-right: 13.5mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 106";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.8pt;
  line-height: 1.36;
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
  line-height: 1.25;
}

.subject-title {
  font-size: 11.5pt;
  font-weight: bold;
  margin-top: 2px;
}

.time-title {
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 1px;
}

.left-box {
  border: 1px solid #000;
  padding: 2.5px 6px;
  text-align: center;
  width: 165px;
  margin: 2px auto 0 auto;
  line-height: 1.22;
}

.left-box .bold-text {
  font-weight: bold;
  font-size: 10pt;
}

.left-box .sub-text {
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
}

.right-box {
  border: 1.3px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 2px;
}

.solid-divider {
  border-top: 1px solid #000;
  margin: 2.5px 0 1.5px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 2.5px 0 3px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 10pt;
  font-style: italic;
  margin-bottom: 2px;
}

.section-title {
  font-weight: bold;
  font-size: 10.8pt;
  margin-top: 3px;
  margin-bottom: 3.5px;
  text-align: justify;
}

.section-subtitle {
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 3px;
}

.question {
  margin-bottom: 3.5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  padding-left: 4px;
  align-items: center;
}

.options-grid div {
  display: flex;
  align-items: center;
  gap: 3.5px;
}

.grid-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.grid-2 {
  grid-template-columns: 1fr 1fr;
}

.sub-item {
  margin-left: 18px;
  margin-bottom: 2px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 15px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9.2pt;
}

.page-break {
  page-break-before: always;
}

.nowrap {
  white-space: nowrap;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: PHẦN I (CÂU 1 ĐẾN CÂU 8) ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ THI THỬ GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ THI THỬ<br>CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 106</div>
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
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 3px 0 3px 0;">
    <img src="assets/gk1_clean_bbt_cau1.png" style="width: 98mm; max-width: 95%;" alt="Bảng biến thiên Câu 1">
  </div>
  Hàm số đã cho đồng biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-2; 2)$.</div>
    <div><b>B.</b> $(-\infty; -2)$.</div>
    <div><b>C.</b> $(-3; 4)$.</div>
    <div><b>D.</b> $(-2; +\infty)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có bảng xét dấu của đạo hàm $f'(x)$ như sau:
  <div style="text-align: center; margin: 3px 0 3px 0;">
    <img src="assets/gk1_clean_bxd_cau2.png" style="width: 108mm; max-width: 95%;" alt="Bảng xét dấu đạo hàm Câu 2">
  </div>
  Số điểm cực tiểu của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $0$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $1$.</div>
    <div><b>D.</b> $3$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3:</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 5$ trên đoạn $[0; 2]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $7$.</div>
    <div><b>D.</b> $1$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4:</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 3x + 5}{x - 1}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = x + 2$.</div>
    <div><b>B.</b> $y = x - 2$.</div>
    <div><b>C.</b> $y = x - 3$.</div>
    <div><b>D.</b> $y = -x + 2$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5:</span> Tọa độ tâm đối xứng của đồ thị hàm số $y = \dfrac{3x - 2}{x + 1}$ là điểm
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 3)$.</div>
    <div><b>B.</b> $I(-1; -2)$.</div>
    <div><b>C.</b> $I(3; -1)$.</div>
    <div><b>D.</b> $I(-1; 3)$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6:</span> Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = \dfrac{2n - 1}{n + 1}$. Số $\dfrac{13}{8}$ là số hạng thứ mấy của dãy số đã cho?
  <div class="options-grid grid-4">
    <div><b>A.</b> Số hạng thứ $7$.</div>
    <div><b>B.</b> Số hạng thứ $8$.</div>
    <div><b>C.</b> Số hạng thứ $6$.</div>
    <div><b>D.</b> Số hạng thứ $5$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7:</span> Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 4$ và công sai $d = -3$. Số hạng thứ mấy của cấp số cộng bằng $-26$?
  <div class="options-grid grid-4">
    <div><b>A.</b> Thứ $11$.</div>
    <div><b>B.</b> Thứ $10$.</div>
    <div><b>C.</b> Thứ $12$.</div>
    <div><b>D.</b> Thứ $9$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8:</span> Cho cấp số nhân $(u_n)$ có số hạng $u_2 = 6$ và $u_5 = 48$. Công bội $q$ của cấp số nhân đó bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $q = 2$.</div>
    <div><b>B.</b> $q = -2$.</div>
    <div><b>C.</b> $q = 4$.</div>
    <div><b>D.</b> $q = 8$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: CÂU 9-12 PHẦN I & CÂU 1-2 PHẦN II ==================== -->
<div class="page-break"></div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9:</span> Cho hình lập phương $ABCD.A'B'C'D'$. Số đo góc giữa hai đường thẳng $A'B$ và $B'C$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $60^\circ$.</div>
    <div><b>B.</b> $90^\circ$.</div>
    <div><b>C.</b> $45^\circ$.</div>
    <div><b>D.</b> $30^\circ$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = a\sqrt{2}$. Góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $60^\circ$.</div>
    <div><b>C.</b> $45^\circ$.</div>
    <div><b>D.</b> $90^\circ$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11:</span> Cho hình chóp tam giác $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$ với $BA = BC = a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = a$. Khoảng cách từ điểm $B$ đến mặt phẳng $(SAC)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $\dfrac{a\sqrt{2}}{2}$.</div>
    <div><b>B.</b> $a\sqrt{2}$.</div>
    <div><b>C.</b> $a$.</div>
    <div><b>D.</b> $\dfrac{a}{2}$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = a, AD = 2a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$. Khoảng cách giữa hai đường thẳng chéo nhau $SA$ và $CD$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $a$.</div>
    <div><b>B.</b> $2a$.</div>
    <div><b>C.</b> $a\sqrt{5}$.</div>
    <div><b>D.</b> $a\sqrt{2}$.</div>
  </div>
</div>

<div class="solid-divider" style="margin-top: 5px;"></div>
<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 Phần II -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = \dfrac{-x^2 - 3x + 4}{x - 3}$ có đồ thị là $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có tiệm cận xiên là đường thẳng $y = -x - 6$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ nhận giao điểm $I(3; -9)$ của hai đường tiệm cận làm tâm đối xứng.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đồ thị $(C)$ có hai điểm cực trị nằm về $2$ phía đối với trục tung $Oy$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đồ thị $(C)$ không cắt trục hoành $Ox$.</div>
</div>

<!-- Câu 2 Phần II -->
<div class="question" style="margin-top: 6px;">
  <span class="question-title">Câu 2:</span> Số dân của một thị trấn sau $t$ năm ($t \ge 0$) kể từ năm 1970 được ước tính bởi công thức:
  $$f(t) = \dfrac{26t + 10}{t + 5}\quad (f(t)\text{ được tính bằng nghìn người}).$$
  <div class="sub-item"><span class="sub-item-label">a)</span> Số dân của thị trấn giảm trong những năm từ 1975 đến 1980.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số $f$ biểu thị tốc độ tăng dân số của thị trấn (tính bằng nghìn người/năm). Vào năm 1998 thì tốc độ tăng dân số là $0,125\text{ nghìn người/năm}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đạo hàm $f'(t) = \dfrac{120}{(t + 5)^2}, (t \ge 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Số dân của thị trấn vào đầu năm 1980 là $18\text{ nghìn người}$.</div>
</div>

<!-- ==================== TRANG 3: CÂU 3-4 PHẦN II & CÂU 1-2 PHẦN III ==================== -->
<div class="page-break"></div>

<!-- Câu 3 Phần II -->
<div class="question">
  <span class="question-title">Câu 3:</span> Một quả bóng cao su được thả rơi tự do từ độ cao $16\text{ m}$ so với mặt đất. Mỗi lần chạm đất, quả bóng lại nảy lên theo phương thẳng đứng với độ cao bằng $\dfrac{3}{4}$ độ cao của lần rơi ngay trước đó. Giả sử quả bóng tiếp tục nảy vô hạn lần. Kí hiệu $h_n$ là độ cao đạt được ở lần nảy thứ $n$ ($n \ge 1$) và $S_n$ là tổng quãng đường quả bóng đã di chuyển kể từ lúc bắt đầu thả cho đến khi bóng chạm đất lần thứ $n$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Dãy số độ cao $(h_n)$ là một cấp số nhân có số hạng đầu $h_1 = 12\text{ m}$ và công bội $q = \dfrac{3}{4}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Độ cao lớn nhất quả bóng đạt được ở lần nảy thứ 3 bằng $6,75\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Quãng đường quả bóng di chuyển từ lúc bắt đầu thả đến khi chạm đất lần thứ hai là $40\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng quãng đường quả bóng di chuyển được kể từ lúc thả rơi cho đến khi nó hoàn toàn dừng lại trên mặt đất bằng $112\text{ m}$.</div>
</div>

<!-- Câu 4 Phần II -->
<div class="question" style="margin-top: 6px;">
  <span class="question-title">Câu 4:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$ và $B$ với $AB = BC = a, AD = 2a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = a\sqrt{2}$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đoạn thẳng $BC$ vuông góc với mặt phẳng $(SAB)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tam giác $SCD$ là tam giác vuông tại $C$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tang của góc giữa đường thẳng $SD$ và mặt phẳng đáy $(ABCD)$ bằng $\dfrac{\sqrt{2}}{2}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách từ điểm $A$ đến mặt phẳng $(SCD)$ bằng $a$.</div>
</div>

<div class="solid-divider" style="margin-top: 5px;"></div>
<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 Phần III -->
<div class="question">
  <span class="question-title">Câu 1:</span> Một kỹ sư công nghệ ký hợp đồng làm việc cho một tập đoàn trong 5 năm (tương ứng với 60 tháng). Công ty đưa ra hai phương án chi trả lương:
  <div style="margin-left: 12px; margin-top: 2px; margin-bottom: 2px;">
    • <b>Phương án 1:</b> Lương tháng đầu tiên là $20\text{ triệu đồng}$; từ tháng thứ hai trở đi, mỗi tháng tiền lương tăng thêm $0,5\text{ triệu đồng}$ so với tháng liền trước.<br>
    • <b>Phương án 2:</b> Lương tháng đầu tiên là $25\text{ triệu đồng}$; trong suốt 12 tháng đầu mức lương giữ nguyên, và cứ sau mỗi chu kỳ 12 tháng (1 năm), mức lương mỗi tháng của năm tiếp theo tăng thêm $4\text{ triệu đồng}$ so với mức lương mỗi tháng của năm trước đó.
  </div>
  Hỏi tổng thu nhập tiền lương cao nhất mà kỹ sư có thể nhận được sau 5 năm làm việc theo một trong hai phương án trên bằng bao nhiêu triệu đồng?
</div>

<!-- Câu 2 Phần III -->
<div class="question" style="margin-top: 6px;">
  <span class="question-title">Câu 2:</span> Cho hình chóp tứ giác đều $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Chiều cao của khối chóp là $SO = \dfrac{a}{2}$ (với $O$ là tâm của đáy). Tính số đo góc giữa mặt bên $(SCD)$ và mặt phẳng đáy $(ABCD)$ (đơn vị: độ).
</div>

<!-- ==================== TRANG 4: CÂU 3-6 PHẦN III & HẾT ==================== -->
<div class="page-break"></div>

<!-- Câu 3 Phần III -->
<div class="question">
  <span class="question-title">Câu 3:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = 6\text{ cm}, AD = 8\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = 6\text{ cm}$. Tính khoảng cách giữa hai đường thẳng chéo nhau $SA$ và $BD$ <i>(kết quả ghi dưới dạng số thập phân theo đơn vị cm)</i>.
</div>

<!-- Câu 4 Phần III -->
<div class="question" style="margin-top: 8px;">
  <span class="question-title">Câu 4:</span> Cho hàm số bậc ba $y = \dfrac{1}{3}x^3 - (m + 1)x^2 + (m^2 + 2m)x - 4$ với $m$ là tham số thực. Tìm giá trị của tham số $m$ để hàm số đã cho đạt cực đại tại điểm $x = 2$.
</div>

<!-- Câu 5 Phần III -->
<div class="question" style="margin-top: 8px;">
  <span class="question-title">Câu 5:</span> Công ty du lịch Hòa Bình muốn mở một tour du lịch bằng du thuyền trên biển và giám đốc công ty đang tính toán các chi phí cần thiết để vận hành du thuyền. Để tính toán chi phí, giám đốc Hòa Bình đã mô hình hóa lượng dầu diesel tiêu thụ ước tính theo hàm số:
  $$G(x) = \dfrac{250}{x} + \dfrac{x}{10}\quad (\text{lít/km})$$
  với $x$ là vận tốc của du thuyền tính bằng km/h ($x > 0$, giả định rằng vận tốc này duy trì không đổi trong suốt quá trình di chuyển). Biết rằng giá dầu diesel là $17,5\text{ nghìn đồng/lít}$. Ngoài ra, công ty cần trả lương cho thuyền trưởng với mức lương $1,5\text{ triệu đồng}$ mỗi giờ để lái du thuyền trong toàn bộ hành trình dài $640\text{ km}$. Hỏi thuyền trưởng phải duy trì vận tốc của du thuyền bằng bao nhiêu km/h để tổng chi phí của chuyến du lịch là thấp nhất? <i>(kết quả làm tròn đến hàng phần mười)</i>.
</div>

<!-- Câu 6 Phần III -->
<div class="question" style="margin-top: 8px;">
  <span class="question-title">Câu 6:</span> Cho một đường tròn $(C)$ có bán kính bằng $4$, vẽ một hình chữ nhật nội tiếp đường tròn $(C)$. Khi diện tích của hình chữ nhật đạt giá trị lớn nhất thì chu vi của hình chữ nhật đó là bao nhiêu? <i>(kết quả làm tròn đến hàng phần mười)</i>.
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

html_path = 'exam_de_thi_thu_gk1_ma106.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'De_Thi_Khao_Sat_Toan_12_Ma_106.pdf'
cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=6000',
    f'--print-to-pdf={output_pdf}',
    html_path
]

print('Running Chrome...')
res = subprocess.run(cmd, capture_output=True, text=True)
print('Chrome exit code:', res.returncode)

reader = pypdf.PdfReader(output_pdf)
print('Total pages:', len(reader.pages))
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_line = lines[0] if lines else 'EMPTY'
    last_line = lines[-1] if lines else 'EMPTY'
    print(f'Page {i+1} ({len(lines)} lines): [First] {first_line[:40]} | [Last] {last_line[:40]}')
