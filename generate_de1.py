import os

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề ôn thi giữa kì 1 - Môn Toán 12 (ĐỀ SỐ 01 - Mã đề: 101)</title>
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
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 101";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.8pt;
  line-height: 1.38;
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

.question {
  margin-bottom: 3px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 1px;
  margin-bottom: 1px;
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
  margin-bottom: 2px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 18px;
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

.bbt-table {
  border-collapse: collapse;
  margin: 2px auto;
  font-size: 9.5pt;
  text-align: center;
}
.bbt-table td {
  padding: 1px 6px;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: PHẦN I (CÂU 1 ĐẾN CÂU 8) ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN THI GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP<br>CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12 (ĐỀ SỐ 01)</div>
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
  <table class="bbt-table">
    <tr style="border-bottom: 1px solid #000;">
      <td style="border-right: 1px solid #000; font-weight: bold; width: 45px;">$x$</td>
      <td style="width: 55px;">$-\infty$</td>
      <td style="width: 35px;"></td>
      <td style="width: 45px;">$-2$</td>
      <td style="width: 35px;"></td>
      <td style="width: 45px;">$1$</td>
      <td style="width: 35px;"></td>
      <td style="width: 55px;">$+\infty$</td>
    </tr>
    <tr style="border-bottom: 1px solid #000;">
      <td style="border-right: 1px solid #000; font-weight: bold;">$f'(x)$</td>
      <td></td>
      <td>$+$</td>
      <td>$0$</td>
      <td>$-$</td>
      <td>$0$</td>
      <td>$+$</td>
      <td></td>
    </tr>
    <tr>
      <td style="border-right: 1px solid #000; font-weight: bold;">$f(x)$</td>
      <td></td>
      <td>$\nearrow$</td>
      <td>$4$</td>
      <td>$\searrow$</td>
      <td></td>
      <td>$\nearrow$</td>
      <td>$+\infty$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid #000;"></td>
      <td>$-\infty$</td>
      <td></td>
      <td></td>
      <td></td>
      <td>$-1$</td>
      <td></td>
      <td></td>
    </tr>
  </table>
  Hàm số đã cho nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4" style="margin-top: 2px;">
    <div><b>A.</b> $(-\infty; -2)$.</div>
    <div><b>B.</b> $(-2; 1)$.</div>
    <div><b>C.</b> $(1; +\infty)$.</div>
    <div><b>D.</b> $(-1; 4)$.</div>
  </div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; padding-right: 15px;">
      <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$. Đồ thị của hàm số đạo hàm $y = f'(x)$ như hình vẽ bên. Điểm cực đại của hàm số $y = f(x)$ là
      <div class="options-grid grid-2" style="margin-top: 5px;">
        <div><b>A.</b> $x = 1$.</div>
        <div><b>B.</b> $x = 3$.</div>
        <div><b>C.</b> $x = -1$.</div>
        <div><b>D.</b> $x = 0$.</div>
      </div>
    </div>
    <div style="width: 180px; text-align: center; flex-shrink: 0;">
      <img src="assets/de4_dothi_fprime_cau2.png" style="width: 175px; max-width: 100%;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Điểm cực tiểu của hàm số $y = x^3 - 3x^2 - 9x + 2$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = -1$.</div>
    <div><b>B.</b> $x = 3$.</div>
    <div><b>C.</b> $x = 2$.</div>
    <div><b>D.</b> $x = -25$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Đạo hàm của hàm số $y = \dfrac{3x - 1}{x + 2}$ trên từng khoảng xác định là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y' = \dfrac{7}{(x + 2)^2}$.</div>
    <div><b>B.</b> $y' = \dfrac{5}{(x + 2)^2}$.</div>
    <div><b>C.</b> $y' = \dfrac{-7}{(x + 2)^2}$.</div>
    <div><b>D.</b> $y' = \dfrac{7}{x + 2}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{x - 1}{x^2 - 3x + 2}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $0$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{2x^2 - 3x + 5}{x - 1}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = 2x - 1$.</div>
    <div><b>B.</b> $y = 2x + 1$.</div>
    <div><b>C.</b> $y = 2x - 3$.</div>
    <div><b>D.</b> $y = x - 1$.</div>
  </div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; padding-right: 15px;">
      <span class="question-title">Câu 7:</span> Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-2" style="margin-top: 5px;">
        <div><b>A.</b> $y = \dfrac{x^2 - x + 1}{x - 1}.$</div>
        <div><b>B.</b> $y = \dfrac{x^2 + x + 1}{x + 1}.$</div>
        <div><b>C.</b> $y = \dfrac{x^2 - 3x + 1}{x - 1}.$</div>
        <div><b>D.</b> $y = \dfrac{2x - 1}{x - 1}.$</div>
      </div>
    </div>
    <div style="width: 180px; text-align: center; flex-shrink: 0;">
      <img src="assets/de4_dothi_cau7.png" style="width: 175px; max-width: 100%;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8:</span> Giá trị lớn nhất của hàm số $y = x^4 - 4x^2 + 3$ trên đoạn $[0; 3]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $48$.</div>
    <div><b>C.</b> $-1$.</div>
    <div><b>D.</b> $50$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: TIẾP PHẦN I (CÂU 9 - 12) & PHẦN II (CÂU 1 - 3) ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 9:</span> Tọa độ tâm đối xứng của đồ thị hàm số $y = \dfrac{x^2 - 2x + 3}{x - 1}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 0)$.</div>
    <div><b>B.</b> $I(1; -1)$.</div>
    <div><b>C.</b> $I(1; 1)$.</div>
    <div><b>D.</b> $I(-1; 0)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10:</span> Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \dfrac{1}{3}x^3 - mx^2 + (2m - 1)x - 3$ đồng biến trên $\mathbb{R}$.
  <div class="options-grid grid-4">
    <div><b>A.</b> $m \le 1$.</div>
    <div><b>B.</b> $m = 1$.</div>
    <div><b>C.</b> $m \ge 1$.</div>
    <div><b>D.</b> $m \in \varnothing$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11:</span> Cho hàm số bậc ba $y = f(x)$ có bảng biến thiên với giá trị cực đại $y_{\text{CĐ}} = 4$ và giá trị cực tiểu $y_{\text{CT}} = -1$. Số nghiệm thực phân biệt của phương trình $2f(x) - 3 = 0$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $0$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 12:</span> Cho hàm số chứa căn thức $y = \sqrt{x^2 - 4x + 8}$. Khẳng định nào sau đây là <b>sai</b>?
  <div class="options-grid grid-2">
    <div><b>A.</b> Tập xác định của hàm số là $D = \mathbb{R}$.</div>
    <div><b>B.</b> Hàm số nghịch biến trên khoảng $(-\infty; 2)$.</div>
    <div><b>C.</b> Điểm cực tiểu của hàm số là $x = 2$.</div>
    <div><b>D.</b> Giá trị nhỏ nhất của hàm số bằng $4$.</div>
  </div>
</div>

<div class="section-title" style="margin-top: 6px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số chứa căn thức $f(x) = x + \sqrt{4 - x^2}$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Tập xác định của hàm số là đoạn $[-2; 2]$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số trên khoảng $(-2; 2)$ là $f'(x) = 1 - \dfrac{x}{\sqrt{4 - x^2}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số đồng biến trên khoảng $(-2; \sqrt{2})$ và nghịch biến trên khoảng $(\sqrt{2}; 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Giá trị lớn nhất của hàm số bằng $2\sqrt{2}$ và giá trị nhỏ nhất của hàm số bằng $0$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = \dfrac{2x - 1}{x - 1}$ có đồ thị là đường cong $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có đường tiệm cận đứng là $x = 1$ và đường tiệm cận ngang là $y = 2$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho nghịch biến trên từng khoảng xác định $(-\infty; 1)$ và $(1; +\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Giao điểm của hai đường tiệm cận của $(C)$ là điểm $I(1; 1)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Xét hai điểm $A, B$ tùy ý lần lượt thuộc hai nhánh khác nhau của đồ thị $(C)$. Khi đó khoảng cách ngắn nhất giữa hai điểm $A$ và $B$ bằng $2\sqrt{2}$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Một chiếc tàu thủy chở hàng chạy ngược dòng trên một khúc sông thẳng có chiều dài $120\text{ km}$. Tốc độ của dòng nước chảy không đổi và bằng $v_0 = 4\text{ km/h}$. Khi tàu duy trì tốc độ $v\text{ (km/h)}$ ($v > 4$) so với dòng nước yên lặng thì định mức tiêu thụ nhiên liệu của động cơ tàu được xác định bởi hàm chi phí $C_x(v) = 2v^3\text{ (nghìn đồng/giờ)}$. Ngoài ra, các chi phí cố định khác cho vận hành (lương thủy thủ đoàn, bảo dưỡng máy móc, hao mòn thiết bị) là $256\text{ nghìn đồng/giờ}$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Thời gian hoàn thành chuyến đi ngược dòng tính theo vận tốc $v$ là $t(v) = \dfrac{120}{v - 4}\text{ (giờ)}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tổng chi phí của chuyến đi ngược dòng biểu diễn theo vận tốc $v$ là hàm số $T(v) = \dfrac{240(v^3 + 128)}{v - 4}\text{ (nghìn đồng)}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Trên khoảng $(4; +\infty)$, đạo hàm $T'(v) = 0$ có đúng một nghiệm là $v = 8\text{ (km/h)}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Để tổng chi phí của chuyến đi là thấp nhất thì tàu cần duy trì vận tốc $v = 8\text{ km/h}$ so với nước, khi đó tổng chi phí thấp nhất bằng $38,4\text{ triệu đồng}$.</div>
</div>

<!-- ==================== TRANG 3: CÂU 4 PHẦN II & CÂU 1 - 5 PHẦN III ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 4:</span> Một công ty xây dựng cần thiết kế một bể chứa nước ngầm có dạng hình hộp chữ nhật có đáy là hình chữ nhật với chiều dài gấp đôi chiều rộng và thể tích bể bằng $V = 256\text{ m}^3$. Nắp bể làm bằng bê tông cốt thép có chi phí $500.000\text{ đồng/m}^2$. Đáy bể tráng men chống thấm có chi phí $400.000\text{ đồng/m}^2$. Bốn mặt thành xung quanh xây bằng gạch trát vữa chống thấm có chi phí $300.000\text{ đồng/m}^2$. Gọi $x\text{ (m)}$ ($x > 0$) là chiều rộng của đáy bể.
  <div class="sub-item" style="margin-top: 5px; margin-bottom: 5px; line-height: 1.45;"><span class="sub-item-label">a)</span> Chiều cao của bể chứa nước tính theo chiều rộng $x$ của đáy là $h = \dfrac{128}{x^2}\text{ (m)}$.</div>
  <div class="sub-item" style="margin-top: 5px; margin-bottom: 5px; line-height: 1.45;"><span class="sub-item-label">b)</span> Hàm số biểu diễn tổng chi phí xây dựng bể là $C(x) = 1800x^2 + \dfrac{230.400}{x}\text{ (nghìn đồng)}$.</div>
  <div class="sub-item" style="margin-top: 5px; margin-bottom: 5px; line-height: 1.45;"><span class="sub-item-label">c)</span> Đạo hàm $C'(x) = 0$ có nghiệm duy nhất trên khoảng $(0; +\infty)$ là $x = 4\text{ (m)}$.</div>
  <div class="sub-item" style="margin-top: 5px; margin-bottom: 5px; line-height: 1.45;"><span class="sub-item-label">d)</span> Tổng chi phí xây dựng thấp nhất của bể là $86,4\text{ triệu đồng}$ khi chiều cao của bể bằng $6\text{ m}$.</div>
</div>

<div class="section-title" style="margin-top: 6px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 2)(x + 1)^2 (x - 4)$ với mọi $x \in \mathbb{R}$. Tìm số điểm cực trị của hàm số $g(x) = f(x^2 - 2x)$.
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để hàm số $y = \dfrac{x + 4}{x + m}$ nghịch biến trên khoảng $(1; +\infty)$?
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Bác Minh mua một chiếc ti vi tại một cửa hàng với giá $21,5\text{ triệu đồng}$ và đã trả trước $10\text{ triệu đồng}$ ngay khi nhận ti vi. Số tiền còn lại bác lựa chọn trả góp trong vòng $12\text{ tháng}$ với lãi suất $3,5\%/\text{tháng}$ theo hình thức lãi kép trên dư nợ giảm dần, tiền lãi được tính dựa trên số dư nợ thực tế tại thời điểm tính lãi. Biết rằng, vào cuối mỗi tháng, bác Minh phải trả cho cửa hàng một số tiền không đổi là $m\text{ triệu đồng}$ để sau đúng $12\text{ tháng}$ thì hết nợ. Giá trị của $m$ bằng bao nhiêu? <i>(Không làm tròn các kết quả trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần trăm).</i>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Một vật chuyển động chịu tác dụng đồng thời của ba lực kéo $\vec{F}_1, \vec{F}_2, \vec{F}_3$ cùng xuất phát từ một điểm $O$. Hai lực $\vec{F}_1$ và $\vec{F}_2$ cùng nằm trong một mặt phẳng nằm ngang, có độ lớn lần lượt là $|\vec{F}_1| = 300\text{ N}$ và $|\vec{F}_2| = 500\text{ N}$, góc tạo bởi hai lực này bằng $60^\circ$. Lực thứ ba $\vec{F}_3$ có phương thẳng đứng hướng lên trên với độ lớn $|\vec{F}_3| = 240\text{ N}$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2 + \vec{F}_3$ tác dụng lên vật (theo đơn vị Newton).
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Một trạm phát điện $A$ được đặt trên bờ một con sông thẳng có bề rộng $AB = 4\text{ km}$ ($AB$ vuông góc với bờ sông). Một nhà máy $C$ nằm ở bờ đối diện và cách điểm $B$ một khoảng $BC = 12\text{ km}$. Người ta cần lắp đặt đường dây tải điện từ $A$ đến một điểm $M$ trên đoạn $BC$ rồi tiếp tục kéo dọc theo bờ sông từ $M$ đến $C$ (như hình vẽ bên dưới). Biết chi phí lắp đặt cáp ngầm dưới sông (đoạn $AM$) là $500\text{ triệu đồng/km}$, còn chi phí kéo cáp trên bờ (đoạn $MC$) là $300\text{ triệu đồng/km}$. Hỏi vị trí điểm $M$ cần cách $B$ một khoảng bằng bao nhiêu kilômét để tổng chi phí lắp đặt đường dây tải điện từ $A$ đến $C$ là thấp nhất?
  <div style="text-align: center; margin: 4px 0 2px 0;">
    <img src="assets/de4_cap_dien_cau5.png" style="width: 100mm; max-width: 95%;">
  </div>
</div>

<!-- ==================== TRANG 4: CÂU 6 PHẦN III & HẾT ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 6:</span> Một bức tranh nghệ thuật có chiều cao $2,7\text{ m}$ ($AB = 2,7\text{ m}$) được treo thẳng đứng trên một bức tường phẳng. Mép dưới $B$ của bức tranh cách mặt sàn $2,4\text{ m}$. Một người xem tranh có tầm mắt cách mặt sàn $1,5\text{ m}$. Hỏi người đó cần đứng cách bức tường một khoảng cách bằng bao nhiêu mét để góc nhìn bức tranh $\theta$ (góc tạo bởi các tia nhìn từ mắt đến mép trên $A$ và mép dưới $B$ của bức tranh) đạt giá trị lớn nhất? (như hình vẽ bên dưới; kết quả ghi dưới dạng số thập phân).
  <div style="text-align: center; margin: 8px 0 4px 0;">
    <img src="assets/de4_ngam_tranh_cau6.png" style="width: 105mm; max-width: 95%;">
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

with open('exam_de1.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("exam_de1.html generated successfully!")
