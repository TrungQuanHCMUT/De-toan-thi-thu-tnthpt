import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 111</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 10mm 14mm 12mm 14mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 111";
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
  <div class="title-meta">Môn: TOÁN – LỚP 12 | <b>Mã đề thi: 111</b> | Biên soạn: Trần Trung Quân</div>
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
    <td class="bold-ans">B</td><td class="bold-ans">C</td><td class="bold-ans">A</td>
    <td class="bold-ans">D</td><td class="bold-ans">A</td><td class="bold-ans">B</td>
    <td class="bold-ans">C</td><td class="bold-ans">B</td><td class="bold-ans">D</td>
    <td class="bold-ans">A</td><td class="bold-ans">C</td><td class="bold-ans">D</td>
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
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
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
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans" style="color: #2b6cb0;">SAI</td>
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
    <td class="bold-ans">26,09</td>
    <td class="bold-ans">2,46</td>
    <td class="bold-ans">5,3</td>
    <td class="bold-ans">25</td>
    <td class="bold-ans">6,09</td>
    <td class="bold-ans">0,92</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Hàm số $y = \dfrac{2x + 3}{x - 1}$.
  <div class="step">Ta có $\lim_{x \to 1^+} \dfrac{2x + 3}{x - 1} = +\infty$ và $\lim_{x \to 1^-} \dfrac{2x + 3}{x - 1} = -\infty$. Do đó đường thẳng $x = 1$ là tiệm cận đứng của đồ thị hàm số.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> $f'(x) = x(x - 2)^2(x + 3)^3$.
  <div class="step">Nghiệm của phương trình $f'(x) = 0$ là $x = 0$ (bội 1), $x = 2$ (bội 2), $x = -3$ (bội 3). Đạo hàm $f'(x)$ chỉ đổi dấu khi qua $x = 0$ và $x = -3$, không đổi dấu khi qua nghiệm bội chẵn $x = 2$. Do đó hàm số có đúng $2$ điểm cực trị.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Xét hàm số $f(x) = x^3 - 3x + 5$ trên $[0; 2]$.
  <div class="step">Đạo hàm $f'(x) = 3x^2 - 3 = 0 \iff x = 1 \in [0; 2]$ (loại $x = -1$).</div>
  <div class="step">Ta có $f(0) = 5$, $f(1) = 3$, $f(2) = 2^3 - 3(2) + 5 = 7$. Do đó giá trị nhỏ nhất là $\min_{[0; 2]} f(x) = f(1) = 3$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Áp dụng các công thức nguyên hàm cơ bản:
  <div class="step">$\int (\sin 2x + e^{3x})\,\mathrm{d}x = -\dfrac{1}{2}\cos 2x + \dfrac{1}{3}e^{3x} + C$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Ta có $\int_{1}^{4} f(x)\,\mathrm{d}x = \int_{1}^{2} f(x)\,\mathrm{d}x + \int_{2}^{4} f(x)\,\mathrm{d}x = 2 + (-5) = -3$.
  <div class="step">Do đó: $\int_{1}^{4} [2f(x) - 3]\,\mathrm{d}x = 2\int_{1}^{4} f(x)\,\mathrm{d}x - \int_{1}^{4} 3\,\mathrm{d}x = 2(-3) - 3(4 - 1) = -6 - 9 = -15$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Phương trình hoành độ giao điểm: $x^2 = 2 - x^2 \iff 2x^2 = 2 \iff x = \pm 1$.
  <div class="step">Diện tích hình phẳng: $S = \int_{-1}^{1} |2 - 2x^2|\,\mathrm{d}x = \int_{-1}^{1} (2 - 2x^2)\,\mathrm{d}x = \left[2x - \dfrac{2x^3}{3}\right]_{-1}^{1} = \left(2 - \dfrac{2}{3}\right) - \left(-2 + \dfrac{2}{3}\right) = \dfrac{8}{3}$.</div>
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 7:</span> Thể tích khối tròn xoay tạo thành khi quay quanh trục hoành là:
  <div class="step">$V = \pi \int_{0}^{1} y^2\,\mathrm{d}x = \pi \int_{0}^{1} (x e^x)^2\,\mathrm{d}x = \pi \int_{0}^{1} x^2 e^{2x}\,\mathrm{d}x$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8:</span> Hình chiếu vuông góc của điểm $A(3; -2; 5)$ lên trục tung $Oy$ giữ nguyên tung độ, còn hoành độ và cao độ bằng $0$, tức là điểm $(0; -2; 0)$.
  <span class="q-ans">&rArr; Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9:</span> Cho $P(1; 4; -3)$ và $Q(-3; 2; 1)$. Tọa độ trung điểm $I$ của $PQ$ là:
  <div class="step">$x_I = \dfrac{1 + (-3)}{2} = -1,\; y_I = \dfrac{4 + 2}{2} = 3,\; z_I = \dfrac{-3 + 1}{2} = -1 \implies I(-1; 3; -1)$.</div>
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10:</span> Ta có $\overrightarrow{u} + \overrightarrow{v} = (1 + 2; 2 - 1; -2 + 2) = (3; 1; 0)$.
  <div class="step">Độ dài: $|\overrightarrow{u} + \overrightarrow{v}| = \sqrt{3^2 + 1^2 + 0^2} = \sqrt{10}$.</div>
  <span class="q-ans">&rArr; Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11:</span> Tích vô hướng: $\overrightarrow{a} \cdot \overrightarrow{b} = 1(0) + 0(1) + 1(1) = 1$.
  <div class="step">Độ dài: $|\overrightarrow{a}| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{2}$, $|\overrightarrow{b}| = \sqrt{0^2 + 1^2 + 1^2} = \sqrt{2}$.</div>
  <div class="step">Côsin của góc giữa hai vectơ: $\cos(\overrightarrow{a}, \overrightarrow{b}) = \dfrac{1}{\sqrt{2} \cdot \sqrt{2}} = \dfrac{1}{2}$.</div>
  <span class="q-ans">&rArr; Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12:</span> Ta có $\overrightarrow{a} = (2; -4; 6) = 2(1; -2; 3) = 2\overrightarrow{u}_4$. Vì hệ số $k = 2 > 0$ nên vectơ $\overrightarrow{u}_4 = (1; -2; 3)$ cùng hướng với vectơ $\overrightarrow{a}$.
  <span class="q-ans">&rArr; Chọn D.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Cho hàm số $y = f(x) = \dfrac{x^2 - x + 1}{x - 1} = x + \dfrac{1}{x - 1}$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Mẫu triệt tiêu tại $x = 1$ nên đồ thị có tiệm cận đứng là $x = 1$. Lại có $\lim_{x \to \pm\infty} [f(x) - x] = \lim_{x \to \pm\infty} \dfrac{1}{x - 1} = 0$, nên đường thẳng $y = x$ là tiệm cận xiên.</li>
    <li><b>b) ĐÚNG:</b> Đạo hàm $f'(x) = 1 - \dfrac{1}{(x - 1)^2} = \dfrac{x(x - 2)}{(x - 1)^2}$. Cho $f'(x) = 0 \iff x = 0$ hoặc $x = 2$. Do đó $f'(x) > 0$ khi $x \in (-\infty; 0) \cup (2; +\infty)$ nên hàm số đồng biến trên mỗi khoảng $(-\infty; 0)$ và $(2; +\infty)$.</li>
    <li><b>c) ĐÚNG:</b> Giao điểm của tiệm cận đứng $x = 1$ và tiệm cận xiên $y = x$ là điểm $I(1; 1)$. Với mọi $x \ne 1$, ta có $f(1 + t) + f(1 - t) = \left(1 + t + \dfrac{1}{t}\right) + \left(1 - t - \dfrac{1}{t}\right) = 2 = 2y_I$. Do đó $I(1; 1)$ là tâm đối xứng của đồ thị hàm số.</li>
    <li><b>d) SAI:</b> Gọi $M\left(1 + u; 1 + u + \dfrac{1}{u}\right)$ với $u > 0$ và $N\left(1 - v; 1 - v - \dfrac{1}{v}\right)$ với $v > 0$ là hai điểm thuộc hai nhánh của đồ thị. Đặt $s = u + v > 0$. Áp dụng bất đẳng thức Cauchy-Schwarz: $\dfrac{1}{u} + \dfrac{1}{v} \ge \dfrac{4}{s}$. Do đó $MN^2 = (u + v)^2 + \left(u + v + \dfrac{1}{u} + \dfrac{1}{v}\right)^2 \ge s^2 + \left(s + \dfrac{4}{s}\right)^2 = 2s^2 + 8 + \dfrac{16}{s^2} \ge 8 + 8\sqrt{2}$ (theo AM-GM). Suy ra khoảng cách nhỏ nhất giữa hai điểm thuộc hai nhánh là $MN_{\min} = \sqrt{8 + 8\sqrt{2}} = 2\sqrt{2 + 2\sqrt{2}} \approx 4,394 \ne 2\sqrt{2}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Cho hàm số $f(x) = 4x^3 - 3x^2 + 2x$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Ta có $[x^4 - x^3 + x^2 + 5]' = 4x^3 - 3x^2 + 2x = f(x)$, nên $F(x) = x^4 - x^3 + x^2 + 5$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$.</li>
    <li><b>b) SAI:</b> Theo định lý cơ bản của phép tính vi tích phân: $F(2) - F(1) = \int_{1}^{2} f(x)\,\mathrm{d}x = [x^4 - x^3 + x^2]_1^2 = (16 - 8 + 4) - (1 - 1 + 1) = 12 - 1 = 11$. Khi đó $F(2) = F(1) + 11 = 3 + 11 = 14 \ne 16$.</li>
    <li><b>c) ĐÚNG:</b> $\int_{0}^{1} [f(x) + e^x]\,\mathrm{d}x = [x^4 - x^3 + x^2 + e^x]_0^1 = (1 - 1 + 1 + e) - (0 + e^0) = 1 + e - 1 = e$.</li>
    <li><b>d) ĐÚNG:</b> Hoành độ giao điểm của hai đồ thị: $f(x) - g(x) = 0 \iff (4x^3 - 3x^2 + 2x) - (4x^3 - 5x^2 + 4x) = 0 \iff 2x^2 - 2x = 0 \iff x = 0$ hoặc $x = 1$. Với mọi $x \in [0; 1]$ thì $g(x) \ge f(x) \ge 0$. Khi quay hình phẳng $D$ quanh trục $Ox$, thể tích khối tròn xoay là: $V = \pi \int_0^1 [g(x)^2 - f(x)^2]\,\mathrm{d}x = \pi \int_0^1 (-16x^5 + 32x^4 - 28x^3 + 12x^2)\,\mathrm{d}x = \dfrac{11\pi}{15}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Tàu hỏa chuyển động chậm dần đều với vận tốc $v(t) = 20 - 2t\text{ (m/s)}$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Tàu dừng hẳn khi $v(t) = 0 \iff 20 - 2t = 0 \iff t = 10\text{ giây}$.</li>
    <li><b>b) ĐÚNG:</b> Vận tốc sau 4 giây: $v(4) = 20 - 2(4) = 12\text{ m/s}$.</li>
    <li><b>c) ĐÚNG:</b> Quãng đường đi được trong 5 giây đầu: $s(5) = \int_{0}^{5} (20 - 2t)\,\mathrm{d}t = [20t - t^2]_0^5 = 100 - 25 = 75\text{ m}$.</li>
    <li><b>d) SAI:</b> Quãng đường tổng cộng cho đến khi dừng hẳn là $s(10) = \int_{0}^{10} (20 - 2t)\,\mathrm{d}t = [20t - t^2]_0^{10} = 200 - 100 = 100\text{ m} \ne 120\text{ m}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Cho hình chóp $S.ABCD$ có $S(0; 0; 3)$, $A(0; 0; 0)$, $B(2; 0; 0)$, $D(0; 2; 0)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG:</b> Đáy $ABCD$ là hình vuông trong mặt phẳng $(Oxy)$ có $A(0;0;0), B(2;0;0), D(0;2;0) \implies C = B + D - A = (2; 2; 0)$.</li>
    <li><b>b) ĐÚNG:</b> Trọng tâm $G$ của tam giác $SAB$ có tọa độ: $x_G = \dfrac{0+2+0}{3} = \dfrac{2}{3},\; y_G = 0,\; z_G = \dfrac{3+0+0}{3} = 1 \implies G\left(\dfrac{2}{3}; 0; 1\right)$.</li>
    <li><b>c) ĐÚNG:</b> $\overrightarrow{SB} = (2; 0; -3)$, $\overrightarrow{SD} = (0; 2; -3) \implies \overrightarrow{SB} \cdot \overrightarrow{SD} = 2(0) + 0(2) + (-3)(-3) = 9$.</li>
    <li><b>d) SAI:</b> Diện tích đáy hình vuông $S_{ABCD} = 2^2 = 4$. Đường cao $h = SA = 3$ (do $S$ thuộc trục $Oz$ và đáy thuộc $(Oxy)$ nên $SA \perp (ABCD)$). Thể tích khối chóp là $V = \dfrac{1}{3} S_{ABCD} \cdot SA = \dfrac{1}{3} \times 4 \times 3 = 4 \ne 6$.</li>
  </ul>
</div>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Một chiếc hộp hình trụ có $R = 4\text{ cm}$, $h = 7\text{ cm}$. Dây quấn 1 vòng từ $A$ đáy trên đến $B$ đáy dưới thẳng đứng với $A$.
  <div class="step">Khi cắt mặt xung quanh của hình trụ dọc theo đường sinh qua $A$ và trải phẳng ra mặt phẳng, ta được một hình chữ nhật có kích thước $h = 7\text{ cm}$ và chu vi đáy $C = 2\pi R = 2\pi \cdot 4 = 8\pi\text{ cm}$.</div>
  <div class="step">Độ dài ngắn nhất của sợi dây quấn quanh thân hình trụ đúng một vòng chính là độ dài đường chéo của hình chữ nhật:</div>
  <div class="step">$L_{\min} = \sqrt{h^2 + C^2} = \sqrt{7^2 + (8\pi)^2} = \sqrt{49 + 64\pi^2} \approx 26,08936\text{ cm}$.</div>
  <div class="step">Làm tròn đến hàng phần trăm: <b>26,09</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 26,09</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Mặt cắt ngang của bồn chứa là hình tròn bán kính $R = 1\text{ m}$.
  <div class="step">Mực nước ngập độ cao $h = 0,5\text{ m}$ ứng với một hình viên phân. Khoảng cách từ tâm đến dây cung mặt nước là $d = 1 - 0,5 = 0,5\text{ m}$.</div>
  <div class="step">Góc ở tâm: $\cos\left(\dfrac{\alpha}{2}\right) = \dfrac{d}{R} = \dfrac{0,5}{1} = \dfrac{1}{2} \implies \dfrac{\alpha}{2} = \dfrac{\pi}{3} \implies \alpha = \dfrac{2\pi}{3}\text{ rad}$.</div>
  <div class="step">Diện tích hình viên phân nước chiếm: $S = \dfrac{1}{2} R^2 (\alpha - \sin\alpha) = \dfrac{1}{2}(1)^2 \left(\dfrac{2\pi}{3} - \dfrac{\sqrt{3}}{2}\right) = \dfrac{\pi}{3} - \dfrac{\sqrt{3}}{4} \approx 0,614185\text{ m}^2$.</div>
  <div class="step">Thể tích nước trong bồn: $V = S \times L = 4 \left(\dfrac{\pi}{3} - \dfrac{\sqrt{3}}{4}\right) = \dfrac{4\pi}{3} - \sqrt{3} \approx 2,45674\text{ m}^3$. Làm tròn đến hàng phần trăm: <b>2,46</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 2,46</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Hai hàm số $f(x) = ax^3 + bx^2 + cx + \dfrac{3}{4}$ và $g(x) = dx^2 + ex - \dfrac{3}{4}$ cắt nhau tại hoành độ $-2; 1; 3$.
  <div class="step">Phương trình hoành độ giao điểm: $f(x) - g(x) = 0 \iff ax^3 + (b - d)x^2 + (c - e)x + \dfrac{3}{2} = 0$.</div>
  <div class="step">Vì cắt nhau tại $-2; 1; 3$ nên $f(x) - g(x) = a(x + 2)(x - 1)(x - 3) = a(x^3 - 2x^2 - 5x + 6)$.</div>
  <div class="step">Đồng nhất hệ số tự do: $6a = \dfrac{3}{2} \implies a = \dfrac{1}{4}$.</div>
  <div class="step">Diện tích hình phẳng: $S = \dfrac{1}{4} \int_{-2}^{3} |(x + 2)(x - 1)(x - 3)|\,\mathrm{d}x = \dfrac{1}{4} \left[ \int_{-2}^{1} (x^3 - 2x^2 - 5x + 6)\,\mathrm{d}x + \int_{1}^{3} -(x^3 - 2x^2 - 5x + 6)\,\mathrm{d}x \right] = \dfrac{1}{4} \left( \dfrac{63}{4} + \dfrac{16}{3} \right) = \dfrac{253}{48} \approx 5,27083$. Làm tròn đến hàng phần mười: <b>5,3</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 5,3</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Chất điểm $A$ có $v(t) = \dfrac{1}{100}t^2 + \dfrac{13}{30}t$. Chất điểm $B$ xuất phát chậm hơn $10\text{ s}$ với gia tốc $a$, sau $15\text{ s}$ đuổi kịp $A$.
  <div class="step">Thời gian chất điểm $A$ đã đi khi $B$ đuổi kịp là: $t_A = 15 + 10 = 25\text{ giây}$.</div>
  <div class="step">Quãng đường $A$ đi được: $s_A = \int_{0}^{25} \left(\dfrac{1}{100}t^2 + \dfrac{13}{30}t\right)\,\mathrm{d}t = \left[\dfrac{t^3}{300} + \dfrac{13t^2}{60}\right]_0^{25} = \dfrac{15625}{300} + \dfrac{8125}{60} = 187,5\text{ m}$.</div>
  <div class="step">Quãng đường $B$ đi được trong $15\text{ s}$ với gia tốc $a$: $s_B = \dfrac{1}{2} a (15)^2 = 112,5a$.</div>
  <div class="step">Vì $B$ đuổi kịp $A$ nên $112,5a = 187,5 \implies a = \dfrac{5}{3}\text{ m/s}^2$.</div>
  <div class="step">Vận tốc của $B$ tại thời điểm đuổi kịp: $v_B(15) = a \cdot 15 = \dfrac{5}{3} \cdot 15 = 25\text{ m/s}$.</div>
  <span class="q-ans">&rArr; Đáp số: 25</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Căn phòng $4\text{ m} \times 3\text{ m} \times 3\text{ m}$, cột nhô ra $0,4\text{ m} \times 0,2\text{ m}$ trên tường $(Oyz)$, bóng đèn $A\left(1; 0; \dfrac{5}{2}\right)$, công tắc $B\left(\dfrac{1}{2}; 4; 1\right)$.
  <div class="step">Trải phẳng các bức tường theo hành trình ngắn nhất từ $A$ trên tường $(Oxz)$ qua tường $(Oyz)$ đến $B$ trên tường $y = 4$:</div>
  <div class="step">- Đoạn ngang từ $A$ đến góc tường $O$: $d_1 = x_A = 1\text{ m}$.</div>
  <div class="step">- Đoạn ngang dọc theo tường $(Oyz)$ ôm quanh 3 mặt của cột nhô ra: Chiều rộng tường là $4\text{ m}$, cột nhô ra $0,2\text{ m}$ nên quãng đường tăng thêm $2 \times 0,2 = 0,4\text{ m} \implies d_2 = 4 + 0,4 = 4,4\text{ m}$.</div>
  <div class="step">- Đoạn ngang từ góc tường $(0; 4)$ đến $B$: $d_3 = x_B = 0,5\text{ m}$.</div>
  <div class="step">Tổng quãng đường theo phương ngang khi trải phẳng: $H = d_1 + d_2 + d_3 = 1 + 4,4 + 0,5 = 5,9\text{ m}$.</div>
  <div class="step">Độ chênh lệch độ cao: $\Delta z = \left|\dfrac{5}{2} - 1\right| = 1,5\text{ m}$.</div>
  <div class="step">Độ dài ngắn nhất của dây điện: $L_{\min} = \sqrt{H^2 + (\Delta z)^2} = \sqrt{5,9^2 + 1,5^2} = \sqrt{34,81 + 2,25} = \sqrt{37,06} \approx 6,08769\text{ m}$. Làm tròn đến hàng phần trăm: <b>6,09</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 6,09</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Khung sắt chứa ô tô nâng bằng 4 dây cáp bằng nhau nghiêng góc $\alpha$ với $(ABCD)$, lực căng mỗi dây $T = 4800\text{ N}$, trọng lượng tổng $P = 7200\sqrt{6}\text{ N}$.
  <div class="step">Thành phần lực căng kéo lên theo phương thẳng đứng của mỗi sợi cáp: $F_{z} = T \sin\alpha = 4800 \sin\alpha$.</div>
  <div class="step">Do tính đối xứng, các thành phần nằm ngang triệt tiêu từng đôi một, tổng hợp lực nâng theo phương thẳng đứng là: $F_{\text{nâng}} = 4 F_z = 4 \times 4800 \sin\alpha = 19200 \sin\alpha$.</div>
  <div class="step">Điều kiện cân bằng tĩnh học (hoặc kéo đều thẳng đứng): $F_{\text{nâng}} = P \iff 19200 \sin\alpha = 7200\sqrt{6} \implies \sin\alpha = \dfrac{7200\sqrt{6}}{19200} = \dfrac{3\sqrt{6}}{8} \approx 0,91855$. Làm tròn đến hàng phần trăm: <b>0,92</b>.</div>
  <span class="q-ans">&rArr; Đáp số: 0,92</span>
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

with open("dap_an_111.html", "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "Bang_Dap_An_Va_HDG_De_111.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "dap_an_111.html"
]

print("Running Chrome to generate Dap An 111 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
