import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 108</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 12mm 15mm 15mm 15mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 108";
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
  <p>Môn: TOÁN – Lớp 12 &nbsp;|&nbsp; Mã đề: 108 &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</p>
</div>

<!-- ==================== A. BẢNG ĐÁP ÁN ==================== -->
<h2 class="sec-title">A. Bảng Đáp Án Toàn Bộ Đề Thi (Mã đề: 108)</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp án</td>
    <td class="bold-ans">C</td><td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">C</td><td class="bold-ans">D</td><td class="bold-ans">B</td>
    <td class="bold-ans">C</td><td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">A</td><td class="bold-ans">B</td>
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
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 1 (Hàm số $y = \sqrt{e^{2x}-2e^x+2}$)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 2 (Tính chất tích phân, thể tích & nguyên hàm)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 3 (Chuyển động thẳng: gia tốc, vận tốc)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 8px;">Câu 4 (Vectơ & toạ độ không gian Oxyz)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
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
    <td class="bold-ans">12</td>
    <td class="bold-ans">1575</td>
    <td class="bold-ans">240</td>
    <td class="bold-ans">180</td>
    <td class="bold-ans">14</td>
    <td class="bold-ans">3</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Quan sát bảng biến thiên, ta thấy đạo hàm $f'(x) > 0$ trên hai khoảng $(-\infty; -2)$ và $(1; +\infty)$. Do đó, hàm số đã cho đồng biến trên $(-\infty; -2)$ và $(1; +\infty)$. Đối chiếu với các phương án đã cho, khoảng $(-\infty; -2)$ thoả mãn.
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Xét hàm số $f(x) = x^3 - 3x^2 + 2$ trên đoạn $[0; 3]$.
  <div class="step">Ta có đạo hàm $f'(x) = 3x^2 - 6x = 3x(x - 2)$.</div>
  <div class="step">Cho $f'(x) = 0 \Leftrightarrow x = 0 \in [0; 3]$ hoặc $x = 2 \in [0; 3]$.</div>
  <div class="step">Tính các giá trị: $f(0) = 2$, $f(2) = 2^3 - 3(2^2) + 2 = -2$, $f(3) = 3^3 - 3(3^2) + 2 = 2$.</div>
  <div class="step">Vậy giá trị nhỏ nhất của hàm số trên đoạn $[0; 3]$ là $\min_{[0; 3]} f(x) = -2$ tại $x = 2$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Áp dụng tính chất của tích phân: $\int_{1}^{2} [2 + f(x)]\,\mathrm{d}x = \int_{1}^{2} 2\,\mathrm{d}x + \int_{1}^{2} f(x)\,\mathrm{d}x = 2(2 - 1) + [F(2) - F(1)]$.
  <div class="step">Vì $F(x) = x^3$ nên $F(2) = 2^3 = 8$ và $F(1) = 1^3 = 1$.</div>
  <div class="step">Do đó: $\int_{1}^{2} [2 + f(x)]\,\mathrm{d}x = 2 + (8 - 1) = 2 + 7 = 9$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Áp dụng bảng công thức nguyên hàm cơ bản:
  <div class="step">$\int (e^{2x} + \cos x)\,\mathrm{d}x = \int e^{2x}\,\mathrm{d}x + \int \cos x\,\mathrm{d}x = \dfrac{1}{2}e^{2x} + \sin x + C$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Theo tính chất tuyến tính của tích phân:
  <div class="step">$\int_{0}^{2} [2f(x) - 3g(x)]\,\mathrm{d}x = 2\int_{0}^{2} f(x)\,\mathrm{d}x - 3\int_{0}^{2} g(x)\,\mathrm{d}x = 2(3) - 3(-1) = 6 + 3 = 9$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y = e^x$, $y = 0$, $x = 0, x = 1$ quanh trục hoành:
  <div class="step">$V = \pi \int_{0}^{1} (e^x)^2\,\mathrm{d}x = \pi \int_{0}^{1} e^{2x}\,\mathrm{d}x = \pi \left[\dfrac{e^{2x}}{2}\right]_0^1 = \dfrac{\pi(e^2 - 1)}{2}$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 7:</span> Phương trình hoành độ giao điểm: $x^2 - 2x = 0 \Leftrightarrow x = 0$ hoặc $x = 2$.
  <div class="step">Trên đoạn $[0; 2]$, ta có $x^2 - 2x \le 0$. Diện tích hình phẳng là:</div>
  <div class="step">$S = \int_{0}^{2} |x^2 - 2x|\,\mathrm{d}x = \int_{0}^{2} (2x - x^2)\,\mathrm{d}x = \left[x^2 - \dfrac{x^3}{3}\right]_0^2 = 4 - \dfrac{8}{3} = \dfrac{4}{3}$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8:</span> Với hai điểm $A(1; 2; -1)$ và $B(3; 0; 2)$, tọa độ vectơ $\overrightarrow{AB}$ là:
  <div class="step">$\overrightarrow{AB} = (3 - 1; 0 - 2; 2 - (-1)) = (2; -2; 3)$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9:</span> Tọa độ trọng tâm $G$ của tam giác $ABC$:
  <div class="step">$x_G = \dfrac{2+4+0}{3} = 2,\quad y_G = \dfrac{-1+0+4}{3} = 1,\quad z_G = \dfrac{3+1-1}{3} = 1 \implies G(2; 1; 1)$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10:</span> Tích vô hướng $\overrightarrow{u} \cdot \overrightarrow{v} = 1(2) + 0(-1) + (-2)(1) = 2 - 2 = 0$. Hai vectơ vuông góc nhau.
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11:</span> Theo quy tắc hình hộp: $\overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AA'} = \overrightarrow{AC'}$.
  <div class="step">Độ dài đường chéo hình lập phương cạnh $a$ là $AC' = \sqrt{a^2 + a^2 + a^2} = a\sqrt{3}$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12:</span> Trạng thái cân bằng: $\overrightarrow{F}_1 + \overrightarrow{F}_2 + \overrightarrow{F}_3 + \overrightarrow{P} = \overrightarrow{0} \implies \overrightarrow{F}_1 + \overrightarrow{F}_2 + \overrightarrow{F}_3 = -\overrightarrow{P}$.
  <div class="step">Độ lớn: $|\overrightarrow{F}_1 + \overrightarrow{F}_2 + \overrightarrow{F}_3| = |-\overrightarrow{P}| = mg = 6 \times 9,8 = 58,8\text{ N}$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Cho hàm số $y = f(x) = \sqrt{e^{2x} - 2e^x + 2}$ có đồ thị là $(C)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Biểu thức dưới dấu căn $e^{2x} - 2e^x + 2 = (e^x - 1)^2 + 1 \ge 1 > 0, \forall x \in \mathbb{R}$. Tập xác định $D = \mathbb{R}$.</li>
    <li><b>b) SAI:</b> Ta có: $f'(x) = \dfrac{(e^{2x} - 2e^x + 2)'}{2\sqrt{e^{2x} - 2e^x + 2}} = \dfrac{2e^{2x} - 2e^x}{2\sqrt{e^{2x} - 2e^x + 2}} = \dfrac{e^x(e^x - 1)}{\sqrt{e^{2x} - 2e^x + 2}}$. Mệnh đề thiếu thừa số $e^x$ ở tử số nên sai.</li>
    <li><b>c) SAI:</b> $f'(x) = 0 \Leftrightarrow e^x - 1 = 0 \Leftrightarrow x = 0$. Qua $x = 0$, $f'(x)$ đổi dấu từ âm sang dương nên $x = 0$ là điểm cực tiểu của hàm số với giá trị cực tiểu $f(0) = 1$. Hàm số không có cực đại.</li>
    <li><b>d) ĐÚNG:</b> Khi $x \to -\infty$, $\lim_{x \to -\infty} e^x = 0 \implies \lim_{x \to -\infty} f(x) = \sqrt{0 - 0 + 2} = \sqrt{2}$. Đường thẳng $y = \sqrt{2}$ là đường tiệm cận ngang của đồ thị $(C)$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Cho $f(x) \ge 0$, $f(2) = 4$ và $\int_{0}^{2} f(x)\,\mathrm{d}x = 3$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> $\int_{0}^{2} [3f(x) - 2x]\,\mathrm{d}x = 3(3) - [x^2]_0^2 = 9 - 4 = 5$.</li>
    <li><b>b) SAI:</b> Đặt $t = 2x \implies \mathrm{d}x = \dfrac{1}{2}\mathrm{d}t$. Tích phân $\int_{0}^{1} f(2x)\,\mathrm{d}x = \dfrac{1}{2}\int_{0}^{2} f(t)\,\mathrm{d}t = \dfrac{3}{2} \ne 3$.</li>
    <li><b>c) ĐÚNG:</b> Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y = \sqrt{f(x)}$, $y = 0$, $x = 0, x = 2$ quanh trục $Ox$ là $V = \pi \int_{0}^{2} (\sqrt{f(x)})^2\,\mathrm{d}x = \pi \int_{0}^{2} f(x)\,\mathrm{d}x = 3\pi$.</li>
    <li><b>d) ĐÚNG:</b> $F(2) - F(0) = \int_{0}^{2} f(x)\,\mathrm{d}x = 3 \implies F(2) = 1 + 3 = 4$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Chuyển động thẳng với gia tốc $a(t) = 3t^2 + 2t$, vận tốc đầu $v(0) = 5\text{ m/s}$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> $v(t) = \int a(t)\,\mathrm{d}t = t^3 + t^2 + C$. Do $v(0) = 5 \implies C = 5$. Vậy $v(t) = t^3 + t^2 + 5$.</li>
    <li><b>b) SAI:</b> Tại $t = 2$, ta có $v(2) = 2^3 + 2^2 + 5 = 17\text{ m/s} \ne 15\text{ m/s}$.</li>
    <li><b>c) ĐÚNG:</b> Quãng đường $s = \int_{0}^{3} (t^3 + t^2 + 5)\,\mathrm{d}t = \left[\dfrac{t^4}{4} + \dfrac{t^3}{3} + 5t\right]_0^3 = 20,25 + 9 + 15 = 44,25\text{ m}$.</li>
    <li><b>d) SAI:</b> Vận tốc trung bình $v_{tb} = \dfrac{44,25}{3} = 14,75\text{ m/s} \ne 15\text{ m/s}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Cho $A(1; 0; 2)$, $B(-1; 1; 3)$, $C(3; 2; 1)$, $D(3; -2; 3)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> $\overrightarrow{AB} = (-2; 1; 1)$ và $AB = \sqrt{(-2)^2 + 1^2 + 1^2} = \sqrt{6}$.</li>
    <li><b>b) ĐÚNG:</b> $\overrightarrow{AC} = (2; 2; -1)$, $|\overrightarrow{AC}| = 3$. Tích vô hướng $\overrightarrow{AB} \cdot \overrightarrow{AC} = -4 + 2 - 1 = -3$. Suy ra $\cos(\overrightarrow{AB}, \overrightarrow{AC}) = \dfrac{-3}{\sqrt{6} \times 3} = -\dfrac{\sqrt{6}}{6}$.</li>
    <li><b>c) ĐÚNG:</b> Ta có $\overrightarrow{AD} = (2; -2; 1) \implies AD = \sqrt{4 + 4 + 1} = 3$. Do $AC = AD = 3$ nên tam giác $ACD$ cân tại $A$. Đường phân giác trong góc $A$ đồng thời là đường trung tuyến, suy ra chân đường phân giác $M$ là trung điểm của đoạn thẳng $CD$. Tọa độ điểm $M$ là $\left(\dfrac{3+3}{2}; \dfrac{2+(-2)}{2}; \dfrac{1+3}{2}\right) = (3; 0; 2)$.</li>
    <li><b>d) SAI:</b> Xét $\overrightarrow{AB} = (-2; 1; 1)$, $\overrightarrow{AC} = (2; 2; -1)$, $\overrightarrow{AD} = (2; -2; 1)$. Tích hỗn tạp $[\overrightarrow{AB}, \overrightarrow{AC}] \cdot \overrightarrow{AD} = (-3)(2) + 0(-2) + (-6)(1) = -12 \ne 0$. Bốn điểm $A, B, C, D$ không đồng phẳng.</li>
  </ul>
</div>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Gọi cạnh đáy hình vuông của chiếc hộp là $x > 0$ (cm), chiều cao là $h = \dfrac{432}{x^2}$ (cm).
  <div class="step">Chi phí làm hai đáy: $8(2x^2) = 16x^2$ (nghìn đồng); chi phí làm bốn mặt xung quanh: $4(4xh) = 16xh = \dfrac{16(432)}{x} = \dfrac{6912}{x}$ (nghìn đồng).</div>
  <div class="step">Hàm chi phí: $C(x) = 16x^2 + \dfrac{6912}{x}$ trên $(0; +\infty)$.</div>
  <div class="step">Đạo hàm: $C'(x) = 32x - \dfrac{6912}{x^2} = 0 \Leftrightarrow x^3 = \dfrac{6912}{32} = 216 \Leftrightarrow x = 6\text{ cm}$.</div>
  <div class="step">Khi $x = 6$, hàm số đạt giá trị nhỏ nhất. Chiều cao hộp là $h = \dfrac{432}{6^2} = 12\text{ cm}$.</div>
  <span class="q-ans">&rArr; Đáp số: 12.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Chọn hệ trục $Oxy$ sao cho gốc $O$ là trung điểm $AB$, $AB$ nằm trên trục $Ox$. Khi đó $A(-2; 0)$, $B(2; 0)$, $S(0; 4)$.
  <div class="step">Phương trình parabol: $(P): y = 4 - x^2$. Tổng diện tích hình phẳng parabol: $S_{total} = \int_{-2}^{2} (4 - x^2)\,\mathrm{d}x = \dfrac{32}{3}\text{ m}^2$.</div>
  <div class="step">Đường tròn tâm $O$ bán kính $R = 2$: $x^2 + y^2 = 4$. Thay $x^2 = 4 - y \implies (4 - y) + y^2 = 4 \implies y = 1 \implies x = \pm\sqrt{3}$.</div>
  <div class="step">Giao điểm $M(-\sqrt{3}; 1), N(\sqrt{3}; 1) \implies \tan\alpha = \dfrac{1}{\sqrt{3}} \implies \alpha = 30^\circ$. Góc ở tâm hình quạt là $\theta = 180^\circ - 2(30^\circ) = 120^\circ = \dfrac{2\pi}{3}\text{ rad}$.</div>
  <div class="step">Diện tích hình quạt (phần giữa): $S_{giữa} = \dfrac{1}{2} R^2 \theta = \dfrac{1}{2} (2^2) \left(\dfrac{2\pi}{3}\right) = \dfrac{4\pi}{3}\text{ m}^2$.</div>
  <div class="step">Diện tích phần kẻ sọc (phần trên): $S_{trên} = \int_{-\sqrt{3}}^{\sqrt{3}} [(4 - x^2) - \sqrt{4 - x^2}]\,\mathrm{d}x = 5\sqrt{3} - \dfrac{4\pi}{3}\text{ m}^2$.</div>
  <div class="step">Diện tích phần còn lại: $S_{còn lại} = S_{total} - S_{giữa} - S_{trên} = \dfrac{32}{3} - 5\sqrt{3}\text{ m}^2$.</div>
  <div class="step">Tổng chi phí: $T = 140000\left(5\sqrt{3} - \dfrac{4\pi}{3}\right) + 150000\left(\dfrac{4\pi}{3}\right) + 160000\left(\dfrac{32}{3} - 5\sqrt{3}\right) = \dfrac{5120000}{3} + \dfrac{40000\pi}{3} - 100000\sqrt{3} \approx 1575349\text{ đồng} \approx 1575\text{ nghìn đồng}$.</div>
  <span class="q-ans">&rArr; Đáp số: 1575.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Lượng nước trong cốc khi nghiêng là một khối nêm hình trụ có đáy là nửa hình tròn bán kính $R = 6\text{ cm}$ và chiều cao $H = 10\text{ cm}$.
  <div class="step">Chọn hệ trục tọa độ sao cho đáy cốc nằm trong mặt phẳng $Oxy$, đường kính mực nước nằm trên trục $Ox$ (từ $-R$ đến $R$).</div>
  <div class="step">Phương trình mặt nước phẳng nghiêng đi qua đường kính đáy và mép miệng cốc: $z = \dfrac{H}{R} y$.</div>
  <div class="step">Mặt cắt thiết diện vuông góc với trục $Ox$ tại $x \in [-R; R]$ là một tam giác vuông có hai cạnh góc vuông là $y = \sqrt{R^2 - x^2}$ và $z = \dfrac{H}{R}\sqrt{R^2 - x^2}$.</div>
  <div class="step">Diện tích thiết diện: $S(x) = \dfrac{1}{2} y z = \dfrac{H}{2R}(R^2 - x^2)$.</div>
  <div class="step">Thể tích lượng nước: $V = \int_{-R}^{R} S(x)\,\mathrm{d}x = \dfrac{H}{R}\int_{0}^{R} (R^2 - x^2)\,\mathrm{d}x = \dfrac{2}{3} R^2 H$.</div>
  <div class="step">Thay số: $V = \dfrac{2}{3} \cdot 6^2 \cdot 10 = \dfrac{2}{3} \cdot 36 \cdot 10 = 240\text{ cm}^3$.</div>
  <span class="q-ans">&rArr; Đáp số: 240.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Biểu thức vận tốc: $v(t) = v(0) + \int_{0}^{t} (-2u - 2)\,\mathrm{d}u = 48 - t^2 - 2t$.
  <div class="step">Tàu dừng hẳn khi $v(t) = 0 \Leftrightarrow -t^2 - 2t + 48 = 0 \Leftrightarrow (t - 6)(t + 8) = 0 \implies t = 6\text{ s}$ (do $t \ge 0$).</div>
  <div class="step">Quãng đường tàu di chuyển được từ lúc bắt đầu hãm phanh đến khi dừng hẳn:</div>
  <div class="step">$s = \int_{0}^{6} (48 - 2t - t^2)\,\mathrm{d}t = \left[48t - t^2 - \dfrac{t^3}{3}\right]_0^6 = 288 - 36 - 72 = 180\text{ (m)}$.</div>
  <span class="q-ans">&rArr; Đáp số: 180.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Đoạn bay $AB$ có $A(1; 8; 12)$, $B(7; 4; 12) \implies \overrightarrow{AB} = (6; -4; 0) = 2(3; -2; 0)$.
  <div class="step">Phương trình tham số đoạn $AB$: $\begin{cases} x = 1 + 3t \\ y = 8 - 2t \\ z = 12 \end{cases}$ với $t \in [0; 2]$.</div>
  <div class="step">Khoảng cách từ $O(0; 0; 0)$ đến máy bay tại $M(t)$:</div>
  <div class="step">$OM^2 = (1 + 3t)^2 + (8 - 2t)^2 + 12^2 = 13t^2 - 26t + 209 = 13(t - 1)^2 + 196$.</div>
  <div class="step">Vì $t \in [0; 2]$, giá trị nhỏ nhất của $OM^2$ đạt được tại $t = 1 \in [0; 2]$: $OM^2_{\min} = 196 \implies OM_{\min} = 14\text{ km}$.</div>
  <span class="q-ans">&rArr; Đáp số: 14.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Gọi $G$ là trọng tâm tam giác $ABC$: $x_G = \dfrac{2+0+4}{3} = 2, y_G = \dfrac{1+3-1}{3} = 1, z_G = \dfrac{-1+1+3}{3} = 1 \implies G(2; 1; 1)$.
  <div class="step">Ta có $\overrightarrow{MA} + \overrightarrow{MB} + \overrightarrow{MC} = 3\overrightarrow{MG} \implies |\overrightarrow{MA} + \overrightarrow{MB} + \overrightarrow{MC}| = 3 MG$.</div>
  <div class="step">Độ dài $MG$ nhỏ nhất khi $M$ là hình chiếu vuông góc của $G(2; 1; 1)$ lên mặt phẳng $(Oxy): z = 0$.</div>
  <div class="step">Do đó $M(2; 1; 0) \implies a = 2, b = 1$. Giá trị $a + b = 2 + 1 = 3$.</div>
  <span class="q-ans">&rArr; Đáp số: 3.</span>
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

html_path = 'dap_an_108.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'Bang_Dap_An_Va_HDG_De_108.pdf'
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
