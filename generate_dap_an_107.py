import os
import subprocess

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 107</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 12mm 15mm 15mm 15mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 107";
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
  margin-bottom: 10px;
  page-break-inside: avoid;
}
.q-title {
  font-weight: bold;
  color: #1a365d;
}

ul {
  margin-top: 3px;
  margin-bottom: 3px;
  padding-left: 20px;
}
li {
  margin-bottom: 3px;
}

.page-break {
  page-break-before: always;
}
</style>
</head>
<body>

<div class="header">
  <h2>KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</h2>
  <h3>BẢNG ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT – MÔN TOÁN 12</h3>
  <p><strong>Chuyên đề: Khảo sát hàm số & Ứng dụng đạo hàm — Mã đề thi: 107</strong></p>
</div>

<h2 class="sec-title">A. BẢNG ĐÁP ÁN TOÀN BỘ ĐỀ THI (MÃ ĐỀ 107)</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td><strong>Đ/A</strong></td>
    <td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">A</td><td class="bold-ans">B</td>
    <td class="bold-ans">C</td><td class="bold-ans">B</td><td class="bold-ans">D</td><td class="bold-ans">A</td>
    <td class="bold-ans">A</td><td class="bold-ans">A</td><td class="bold-ans">D</td><td class="bold-ans">B</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (4 câu – 4,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 35%;">Câu hỏi</th>
    <th style="width: 16%;">Lệnh a)</th>
    <th style="width: 16%;">Lệnh b)</th>
    <th style="width: 16%;">Lệnh c)</th>
    <th style="width: 16%;">Lệnh d)</th>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 1</strong> <i>(Hồ nước nhân tạo trong công viên)</i></td>
    <td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 2</strong> <i>(Hàm số $y = \frac{-x^2-3x+4}{x-3}$)</i></td>
    <td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 3</strong> <i>(Hàm số $y = \frac{x+2}{x-2}$)</i></td>
    <td style="color:#2b6cb0; font-weight:bold;">SAI</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 4</strong> <i>(Bài toán cho thuê 100 căn hộ)</i></td>
    <td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th>
  </tr>
  <tr>
    <td><strong>Đáp số</strong></td>
    <td class="bold-ans">7,2</td>
    <td class="bold-ans">164</td>
    <td class="bold-ans">3</td>
    <td class="bold-ans">900</td>
    <td class="bold-ans">80</td>
    <td class="bold-ans">125,7</td>
  </tr>
</table>

<div class="page-break"></div>

<h2 class="sec-title">B. HƯỚNG DẪN GIẢI CHI TIẾT</h2>

<h3 class="sub-title">PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN</h3>

<div class="q-block">
  <span class="q-title">Câu 1:</span> Quan sát bảng biến thiên, trên khoảng $(-1; 2)$ đạo hàm $f'(x) < 0$ và mũi tên chiều biến thiên đi xuống. Do đó hàm số nghịch biến trên $(-1; 2)$. $\implies$ <strong>Chọn A.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 2:</span> Ta có $f'(x) = x(x - 1)^2(x + 2)^3 = 0 \Leftrightarrow x \in \{0; 1; -2\}$. Nghiệm $x = 1$ là nghiệm bội 2 (bội chẵn) nên đạo hàm không đổi dấu khi qua $x = 1$. Hai nghiệm $x = 0$ (bội 1) và $x = -2$ (bội 3) là các nghiệm bội lẻ nên $f'(x)$ đổi dấu qua hai điểm này. Vậy hàm số có đúng 2 điểm cực trị. $\implies$ <strong>Chọn B.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 3:</span> Áp dụng công thức đạo hàm hàm phân thức bậc nhất: $\left(\frac{ax + b}{cx + d}\right)' = \frac{ad - bc}{(cx + d)^2}$. Với $y = \frac{2x - 1}{x + 1} \implies y' = \frac{2(1) - (-1)(1)}{(x + 1)^2} = \frac{3}{(x + 1)^2}$. $\implies$ <strong>Chọn A.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 4:</span> Rút gọn hàm số với $x \ne -2$: $y = \frac{x + 2}{x^2 - 4} = \frac{x + 2}{(x - 2)(x + 2)} = \frac{1}{x - 2}$.<br>
  - Tiệm cận đứng: $\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty \implies x = 2$ là đường tiệm cận đứng (tại $x = -2$ giới hạn hữu hạn bằng $-\frac{1}{4}$ nên không là TCĐ).<br>
  - Tiệm cận ngang: $\lim_{x \to \pm\infty} y = 0 \implies y = 0$ là đường tiệm cận ngang.<br>
  Vậy đồ thị có đúng 2 đường tiệm cận. $\implies$ <strong>Chọn B.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 5:</span> Nhánh bên phải của đồ thị hướng lên nên hệ số bậc cao nhất $a > 0$. Đồ thị đi qua gốc toạ độ $O(0; 0)$ nên loại B và D. Đồ thị có 2 điểm cực trị đối xứng qua gốc toạ độ: cực đại $(-1; 2)$ và cực tiểu $(1; -2)$. Hàm số thỏa mãn là $y = x^3 - 3x$. $\implies$ <strong>Chọn C.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 6:</span> Chia đa thức: $y = \frac{x^2 - 3x + 5}{x - 1} = x - 2 + \frac{3}{x - 1}$. Vì $\lim_{x \to \pm\infty} \frac{3}{x - 1} = 0$ nên tiệm cận xiên của đồ thị là đường thẳng $y = x - 2$. $\implies$ <strong>Chọn B.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 7:</span> Tiệm cận đứng: $x = -1$, tiệm cận ngang: $y = 3$. Tâm đối xứng của đồ thị là giao điểm hai đường tiệm cận $I(-1; 3)$. $\implies$ <strong>Chọn D.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 8:</span> $f'(x) = 3x^2 - 3 = 0 \Leftrightarrow x = \pm 1$. Xét trên đoạn $[0; 2]$, ta nhận điểm $x = 1$. Tính các giá trị: $f(0) = 5$; $f(1) = 3$; $f(2) = 7$. Do đó $\min_{[0; 2]} f(x) = 3$ (tại $x = 1$). $\implies$ <strong>Chọn A.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 9:</span> TXĐ: $D = [-2; 2]$. Đạo hàm: $y' = \frac{-x}{\sqrt{4 - x^2}} < 0 \Leftrightarrow x > 0$. Kết hợp TXĐ suy ra hàm số nghịch biến trên khoảng $(0; 2)$. $\implies$ <strong>Chọn A.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 10:</span> TXĐ: $D = \mathbb{R} \setminus \{m\}$. Đạo hàm: $y' = \frac{-m + 3}{(x - m)^2}$. Hàm số đồng biến trên $(0; +\infty) \Leftrightarrow y' > 0, \forall x \in (0; +\infty)$ và $m \notin (0; +\infty) \Leftrightarrow -m + 3 > 0$ và $m \le 0 \Leftrightarrow m \le 0$. Vì $m \in [-5; 5], m \in \mathbb{Z} \implies m \in \{-5; -4; -3; -2; -1; 0\}$ (gồm 6 giá trị). $\implies$ <strong>Chọn A.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 11:</span> Dựa vào BBT, $f'(x)$ đổi dấu từ dương sang âm khi qua $x = 0$, hàm số đạt cực đại tại $x = 0$ (giá trị cực đại $y_{\text{CĐ}} = 3$). Điểm cực đại của hàm số là $x = 0$. $\implies$ <strong>Chọn D.</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 12:</span> $f'(x) = x^2(x - 1)(x - 2)^3$. Ta thấy $x = 0$ là nghiệm bội chẵn. Xét dấu $f'(x)$ qua $x = 1$ và $x = 2$: qua $x = 1$, $f'(x)$ đổi dấu từ $+$ sang $-$ nên $x = 1$ là điểm cực đại; qua $x = 2$, $f'(x)$ đổi dấu từ $-$ sang $+$ nên $x = 2$ là điểm cực tiểu. Vậy hàm số có đúng 1 điểm cực đại. $\implies$ <strong>Chọn B.</strong>
</div>

<h3 class="sub-title">PHẦN II. TRẮC NGHIỆM ĐÚNG / SAI</h3>

<div class="q-block">
  <span class="q-title">Câu 1 (Hồ nước nhân tạo trong công viên):</span>
  <ul>
    <li><strong>a) ĐÚNG:</strong> Trên trục hoành $Ox$, hồ nước giới hạn từ $x = 0$ đến $x = 8$. Mỗi đơn vị đo trên hệ trục toạ độ là $100\text{ m}$. Chiều dài đường đi dạo ven hồ trên thực tế là $8 \times 100\text{ m} = 800\text{ m}$.</li>
    <li><strong>b) SAI:</strong> Khoảng cách theo phương thẳng đứng từ điểm $(x; 0)$ trên trục $Ox$ đến bờ hồ đối diện là $y = f(x)$. Đạo hàm: $f'(x) = -\frac{3}{10}(x - 1)(x - 5)$. Với mọi $x \in (0; 1)$, ta có $(x - 1)(x - 5) > 0 \implies f'(x) < 0$, nên hàm số nghịch biến trên $[0; 1]$. Khoảng cách theo phương thẳng đứng giảm dần từ $560\text{ m}$ (tại $x = 0$) xuống $490\text{ m}$ (tại $x = 1$), chứ không phải tăng dần.</li>
    <li><strong>c) SAI:</strong> Xét $f(x)$ trên $[0; 8]$. Đạo hàm $f'(x) = 0 \Leftrightarrow x = 1$ hoặc $x = 5$. Tính các giá trị: $f(0) = 5,6 \implies 560\text{ m}$; $f(1) = 4,9 \implies 490\text{ m}$; $f(5) = 8,1 \implies 810\text{ m}$; $f(8) = 0 \implies 0\text{ m}$. Khoảng cách lớn nhất bằng $810\text{ m}$ (tại $x = 5$), không phải $800\text{ m}$.</li>
    <li><strong>d) ĐÚNG:</strong> Đường thẳng $d: x + y - 15 = 0$. Khoảng cách từ $M(x; f(x))$ đến $d$ là $d(M, d) = \frac{15 - x - f(x)}{\sqrt{2}}$. Đặt $g(x) = x + f(x) - 15$. Ta có $g'(x) = 1 + f'(x) = \frac{-3x^2 + 18x - 5}{10} = 0$. Điểm cực đại của $g(x)$ trên $(0; 8)$ là $x_0 = \frac{9 + \sqrt{66}}{3} \approx 5,708$. Tại điểm này, $g(x_0) \approx -1,528 \implies d_{\min} \approx 1,0806\text{ đơn vị toạ độ} \approx 108,06\text{ m} > 90\text{ m}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2 ($y = \frac{-x^2 - 3x + 4}{x - 3}$):</span>
  <ul>
    <li><strong>a) ĐÚNG:</strong> ĐKXĐ: $x - 3 \ne 0 \Leftrightarrow x \ne 3 \implies D = \mathbb{R} \setminus \{3\}$.</li>
    <li><strong>b) ĐÚNG:</strong> Thực hiện phép chia: $\frac{-x^2 - 3x + 4}{x - 3} = -x - 6 - \frac{14}{x - 3} \implies$ TCX là $y = -x - 6$.</li>
    <li><strong>c) SAI:</strong> $y' = \frac{(-2x - 3)(x - 3) - (-x^2 - 3x + 4)}{(x - 3)^2} = \frac{-x^2 + 6x + 5}{(x - 3)^2} = 0 \Leftrightarrow x = 3 \pm \sqrt{14}$. Do $3 + \sqrt{14} \approx 6,74 < 7$, trên khoảng $(3 + \sqrt{14}; 7)$ có $y' < 0$ (hàm số nghịch biến) nên không đồng biến trên toàn khoảng $(3; 7)$.</li>
    <li><strong>d) ĐÚNG:</strong> Tích hai nghiệm của phương trình hoành độ cực trị là $x_1 x_2 = -5 < 0$, suy ra hai điểm cực trị nằm về 2 phía so với trục tung $Oy$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3 ($y = \frac{x + 2}{x - 2}$):</span>
  <ul>
    <li><strong>a) SAI:</strong> Tiệm cận ngang của đồ thị là $y = 1$, mệnh đề ghi $y = 2$ là sai.</li>
    <li><strong>b) SAI:</strong> Tâm đối xứng là giao điểm hai tiệm cận $x = 2$ và $y = 1$, tức $I(2; 1)$, mệnh đề ghi $I(1; 1)$ là sai.</li>
    <li><strong>c) ĐÚNG:</strong> PTHĐGĐ: $\frac{x + 2}{x - 2} = x - 1 \Leftrightarrow x + 2 = x^2 - 3x + 2 \Leftrightarrow x^2 - 4x = 0 \Leftrightarrow x = 0$ hoặc $x = 4$ (cả hai đều khác 2) $\implies$ cắt tại 2 điểm phân biệt.</li>
    <li><strong>d) ĐÚNG:</strong> Với $M\left(x_0; 1 + \frac{4}{x_0 - 2}\right)$, tổng khoảng cách đến hai đường tiệm cận là $d = |x_0 - 2| + \frac{4}{|x_0 - 2|} \ge 2\sqrt{4} = 4$. Dấu bằng đạt được khi $|x_0 - 2| = 2$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4 (Bài toán thực tế 100 căn hộ cho thuê):</span>
  <ul>
    <li><strong>a) ĐÚNG:</strong> Giá thuê 5 triệu là tăng 2 triệu $= 20$ lần tăng 100.000 đồng $\implies$ số căn trống là $20 \times 2 = 40$ căn.</li>
    <li><strong>b) SAI:</strong> Với giá thuê $p$ (triệu đồng), số lần tăng giá là $\frac{p - 3}{0,1} = 10(p - 3)$. Số căn hộ được thuê là $x = 100 - 2 \cdot 10(p - 3) = 160 - 20p \implies p = -\frac{1}{20}x + 8$ (mệnh đề ghi $+ 9$ là sai).</li>
    <li><strong>c) SAI:</strong> Doanh thu $R(p) = p \cdot x = p(160 - 20p) = -20p^2 + 160p$ (mệnh đề ghi $140p$ là sai).</li>
    <li><strong>d) ĐÚNG:</strong> $R(p) = -20(p - 4)^2 + 320 \le 320$ triệu đồng khi đặt giá $p = 4$ triệu đồng/tháng.</li>
  </ul>
</div>

<div class="page-break"></div>

<h3 class="sub-title">PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN</h3>

<div class="q-block">
  <span class="q-title">Câu 1 (Đường đi của khinh khí cầu):</span><br>
  Quỹ đạo khinh khí cầu là hàm phân thức bậc hai trên bậc nhất cắt trục hoành tại $(1; 0)$ và $(8; 0)$ nên có dạng:<br>
  $$y = \frac{A(x - 1)(x - 8)}{x - x_0} = \frac{A(x^2 - 9x + 8)}{x - x_0}$$
  - Đồ thị đạt cực đại tại điểm $(6; 5) \implies y(6) = 5 \Leftrightarrow \frac{-10A}{6 - x_0} = 5 \Leftrightarrow 6 - x_0 = -2A$.<br>
  - Đạo hàm tại điểm cực trị bằng $0$: $y'(6) = 0 \Leftrightarrow 3(6 - x_0) - (-10) = 0 \Leftrightarrow 6 - x_0 = -\frac{10}{3}$.<br>
  Suy ra: $-2A = -\frac{10}{3} \implies A = \frac{5}{3}$ và $x_0 = 6 + \frac{10}{3} = \frac{28}{3}$.<br>
  Phương trình quỹ đạo là: $y = \frac{5(x^2 - 9x + 8)}{3x - 28}$.<br>
  - Khi khí cầu cách mặt đất $3875\text{ m} = 3,875\text{ km} = \frac{31}{8}\text{ km}$, ta giải phương trình:<br>
  $$\frac{5(x^2 - 9x + 8)}{3x - 28} = \frac{31}{8} \Leftrightarrow 40x^2 - 453x + 1188 = 0$$
  Phương trình có biệt thức $\Delta = 15129 = 123^2$, cho hai nghiệm: $x_1 = 4,125\text{ km}$ và $x_2 = 7,2\text{ km}$.<br>
  Vì thời điểm xét là sau khi khinh khí cầu đã đi qua điểm cực đại ($x > 6$), ta chọn nghiệm $x = 7,2\text{ km}$.<br>
  Vậy khinh khí cầu cách gốc toạ độ theo phương ngang là $7,2\text{ km}$.<br>
  $\implies$ <strong>Đáp số: 7,2</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 2 (Lát cắt địa hình Đồi và Hồ):</span><br>
  Mặt cắt là hàm bậc ba $f(x)$ đi qua gốc toạ độ $O(0; 0)$, chân đồi $A(2; 0)$ và bờ hồ $B(3; 0)$, nên có phương trình:<br>
  $$f(x) = k \cdot x(x - 2)(x - 3) = k(x^3 - 5x^2 + 6x)\quad (k > 0)$$
  Đạo hàm: $f'(x) = k(3x^2 - 10x + 6) = 0 \Leftrightarrow x_1 = \frac{5 - \sqrt{7}}{3}$ (đỉnh đồi), $x_2 = \frac{5 + \sqrt{7}}{3}$ (đáy hồ).<br>
  Chia đa thức $x^3 - 5x^2 + 6x$ cho $3x^2 - 10x + 6$, ta được phần dư là $\frac{2}{9}(15 - 7x)$. Do đó giá trị tại cực trị là $f(x) = \frac{2k}{9}(15 - 7x)$.<br>
  - Chiều cao đỉnh đồi: $h_{\text{đồi}} = f(x_1) = \frac{2k}{27}(10 + 7\sqrt{7}) = 550\text{ m}$.<br>
  - Độ sâu đáy hồ: $h_{\text{hồ}} = -f(x_2) = \frac{2k}{27}(7\sqrt{7} - 10)$.<br>
  Lập tỉ số:
  $$\frac{h_{\text{hồ}}}{h_{\text{đồi}}} = \frac{7\sqrt{7} - 10}{7\sqrt{7} + 10} \implies h_{\text{hồ}} = 550 \times \frac{7\sqrt{7} - 10}{7\sqrt{7} + 10} \approx 164,309\text{ m}$$
  Làm tròn đến hàng đơn vị theo yêu cầu: <strong>164</strong>.<br>
  $\implies$ <strong>Đáp số: 164</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 3 (Tham số $m$ để hàm phân thức đồng biến):</span><br>
  Xét hàm số $f(x) = \frac{x^2 + 3x + m - 1}{x + 2}$. TXĐ: $D = \mathbb{R} \setminus \{-2\}$.<br>
  $$f'(x) = \frac{(2x + 3)(x + 2) - (x^2 + 3x + m - 1)}{(x + 2)^2} = \frac{x^2 + 4x + 7 - m}{(x + 2)^2}$$
  Hàm số đồng biến trên từng khoảng xác định $\Leftrightarrow f'(x) \ge 0, \forall x \ne -2$ (và bằng 0 tại hữu hạn điểm):<br>
  $$\Leftrightarrow x^2 + 4x + 7 - m \ge 0, \forall x \in \mathbb{R} \Leftrightarrow \Delta' = 2^2 - (7 - m) = m - 3 \le 0 \Leftrightarrow m \le 3$$
  Vì $m$ là số nguyên dương ($m \in \mathbb{Z}^+$) nên $m \in \{1; 2; 3\}$ (gồm đúng 3 giá trị).<br>
  $\implies$ <strong>Đáp số: 3</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 4 (Tối ưu trang sách giáo khoa Toán):</span><br>
  Đổi đơn vị: Diện tích trang sách $S = 491,04\text{ cm}^2 = 49104\text{ mm}^2$.<br>
  Gọi chiều rộng trang sách là $x$ (mm), chiều cao là $y$ (mm) với $x > 31, y > 44$. Khi đó $y = \frac{49104}{x}$.<br>
  Tổng lề trái và lề phải: $15 + 16 = 31\text{ mm}$. Tổng lề trên và lề dưới: $22 + 22 = 44\text{ mm}$.<br>
  Diện tích phần trình bày là:
  $$S_{\text{tb}} = (x - 31)(y - 44) = (x - 31)\left(\frac{49104}{x} - 44\right) = 49104 + 1364 - \left(44x + \frac{31 \times 49104}{x}\right) = 50468 - \left(44x + \frac{1522224}{x}\right)$$
  Để $S_{\text{tb}}$ lớn nhất thì biểu thức $\left(44x + \frac{1522224}{x}\right)$ nhỏ nhất. Áp dụng BĐT AM-GM cho hai số dương:
  $$44x + \frac{1522224}{x} \ge 2\sqrt{44 \times 1522224} = 2 \times 8184 = 16368$$
  Dấu đẳng thức xảy ra khi:
  $$44x = \frac{1522224}{x} \Leftrightarrow x^2 = \frac{1522224}{44} = 34596 \implies x = \sqrt{34596} = 186\text{ mm}$$
  Suy ra chiều cao: $y = \frac{49104}{186} = 264\text{ mm}$.<br>
  Chu vi trang sách: $P = 2(x + y) = 2(186 + 264) = 2 \times 450 = 900\text{ mm}$.<br>
  $\implies$ <strong>Đáp số: 900</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 5 (Mô hình quần thể tảo):</span><br>
  Hàm số $P(t) = \frac{a}{b + e^{-0,6t}}$.<br>
  Theo giả thiết:
  $$P(0) = \frac{a}{b + 1} = 40 \implies a = 40(b + 1)$$
  Đạo hàm: $P'(t) = \frac{-a \cdot (-0,6 e^{-0,6t})}{(b + e^{-0,6t})^2} = \frac{0,6a e^{-0,6t}}{(b + e^{-0,6t})^2}$.<br>
  Tại $t = 0$:
  $$P'(0) = \frac{0,6a}{(b + 1)^2} = 12 \implies \frac{0,6 \cdot 40(b + 1)}{(b + 1)^2} = \frac{24}{b + 1} = 12 \implies b + 1 = 2 \implies b = 1, a = 80$$
  Khi thời gian nuôi kéo dài ($t \to +\infty$), ta có $\lim_{t \to +\infty} e^{-0,6t} = 0$, do đó:
  $$\lim_{t \to +\infty} P(t) = \frac{80}{1 + 0} = 80\text{ (nghìn cá thể)}$$
  Vậy số lượng cá thể tảo trong bể sẽ không vượt quá 80 nghìn cá thể.<br>
  $\implies$ <strong>Đáp số: 80</strong>
</div>

<div class="q-block">
  <span class="q-title">Câu 6 (Tốc độ tăng diện tích gợn sóng hình tròn):</span><br>
  Diện tích hình tròn tạo bởi gợn sóng ngoài cùng theo bán kính $r$ là $S = \pi r^2$.<br>
  Lấy đạo hàm hai vế theo thời gian $t$:
  $$\frac{dS}{dt} = \frac{d}{dt}(\pi r^2) = 2\pi r \cdot \frac{dr}{dt}$$
  Theo đề bài, tốc độ tăng bán kính $\frac{dr}{dt} = 2\text{ cm/s}$.<br>
  Tại thời điểm bán kính $r = 10\text{ cm}$, tốc độ tăng diện tích hình tròn là:
  $$\frac{dS}{dt} = 2\pi \cdot 10 \cdot 2 = 40\pi \approx 125,6637\dots\text{ cm}^2/\text{s}$$
  Làm tròn đến 1 chữ số thập phân: <strong>125,7</strong>.<br>
  $\implies$ <strong>Đáp số: 125,7</strong>
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

with open("dap_an_107.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved dap_an_107.html. Running Chrome...")
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=5000",
    "--print-to-pdf=Bang_Dap_An_Va_HDG_De_107.pdf",
    "dap_an_107.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)
