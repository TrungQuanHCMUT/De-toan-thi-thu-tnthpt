import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 113</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 10mm 14mm 12mm 14mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 113";
    font-family: 'Times New Roman', Times, serif;
    font-size: 9pt;
    font-style: italic;
    color: #444;
  }
}

body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 10.5pt;
  line-height: 1.4;
  color: #111;
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

.header {
  text-align: center;
  border-bottom: 2px solid #2b4c7e;
  padding-bottom: 6px;
  margin-bottom: 10px;
}

.title-main {
  font-size: 13pt;
  font-weight: bold;
  text-transform: uppercase;
  color: #1a365d;
  margin: 0;
}

.title-sub {
  font-size: 11pt;
  font-weight: bold;
  color: #2b4c7e;
  margin: 2px 0;
}

.title-meta {
  font-size: 9.5pt;
  font-style: italic;
  color: #333;
}

.sec-title {
  font-size: 11pt;
  font-weight: bold;
  color: #1a365d;
  text-transform: uppercase;
  border-left: 4px solid #2b4c7e;
  padding-left: 8px;
  margin: 10px 0 6px 0;
}

.sub-title {
  font-size: 10.5pt;
  font-weight: bold;
  color: #2c5282;
  margin: 6px 0 4px 0;
}

.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
  text-align: center;
}

.ans-table th, .ans-table td {
  border: 1px solid #cbd5e0;
  padding: 4px 6px;
  font-size: 10pt;
}

.ans-table th {
  background-color: #ebf8ff;
  color: #2b4c7e;
  font-weight: bold;
}

.bold-ans {
  font-weight: bold;
  color: #c53030;
  font-size: 10.5pt;
}

.q-block {
  margin-bottom: 8px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.q-title {
  font-weight: bold;
  color: #1a365d;
}

.q-ans {
  font-weight: bold;
  color: #c53030;
  margin-left: 6px;
}

.solution-list {
  margin: 2px 0 0 0;
  padding-left: 18px;
}

.solution-list li {
  margin-bottom: 2px;
}

.step {
  margin-left: 10px;
  margin-top: 1px;
}
</style>
</head>
<body>

<div class="header">
  <div class="title-main">BẢNG ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT</div>
  <div class="title-sub">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 – ĐỀ ÔN LUYỆN TỔNG HỢP</div>
  <div class="title-meta">Môn: TOÁN – LỚP 12 | <b>Mã đề thi: 113</b> | Biên soạn: Trần Trung Quân</div>
</div>

<!-- ==================== A. BẢNG ĐÁP ÁN ==================== -->
<h2 class="sec-title">A. Bảng Đáp Án</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp án</td>
    <td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">D</td>
    <td class="bold-ans">B</td><td class="bold-ans">C</td><td class="bold-ans">B</td>
    <td class="bold-ans">D</td><td class="bold-ans">C</td><td class="bold-ans">C</td>
    <td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">A</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (4 câu – 4,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 16%;">Câu hỏi</th>
    <th style="width: 21%;">Lệnh hỏi a</th>
    <th style="width: 21%;">Lệnh hỏi b</th>
    <th style="width: 21%;">Lệnh hỏi c</th>
    <th style="width: 21%;">Lệnh hỏi d</th>
  </tr>
  <tr>
    <td><b>Câu 1</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
  <tr>
    <td><b>Câu 2</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
  </tr>
  <tr>
    <td><b>Câu 3</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
</table>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 15%;">Câu</th>
    <th style="width: 20%;">Đáp án</th>
    <th style="width: 65%;">Nội dung kết quả</th>
  </tr>
  <tr>
    <td><b>Câu 1</b></td>
    <td class="bold-ans">2</td>
    <td style="text-align: left; padding-left: 12px;">Khoảng cách đứng cách bức tường để góc nhìn tấm pano lớn nhất ($x = 2\text{ m}$)</td>
  </tr>
  <tr>
    <td><b>Câu 2</b></td>
    <td class="bold-ans">45</td>
    <td style="text-align: left; padding-left: 12px;">Số đo góc giữa hai vectơ $\overrightarrow{SD}$ và $\overrightarrow{BC}$ ($\alpha = 45^\circ$)</td>
  </tr>
  <tr>
    <td><b>Câu 3</b></td>
    <td class="bold-ans">25,6</td>
    <td style="text-align: left; padding-left: 12px;">Tổng chi phí sơn phản quang hai mặt bên vòm cầu parabol ($25,6\text{ triệu đồng}$)</td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td class="bold-ans">144</td>
    <td style="text-align: left; padding-left: 12px;">Thể tích của khối đá phong thủy có thiết diện hình vuông ($V = 144\text{ dm}^3$)</td>
  </tr>
  <tr>
    <td><b>Câu 5</b></td>
    <td class="bold-ans">9</td>
    <td style="text-align: left; padding-left: 12px;">Tổng chiều dài cáp nhánh ngắn nhất từ trạm $M \in (\alpha)$ đến hai điểm $A, B$ ($L_{\min} = 9\text{ km}$)</td>
  </tr>
  <tr>
    <td><b>Câu 6</b></td>
    <td class="bold-ans">4</td>
    <td style="text-align: left; padding-left: 12px;">Bán kính nhỏ nhất của đường tròn giao tuyến mặt cầu chứa đường thẳng ($r_{\min} = 4$)</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title" style="margin-top: 16px;">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Xét hàm số $y = \dfrac{2x - 3}{x + 1}$.<br>
  Tập xác định: $D = \mathbb{R} \setminus \{-1\}$.<br>
  Đạo hàm: $y' = \dfrac{2 \cdot 1 - (-3) \cdot 1}{(x + 1)^2} = \dfrac{5}{(x + 1)^2} > 0,\; \forall x \ne -1$.<br>
  Do đó, hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(-1; +\infty)$.<span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Xét hàm số $f(x) = x^3 - 3x^2 + 2$ trên $[-1; 2]$.<br>
  Đạo hàm: $f'(x) = 3x^2 - 6x = 3x(x - 2) = 0 \iff x = 0$ hoặc $x = 2$ (đều thuộc đoạn $[-1; 2]$).<br>
  Ta có: $f(-1) = -2$, $f(0) = 2$, $f(2) = -2$. Vậy $\min_{[-1; 2]} f(x) = -2$.<span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Với $A(1; 2; -1)$ và $B(3; 0; 5)$, ta có $\overrightarrow{AB} = (3 - 1; 0 - 2; 5 - (-1)) = (2; -2; 6)$.<span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Tích vô hướng của $\overrightarrow{u} = (2; -1; 1)$ và $\overrightarrow{v} = (1; 3; -2)$ là:
  $$\overrightarrow{u} \cdot \overrightarrow{v} = 2(1) + (-1)(3) + 1(-2) = 2 - 3 - 2 = -3.$$<span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Nguyên hàm: $\int (4x^3 + \cos x)\,\mathrm{d}x = x^4 + \sin x + C$.<span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Áp dụng tính tuyến tính:
  $$\int_{0}^{3} [2f(x) - 3g(x)]\,\mathrm{d}x = 2 \int_{0}^{3} f(x)\,\mathrm{d}x - 3 \int_{0}^{3} g(x)\,\mathrm{d}x = 2(4) - 3(-2) = 8 + 6 = 14.$$<span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 7.</span> Tích phân: $\int_{0}^{1} e^{2x}\,\mathrm{d}x = \left. \dfrac{1}{2} e^{2x} \right|_{0}^{1} = \dfrac{e^2 - 1}{2}$.<span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8.</span> Diện tích hình phẳng: $S = \int_{0}^{2} 3x^2\,\mathrm{d}x = \left. x^3 \right|_{0}^{2} = 8 - 0 = 8$.<span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9.</span> Mặt cầu $(S): (x - 1)^2 + (y + 3)^2 + (z - 2)^2 = 16$ có tâm $I(1; -3; 2)$ và bán kính $R = \sqrt{16} = 4$.<span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10.</span> Mặt phẳng $(P)$ qua $M(2; -1; 3)$ có VTPT $\overrightarrow{n} = (1; 3; -2)$:
  $$1(x - 2) + 3(y + 1) - 2(z - 3) = 0 \iff x + 3y - 2z + 7 = 0.$$<span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11.</span> Đường thẳng $d$ qua $A(1; -2; 4)$ với VTCP $\overrightarrow{u} = (2; 5; -3)$:
  $$\dfrac{x - 1}{2} = \dfrac{y + 2}{5} = \dfrac{z - 4}{-3}.$$<span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12.</span> Khoảng cách:
  $$d(M, (P)) = \dfrac{|2(1) - 2(-2) + 3 + 2|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \dfrac{11}{\sqrt{9}} = \dfrac{11}{3}.$$<span class="q-ans">Chọn A.</span>
</div>

<h3 class="sub-title" style="margin-top: 14px;">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 3}{x - 1} = x - 2 + \dfrac{1}{x - 1}$.
  <ul class="solution-list">
    <li><b>a) Đúng:</b> Ta có $y' = 1 - \dfrac{1}{(x - 1)^2} = \dfrac{x(x - 2)}{(x - 1)^2}$. Nghiệm $y' = 0 \iff x = 0$ hoặc $x = 2$. Do đó hàm số đồng biến trên các khoảng $(-\infty; 0)$ và $(2; +\infty)$.</li>
    <li><b>b) Đúng:</b> Tiệm cận đứng là $x = 1$ do $\lim_{x \to 1} y = \infty$. Tiệm cận xiên là $y = x - 2$ vì $\lim_{x \to \infty} [y - (x - 2)] = 0$.</li>
    <li><b>c) Đúng:</b> Tại hoành độ $x_0 = 0$, tung độ $y(0) = -3$ và hệ số góc $k = y'(0) = 0$. Tiếp tuyến là đường thẳng $y = -3$, song song với trục hoành $Ox$.</li>
    <li><b>d) Đúng:</b> Giao điểm hai đường tiệm cận là $I(1; -1)$. Đồ thị hàm phân thức bậc hai/bậc nhất luôn nhận giao điểm của hai tiệm cận làm tâm đối xứng.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Trong không gian $Oxyz$, cho $A(1; 0; 0)$, $B(2; 1; -1)$, $C(0; 3; 1)$, $S(1; 2; 4)$.
  <ul class="solution-list">
    <li><b>a) Sai:</b> Vì $ABCD$ là hình bình hành nên $\overrightarrow{AB} = \overrightarrow{DC} \iff D = C - B + A = (-1; 2; 2)$. Mệnh đề ghi $D(1; 2; 2)$ là sai hoành độ.</li>
    <li><b>b) Đúng:</b> Trọng tâm $G = \dfrac{S + A + B}{3} = \left(\dfrac{1+1+2}{3}; \dfrac{2+0+1}{3}; \dfrac{4+0-1}{3}\right) = \left(\dfrac{4}{3}; 1; 1\right)$.</li>
    <li><b>c) Sai:</b> Ta có $\overrightarrow{AB} = (1; 1; -1)$, $\overrightarrow{AD} = (-2; 2; 2)$, $\overrightarrow{AS} = (0; 2; 4) \implies [\overrightarrow{AB}, \overrightarrow{AD}] = (4; 0; 4)$. Thể tích khối chóp $V_{S.ABCD} = \dfrac{1}{3} |[\overrightarrow{AB}, \overrightarrow{AD}] \cdot \overrightarrow{AS}| = \dfrac{16}{3} \ne 8$.</li>
    <li><b>d) Sai:</b> $\overrightarrow{AB} = (1; 1; -1) \implies |\overrightarrow{AB}| = \sqrt{3}$; $\overrightarrow{AD} = (-2; 2; 2) \implies |\overrightarrow{AD}| = 2\sqrt{3}$. Khi đó $\cos(\overrightarrow{AB}, \overrightarrow{AD}) = \dfrac{-2}{\sqrt{3} \cdot 2\sqrt{3}} = -\dfrac{1}{3} \ne -\dfrac{\sqrt{6}}{6}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Xác định hàm vận tốc $v(t)$ trên từng giai đoạn chuyển động từ đồ thị:
  - $t \in [0; 3]$: đoạn thẳng ngang $v(t) = 11\text{ (m/s)}$.
  - $t \in [3; 8]$: parabol đỉnh $A(5; 3) \implies v(t) = a(t - 5)^2 + 3$. Do $v(3) = 11 \implies 4a + 3 = 11 \iff a = 2 \implies v(t) = 2(t - 5)^2 + 3 = 2t^2 - 20t + 53\text{ (m/s)}$. Tại $t = 8$ thì $v(8) = 21\text{ m/s}$.
  - $t \in [8; 15]$: đoạn thẳng qua $(8; 21)$ và $(15; 0) \implies v(t) = -3(t - 15) = -3t + 45\text{ (m/s)}$.
  <ul class="solution-list">
    <li><b>a) Đúng:</b> Trên đoạn $[0; 15]$, vận tốc đạt giá trị lớn nhất tại $t = 8\text{ s}$ với $v_{\max} = 21\text{ m/s}$.</li>
    <li><b>b) Đúng:</b> Gia tốc tức thời tại $t = 6\text{ s} \in (3; 8)$ là $a(t) = v'(t) = 4(t - 5) \implies a(6) = 4(6 - 5) = 4\text{ m/s}^2$.</li>
    <li><b>c) Đúng:</b> Quãng đường chất điểm đi được từ $8\text{ s}$ đến $15\text{ s}$ bằng diện tích tam giác: $S_3 = \dfrac{1}{2} \times (15 - 8) \times 21 = 73,5\text{ m}$.</li>
    <li><b>d) Đúng:</b> Tổng quãng đường: $S_1 = 11 \times 3 = 33\text{ m}$; $S_2 = \int_{3}^{8} [2(t - 5)^2 + 3]\,\mathrm{d}t = \left. \left[\dfrac{2(t - 5)^3}{3} + 3t\right] \right|_{3}^{8} = 42 - \dfrac{11}{3} = \dfrac{115}{3}\text{ m}$; $S_3 = 73,5\text{ m} = \dfrac{147}{2}\text{ m}$. Suy ra $S_{\text{tổng}} = 33 + \dfrac{115}{3} + \dfrac{147}{2} = \dfrac{869}{6}\text{ m}$. Vận tốc trung bình trong $15\text{ s}$ là $v_{tb} = \dfrac{S_{\text{tổng}}}{15} = \dfrac{\frac{869}{6}}{15} = \dfrac{869}{90}\text{ m/s} \approx 9,66\text{ m/s}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Cho mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 4z - 7 = 0$ và $(P): 2x + 2y - z + 10 = 0$.
  <ul class="solution-list">
    <li><b>a) Đúng:</b> Tâm $I(1; -2; 2)$, bán kính $R = \sqrt{1^2 + (-2)^2 + 2^2 - (-7)} = \sqrt{16} = 4$.</li>
    <li><b>b) Đúng:</b> $d(I, (P)) = \dfrac{|2(1) + 2(-2) - 2 + 10|}{\sqrt{2^2 + 2^2 + (-1)^2}} = \dfrac{6}{3} = 2$.</li>
    <li><b>c) Đúng:</b> Do $d(I, (P)) = 2 < R = 4$ nên $(P)$ cắt $(S)$ theo đường tròn có bán kính $r = \sqrt{R^2 - d^2} = \sqrt{16 - 4} = 2\sqrt{3}$. Chu vi giao tuyến bằng $C = 2\pi r = 4\sqrt{3}\pi$.</li>
    <li><b>d) Đúng:</b> Đường thẳng $\Delta \perp (P)$ có VTCP là $\overrightarrow{n}_{(P)} = (2; 2; -1)$. Điểm đi qua là $I(1; -2; 2)$ nên phương trình tham số đúng là $\begin{cases} x = 1 + 2t \\ y = -2 + 2t \\ z = 2 - t \end{cases}$ ($t \in \mathbb{R}$).</li>
  </ul>
</div>

<h3 class="sub-title" style="margin-top: 14px;">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Gọi $x$ ($x > 0$) là khoảng cách từ người đến bức tường. Tầm mắt ở độ cao $h_E = 1,6\text{ m}$, mép dưới $h_A = 2,6\text{ m}$, mép trên $h_B = 5,6\text{ m}$.<br>
  Khoảng cách thẳng đứng: $a = 2,6 - 1,6 = 1,0\text{ m}$ và $b = 5,6 - 1,6 = 4,0\text{ m}$.<br>
  Góc trông $\alpha = \theta_2 - \theta_1 \implies \tan\alpha = \dfrac{\frac{4}{x} - \frac{1}{x}}{1 + \frac{4}{x^2}} = \dfrac{3}{x + \frac{4}{x}}$.<br>
  Theo AM – GM: $x + \dfrac{4}{x} \ge 2\sqrt{4} = 4 \implies \tan\alpha \le \dfrac{3}{4}$.<br>
  Góc trông lớn nhất khi $x = \dfrac{4}{x} \iff x = 2\text{ m}$.<span class="q-ans">Đáp án: 2</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$ và $B$ ($AD = a, BC = 2a, AB = a$), $\Delta SAB$ đều cạnh $a$ và nằm trong mặt phẳng vuông góc với $(ABCD)$. Gọi $H$ là trung điểm của $AB \implies SH \perp (ABCD)$ và $SH = \dfrac{a\sqrt{3}}{2}$.<br>
  <b>Cách 1 (Gắn hệ trục tọa độ):</b> Chuẩn hóa $a = 2 \implies AB = 2, AD = 2, BC = 4, SH = \sqrt{3}$.<br>
  Chọn gốc tọa độ $A(0; 0; 0)$, trục $Ox$ dọc theo tia $AD$, trục $Oy$ dọc theo tia $AB$, trục $Oz \parallel HS$:<br>
  $D(2; 0; 0)$, $B(0; 2; 0)$, $C(4; 2; 0)$, $H(0; 1; 0)$, $S(0; 1; \sqrt{3})$.<br>
  Vectơ $\overrightarrow{SD} = (2;\; -1;\; -\sqrt{3}) \implies |\overrightarrow{SD}| = \sqrt{4 + 1 + 3} = 2\sqrt{2}$.<br>
  Vectơ $\overrightarrow{BC} = (4;\; 0;\; 0) \implies |\overrightarrow{BC}| = 4$.<br>
  Tích vô hướng: $\overrightarrow{SD} \cdot \overrightarrow{BC} = 2(4) + (-1)(0) + (-\sqrt{3})(0) = 8$.<br>
  Côsin của góc giữa hai vectơ:
  $$\cos(\overrightarrow{SD}, \overrightarrow{BC}) = \dfrac{\overrightarrow{SD} \cdot \overrightarrow{BC}}{|\overrightarrow{SD}| \cdot |\overrightarrow{BC}|} = \dfrac{8}{2\sqrt{2} \cdot 4} = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2} \implies (\overrightarrow{SD}, \overrightarrow{BC}) = 45^\circ.$$<br>
  <b>Cách 2 (Phương pháp vectơ thuần túy):</b> $\overrightarrow{SD} \cdot \overrightarrow{BC} = (\overrightarrow{SH} + \overrightarrow{HA} + \overrightarrow{AD}) \cdot 2\overrightarrow{AD} = 2AD^2 = 2a^2$.<br>
  Vì $AD \perp (SAB) \implies AD \perp SA \implies SD = \sqrt{a^2 + a^2} = a\sqrt{2}$. Khi đó $\cos(\overrightarrow{SD}, \overrightarrow{BC}) = \dfrac{2a^2}{(a\sqrt{2})(2a)} = \dfrac{\sqrt{2}}{2} \implies 45^\circ$.<span class="q-ans">Đáp án: 45</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Thiết lập hệ trục $Oxy$ với trục hoành trên mặt nước, gốc $O$ là trung điểm đoạn nối hai chân vòm cầu:<br>
  Hai chân cầu là $(-12; 0)$ và $(12; 0)$, đỉnh parabol là $I(0; 18) \implies y = ax^2 + 18$. Vì đi qua $(12; 0) \implies 144a + 18 = 0 \iff a = -\dfrac{1}{8}$.<br>
  Phương trình vòm cầu: $y = -\dfrac{1}{8}x^2 + 18$. Mặt sàn cầu cách mặt nước $10\text{ m} \implies y = 10$.<br>
  Giao điểm: $-\dfrac{1}{8}x^2 + 18 = 10 \iff x = \pm 8$.<br>
  Diện tích một mặt bên:
  $$S = \int_{-8}^{8} \left(8 - \dfrac{1}{8}x^2\right)\,\mathrm{d}x = 2 \left. \left(8x - \dfrac{x^3}{24}\right) \right|_{0}^{8} = 2 \left(64 - \dfrac{64}{3}\right) = \dfrac{256}{3}\text{ m}^2.$$<br>
  Tổng diện tích 2 mặt bên: $S_{\text{tổng}} = 2S = \dfrac{512}{3}\text{ m}^2$.<br>
  Tổng chi phí: $\dfrac{512}{3} \times 150.000 = 25.600.000\text{ đồng} = 25,6\text{ triệu đồng}$.<span class="q-ans">Đáp án: 25,6</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Đặt hệ trục $Oxy$ với gốc $O$ tại tâm đường tròn đáy, trục $Ox$ vuông góc với mặt phẳng cắt.<br>
  Đường tròn đáy bán kính $R = 3\text{ dm}$ có phương trình $x^2 + y^2 = 9$.<br>
  Với mỗi $x \in [-3; 3]$, độ dài cạnh thiết diện hình vuông là $a(x) = 2\sqrt{9 - x^2}$.<br>
  Diện tích thiết diện: $S(x) = [a(x)]^2 = 4(9 - x^2)$.<br>
  Thể tích khối đá:
  $$V = \int_{-3}^{3} S(x)\,\mathrm{d}x = \int_{-3}^{3} 4(9 - x^2)\,\mathrm{d}x = 4 \left. \left(9x - \dfrac{x^3}{3}\right) \right|_{-3}^{3} = 4(18 - (-18)) = 144\text{ dm}^3.$$<span class="q-ans">Đáp án: 144</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Hai điểm $A(5; 2; 5)$ và $B(5; 8; 8)$ cùng phía đối với mặt phẳng $(\alpha): 2x - y + 2z - 9 = 0$ (cùng cho giá trị dương $9 > 0$).<br>
  Hình chiếu vuông góc của $A$ lên $(\alpha)$ là $H(3; 3; 3)$. Điểm đối xứng của $A$ qua $(\alpha)$ là $A'(1; 4; 1)$.<br>
  Với mọi $M \in (\alpha)$, $MA + MB = MA' + MB \ge A'B$.<br>
  Tổng chiều dài cáp nhánh ngắn nhất:
  $$A'B = \sqrt{(5 - 1)^2 + (8 - 4)^2 + (8 - 1)^2} = \sqrt{16 + 16 + 49} = \sqrt{81} = 9\text{ km}.$$<span class="q-ans">Đáp án: 9</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Mặt cầu $(S)$ có tâm $I(3; -2; 0)$, bán kính $R = 5$.<br>
  Đường thẳng $d$ qua $H(1; 0; -1)$, có VTCP $\overrightarrow{u} = (1; 2; 2)$.<br>
  Ta có $\overrightarrow{HI} = (2; -2; 1) \implies \overrightarrow{HI} \cdot \overrightarrow{u} = 2 - 4 + 2 = 0 \implies HI \perp d$.<br>
  Do đó khoảng cách từ tâm $I$ đến đường thẳng $d$ là $d(I, d) = IH = \sqrt{4 + 4 + 1} = 3 < R = 5$.<br>
  Với mọi mặt phẳng $(P)$ chứa $d$, khoảng cách $h = d(I, (P)) \le d(I, d) = 3$.<br>
  Bán kính đường tròn giao tuyến: $r = \sqrt{R^2 - h^2} = \sqrt{25 - h^2} \ge \sqrt{25 - 3^2} = 4$.<br>
  Bán kính nhỏ nhất của đường tròn giao tuyến $(C)$ bằng $4$.<span class="q-ans">Đáp án: 4</span>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "$", right: "$", display: false}
    ],
    throwOnError: false
  });
});
</script>
</body>
</html>
"""

html_filename = 'dap_an_113.html'
pdf_name = "Bang_Dap_An_Va_HDG_De_113.pdf"

with open(html_filename, 'w', encoding='utf-8') as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    html_filename
]

print("Running Chrome to generate Dap An 113 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages for Dap An 113: {len(reader.pages)}")
