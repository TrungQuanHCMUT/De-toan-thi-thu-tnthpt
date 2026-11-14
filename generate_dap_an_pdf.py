import os
import subprocess
import pypdf

template = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải - Đề Thi Thử Giữa Kì 1 - Mã đề: 105</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin-top: 9mm;
  margin-bottom: 10mm;
  margin-left: 13mm;
  margin-right: 13mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 105";
    font-family: 'Times New Roman', Times, serif;
    font-size: 8.8pt;
    font-style: italic;
    color: #444;
  }
  @bottom-left {
    content: "";
  }
}

body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 9.7pt;
  line-height: 1.35;
  color: #111;
  margin: 0;
  padding: 0;
}

/* Header styling */
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

.sub-header {
  font-size: 9pt;
  text-transform: uppercase;
  font-weight: bold;
}

.main-title {
  font-size: 10pt;
  font-weight: bold;
  text-transform: uppercase;
}

.doc-title-container {
  text-align: center;
  margin: 4px 0 6px 0;
  padding: 3px 0;
  border-top: 1.5px solid #1a365d;
  border-bottom: 1.5px solid #1a365d;
}

.doc-title {
  font-size: 12pt;
  font-weight: bold;
  color: #1a365d;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.doc-subtitle {
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
  color: #2d3748;
}

/* Section Titles */
.section-title {
  background: #edf2f7;
  color: #1a365d;
  font-size: 10pt;
  font-weight: bold;
  padding: 2.5px 8px;
  margin-top: 6px;
  margin-bottom: 5px;
  border-left: 3.5px solid #1a365d;
  border-radius: 2px;
}

/* Tables */
table.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 5px;
  text-align: center;
  font-size: 9pt;
}

table.ans-table th, table.ans-table td {
  border: 1px solid #718096;
  padding: 2.5px 1px;
}

table.ans-table th {
  background-color: #f7fafc;
  color: #2d3748;
  font-weight: bold;
}

table.ans-table tr.ans-row td {
  font-weight: bold;
  color: #1a365d;
  font-size: 9.6pt;
}

table.p2-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 5px;
  font-size: 9pt;
}

table.p2-table th, table.p2-table td {
  border: 1px solid #718096;
  padding: 2.5px 4px;
  text-align: center;
}

table.p2-table th {
  background-color: #f7fafc;
  font-weight: bold;
}

.tag-true {
  color: #22543d;
  background-color: #c6f6d5;
  padding: 0.5px 6px;
  border-radius: 3px;
  font-weight: bold;
  display: inline-block;
  font-size: 8.8pt;
}

.tag-false {
  color: #742a2a;
  background-color: #fed7d7;
  padding: 0.5px 6px;
  border-radius: 3px;
  font-weight: bold;
  display: inline-block;
  font-size: 8.8pt;
}

/* Question / Solution Box */
.question-block {
  margin-bottom: 6px;
}

.question-heading {
  font-weight: bold;
  font-size: 9.8pt;
  color: #1a365d;
  margin-bottom: 2px;
  border-bottom: 1px dashed #cbd5e0;
  padding-bottom: 1px;
}

.solution-box {
  background-color: #fcfdfd;
  border-left: 2.5px solid #4a5568;
  padding: 4px 8px;
  margin-top: 2px;
  border-radius: 0 3px 3px 0;
}

.solution-step {
  margin-bottom: 3px;
  text-align: justify;
}

.final-ans {
  font-weight: bold;
  color: #c53030;
}

.katex-display { margin: 2.5px 0 !important; }
.katex {
  font-size: 1.01em;
}

.page-break {
  page-break-before: always;
}
</style>
</head>
<body>

<!-- Header -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="sub-header">SỞ GD&ĐT QUẢNG TRỊ</div>
      <div class="main-title">TRƯỜNG THPT QUẢNG TRỊ</div>
      <div style="font-size: 8.8pt; font-style: italic; margin-top: 1px;">Biên soạn: Trần Trung Quân</div>
    </td>
    <td class="right-header">
      <div class="sub-header">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 NĂM HỌC 2026 - 2027</div>
      <div class="main-title">MÔN: TOÁN – LỚP 12 (ĐỀ THI THỬ GIỮA KÌ 1)</div>
      <div style="font-size: 8.8pt; font-weight: bold; margin-top: 1px;">MÃ ĐỀ THI: 105</div>
    </td>
  </tr>
</table>

<div class="doc-title-container">
  <div class="doc-title">BẢNG ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT</div>
  <div class="doc-subtitle">(Bảng đáp án toàn bộ đề thi & Hướng dẫn giải Phần II, Phần III)</div>
</div>

<!-- ==================== A. BẢNG ĐÁP ÁN (3 PHẦN TỪ TRÊN XUỐNG DƯỚI) ==================== -->
<div class="section-title">A. BẢNG ĐÁP ÁN TOÀN BỘ ĐỀ THI (MÃ ĐỀ: 105)</div>

<div style="font-weight: bold; margin-bottom: 2px; font-size: 9.2pt; color: #2b6cb0;">
  PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)
</div>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr class="ans-row">
    <td>Đáp án</td>
    <td>B</td><td>C</td><td>A</td><td>C</td><td>B</td><td>D</td>
    <td>A</td><td>A</td><td>C</td><td>D</td><td>D</td><td>B</td>
  </tr>
</table>

<div style="font-weight: bold; margin-top: 3px; margin-bottom: 2px; font-size: 9.2pt; color: #2b6cb0;">
  PHẦN II. Câu trắc nghiệm đúng sai (4 câu – 4,0 điểm)
</div>
<table class="p2-table">
  <tr>
    <th style="width: 20%;">Câu hỏi</th>
    <th style="width: 20%;">Lệnh hỏi a)</th>
    <th style="width: 20%;">Lệnh hỏi b)</th>
    <th style="width: 20%;">Lệnh hỏi c)</th>
    <th style="width: 20%;">Lệnh hỏi d)</th>
  </tr>
  <tr>
    <td><strong>Câu 1</strong> (BBT hàm bậc 3)</td>
    <td><span class="tag-false">SAI</span></td>
    <td><span class="tag-false">SAI</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
  </tr>
  <tr>
    <td><strong>Câu 2</strong> (Hàm bậc 2/1)</td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-false">SAI</span></td>
  </tr>
  <tr>
    <td><strong>Câu 3</strong> (Dân số thị trấn)</td>
    <td><span class="tag-false">SAI</span></td>
    <td><span class="tag-false">SAI</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
  </tr>
  <tr>
    <td><strong>Câu 4</strong> (Tàu đổ bộ)</td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-true">ĐÚNG</span></td>
    <td><span class="tag-false">SAI</span></td>
    <td><span class="tag-false">SAI</span></td>
  </tr>
</table>

<div style="font-weight: bold; margin-top: 3px; margin-bottom: 2px; font-size: 9.2pt; color: #2b6cb0;">
  PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu – 3,0 điểm)
</div>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th>
  </tr>
  <tr class="ans-row">
    <td>Đáp số</td>
    <td>473</td><td>57,9</td><td>3</td><td>11,3</td><td>2</td><td>22,6</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI PHẦN II ==================== -->
<div class="section-title">B. HƯỚNG DẪN GIẢI CHI TIẾT PHẦN II (CÂU TRẮC NGHIỆM ĐÚNG SAI)</div>

<!-- Câu 1 PHẦN II -->
<div class="question-block">
  <div class="question-heading">Câu 1</div>
  <div class="solution-box">
    <div class="solution-step">
      Giả sử hàm số bậc ba có dạng $f(x) = ax^3 + bx^2 + cx + d\quad (a \ne 0)$.<br>
      Đạo hàm: $f'(x) = 3ax^2 + 2bx + c$.<br>
      Từ bảng biến thiên, đồ thị có 2 điểm cực trị là $(-1; 3)$ và $(1; -5)$. Ta lập hệ 4 phương trình 4 ẩn:
      $$\begin{cases}
      f(-1) = 3 \\
      f(1) = -5 \\
      f'(-1) = 0 \\
      f'(1) = 0
      \end{cases}
      \Leftrightarrow
      \begin{cases}
      -a + b - c + d = 3 \\
      a + b + c + d = -5 \\
      3a - 2b + c = 0 \\
      3a + 2b + c = 0
      \end{cases}
      \Leftrightarrow
      \begin{cases}
      a = 2 \\
      b = 0 \\
      c = -6 \\
      d = -1
      \end{cases}
      \implies f(x) = 2x^3 - 6x - 1$$
    </div>
    <div class="solution-step">
      • <strong>a)</strong> Khi qua $x = 1$, $f'(x)$ đổi dấu từ âm sang dương và $f(1) = -5$ nên $x = 1$ là <strong>điểm cực tiểu</strong> của hàm số (điểm cực đại là $x = -1$ với $f(-1) = 3$). $\implies$ <span class="tag-false">SAI</span>.
    </div>
    <div class="solution-step">
      • <strong>b)</strong> Hàm số chỉ đồng biến trên $(-\infty; -1)$ và $(1; +\infty)$. Khoảng $(-5; +\infty)$ chứa khoảng $(-1; 1)$ hàm số nghịch biến, do đó khẳng định hàm số đồng biến trên $(-5; +\infty)$ là sai. $\implies$ <span class="tag-false">SAI</span>.
    </div>
    <div class="solution-step">
      • <strong>c)</strong> Thay $x = 0$ vào hàm số: $f(0) = 2(0^3) - 6(0) - 1 = -1 \implies$ đồ thị hàm số đi qua điểm $(0; -1)$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>d)</strong> Ta có $f(-1) = 3$. Tính giá trị tại $x = 2$: $f(2) = 2(2^3) - 6(2) - 1 = 16 - 12 - 1 = 3$. Do đó $f(-1) = f(2) = 3$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
  </div>
</div>



<div class="page-break"></div>
<!-- Câu 2 PHẦN II -->
<div class="question-block">
  <div class="question-heading">Câu 2</div>
  <div class="solution-box">
    <div class="solution-step">
      Xét hàm số $y = \dfrac{-x^2 - 3x + 4}{x - 3}$. Chia tử cho mẫu:
      $$-x^2 - 3x + 4 = -(x - 3)(x + 6) - 14 \implies y = -x - 6 - \dfrac{14}{x - 3}$$
    </div>
    <div class="solution-step">
      • <strong>a)</strong> Vì $\lim_{x \to \pm\infty} [y - (-x - 6)] = \lim_{x \to \pm\infty} \left(-\dfrac{14}{x - 3}\right) = 0$, nên đường tiệm cận xiên là $y = -x - 6$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>b)</strong> Tiệm cận đứng là $x = 3$. Thay $x = 3$ vào tiệm cận xiên: $y = -3 - 6 = -9 \implies$ giao điểm hai đường tiệm cận là $I(3; -9)$, là tâm đối xứng của đồ thị. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>c)</strong> $y' = -1 + \dfrac{14}{(x - 3)^2} = \dfrac{-x^2 + 6x + 5}{(x - 3)^2}$. Cho $y' = 0 \Leftrightarrow x^2 - 6x - 5 = 0$. Có $a \cdot c = 1 \cdot (-5) < 0$ nên luôn có hai nghiệm phân biệt trái dấu $x_1 < 0 < x_2 \implies$ hai điểm cực trị nằm về hai phía đối với trục tung $Oy$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>d)</strong> Hoành độ giao điểm với trục hoành: $\dfrac{-x^2 - 3x + 4}{x - 3} = 0 \Leftrightarrow -x^2 - 3x + 4 = 0 \Leftrightarrow x = 1$ hoặc $x = -4$ (thỏa mãn $x \ne 3$). Đồ thị cắt $Ox$ tại hai điểm phân biệt $(1; 0)$ và $(-4; 0)$. Khẳng định "không cắt trục hoành" là sai. $\implies$ <span class="tag-false">SAI</span>.
    </div>
  </div>
</div>

<!-- PAGE BREAK: PAGE 2 -->


<!-- Câu 3 PHẦN II -->
<div class="question-block">
  <div class="question-heading">Câu 3</div>
  <div class="solution-box">
    <div class="solution-step">
      Hàm số số dân thị trấn: $f(t) = \dfrac{26t + 10}{t + 5}\quad (t \ge 0)$.
    </div>
    <div class="solution-step">
      • <strong>a)</strong> $f'(t) = \dfrac{26(5) - 10(1)}{(t + 5)^2} = \dfrac{120}{(t + 5)^2} > 0, \forall t \ge 0$. Hàm số luôn đồng biến trên $[0; +\infty)$, tức số dân luôn tăng theo thời gian, không bao giờ giảm. Khẳng định "dân số giảm" là sai. $\implies$ <span class="tag-false">SAI</span>.
    </div>
    <div class="solution-step">
      • <strong>b)</strong> Năm 1998 ứng với $t = 1998 - 1970 = 28$. Tốc độ tăng dân số:
      $$f'(28) = \dfrac{120}{(28 + 5)^2} = \dfrac{120}{33^2} = \dfrac{120}{1089} \approx 0{,}1102\text{ (nghìn người/năm)} \ne 0{,}125$$
      $\implies$ <span class="tag-false">SAI</span>.
    </div>
    <div class="solution-step">
      • <strong>c)</strong> Áp dụng công thức đạo hàm phân thức bậc nhất trên bậc nhất: $f'(t) = \dfrac{26 \cdot 5 - 10 \cdot 1}{(t + 5)^2} = \dfrac{120}{(t + 5)^2},\ (t \ge 0)$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>d)</strong> Đầu năm 1980 ứng với $t = 1980 - 1970 = 10$. Thay $t = 10$: $f(10) = \dfrac{26(10) + 10}{10 + 5} = \dfrac{270}{15} = 18\text{ (nghìn người)}$. $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
  </div>
</div>

<!-- Câu 4 PHẦN II -->
<div class="question-block">
  <div class="question-heading">Câu 4</div>
  <div class="solution-box">
    <div class="solution-step">
      Độ cao con tàu đổ bộ Mặt Trăng: $h(t) = -0{,}01t^3 + 1{,}1t^2 - 30t + 250\quad (0 \le t \le 50)$.
    </div>
    <div class="solution-step">
      • <strong>a)</strong> Vận tốc tức thời là đạo hàm bậc nhất của hàm độ cao:
      $$v(t) = h'(t) = (-0{,}01t^3 + 1{,}1t^2 - 30t + 250)' = -0{,}03t^2 + 2{,}2t - 30,\quad (0 \le t \le 50)$$
      $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>b)</strong> Thay $t = 25$ vào biểu thức vận tốc:
      $$v(25) = -0{,}03 \cdot (25)^2 + 2{,}2 \cdot 25 - 30 = -18{,}75 + 55 - 30 = 6{,}25\text{ (km/s)}$$
      $\implies$ <span class="tag-true">ĐÚNG</span>.
    </div>
    <div class="solution-step">
      • <strong>c)</strong> Gia tốc tức thời của con tàu: $a(t) = v'(t) = -0{,}06t + 2{,}2$. Tại $t = 25$:
      $$a(25) = -0{,}06(25) + 2{,}2 = -1{,}5 + 2{,}2 = 0{,}7\text{ km/s}^2 > 0$$
      Vì $v'(25) > 0$ nên tại $t = 25$ vận tốc tức thời của con tàu <strong>đang tăng</strong>, không phải tiếp tục giảm. $\implies$ <span class="tag-false">SAI</span>.
    </div>
    <div class="solution-step">
      • <strong>d)</strong> Cho $h'(t) = v(t) = 0 \Leftrightarrow -0{,}03t^2 + 2{,}2t - 30 = 0 \Leftrightarrow 3t^2 - 220t + 3000 = 0$.<br>
      Nghiệm thuộc khoảng $(0; 50)$ là $t_1 = \dfrac{110 - \sqrt{3100}}{3} \approx 18{,}108\text{ (giây)}$. Độ cao nhỏ nhất là:
      $$h(18{,}108) = -0{,}01(18{,}108)^3 + 1{,}1(18{,}108)^2 - 30(18{,}108) + 250 \approx 8{,}07\text{ km} \ne 10\text{ km}$$
      $\implies$ <span class="tag-false">SAI</span>.
    </div>
  </div>
</div>


<div class="page-break"></div>
<!-- ==================== C. HƯỚNG DẪN GIẢI PHẦN III ==================== -->
<div class="section-title">C. HƯỚNG DẪN GIẢI CHI TIẾT PHẦN III (CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN)</div>

<!-- Câu 1 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 1</div>
  <div class="solution-box">
    <div class="solution-step">
      • Đặt khoảng cách $HC = x\text{ (m)}$ với $0 < x < 900$.<br>
      • Quãng đường chiến sỹ chạy bộ dọc theo bờ sông từ điểm $C$ đến điểm $B$ là:
      $$CB = HB - HC = 900 - x\text{ (m)}$$
      Thời gian chạy bộ trên bờ với vận tốc $3\text{ m/s}$ là:
      $$t_2 = \dfrac{900 - x}{3} = 300 - \dfrac{x}{3}\text{ (giây)}$$
      • Xét chuyển động bơi từ điểm $A$ đến điểm $C$:<br>
      Chọn hệ trục tọa độ với gốc tại $A(0; 0)$, bờ sông xuất phát là $y = 0$, bờ sông bên kia là $y = 300$. Điểm $H(0; 300)$ và điểm $C(x; 300)$.<br>
      Véctơ độ dời bơi là $\vec{AC} = (x; 300)$. Vận tốc dòng nước chảy từ $H$ sang $B$ là $\vec{v}_n = (1; 0)\text{ m/s}$.<br>
      Gọi $\vec{v}_{b/n}$ là vận tốc bơi của chiến sỹ so với nước ($|\vec{v}_{b/n}| = 1\text{ m/s}$). Vận tốc thực tế so với bờ là $\vec{v} = \vec{v}_{b/n} + \vec{v}_n$.<br>
      Gọi $t_1$ là thời gian bơi từ $A$ sang $C$, ta có hệ thức véctơ:
      $$\vec{AC} = \vec{v} \cdot t_1 = (\vec{v}_{b/n} + \vec{v}_n) t_1 \implies \vec{v}_{b/n} \cdot t_1 = \vec{AC} - \vec{v}_n \cdot t_1 = (x - t_1;\ 300)$$
      Lấy bình phương độ lớn hai vế:
      $$(|\vec{v}_{b/n}| \cdot t_1)^2 = (x - t_1)^2 + 300^2 \Leftrightarrow t_1^2 = x^2 - 2xt_1 + t_1^2 + 90000$$
      $$\Leftrightarrow 2xt_1 = x^2 + 90000 \Leftrightarrow t_1 = \dfrac{x^2 + 90000}{2x} = \dfrac{x}{2} + \dfrac{45000}{x}\text{ (giây)}$$
      • Tổng thời gian hoàn thành kế hoạch là:
      $$T(x) = t_1 + t_2 = \left(\dfrac{x}{2} + \dfrac{45000}{x}\right) + \left(300 - \dfrac{x}{3}\right) = 300 + \dfrac{x}{6} + \dfrac{45000}{x}$$
      • Xét đạo hàm của hàm số $T(x)$ trên khoảng $(0; 900)$:
      $$T'(x) = \dfrac{1}{6} - \dfrac{45000}{x^2} = \dfrac{x^2 - 270000}{6x^2}$$
      Cho $T'(x) = 0 \Leftrightarrow x^2 = 270000 \Leftrightarrow x = 300\sqrt{3} \approx 519{,}6\text{ m}\quad (\text{do } 0 < x < 900)$.<br>
      • Xét dấu đạo hàm: Với $x \in (0; 300\sqrt{3})$ thì $T'(x) < 0$ (hàm giảm); với $x \in (300\sqrt{3}; 900)$ thì $T'(x) > 0$ (hàm tăng).<br>
      Do đó hàm số $T(x)$ đạt giá trị nhỏ nhất tại $x = 300\sqrt{3}$.<br>
      • Tổng thời gian ít nhất là:
      $$T_{\min} = T(300\sqrt{3}) = 300 + \dfrac{300\sqrt{3}}{6} + \dfrac{45000}{300\sqrt{3}} = 300 + 100\sqrt{3} \approx 473{,}205\text{ (giây)}$$
      Làm tròn đến hàng đơn vị, kết quả là <span class="final-ans">473</span>.
    </div>
  </div>
</div>

<!-- PAGE BREAK: PAGE 3 -->



<!-- Câu 2 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 2</div>
  <div class="solution-box">
    <div class="solution-step">
      • Thời gian thực hiện chuyến đi dài $640\text{ km}$ với vận tốc duy trì $x\text{ (km/h)}$: $t = \dfrac{640}{x}\text{ (giờ)}$.<br>
      • Tổng lượng dầu diesel tiêu thụ: $V = 640 \cdot G(x) = 640 \left(\dfrac{250}{x} + \dfrac{x}{10}\right)\text{ (lít)}$.<br>
      • Chi phí mua nhiên liệu dầu diesel ($17{,}5\text{ nghìn đồng/lít}$):
      $$C_{\text{dầu}} = 17{,}5 \cdot 640 \left(\dfrac{250}{x} + \dfrac{x}{10}\right) = 640 \left(\dfrac{4375}{x} + 1{,}75x\right)\text{ (nghìn đồng)}$$
      • Chi phí trả lương thuyền trưởng ($1{,}5\text{ triệu đồng} = 1500\text{ nghìn đồng/giờ}$):
      $$C_{\text{lương}} = 1500 \cdot t = 1500 \cdot \dfrac{640}{x} = 640 \cdot \dfrac{1500}{x}\text{ (nghìn đồng)}$$
      • Tổng chi phí vận hành toàn bộ chuyến đi:
      $$C(x) = C_{\text{dầu}} + C_{\text{lương}} = 640 \left(\dfrac{4375 + 1500}{x} + 1{,}75x\right) = 640 \left(\dfrac{5875}{x} + 1{,}75x\right)$$
      • Xét đạo hàm của hàm số $C(x)$ với $x > 0$:
      $$C'(x) = 640 \left(-\dfrac{5875}{x^2} + 1{,}75\right) = 640 \cdot \dfrac{1{,}75x^2 - 5875}{x^2}$$
      Cho $C'(x) = 0 \Leftrightarrow 1{,}75x^2 - 5875 = 0 \Leftrightarrow x^2 = \dfrac{5875}{1{,}75} = \dfrac{23500}{7} \implies x = \sqrt{\dfrac{23500}{7}} \approx 57{,}9408\text{ (km/h)}$.<br>
      • Với $x \in \left(0; \sqrt{\dfrac{23500}{7}}\right)$ thì $C'(x) < 0$; với $x \in \left(\sqrt{\dfrac{23500}{7}}; +\infty\right)$ thì $C'(x) > 0$.<br>
      Do đó chi phí $C(x)$ đạt giá trị nhỏ nhất khi vận tốc $x = \sqrt{\dfrac{23500}{7}} \approx 57{,}9408\text{ km/h}$.<br>
      Làm tròn đến hàng phần mười, kết quả là <span class="final-ans">57,9</span>.
    </div>
  </div>
</div>

<div class="page-break"></div>
<!-- Câu 3 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 3</div>
  <div class="solution-box">
    <div class="solution-step">
      Xét hàm số: $y = \dfrac{\sqrt{x^2 - 9}}{x^3 - 16x}$.<br>
      • <strong>Tập xác định:</strong> $x^2 - 9 \ge 0 \Leftrightarrow x \in (-\infty; -3] \cup [3; +\infty)$ và $x(x^2 - 16) \ne 0 \Leftrightarrow x \notin \{0; \pm 4\}$.<br>
      Do $0 \notin (-\infty; -3] \cup [3; +\infty)$ nên tập xác định là: $D = (-\infty; -4) \cup (-4; -3] \cup [3; 4) \cup (4; +\infty)$.<br>
      • <strong>Tiệm cận ngang:</strong> $\lim_{x \to \pm\infty} \dfrac{\sqrt{x^2 - 9}}{x^3 - 16x} = 0 \implies y = 0$ là đường tiệm cận ngang duy nhất (bậc tử sau khai căn là 1, bậc mẫu là 3 nên không có tiệm cận xiên).<br>
      • <strong>Tiệm cận đứng:</strong><br>
      - Tại $x = 4$: Mẫu bằng $0$, tử bằng $\sqrt{4^2 - 9} = \sqrt{7} \ne 0 \implies \lim_{x \to 4^+} y = +\infty \implies x = 4$ là tiệm cận đứng.<br>
      - Tại $x = -4$: Mẫu bằng $0$, tử bằng $\sqrt{(-4)^2 - 9} = \sqrt{7} \ne 0 \implies \lim_{x \to -4^+} y = +\infty \implies x = -4$ là tiệm cận đứng.<br>
      - Điểm $x = 0$ không thuộc tập xác định và xung quanh $x = 0$ hàm số không xác định nên không thể xét giới hạn $\implies x = 0$ không là tiệm cận đứng.<br>
      • <strong>Tổng số đường tiệm cận:</strong> $1$ (tiệm cận ngang) $+ 2$ (tiệm cận đứng) $= 3$ đường tiệm cận. Điền đáp số: <span class="final-ans">3</span>.
    </div>
  </div>
</div>


<!-- Câu 4 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 4</div>
  <div class="solution-box">
    <div class="solution-step">
      • Hình vuông ban đầu có cạnh bằng $6\text{ cm}$, đường chéo bằng $6\sqrt{2}\text{ cm}$. Khoảng cách từ tâm đến mỗi đỉnh là $3\sqrt{2}\text{ cm}$.<br>
      • Gọi cạnh đáy của hình hộp là $b$ ($0 < b < 3\sqrt{2}\text{ cm}$) và chiều cao thành hộp là $a$. Nửa đường chéo đáy hình vuông có độ dài là $\dfrac{b}{\sqrt{2}}$.<br>
      • Dọc theo phương đường chéo ban đầu: $a + b = 3\sqrt{2} \implies a = 3\sqrt{2} - b$.<br>
      • Thể tích của hình hộp: $V(b) = a \cdot b^2 = (3\sqrt{2} - b)b^2 = 3\sqrt{2}b^2 - b^3\quad (0 < b < 3\sqrt{2})$.<br>
      • Đạo hàm: $V'(b) = 6\sqrt{2}b - 3b^2 = 3b(2\sqrt{2} - b) = 0 \Leftrightarrow b = 2\sqrt{2}\text{ cm} \implies a = \sqrt{2}\text{ cm}$.<br>
      • Thể tích lớn nhất: $V_{\max} = \sqrt{2} \cdot (2\sqrt{2})^2 = 8\sqrt{2} \approx 11{,}3137\text{ cm}^3$. Làm tròn đến hàng phần chục: <span class="final-ans">11,3</span>.
    </div>
  </div>
</div>

<!-- Câu 5 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 5</div>
  <div class="solution-box">
    <div class="solution-step">
      Xét hàm số: $y = \dfrac{1}{3}x^3 - (m + 1)x^2 + (m^2 + 2m)x - 4$ trên $\mathbb{R}$.<br>
      Đạo hàm bậc nhất và bậc hai: $y' = x^2 - 2(m + 1)x + (m^2 + 2m)$ và $y'' = 2x - 2(m + 1)$.<br>
      • <strong>Điều kiện cần:</strong> Để hàm số đạt cực trị tại $x = 2$ thì $y'(2) = 0$:
      $$2^2 - 2(m + 1)(2) + m^2 + 2m = 0 \Leftrightarrow m^2 - 2m = 0 \Leftrightarrow \begin{bmatrix} m = 0 \\ m = 2 \end{bmatrix}$$
      • <strong>Điều kiện đủ (thử lại):</strong><br>
      - Với $m = 0$: $y''(2) = 4 - 2(1) = 2 > 0 \implies x = 2$ là điểm <strong>cực tiểu</strong> (loại).<br>
      - Với $m = 2$: $y''(2) = 4 - 2(3) = -2 < 0 \implies x = 2$ là điểm <strong>cực đại</strong> (thỏa mãn yêu cầu).<br>
      <em>(Kiểm tra: khi $m = 2$, $y' = x^2 - 6x + 8 = (x - 2)(x - 4)$, qua $x = 2$ thì $y'$ đổi dấu từ $+$ sang $-$, đúng là điểm cực đại).</em><br>
      Vậy giá trị của tham số $m$ cần tìm là <span class="final-ans">2</span>.
    </div>
  </div>
</div>

<!-- PAGE BREAK: PAGE 4 -->



<div class="page-break"></div>
<!-- Câu 6 PHẦN III -->
<div class="question-block">
  <div class="question-heading">Câu 6</div>
  <div class="solution-box">
    <div class="solution-step">
      • Vì hình chữ nhật nội tiếp đường tròn bán kính $R = 4$ nên đường chéo của hình chữ nhật bằng đường kính đường tròn:
      $$d = 2R = 2 \cdot 4 = 8$$
      • Gọi độ dài một cạnh của hình chữ nhật là $x$ với điều kiện $0 < x < 8$.<br>
      Theo định lý Pythagore trong tam giác vuông tạo bởi hai cạnh kề và đường chéo, độ dài cạnh còn lại của hình chữ nhật là:
      $$y = \sqrt{d^2 - x^2} = \sqrt{8^2 - x^2} = \sqrt{64 - x^2}$$
      • Diện tích của hình chữ nhật được biểu diễn theo biến $x$ bởi hàm số:
      $$S(x) = x \cdot \sqrt{64 - x^2}\quad (0 < x < 8)$$
      • Xét đạo hàm của hàm số $S(x)$ trên khoảng $(0; 8)$:
      $$S'(x) = 1 \cdot \sqrt{64 - x^2} + x \cdot \dfrac{-2x}{2\sqrt{64 - x^2}} = \sqrt{64 - x^2} - \dfrac{x^2}{\sqrt{64 - x^2}} = \dfrac{64 - 2x^2}{\sqrt{64 - x^2}}$$
      • Cho $S'(x) = 0 \Leftrightarrow 64 - 2x^2 = 0 \Leftrightarrow x^2 = 32 \Leftrightarrow x = \sqrt{32} = 4\sqrt{2}\quad (\text{do } 0 < x < 8)$.<br>
      • Xét dấu đạo hàm trên khoảng $(0; 8)$:<br>
      - Với $x \in (0; 4\sqrt{2})$: $S'(x) > 0 \implies$ hàm số $S(x)$ đồng biến.<br>
      - Với $x \in (4\sqrt{2}; 8)$: $S'(x) < 0 \implies$ hàm số $S(x)$ nghịch biến.<br>
      Do đó hàm số $S(x)$ đạt giá trị lớn nhất tại điểm $x = 4\sqrt{2}$.<br>
      • Khi đó độ dài cạnh còn lại là:
      $$y = \sqrt{64 - (4\sqrt{2})^2} = \sqrt{32} = 4\sqrt{2}$$
      (tức diện tích đạt giá trị lớn nhất khi hình chữ nhật là hình vuông cạnh $4\sqrt{2}$).<br>
      • Chu vi của hình chữ nhật khi diện tích đạt giá trị lớn nhất là:
      $$P = 2(x + y) = 2(4\sqrt{2} + 4\sqrt{2}) = 16\sqrt{2} \approx 22{,}6274$$
      Làm tròn kết quả đến hàng phần mười, ta được <span class="final-ans">22,6</span>.
    </div>
  </div>
</div>
<div style="text-align: center; margin-top: 15px; font-weight: bold; font-size: 9.5pt; color: #4a5568;">
  ----------------------- HẾT -----------------------
</div>

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

with open("dap_an_hdg_gk1_de105.html", "w", encoding="utf-8") as f:
    f.write(template)

print("dap_an_hdg_gk1_de105.html generated successfully!")

# Run Google Chrome headless to convert HTML to PDF
output_pdf = "/Users/macbookair/Desktop/Đề prompt/Bang_Dap_An_Va_HDG_De_Thi_Thu_GK1_Toan_12.pdf"
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=4000",
    f"--print-to-pdf={output_pdf}",
    "dap_an_hdg_gk1_de105.html"
]

print("Converting to PDF using Google Chrome headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)
if os.path.exists(output_pdf):
    print("PDF generated successfully! Size:", os.path.getsize(output_pdf), "bytes")
    reader = pypdf.PdfReader(output_pdf)
    print("Exact Page count in PDF:", len(reader.pages))
    for i, p in enumerate(reader.pages):
        lines = [l.strip() for l in p.extract_text().splitlines() if l.strip()]
        first_few = ' | '.join(lines[:3]) if lines else 'EMPTY'
        print(f"Page {i+1} ({len(lines)} lines): {first_few[:100]}")
else:
    print("PDF generation failed!")
