import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 109</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 12mm 15mm 15mm 15mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 109";
    font-family: 'Times New Roman', Times, serif;
    font-size: 9pt;
    font-style: italic;
    color: #444;
  }
}

body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #111;
  margin: 0;
  padding: 0;
}

/* Tinh chỉnh dấu mũi tên chỉ vectơ to, rõ và đẹp */
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
  padding-bottom: 8px;
  margin-bottom: 14px;
}
.header h2 {
  margin: 0 0 4px 0;
  font-size: 14pt;
  text-transform: uppercase;
  color: #1a365d;
}
.header h3 {
  margin: 0 0 4px 0;
  font-size: 12pt;
  font-weight: normal;
  color: #2b4c7e;
}
.header p {
  margin: 0;
  font-size: 10.5pt;
  font-style: italic;
  color: #555;
}

h2.sec-title {
  font-size: 12pt;
  color: #1a365d;
  background-color: #f0f4f8;
  padding: 5px 10px;
  border-left: 4px solid #2b4c7e;
  margin-top: 14px;
  margin-bottom: 8px;
  text-transform: uppercase;
}

h3.sub-title {
  font-size: 11pt;
  color: #2b4c7e;
  margin-top: 10px;
  margin-bottom: 6px;
}

table.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 12px;
  text-align: center;
}
table.ans-table th, table.ans-table td {
  border: 1px solid #777;
  padding: 5px 4px;
  font-size: 10.5pt;
}
table.ans-table th {
  background-color: #e9eef4;
  color: #1a365d;
}

.bold-ans {
  font-weight: bold;
  color: #c53030;
}

.q-block {
  margin-bottom: 11px;
  page-break-inside: avoid;
  break-inside: avoid;
  text-align: justify;
}
.q-title {
  font-weight: bold;
  color: #1a365d;
}
.q-ans {
  font-weight: bold;
  color: #c53030;
  margin-left: 4px;
}
.step {
  margin-top: 3px;
  margin-bottom: 3px;
}
ul.solution-list {
  margin: 4px 0 6px 18px;
  padding: 0;
}
ul.solution-list li {
  margin-bottom: 3px;
}
</style>
</head>
<body>

<div class="header">
  <h2>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết</h2>
  <h3>KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 – ĐỀ ÔN LUYỆN TỔNG HỢP</h3>
  <p>Môn: TOÁN – Lớp 12 &nbsp;|&nbsp; Mã đề: 109 &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</p>
</div>

<!-- ==================== A. BẢNG ĐÁP ÁN ==================== -->
<h2 class="sec-title">A. Bảng Đáp Án Toàn Bộ Đề Thi (Mã đề: 109)</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp án</td>
    <td class="bold-ans">B</td><td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">C</td><td class="bold-ans">B</td><td class="bold-ans">D</td>
    <td class="bold-ans">A</td><td class="bold-ans">C</td><td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">C</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (4 câu – 4,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 32%;">Câu hỏi</th>
    <th style="width: 17%;">Lệnh hỏi a)</th>
    <th style="width: 17%;">Lệnh hỏi b)</th>
    <th style="width: 17%;">Lệnh hỏi c)</th>
    <th style="width: 17%;">Lệnh hỏi d)</th>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 1 (Khảo sát hàm phân thức $y = \frac{x^2-3x+3}{x-1}$)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 2 (Tích phân từng phần và đổi biến)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 3 (Ứng dụng tích phân: tốc độ bơm nước)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 4 (Vectơ & toạ độ Oxyz: tích có hướng, tứ diện)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp số</td>
    <td class="bold-ans">1800</td>
    <td class="bold-ans">216</td>
    <td class="bold-ans">120</td>
    <td class="bold-ans">300</td>
    <td class="bold-ans">66</td>
    <td class="bold-ans">6</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Xét hàm số phân thức $y = \dfrac{2x - 1}{x + 1}$.
  <div class="step">Đường tiệm cận đứng là $x = -1$ (do mẫu bằng $0$ tại $x = -1$ và tử bằng $-3 \ne 0$).</div>
  <div class="step">Đường tiệm cận ngang là $y = \lim_{x \to \pm\infty} \dfrac{2x - 1}{x + 1} = 2$.</div>
  <div class="step">Vậy giao điểm của hai đường tiệm cận là $I(-1; 2)$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Xét đạo hàm $f'(x) = (x + 1)^2(x - 2)(x - 5)$.
  <div class="step">Phương trình $f'(x) = 0$ có các nghiệm: $x = -1$ (bội chẵn), $x = 2$ (bội lẻ) và $x = 5$ (bội lẻ).</div>
  <div class="step">Đạo hàm chỉ đổi dấu khi $x$ đi qua các nghiệm bội lẻ là $x = 2$ và $x = 5$. Do đó hàm số có 2 điểm cực trị.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Trên khoảng $\left(-\dfrac{1}{2}; +\infty\right)$, ta có $2x + 1 > 0$.
  <div class="step">Áp dụng công thức nguyên hàm cơ bản: $\int \dfrac{1}{2x + 1}\,\mathrm{d}x = \dfrac{1}{2}\ln(2x + 1) + C$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Áp dụng định nghĩa tích phân:
  <div class="step">$I = \int_{0}^{\frac{\pi}{2}} \sin x\,\mathrm{d}x = [-\cos x]_0^{\frac{\pi}{2}} = -\cos\left(\dfrac{\pi}{2}\right) - (-\cos 0) = 0 - (-1) = 1$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Theo tính chất chèn cận: $\int_{1}^{3} f(x)\,\mathrm{d}x = \int_{1}^{2} f(x)\,\mathrm{d}x + \int_{2}^{3} f(x)\,\mathrm{d}x$.
  <div class="step">Suy ra: $\int_{1}^{2} f(x)\,\mathrm{d}x = \int_{1}^{3} f(x)\,\mathrm{d}x - \int_{2}^{3} f(x)\,\mathrm{d}x = 5 - 2 = 3$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Hoành độ giao điểm của parabol $y = x^2$ và đường thẳng $y = 2x$ là nghiệm của: $x^2 = 2x \Leftrightarrow x = 0$ hoặc $x = 2$.
  <div class="step">Trên đoạn $[0; 2]$, ta có $2x \ge x^2$. Diện tích hình phẳng là:</div>
  <div class="step">$S = \int_{0}^{2} (2x - x^2)\,\mathrm{d}x = \left[x^2 - \dfrac{x^3}{3}\right]_0^2 = 4 - \dfrac{8}{3} = \dfrac{4}{3}$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 7:</span> Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y = \sqrt{2x + 1}$, $y = 0$, $x = 0, x = 4$ quanh trục hoành:
  <div class="step">$V = \pi \int_{0}^{4} (\sqrt{2x + 1})^2\,\mathrm{d}x = \pi \int_{0}^{4} (2x + 1)\,\mathrm{d}x = \pi \left[x^2 + x\right]_0^4 = \pi (16 + 4) = 20\pi$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8:</span> Với $A(2; -3; 5)$ và $B(4; 1; -1)$, toạ độ trung điểm $M$ của đoạn thẳng $AB$ là:
  <div class="step">$x_M = \dfrac{2 + 4}{2} = 3;\quad y_M = \dfrac{-3 + 1}{2} = -1;\quad z_M = \dfrac{5 - 1}{2} = 2 \implies M(3; -1; 2)$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9:</span> Ta có $2\overrightarrow{a} = 2(1; 2; -2) = (2; 4; -4)$ và $\overrightarrow{b} = (-1; 0; 3)$.
  <div class="step">Toạ độ $\overrightarrow{u} = 2\overrightarrow{a} - \overrightarrow{b} = (2 - (-1); 4 - 0; -4 - 3) = (3; 4; -7)$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10:</span> Ta có $\overrightarrow{u} \cdot \overrightarrow{v} = 1(0) + 0(1) + 1(-1) = -1$.
  <div class="step">Độ dài: $|\overrightarrow{u}| = \sqrt{1^2+0^2+1^2} = \sqrt{2}$, $|\overrightarrow{v}| = \sqrt{0^2+1^2+(-1)^2} = \sqrt{2}$.</div>
  <div class="step">Suy ra: $\cos(\overrightarrow{u}, \overrightarrow{v}) = \dfrac{-1}{\sqrt{2} \cdot \sqrt{2}} = -\dfrac{1}{2}$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11:</span> Tứ giác $ABCD$ là hình bình hành khi $\overrightarrow{AD} = \overrightarrow{BC}$.
  <div class="step">Với $D(x; y; z)$, ta có $\overrightarrow{AD} = (x - 1; y - 1; z - 2)$ và $\overrightarrow{BC} = (3 - 2; 2 - (-1); -1 - 1) = (1; 3; -2)$.</div>
  <div class="step">Suy ra: $x - 1 = 1 \implies x = 2;\; y - 1 = 3 \implies y = 4;\; z - 2 = -2 \implies z = 0 \implies D(2; 4; 0)$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12:</span> Hợp lực của hai lực vuông góc $\overrightarrow{F}_{12} = \overrightarrow{F}_1 + \overrightarrow{F}_2$ có độ lớn:
  <div class="step">$|\overrightarrow{F}_{12}| = \sqrt{30^2 + 40^2} = 50\text{ N}$.</div>
  <div class="step">Vì $\overrightarrow{F}_3 \perp \overrightarrow{F}_{12}$ nên hợp lực $|\overrightarrow{F}| = \sqrt{|\overrightarrow{F}_{12}|^2 + |\overrightarrow{F}_3|^2} = \sqrt{50^2 + 50^2} = 50\sqrt{2}\text{ N}$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 3}{x - 1} = x - 2 + \dfrac{1}{x - 1}$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> $\lim_{x \to \pm\infty} [f(x) - (x - 2)] = \lim_{x \to \pm\infty} \dfrac{1}{x - 1} = 0$, nên đường tiệm cận xiên là $y = x - 2$.</li>
    <li><b>b) ĐÚNG:</b> Đạo hàm $f'(x) = 1 - \dfrac{1}{(x - 1)^2} = \dfrac{x^2 - 2x}{(x - 1)^2}$. Cho $f'(x) = 0 \Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu cho thấy $f'(x) > 0$ trên $(-\infty; 0)$ và $(2; +\infty)$ nên hàm số đồng biến trên các khoảng này.</li>
    <li><b>c) SAI:</b> $x = 0$ là điểm cực đại với giá trị cực đại $y(0) = -3$; còn điểm $M(2; 1)$ là điểm cực tiểu của đồ thị hàm số.</li>
    <li><b>d) SAI:</b> Tiệm cận đứng $x = 1$, tiệm cận xiên $y = x - 2$. Giao điểm là $I(1; -1)$, không phải $I(1; 1)$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Xét tích phân $I = \int_{0}^{1} (2x + 1)e^x\,\mathrm{d}x$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Đặt $u = 2x + 1 \implies \mathrm{d}u = 2\,\mathrm{d}x$; $\mathrm{d}v = e^x\,\mathrm{d}x \implies v = e^x$.</li>
    <li><b>b) ĐÚNG:</b> $I = [(2x + 1)e^x]_0^1 - \int_{0}^{1} 2e^x\,\mathrm{d}x = (3e - 1) - 2(e - 1) = e + 1$.</li>
    <li><b>c) ĐÚNG:</b> Với $J = \int_{1}^{e} \dfrac{\ln x}{x}\,\mathrm{d}x$, đặt $t = \ln x \implies \mathrm{d}t = \dfrac{1}{x}\mathrm{d}x$. Khi $x=1 \implies t=0$, khi $x=e \implies t=1$. Ta được $J = \int_{0}^{1} t\,\mathrm{d}t = \dfrac{1}{2}$.</li>
    <li><b>d) SAI:</b> Vì $e \approx 2,718 \implies I = e + 1 \approx 3,718 > 3$. Mệnh đề cho $I < 3$ là sai.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Một bồn nước ban đầu có $200$ lít nước, tốc độ bơm là $v(t) = 30 + 6t$ (lít/phút).
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Lượng nước bơm vào bồn từ $t = 0$ đến $t = t_0$ là tích phân của tốc độ bơm: $\int_{0}^{t_0} v(t)\,\mathrm{d}t$.</li>
    <li><b>b) ĐÚNG:</b> Tại $t = 5$, tốc độ bơm là $v(5) = 30 + 6(5) = 60$ lít/phút.</li>
    <li><b>c) SAI:</b> Lượng nước bơm vào sau $10$ phút là: $\int_{0}^{10} (30 + 6t)\,\mathrm{d}t = [30t + 3t^2]_0^{10} = 300 + 300 = 600$ lít (không phải $500$ lít).</li>
    <li><b>d) ĐÚNG:</b> Tổng lượng nước trong bồn sau $10$ phút là: $200 + 600 = 800$ lít.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Cho $A(1; 2; -1)$, $B(2; 3; 1)$, $C(0; 1; 2)$ và $D(2; 1; 3)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> $\overrightarrow{AB} = (1; 1; 2)$, $\overrightarrow{AC} = (-1; -1; 3)$. Tích có hướng $[\overrightarrow{AB}, \overrightarrow{AC}] = (5; -5; 0) = 5(1; -1; 0)$, cùng phương với $\overrightarrow{n} = (1; -1; 0)$.</li>
    <li><b>b) SAI:</b> $\overrightarrow{AB} \cdot \overrightarrow{AC} = 1(-1) + 1(-1) + 2(3) = 4 \ne 0$, nên tam giác $ABC$ không vuông tại $A$.</li>
    <li><b>c) ĐÚNG:</b> Diện tích tam giác $ABC$: $S_{\triangle ABC} = \dfrac{1}{2} |[\overrightarrow{AB}, \overrightarrow{AC}]| = \dfrac{1}{2} \sqrt{5^2 + (-5)^2 + 0} = \dfrac{5\sqrt{2}}{2}$.</li>
    <li><b>d) ĐÚNG:</b> $\overrightarrow{AD} = (1; -1; 4)$. Thể tích tứ diện $V = \dfrac{1}{6} |[\overrightarrow{AB}, \overrightarrow{AC}] \cdot \overrightarrow{AD}| = \dfrac{1}{6} |5(1) + (-5)(-1) + 0| = \dfrac{10}{6} = \dfrac{5}{3}$.</li>
  </ul>
</div>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Chiều dài hàng rào bao bọc ba cạnh khu đất: $x + 2y = 120 \implies x = 120 - 2y$.
  <div class="step">Diện tích khu đất: $S = x \cdot y = (120 - 2y)y = -2y^2 + 120y = -2(y - 30)^2 + 1800 \le 1800\text{ m}^2$.</div>
  <div class="step">Giá trị lớn nhất đạt được khi $y = 30\text{ m}$ và $x = 60\text{ m}$.</div>
  <span class="q-ans">&rArr; Đáp số: 1800</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Tại vị trí có khoảng cách $x \in [0; 12]$, thiết diện là hình vuông cạnh $\sqrt{36 - 3x}$ nên diện tích thiết diện là:
  <div class="step">$S(x) = (\sqrt{36 - 3x})^2 = 36 - 3x$.</div>
  <div class="step">Thể tích vật thể: $V = \int_{0}^{12} (36 - 3x)\,\mathrm{d}x = \left[36x - \dfrac{3x^2}{2}\right]_0^{12} = 36(12) - \dfrac{3(144)}{2} = 432 - 216 = 216\text{ cm}^3$.</div>
  <span class="q-ans">&rArr; Đáp số: 216</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Thể tích lòng trong của bình hoa:
  <div class="step">$V = \pi \int_{0}^{12} (\sqrt{x + 4})^2\,\mathrm{d}x = \pi \int_{0}^{12} (x + 4)\,\mathrm{d}x = \pi \left[\dfrac{x^2}{2} + 4x\right]_0^{12} = \pi (72 + 48) = 120\pi\text{ cm}^3$.</div>
  <div class="step">Do $V = k\pi \implies k = 120$.</div>
  <span class="q-ans">&rArr; Đáp số: 120</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Vận tốc tại thời điểm $t$ giây:
  <div class="step">$v(t) = v_0 + \int_{0}^{t} a(u)\,\mathrm{d}u = 10 + \int_{0}^{t} (2 + 0,6u)\,\mathrm{d}u = 10 + 2t + 0,3t^2\text{ (m/s)}$.</div>
  <div class="step">Quãng đường ô tô đi được trong $10$ giây đầu tiên:</div>
  <div class="step">$S = \int_{0}^{10} (10 + 2t + 0,3t^2)\,\mathrm{d}t = \left[10t + t^2 + 0,1t^3\right]_0^{10} = 100 + 100 + 100 = 300\text{ m}$.</div>
  <span class="q-ans">&rArr; Đáp số: 300</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Trọng tâm tam giác $ABC$ là $G(3; 3; 4)$.
  <div class="step">Ta có: $T = MA^2 + MB^2 + MC^2 = 3MG^2 + GA^2 + GB^2 + GC^2$.</div>
  <div class="step">Khoảng cách: $GA^2 = (-2)^2 + (-1)^2 + 0^2 = 5$; $GB^2 = 0^2 + 1^2 + (-2)^2 = 5$; $GC^2 = 2^2 + 0^2 + 2^2 = 8$.</div>
  <div class="step">Suy ra $GA^2 + GB^2 + GC^2 = 18$. Biểu thức $T$ nhỏ nhất khi $MG$ nhỏ nhất.</div>
  <div class="step">Với $M \in (Oxy)$, $M$ là hình chiếu của $G$ lên $(Oxy) \implies M(3; 3; 0) \implies MG = 4 \implies MG^2 = 16$.</div>
  <div class="step">Vậy $T_{\min} = 3(16) + 18 = 48 + 18 = 66$.</div>
  <span class="q-ans">&rArr; Đáp số: 66</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Điểm $A(1; 2; 3)$ có $z_A = 3 > 0$, điểm $B(5; 4; -1)$ có $z_B = -1 < 0$.
  <div class="step">Hai điểm $A$ và $B$ nằm về hai phía khác nhau đối với mặt phẳng $(Oxy)$.</div>
  <div class="step">Với mọi điểm $M \in (Oxy)$, ta có $MA + MB \ge AB$.</div>
  <div class="step">Dấu "=" xảy ra khi $M = AB \cap (Oxy)$.</div>
  <div class="step">Do đó $(MA + MB)_{\min} = AB = \sqrt{(5 - 1)^2 + (4 - 2)^2 + (-1 - 3)^2} = \sqrt{16 + 4 + 16} = \sqrt{36} = 6$.</div>
  <span class="q-ans">&rArr; Đáp số: 6</span>
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

with open("dap_an_109.html", "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "Bang_Dap_An_Va_HDG_De_109.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "dap_an_109.html"
]

print("Running Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
