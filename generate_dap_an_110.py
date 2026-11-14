import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 110</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 10mm 14mm 12mm 14mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 110";
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
  <div class="title-meta">Môn: TOÁN – LỚP 12 | <b>Mã đề thi: 110</b> | Biên soạn: Trần Trung Quân</div>
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
    <td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">D</td>
    <td class="bold-ans">B</td><td class="bold-ans">A</td><td class="bold-ans">C</td>
    <td class="bold-ans">B</td><td class="bold-ans">D</td><td class="bold-ans">A</td>
    <td class="bold-ans">D</td><td class="bold-ans">B</td><td class="bold-ans">B</td>
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
    <td style="font-weight: bold;">Câu 1</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Câu 2</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Câu 3</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Câu 4</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
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
    <td class="bold-ans">125,7</td>
    <td class="bold-ans">11,44</td>
    <td class="bold-ans">115586</td>
    <td class="bold-ans">32</td>
    <td class="bold-ans">60</td>
    <td class="bold-ans">75,6</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Xét hàm số $f(x) = \dfrac{2x - 1}{x + 2}$ trên đoạn $[0; 2]$.
  <div class="step">Đạo hàm: $f'(x) = \dfrac{2(2) - (-1)(1)}{(x + 2)^2} = \dfrac{5}{(x + 2)^2} > 0,\; \forall x \in [0; 2]$.</div>
  <div class="step">Hàm số đồng biến trên $[0; 2]$ nên $\max_{[0; 2]} f(x) = f(2) = \dfrac{2(2) - 1}{2 + 2} = \dfrac{3}{4}$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Xét hàm số $y = -x^4 + 2x^2 + 3$.
  <div class="step">Đạo hàm: $y' = -4x^3 + 4x = -4x(x^2 - 1) = -4x(x - 1)(x + 1)$. Cho $y' = 0 \Leftrightarrow x \in \{-1; 0; 1\}$.</div>
  <div class="step">Xét dấu $y'$: $y' < 0$ khi $x \in (-1; 0) \cup (1; +\infty)$ và $y' > 0$ khi $x \in (-\infty; -1) \cup (0; 1)$. Khoảng nghịch biến của hàm số là $(-1; 0)$ và $(1; +\infty)$. Ở phương án C là $(-1; 0)$ (nghịch biến).</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Ta có: $\int \left(3x^2 + \dfrac{1}{x^2}\right)\,\mathrm{d}x = 3 \cdot \dfrac{x^3}{3} + \left(-\dfrac{1}{x}\right) + C = x^3 - \dfrac{1}{x} + C$.
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> $I = \int_{0}^{\ln 3} e^x\,\mathrm{d}x = \left[e^x\right]_0^{\ln 3} = e^{\ln 3} - e^0 = 3 - 1 = 2$.
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Theo tính chất tuyến tính của tích phân đối với hằng số: $\int_{0}^{2} 4f(x)\,\mathrm{d}x = 4\int_{0}^{2} f(x)\,\mathrm{d}x = 4 \times 3 = 12$.
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Diện tích hình phẳng: $S = \int_{1}^{e^2} \dfrac{1}{x}\,\mathrm{d}x = [\ln x]_1^{e^2} = \ln(e^2) - \ln 1 = 2$.
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 7:</span> Thể tích khối tròn xoay quanh trục hoành:
  <div class="step">$V = \pi \int_{0}^{\frac{\pi}{2}} (\sqrt{\cos x})^2\,\mathrm{d}x = \pi \int_{0}^{\frac{\pi}{2}} \cos x\,\mathrm{d}x = \pi [\sin x]_0^{\frac{\pi}{2}} = \pi (1 - 0) = \pi$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8:</span> Điểm đối xứng của $M(2; -3; 4)$ qua mặt phẳng $(Oxy)$ có tọa độ là $M'(2; -3; -4)$.
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9:</span> Với $\overrightarrow{u} = (2; -3; 6)$, độ dài của vectơ là:
  <div class="step">$|\overrightarrow{u}| = \sqrt{2^2 + (-3)^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10:</span> Hai vectơ $\overrightarrow{a} = (2; -1; 3)$ và $\overrightarrow{b} = (-4; m; n)$ cùng phương khi:
  <div class="step">$\dfrac{-4}{2} = \dfrac{m}{-1} = \dfrac{n}{3} = -2 \implies m = 2,\; n = -6 \implies m + n = 2 + (-6) = -4$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11:</span> Cho $A(1; 2; 0)$, $B(3; -1; 1)$ và $C(1; 1; 2)$. Ta có $\overrightarrow{AB} = (2; -3; 1)$ và $\overrightarrow{AC} = (0; -1; 2)$.
  <div class="step">Tích vô hướng: $\overrightarrow{AB} \cdot \overrightarrow{AC} = 2(0) + (-3)(-1) + 1(2) = 0 + 3 + 2 = 5$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12:</span> Vectơ độ dời $\overrightarrow{MN} = (3 - 1; 0 - 3; 4 - 2) = (2; -3; 2)$.
  <div class="step">Công sinh ra: $A = \overrightarrow{F} \cdot \overrightarrow{MN} = 4(2) + (-2)(-3) + 5(2) = 8 + 6 + 10 = 24\text{ J}$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Cho hàm số bậc ba $y = f(x)$ có đồ thị $(C)$ với hai điểm cực trị $A(0; 2)$ và $B(2; -2)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Điểm uốn $I$ là tâm đối xứng của đồ thị, cũng là trung điểm của đoạn nối hai cực trị: $x_I = \dfrac{0+2}{2} = 1$, $y_I = \dfrac{2+(-2)}{2} = 0 \implies I(1; 0)$.</li>
    <li><b>b) ĐÚNG:</b> Đồ thị đi lên trên $(-\infty; 0)$ và $(2; +\infty)$ nên hàm số đồng biến trên mỗi khoảng $(-\infty; 0)$ và $(2; +\infty)$.</li>
    <li><b>c) ĐÚNG:</b> Đạo hàm $f'(x) = 3ax(x - 2) = 3ax^2 - 6ax \implies f(x) = ax^3 - 3ax^2 + d$. Đồ thị qua $A(0; 2) \implies d = 2$; qua $B(2; -2) \implies 8a - 12a + 2 = -2 \Leftrightarrow -4a = -4 \Leftrightarrow a = 1$. Vậy $y = x^3 - 3x^2 + 2$.</li>
    <li><b>d) SAI:</b> Tại $x = 3 \implies y(3) = 2$. Hệ số góc tiếp tuyến $k = f'(3) = 3(3^2) - 6(3) = 9$. Phương trình tiếp tuyến: $y = 9(x - 3) + 2 = 9x - 25$. Tại $x = 2$, tung độ tiếp tuyến là $y = 9(2) - 25 = -7 \ne -5$, do đó tiếp tuyến không đi qua $N(2; -5)$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Cho hàm số $f(x) = 3x^2 - 2x$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Ta có $\int (3x^2 - 2x)\,\mathrm{d}x = x^3 - x^2 + C$. Do đó $F(x) = x^3 - x^2 + C$ là một nguyên hàm của $f(x)$.</li>
    <li><b>b) ĐÚNG:</b> Với $F(x) = x^3 - x^2 + C$, có $F(2) = 8 - 4 + C = 4 + C = 5 \implies C = 1$. Khi đó $F(5) = 5^3 - 5^2 + 1 = 125 - 25 + 1 = 101$.</li>
    <li><b>c) ĐÚNG:</b> $\int_{1}^{3} [f(x) + 2x]\,\mathrm{d}x = \int_{1}^{3} 3x^2\,\mathrm{d}x = [x^3]_1^3 = 27 - 1 = 26$.</li>
    <li><b>d) SAI:</b> Phương trình hoành độ giao điểm $3x^2 - 2x = 0 \Leftrightarrow x = 0$ hoặc $x = \dfrac{2}{3}$. Diện tích hình phẳng trên $[0; 1]$ là:
      $$S = \int_{0}^{\frac{2}{3}} (2x - 3x^2)\,\mathrm{d}x + \int_{\frac{2}{3}}^{1} (3x^2 - 2x)\,\mathrm{d}x = \left[x^2 - x^3\right]_0^{2/3} + \left[x^3 - x^2\right]_{2/3}^1 = \dfrac{4}{27} + \dfrac{4}{27} = \dfrac{8}{27} \ne 1.$$
    </li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Vi khuẩn tăng trưởng với tốc độ $N'(t) = 150e^{0,5t}$, ban đầu $N(0) = 300$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Tại $t = 0$, tốc độ tăng trưởng là $N'(0) = 150e^0 = 150$ con/giờ.</li>
    <li><b>b) ĐÚNG:</b> $N(t) = 300 + \int_{0}^{t} 150e^{0,5u}\,\mathrm{d}u = 300 + 300(e^{0,5t} - 1) = 300e^{0,5t}$ con.</li>
    <li><b>c) ĐÚNG:</b> Số vi khuẩn tăng thêm sau 4 giờ là $\Delta N = N(4) - N(0) = 300e^2 - 300 = 300(e^2 - 1)$ con.</li>
    <li><b>d) SAI:</b> Sau 2 giờ, số lượng vi khuẩn là $N(2) = 300e^1 \approx 815,5$ con $< 1000$ con.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Hình hộp chữ nhật $ABCD.A'B'C'D'$ có $A(0; 0; 0)$, $B(4; 0; 0)$, $D(0; 6; 0)$, $A'(0; 0; 3)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Đỉnh đối diện $C'$ có tọa độ $C'(4; 6; 3)$.</li>
    <li><b>b) SAI:</b> Tứ diện $A'BCD$ có $A'(0; 0; 3)$, $B(4; 0; 0)$, $C(4; 6; 0)$, $D(0; 6; 0)$. Trọng tâm $G\left(\dfrac{8}{4}; \dfrac{12}{4}; \dfrac{3}{4}\right) = G\left(2; 3; \dfrac{3}{4}\right) \ne (1; 2; 1)$.</li>
    <li><b>c) ĐÚNG:</b> Độ dài đường chéo $AC' = \sqrt{4^2 + 6^2 + 3^2} = \sqrt{61}$.</li>
    <li><b>d) ĐÚNG:</b> Thể tích khối hộp $V = 4 \times 6 \times 3 = 72$.</li>
  </ul>
</div>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Bán kính gợn sóng tăng với tốc độ $\dfrac{\mathrm{d}r}{\mathrm{d}t} = 2\text{ cm/s}$. Diện tích hình tròn là $S(t) = \pi r(t)^2$.
  <div class="step">Tốc độ biến thiên diện tích: $\dfrac{\mathrm{d}S}{\mathrm{d}t} = 2\pi r \dfrac{\mathrm{d}r}{\mathrm{d}t}$.</div>
  <div class="step">Tại thời điểm $r = 10\text{ cm}$: $\dfrac{\mathrm{d}S}{\mathrm{d}t} = 2\pi(10)(2) = 40\pi \approx 125,6637\text{ cm}^2/\text{s}$. Làm tròn đến hàng phần mười: <b>125,7</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 125,7</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Chọn hệ trục $Oxy$ với $H \equiv O(0; 0)$, trục $Ox$ dọc theo $AB$, trục $Oy$ dọc theo $GH$.
  <div class="step">Parabol có đỉnh $G(0; 4)$ và qua $(\pm 2; 0) \implies y = 4 - x^2$. Diện tích toàn bộ vòm parabol: $S = \int_{-2}^{2} (4 - x^2)\,\mathrm{d}x = \dfrac{32}{3}\text{ m}^2$.</div>
  <div class="step">Cánh cổng hình chữ nhật $CDEF$: vì $AB = 4\text{ m}, AC = BD = 0,9\text{ m}$ nên $CD = 4 - 1,8 = 2,2\text{ m}$. Hoành độ điểm $D$ là $1,1\text{ m} \implies$ chiều cao $DE = 4 - (1,1)^2 = 2,79\text{ m}$.</div>
  <div class="step">Diện tích cánh cổng $S_1 = 2,2 \times 2,79 = 6,138\text{ m}^2$. Diện tích xiên hoa $S_2 = \dfrac{32}{3} - 6,138\text{ m}^2$.</div>
  <div class="step">Tổng chi phí: $T = 6,138 \times 1\,200\,000 + \left(\dfrac{32}{3} - 6,138\right) \times 900\,000 = 6,138 \times 300\,000 + 32 \times 300\,000 = 11\,441\,400\text{ đồng} \approx 11,44\text{ triệu đồng}$.</div>
  <span class="q-ans">&rArr; Đáp số: 11,44</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Nền sân là elip $(E): \dfrac{x^2}{75^2} + \dfrac{y^2}{45^2} = 1$ với $a = 75\text{ m}, b = 45\text{ m}$.
  <div class="step">Cắt theo mặt phẳng vuông góc với trục lớn tại vị trí $x \in [-75; 75]$: Dây cung $MN = 2b\sqrt{1 - \dfrac{x^2}{a^2}}$.</div>
  <div class="step">Thiết diện là hình viên phân góc ở tâm $\widehat{MIN} = 90^\circ$: Tam giác $IMN$ vuông cân tại $I \implies MN^2 = 2R^2 \implies R^2 = \dfrac{MN^2}{2} = 2b^2\left(1 - \dfrac{x^2}{a^2}\right)$.</div>
  <div class="step">Diện tích viên phân: $S(x) = S_{\text{quạt}} - S_{\Delta IMN} = \dfrac{1}{2} R^2 \dfrac{\pi}{2} - \dfrac{1}{2} R^2 = \dfrac{R^2(\pi - 2)}{4} = \dfrac{b^2(\pi - 2)}{2}\left(1 - \dfrac{x^2}{a^2}\right)$.</div>
  <div class="step">Thể tích không gian mái vòm: $V = \int_{-a}^{a} S(x)\,\mathrm{d}x = \dfrac{2}{3} a b^2 (\pi - 2) = \dfrac{2}{3}(75)(45^2)(\pi - 2) = 101\,250(\pi - 2) \approx 115\,586,26\text{ m}^3$. Làm tròn đến hàng đơn vị: <b>115586</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 115586</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Ta có $\dfrac{\mathrm{d}S}{\sqrt{S}} = k\,\mathrm{d}t \implies 2\sqrt{S} = kt + C \iff \sqrt{S(t)} = \dfrac{k}{2}t + C_1$.
  <div class="step">Tại $t = 0$: $S(0) = 16 \implies C_1 = \sqrt{16} = 4$. Suy ra $\sqrt{S(t)} = \dfrac{k}{2}t + 4$.</div>
  <div class="step">Tại $t = 3$: $S(3) = 32 \implies \sqrt{32} = 4\sqrt{2} = \dfrac{3k}{2} + 4 \implies \dfrac{k}{2} = \dfrac{4(\sqrt{2} - 1)}{3}$.</div>
  <div class="step">Khi phủ kín mặt hồ $470\text{ m}^2$: $\sqrt{470} = \dfrac{4(\sqrt{2} - 1)}{3} t + 4 \iff t = \dfrac{3(\sqrt{470} - 4)}{4(\sqrt{2} - 1)} \approx \dfrac{53,03845}{1,656854} \approx 32,01\text{ ngày}$. Làm tròn: <b>32</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 32</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Cho hình lập phương $ABCD.A'B'C'D'$. Đặt cạnh hình lập phương bằng $a > 0$.
  <div class="step"><b>Cách 1 (Dùng tích vô hướng):</b> Ta có $\overrightarrow{A'D} = \overrightarrow{B'C}$ (do tứ giác $A'B'CD$ là hình bình hành).</div>
  <div class="step">Suy ra: $\overrightarrow{AC} \cdot \overrightarrow{A'D} = \overrightarrow{AC} \cdot \overrightarrow{B'C} = (\overrightarrow{AB} + \overrightarrow{BC}) \cdot (\overrightarrow{B'B} + \overrightarrow{BC})$.</div>
  <div class="step">Vì $BB' \perp (ABCD) \implies \overrightarrow{B'B} \cdot \overrightarrow{AB} = 0$, $\overrightarrow{B'B} \cdot \overrightarrow{BC} = 0$, và $ABCD$ là hình vuông $\implies \overrightarrow{AB} \cdot \overrightarrow{BC} = 0$.</div>
  <div class="step">Do đó $\overrightarrow{AC} \cdot \overrightarrow{A'D} = \overrightarrow{BC}^2 = a^2$.</div>
  <div class="step">Độ dài: $|\overrightarrow{AC}| = a\sqrt{2}$ và $|\overrightarrow{A'D}| = a\sqrt{2}$.</div>
  <div class="step">Suy ra $\cos(\overrightarrow{AC}, \overrightarrow{A'D}) = \dfrac{a^2}{a\sqrt{2} \cdot a\sqrt{2}} = \dfrac{1}{2} \implies (\overrightarrow{AC}, \overrightarrow{A'D}) = 60^\circ$.</div>
  <div class="step"><b>Cách 2 (Hình học thuần túy):</b> Xét tam giác $ACB'$ có các cạnh $AC = CB' = B'A = a\sqrt{2}$ (đường chéo của các mặt hình vuông bằng nhau), nên tam giác $ACB'$ đều $\implies \widehat{ACB'} = 60^\circ$. Do $\overrightarrow{A'D} = \overrightarrow{B'C} = -\overrightarrow{CB'}$ và $\overrightarrow{AC} = -\overrightarrow{CA}$ nên $(\overrightarrow{AC}, \overrightarrow{A'D}) = (\overrightarrow{CA}, \overrightarrow{CB'}) = \widehat{ACB'} = 60^\circ$.</div>
  <span class="q-ans">&rArr; Đáp số: 60</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Gọi $H$ là tâm đèn tròn, $R = 0,5\text{ m} = 50\text{ cm}$. Các góc giữa dây và trục thẳng đứng $OH$ bằng $\alpha$.
  <div class="step">Trong tam giác vuông $OHA$: $\cos\alpha = \dfrac{OH}{OA} = \dfrac{\sqrt{L^2 - R^2}}{L}$.</div>
  <div class="step">Điều kiện cân bằng tĩnh học: $3T \cos\alpha = P = 27\text{ N} \implies T = \dfrac{9}{\cos\alpha}$.</div>
  <div class="step">Lực căng tối đa $12\text{ N} \implies \dfrac{9}{\cos\alpha} \le 12 \iff \cos\alpha \ge \dfrac{3}{4} \iff \dfrac{L^2 - R^2}{L^2} \ge \dfrac{9}{16} \iff L \ge \dfrac{4\sqrt{7}}{7} R$.</div>
  <div class="step">Với $R = 50\text{ cm} \implies L \ge \dfrac{200\sqrt{7}}{7} \approx 75,5929\text{ cm}$. Làm tròn đến 1 chữ số thập phân: <b>75,6</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 75,6</span>
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

with open("dap_an_110.html", "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "Bang_Dap_An_Va_HDG_De_110.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "dap_an_110.html"
]

print("Running Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
