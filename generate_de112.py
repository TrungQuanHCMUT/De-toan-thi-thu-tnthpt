import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 112)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 5mm;
  margin-bottom: 5mm;
  margin-left: 11.5mm;
  margin-right: 11.5mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 112";
    font-family: 'Times New Roman', serif;
    font-size: 9.5pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10pt;
  line-height: 1.25;
  color: #000;
  margin: 0;
  padding: 0;
}

.katex .accent-vec > svg {
  transform: scale(1.4);
  transform-origin: center bottom;
}
.katex .svg-align > svg {
  transform: scale(1.25);
  transform-origin: center bottom;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5px;
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
  font-size: 10pt;
  font-style: italic;
  margin-top: 1px;
}

.exam-title {
  font-size: 11.5pt;
  font-weight: bold;
  line-height: 1.22;
  text-transform: uppercase;
}

.subject-title {
  font-size: 11pt;
  font-weight: bold;
  margin-top: 1.5px;
}

.time-title {
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
}

.left-box {
  border: 1px solid #000;
  padding: 1.5px 5px;
  text-align: center;
  width: 170px;
  margin: 2px auto 0 auto;
  line-height: 1.2;
}

.left-box .bold-text {
  font-weight: bold;
  font-size: 9.5pt;
}

.left-box .sub-text {
  font-size: 8.5pt;
  font-style: italic;
  margin-top: 1px;
}

.right-box {
  border: 1.3px solid #000;
  padding: 1.5px 12px;
  font-weight: bold;
  font-size: 10.5pt;
  display: inline-block;
  margin-top: 1.5px;
}

.solid-divider {
  border-top: 1px solid #000;
  margin: 2px 0 1px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 2px 0 3px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 9.5pt;
  font-style: italic;
  margin-bottom: 1.5px;
}

.section-title {
  font-weight: bold;
  font-size: 10.2pt;
  margin-top: 2px;
  margin-bottom: 1.5px;
  text-align: justify;
}

.section-subtitle {
  font-style: italic;
  font-size: 9pt;
  margin-bottom: 2.5px;
}

.question {
  margin-bottom: 2.5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4px;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  padding-left: 4px;
}

.options-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  padding-left: 4px;
}

.sub-item {
  margin-left: 15px;
  margin-top: 1.8px;
  margin-bottom: 2px;
  line-height: 1.3;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 8px;
  margin-bottom: 1.5px;
  font-weight: bold;
  font-size: 10pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9pt;
}

.bbt-table {
  margin: 2px auto;
  border-collapse: collapse;
  text-align: center;
  font-size: 9.5pt;
  border: 1px solid #000;
}

.bbt-table td {
  padding: 1px 7px;
}

.bbt-border-r {
  border-right: 1px solid #000;
  font-weight: bold;
}

.bbt-border-b {
  border-bottom: 1px solid #000;
}
</style>
</head>
<body>

<!-- HEADER -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 03 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">ĐỀ ÔN TẬP GIỮA KỲ I TOÁN 12</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 112</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 2px 0 2px 0;"><img src="assets/de112_bbt_cau1.svg" style="width: 84mm; max-width: 90%; display: inline-block;" alt="Bảng biến thiên Câu 1"></div>
  Hàm số đã cho nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid-4">
    <div><strong>A.</strong> $(-\infty; -1)$.</div>
    <div><strong>B.</strong> $(-1; 3)$.</div>
    <div><strong>C.</strong> $(3; +\infty)$.</div>
    <div><strong>D.</strong> $(-2; 4)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 1)^2(x + 2)(x - 3)^3$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $4$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x^2 - 9x + 5$ trên đoạn $[0; 4]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $5$.</div>
    <div><strong>B.</strong> $-15$.</div>
    <div><strong>C.</strong> $-22$.</div>
    <div><strong>D.</strong> $-27$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Đường tiệm cận đứng của đồ thị hàm số $y = \dfrac{2x - 5}{x + 3}$ là đường thẳng có phương trình
  <div class="options-grid-4">
    <div><strong>A.</strong> $x = -3$.</div>
    <div><strong>B.</strong> $x = 3$.</div>
    <div><strong>C.</strong> $y = 2$.</div>
    <div><strong>D.</strong> $y = -3$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 3x + 5}{x - 2}$ là đường thẳng có phương trình
  <div class="options-grid-4">
    <div><strong>A.</strong> $y = x - 1$.</div>
    <div><strong>B.</strong> $y = x + 1$.</div>
    <div><strong>C.</strong> $y = x - 3$.</div>
    <div><strong>D.</strong> $y = 2x - 1$.</div>
  </div>
</div>

<!-- Câu 6: HÌNH ĐỒ THỊ -->
<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; padding-right: 10px;">
      <span class="question-title">Câu 6.</span> Đường cong ở hình bên là đồ thị của một trong bốn hàm số dưới đây. Hàm số đó là hàm số nào?
      <div class="options-grid-2" style="margin-top: 5px;">
        <div><strong>A.</strong> $y = -x^3 + 3x + 1$.</div>
        <div><strong>B.</strong> $y = x^3 - 3x + 1$.</div>
      </div>
      <div class="options-grid-2" style="margin-top: 4px;">
        <div><strong>C.</strong> $y = x^3 - 3x - 1$.</div>
        <div><strong>D.</strong> $y = x^4 - 2x^2 + 1$.</div>
      </div>
    </div>
    <div style="width: 175px; text-align: center; flex-shrink: 0;">
      <svg width="170" height="118" viewBox="0 0 210 165">
        <defs>
          <marker id="arr1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000" />
          </marker>
        </defs>
        <line x1="18" y1="85" x2="202" y2="85" stroke="#000" stroke-width="1.3" marker-end="url(#arr1)" />
        <text x="194" y="78" font-family="Times New Roman" font-size="13" font-style="italic">x</text>
        <line x1="105" y1="155" x2="105" y2="10" stroke="#000" stroke-width="1.3" marker-end="url(#arr1)" />
        <text x="113" y="18" font-family="Times New Roman" font-size="13" font-style="italic">y</text>
        <text x="93" y="98" font-family="Times New Roman" font-size="12" font-style="italic">O</text>
        <line x1="65" y1="85" x2="65" y2="35" stroke="#666" stroke-width="0.9" stroke-dasharray="3,3" />
        <line x1="65" y1="35" x2="105" y2="35" stroke="#666" stroke-width="0.9" stroke-dasharray="3,3" />
        <line x1="145" y1="85" x2="145" y2="135" stroke="#666" stroke-width="0.9" stroke-dasharray="3,3" />
        <line x1="105" y1="135" x2="145" y2="135" stroke="#666" stroke-width="0.9" stroke-dasharray="3,3" />
        <text x="54" y="98" font-family="Times New Roman" font-size="11.5">-1</text>
        <text x="142" y="77" font-family="Times New Roman" font-size="11.5">1</text>
        <text x="111" y="38" font-family="Times New Roman" font-size="11.5">3</text>
        <text x="89" y="139" font-family="Times New Roman" font-size="11.5">-1</text>
        <text x="111" y="70" font-family="Times New Roman" font-size="11.5">1</text>
        <circle cx="105" cy="68" r="2.8" fill="#000" />
        <circle cx="65" cy="35" r="2.8" fill="#000" />
        <circle cx="145" cy="135" r="2.8" fill="#000" />
        <polyline fill="none" stroke="#003366" stroke-width="2.0" points="35,152 45,118 55,62 65,35 75,37 85,48 95,58 105,68 115,82 125,108 135,128 145,135 155,131 165,105 175,55 182,18" />
      </svg>
    </div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Cho hàm số $y = f(x)$ liên tục trên $\mathbb{R}$ và có bảng biến thiên như sau:
  <div style="text-align: center; margin: 2px 0 2px 0;"><img src="assets/de112_bbt_cau7.svg" style="width: 84mm; max-width: 90%; display: inline-block;" alt="Bảng biến thiên Câu 7"></div>
  Số nghiệm thực phân biệt của phương trình $2f(x) - 1 = 0$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $4$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Tọa độ giao điểm của đồ thị hàm số $y = \dfrac{x - 3}{x + 1}$ với trục tung là
  <div class="options-grid-4">
    <div><strong>A.</strong> $(0; -3)$.</div>
    <div><strong>B.</strong> $(3; 0)$.</div>
    <div><strong>C.</strong> $(0; 3)$.</div>
    <div><strong>D.</strong> $(-1; 0)$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{x - 1}{x^2 - 3x + 2}$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $0$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Tọa độ điểm cực đại của đồ thị hàm số $y = -x^3 + 3x^2 + 2$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $(0; 2)$.</div>
    <div><strong>B.</strong> $(2; 6)$.</div>
    <div><strong>C.</strong> $(2; 2)$.</div>
    <div><strong>D.</strong> $(6; 2)$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Một chất điểm chuyển động thẳng có phương trình tọa độ $s(t) = -t^3 + 6t^2 + 15t + 2$, trong đó $t$ tính bằng giây ($t \ge 0$) và $s$ tính bằng mét. Vận tốc tức thời của chất điểm đạt giá trị lớn nhất tại thời điểm $t$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $t = 2\text{ s}$.</div>
    <div><strong>B.</strong> $t = 4\text{ s}$.</div>
    <div><strong>C.</strong> $t = 5\text{ s}$.</div>
    <div><strong>D.</strong> $t = 1\text{ s}$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Có bao nhiêu giá trị nguyên của tham số $m \in [-100; 100]$ để hàm số $y = \dfrac{x - 3}{x - m}$ đồng biến trên khoảng $(4; +\infty)$?
  <div class="options-grid-4">
    <div><strong>A.</strong> $103$.</div>
    <div><strong>B.</strong> $104$.</div>
    <div><strong>C.</strong> $102$.</div>
    <div><strong>D.</strong> $97$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 1px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 3}{x - 1}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số đồng biến trên các khoảng $(-\infty; 0)$ và $(2; +\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ có đường tiệm cận đứng là $x = 1$ và đường tiệm cận xiên là $y = x - 2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tọa độ tâm đối xứng của đồ thị $(C)$ là giao điểm của hai đường tiệm cận $I(1; 1)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách giữa hai điểm cực trị của đồ thị hàm số $(C)$ bằng $2\sqrt{5}$.</div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x) = \dfrac{1}{3}x^3 - mx^2 + (m^2 - 4)x + 1$ (với $m$ là tham số thực). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Với mọi $m \in \mathbb{R}$, hàm số luôn có hai điểm cực trị phân biệt.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hai điểm cực trị của hàm số đã cho là $x_1 = m - 2$ và $x_2 = m + 2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số đồng biến trên khoảng $(5; +\infty)$ khi và chỉ khi $m \le 3$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Có đúng hai giá trị của tham số $m$ để hai hoành độ cực trị $x_1, x_2$ thoả mãn $x_1^2 + x_2^2 = 20$.</div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Khi một bệnh nhân được tiêm một liều thuốc kháng sinh vào cơ thể, nồng độ của thuốc trong máu sau $t$ giờ (kể từ khi bắt đầu tiêm) được mô tả bởi hàm số:
  $$C(t) = \dfrac{8t}{t^2 + 4}\quad (\text{mg/L}),\quad t \ge 0.$$
  Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tại thời điểm ban đầu ($t = 0$), nồng độ thuốc trong máu của bệnh nhân bằng $0\text{ mg/L}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Nồng độ thuốc trong máu của bệnh nhân đạt giá trị lớn nhất sau khi tiêm $2\text{ giờ}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Nồng độ thuốc lớn nhất trong máu của bệnh nhân ghi nhận được bằng $4\text{ mg/L}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Trong khoảng thời gian từ $t = 2\text{ giờ}$ trở đi, nồng độ thuốc trong máu giảm dần theo thời gian.</div>
</div>

<!-- Câu 4: HÌNH ĐẶT PHÍA DƯỚI CÂU HỎI -->
<div class="question">
  <span class="question-title">Câu 4.</span> Hai trụ đèn cao áp đặt cố định vuông góc với mặt đất bằng phẳng lần lượt có chiều cao là $AH = 6\text{ m}$ và $BK = 12\text{ m}$. Khoảng cách giữa hai chân trụ đèn là $HK = 24\text{ m}$. Để phục vụ chiếu sáng trang trí, một kỹ sư điện muốn đóng một cọc chốt tại điểm $M$ trên đoạn thẳng $HK$ nối hai chân trụ để giăng hai dây cáp thẳng nối từ $M$ đến đỉnh $A$ và từ $M$ đến đỉnh $B$. Đặt khoảng cách $HM = x\text{ (m)}$ với $0 \le x \le 24$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Chiều dài đoạn dây cáp $BM$ tính theo $x$ là $BM = \sqrt{(24 - x)^2 + 144}\text{ (m)}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Nếu đóng cọc chốt tại vị trí trung điểm của đoạn thẳng $HK$ thì tổng chiều dài hai đoạn dây cáp bằng $18\sqrt{2}\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tổng chiều dài hai đoạn dây cáp là ngắn nhất khi cọc chốt $M$ cách chân trụ $H$ một khoảng $8\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Chiều dài ngắn nhất của tổng hai đoạn dây cáp giăng từ $M$ đến hai đỉnh trụ đèn bằng $30\text{ m}$.</div>
  <div style="text-align: center; margin-top: 3px; margin-bottom: 1px;">
    <svg width="460" height="250" viewBox="0 0 210 130">
      <line x1="15" y1="105" x2="195" y2="105" stroke="#000" stroke-width="2.2" />
      <line x1="5" y1="105" x2="205" y2="105" stroke="#666" stroke-width="0.9" stroke-dasharray="2,2" />
      <line x1="28" y1="105" x2="28" y2="58" stroke="#000" stroke-width="3.2" />
      <text x="21" y="51" font-family="Times New Roman" font-size="12.5" font-weight="bold">A</text>
      <text x="21" y="121" font-family="Times New Roman" font-size="12.5" font-weight="bold">H</text>
      <text x="4" y="84" font-family="Times New Roman" font-size="11">6m</text>
      <line x1="182" y1="105" x2="182" y2="16" stroke="#000" stroke-width="3.2" />
      <text x="178" y="12" font-family="Times New Roman" font-size="12.5" font-weight="bold">B</text>
      <text x="178" y="121" font-family="Times New Roman" font-size="12.5" font-weight="bold">K</text>
      <text x="187" y="65" font-family="Times New Roman" font-size="11">12m</text>
      <circle cx="83" cy="105" r="3.8" fill="#cc0000" />
      <text x="79" y="123" font-family="Times New Roman" font-size="12.5" font-weight="bold" fill="#cc0000">M</text>
      <line x1="28" y1="58" x2="83" y2="105" stroke="#0066cc" stroke-width="2.2" />
      <line x1="83" y1="105" x2="182" y2="16" stroke="#0066cc" stroke-width="2.2" />
      <text x="100" y="128" font-family="Times New Roman" font-size="11" font-style="italic">24 m</text>
    </svg>
  </div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 1px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = x^3 - 3(m + 1)x^2 + 3m(m + 2)x + 2026$. Gọi $S$ là tập hợp tất cả các giá trị nguyên của tham số $m \in [-100; 100]$ để hàm số đã cho đồng biến trên khoảng $(2; 6)$. Tính tổng tất cả các phần tử của tập hợp $S$.
</div>

<!-- Câu 2 -->
<div class="question" style="margin-top: 2px; margin-bottom: 3px;">
  <span class="question-title">Câu 2.</span> Một doanh nghiệp sản xuất độc quyền một loại sản phẩm. Nếu doanh nghiệp sản xuất và bán ra $x$ sản phẩm mỗi ngày ($0 < x \le 200$) thì giá bán mỗi sản phẩm là $p(x) = 400 - x\text{ (nghìn đồng)}$, và tổng chi phí sản xuất $x$ sản phẩm đó là $C(x) = x^2 + 40x + 2000\text{ (nghìn đồng)}$. Để điều tiết thị trường, Nhà nước áp dụng mức thuế phụ thu là $t\text{ (nghìn đồng)}$ trên mỗi đơn vị sản phẩm bán ra ($0 < t < 360$). Biết rằng doanh nghiệp luôn chọn mức sản lượng $x$ để tối đa hóa lợi nhuận sau khi nộp thuế. Để tổng số tiền thuế thu được từ doanh nghiệp trong một ngày là lớn nhất, Nhà nước cần ấn định mức thuế $t$ bằng bao nhiêu nghìn đồng?
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Tìm giá trị của tham số thực $m$ để giá trị lớn nhất của hàm số $f(x) = \dfrac{2x + m}{x - 1}$ trên đoạn $[2; 4]$ bằng $5$.
</div>

<!-- Câu 4 -->
<div class="question" style="margin-top: 2px; margin-bottom: 3px;">
  <span class="question-title">Câu 4.</span> Nhà máy A chuyên sản xuất một loại sản phẩm cho nhà máy B; Hai nhà máy thỏa thuận rằng, hàng tháng nhà máy A cung cấp cho nhà máy B số lượng sản phẩm theo đơn đặt hàng của nhà máy B (tối đa $90\text{ tấn sản phẩm}$). Nếu số lượng đặt hàng là $x\text{ tấn sản phẩm}$ thì giá bán cho mỗi tấn sản phẩm là $P(x) = 90 - 0{,}01x^2\text{ (đơn vị triệu đồng)}$. Chi phí để nhà máy A sản xuất $x\text{ tấn sản phẩm}$ trong một tháng là $C(x) = \dfrac{1}{2}(200 + 27x)\text{ (đơn vị triệu đồng)}$, thuế giá trị gia tăng mà nhà máy A phải đóng cho nhà nước là $10\%$ tổng doanh thu mỗi tháng. Hỏi mỗi tháng nhà máy A thu được lợi nhuận cao nhất bao nhiêu triệu đồng (sau khi đã trừ thuế giá trị gia tăng)?
</div>

<!-- Câu 5: HÌNH VẼ PHÓNG TO THÊM 50% NỮA (width=350px, height=235px) ĐẶT GIỮA -->
<div class="question" style="margin-top: 3px; margin-bottom: 4px;">
  <div>
    <span class="question-title">Câu 5.</span> Có ba ngôi nhà $A, B, C$ mà khoảng cách giữa từng cặp ngôi nhà đều bằng $4\text{ km}$. Một ngôi nhà thứ tư $D$ ở bên ngoài vùng tam giác $ABC$, mà góc nhìn của $D$ đối với hai ngôi nhà $A, B$ là $120^\circ$ và khoảng cách từ $D$ đến $A$ và $B$ bằng nhau (như hình vẽ bên dưới). Người ta muốn chọn điểm $M$ nằm giữa $B$ và $C$, để làm con đường đi từ $C$ đến $M$ rồi từ $M$ đến $D$. Biết giá tiền làm đường trên đoạn $BC$ là $200\text{ triệu đồng/km}$ và trên đoạn $MD$ là $400\text{ triệu đồng/km}$. Hỏi tổng chi phí nhỏ nhất để làm con đường đó là bao nhiêu triệu đồng?
  </div>
  <div style="text-align: center; margin-top: 5px; margin-bottom: 4px;">
    <!-- Enlarged by +50% (width 350px, height 235px) -->
    <svg width="350" height="235" viewBox="0 0 215 145">
      <defs>
        <g id="house_icon">
          <rect x="-7" y="-3.5" width="14" height="10" fill="#fff" stroke="#000" stroke-width="1.2"/>
          <polygon points="-9,-3.5 0,-11.5 9,-3.5" fill="#fff" stroke="#000" stroke-width="1.2"/>
        </g>
      </defs>
      <line x1="58" y1="126" x2="192" y2="126" stroke="#000" stroke-width="1.6" />
      <line x1="58" y1="126" x2="125" y2="18" stroke="#000" stroke-width="1.6" />
      <line x1="192" y1="126" x2="125" y2="18" stroke="#000" stroke-width="1.6" />
      <line x1="58" y1="126" x2="58" y2="54" stroke="#000" stroke-width="1.6" />
      <line x1="58" y1="54" x2="125" y2="18" stroke="#000" stroke-width="1.6" />
      <line x1="55" y1="90" x2="61" y2="90" stroke="#000" stroke-width="1.3" />
      <line x1="89" y1="33" x2="94" y2="40" stroke="#000" stroke-width="1.3" />
      <path d="M 58 68 A 15 15 0 0 0 71 46" fill="none" stroke="#000" stroke-width="1.3" />
      <line x1="192" y1="126" x2="103" y2="126" stroke="#e02475" stroke-width="3.2" />
      <line x1="103" y1="126" x2="58" y2="54" stroke="#e02475" stroke-width="2.6" />
      <circle cx="103" cy="126" r="3.5" fill="#e02475" />
      <text x="98" y="142" font-family="Times New Roman" font-size="12" font-weight="bold" fill="#e02475">M</text>
      <use href="#house_icon" x="140" y="14" />
      <text x="110" y="13" font-family="Times New Roman" font-size="13" font-weight="bold">A</text>
      <use href="#house_icon" x="45" y="122" />
      <text x="42" y="142" font-family="Times New Roman" font-size="13" font-weight="bold">B</text>
      <use href="#house_icon" x="204" y="122" />
      <text x="201" y="142" font-family="Times New Roman" font-size="13" font-weight="bold">C</text>
      <use href="#house_icon" x="45" y="52" />
      <text x="41" y="65" font-family="Times New Roman" font-size="13" font-weight="bold">D</text>
    </svg>
  </div>
</div>

<!-- Câu 6: THUẦN CHỮ KHÔNG CÓ HÌNH VẼ -->
<div class="question" style="margin-top: 3px;">
  <span class="question-title">Câu 6.</span> Một hộ gia đình dự định xây một bể chứa nước sinh hoạt hình hộp chữ nhật không nắp có thể tích bằng $60\text{ m}^3$. Đáy bể là hình chữ nhật có chiều dài gấp đôi chiều rộng. Biết chi phí vật liệu xây đáy bể là $500.000\text{ đồng/m}^2$ và chi phí xây bốn mặt thành xung quanh bể là $300.000\text{ đồng/m}^2$. Hỏi chi phí nhỏ nhất mà hộ gia đình cần bỏ ra để hoàn thành bể nước đó là bao nhiêu triệu đồng?
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

html_path = 'exam_de_khao_sat_toan_12_ma112.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'De_Thi_Khao_Sat_Toan_12_Ma_112.pdf'
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

print('Running Chrome for exam PDF...')
res = subprocess.run(cmd, capture_output=True, text=True)
print('Chrome exit code:', res.returncode)

reader = pypdf.PdfReader(output_pdf)
print('Total pages of exam PDF:', len(reader.pages))
