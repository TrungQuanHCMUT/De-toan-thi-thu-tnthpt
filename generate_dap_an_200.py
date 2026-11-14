import subprocess
import pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã đề 200</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4 portrait;
  margin: 8mm 12mm 8mm 12mm;
}
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 9.6pt;
  line-height: 1.28;
  color: #1a202c;
  margin: 0;
  padding: 0;
}
.katex { font-size: 1.01em; }
.katex-display { margin: 2px 0; }
.header {
  text-align: center;
  border-bottom: 2px solid #2b6cb0;
  padding-bottom: 5px;
  margin-bottom: 7px;
}
.title-main {
  font-size: 13pt;
  font-weight: bold;
  color: #1a365d;
  text-transform: uppercase;
  margin-bottom: 2px;
}
.title-sub {
  font-size: 10.4pt;
  font-weight: bold;
  color: #2b6cb0;
  margin-bottom: 2px;
}
.title-meta {
  font-size: 9.4pt;
  font-style: italic;
  color: #4a5568;
}
.sec-title {
  font-size: 10.8pt;
  font-weight: bold;
  color: #2b6cb0;
  text-transform: uppercase;
  margin-top: 7px;
  margin-bottom: 4px;
  border-left: 4px solid #2b6cb0;
  padding-left: 7px;
}
.sub-title {
  font-size: 9.8pt;
  font-weight: bold;
  color: #2d3748;
  margin-top: 5px;
  margin-bottom: 3px;
}
.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 6px;
  font-size: 9.3pt;
  text-align: center;
}
.ans-table th {
  background-color: #edf2f7;
  color: #2d3748;
  font-weight: bold;
  border: 1px solid #cbd5e0;
  padding: 3px 4px;
}
.ans-table td {
  border: 1px solid #cbd5e0;
  padding: 3px 4px;
}
.bold-ans {
  font-weight: bold;
  color: #c53030;
}
.q-block {
  margin-bottom: 5.5px;
  text-align: justify;
  background-color: #f7fafc;
  padding: 4px 8px;
  border-radius: 4px;
  border-left: 3px solid #cbd5e0;
}
.q-title {
  font-weight: bold;
  color: #2b6cb0;
}
.q-ans {
  font-weight: bold;
  color: #c53030;
}
.solution-list {
  margin: 2px 0 0 0;
  padding-left: 16px;
}
.solution-list li {
  margin-bottom: 2px;
}
</style>
</head>
<body>

<!-- ==================== PAGE 1 ==================== -->
<div class="header">
  <div class="title-main">BẢNG ĐÁP ÁN &amp; HƯỚNG DẪN GIẢI CHI TIẾT</div>
  <div class="title-sub">ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA – MÔN TOÁN (MÃ ĐỀ 200)</div>
  <div class="title-meta">Chương trình GDPT 2018 (Toán lớp 10, 11, 12) – Thời gian làm bài: 90 phút &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</div>
</div>

<div class="sec-title">A. BẢNG ĐÁP ÁN</div>

<div class="sub-title">PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (3,0 điểm)</div>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <th>Đáp án</th>
    <td class="bold-ans">A</td><td class="bold-ans">C</td><td class="bold-ans">B</td><td class="bold-ans">D</td>
    <td class="bold-ans">C</td><td class="bold-ans">A</td><td class="bold-ans">D</td><td class="bold-ans">B</td>
    <td class="bold-ans">C</td><td class="bold-ans">A</td><td class="bold-ans">D</td><td class="bold-ans">B</td>
  </tr>
</table>

<div class="sub-title">PHẦN II. Trắc nghiệm đúng sai (4,0 điểm)</div>
<table class="ans-table">
  <tr>
    <th style="width: 14%;">Câu</th><th style="width: 21.5%;">Ý a)</th><th style="width: 21.5%;">Ý b)</th><th style="width: 21.5%;">Ý c)</th><th style="width: 21.5%;">Ý d)</th>
  </tr>
  <tr>
    <th>Câu 1</th>
    <td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#c53030;">Sai</td><td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#276749;">Đúng</td>
  </tr>
  <tr>
    <th>Câu 2</th>
    <td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#c53030;">Sai</td><td style="font-weight:bold; color:#276749;">Đúng</td>
  </tr>
  <tr>
    <th>Câu 3</th>
    <td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#c53030;">Sai</td><td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#c53030;">Sai</td>
  </tr>
  <tr>
    <th>Câu 4</th>
    <td style="font-weight:bold; color:#c53030;">Sai</td><td style="font-weight:bold; color:#276749;">Đúng</td><td style="font-weight:bold; color:#c53030;">Sai</td><td style="font-weight:bold; color:#276749;">Đúng</td>
  </tr>
</table>

<div class="sub-title">PHẦN III. Trắc nghiệm trả lời ngắn (3,0 điểm)</div>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th>
  </tr>
  <tr>
    <th>Đáp án</th>
    <td class="bold-ans">96,5</td><td class="bold-ans">15,6</td><td class="bold-ans">111</td><td class="bold-ans">7</td><td class="bold-ans">0,55</td><td class="bold-ans">56,5</td>
  </tr>
</table>

<div class="sec-title">B. HƯỚNG DẪN GIẢI CHI TIẾT</div>
<div class="sub-title">PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN</div>

<div class="q-block">
  <span class="q-title">Câu 1.</span> <span class="q-ans">Chọn A.</span><br>
  Ta có $y = \dfrac{2x^2 - 5x + 1}{x - 1} = 2x - 3 - \dfrac{2}{x - 1}$. Vì $\lim\limits_{x \to \pm\infty} [y - (2x - 3)] = 0$ nên đường tiệm cận xiên là $\Delta: y = 2x - 3$.<br>
  Giao điểm của $\Delta$ với $Ox$ là $A\left(\dfrac{3}{2}; 0\right)$, với $Oy$ là $B(0; -3)$. Diện tích $\triangle OAB$ bằng $S = \dfrac{1}{2}\cdot OA\cdot OB = \dfrac{1}{2}\cdot\dfrac{3}{2}\cdot 3 = \dfrac{9}{4}$.
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> <span class="q-ans">Chọn C.</span><br>
  Hàm số $f(x) = x - 2\ln x$ liên tục trên $[1; e]$ và có đạo hàm $f'(x) = 1 - \dfrac{2}{x} = 0 \Leftrightarrow x = 2 \in [1; e]$.<br>
  Ta có $f(1) = 1$, $f(2) = 2 - 2\ln 2 \approx 0,614$, $f(e) = e - 2 \approx 0,718$. Vậy $\min\limits_{[1; e]} f(x) = 2 - 2\ln 2$.
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> <span class="q-ans">Chọn B.</span><br>
  Áp dụng đạo hàm của thương và công thức $(e^{2x})' = 2e^{2x}$:<br>
  $y' = \dfrac{(e^{2x})'(x + 1) - e^{2x}(x + 1)'}{(x + 1)^2} = \dfrac{2e^{2x}(x + 1) - e^{2x}}{(x + 1)^2} = \dfrac{(2x + 1)e^{2x}}{(x + 1)^2}$.
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> <span class="q-ans">Chọn D.</span><br>
  Theo định lí côsin: $BC = \sqrt{5^2 + 8^2 - 2\cdot 5\cdot 8\cdot \cos 60^\circ} = \sqrt{25 + 64 - 40} = 7$.<br>
  Theo định lí sin, bán kính đường tròn ngoại tiếp $\triangle ABC$ là $R = \dfrac{BC}{2\sin 60^\circ} = \dfrac{7}{2\cdot \dfrac{\sqrt{3}}{2}} = \dfrac{7\sqrt{3}}{3}$.
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> <span class="q-ans">Chọn C.</span><br>
  $\sin\left(2x - \dfrac{\pi}{3}\right) = \dfrac{1}{2} \Leftrightarrow \left[\begin{array}{l} 2x - \dfrac{\pi}{3} = \dfrac{\pi}{6} + k2\pi \\ 2x - \dfrac{\pi}{3} = \dfrac{5\pi}{6} + k2\pi \end{array}\right. \Leftrightarrow \left[\begin{array}{l} x = \dfrac{\pi}{4} + k\pi \\ x = \dfrac{7\pi}{12} + k\pi \end{array}\right.$ ($k \in \mathbb{Z}$).<br>
  Trên $[0; \pi]$, phương trình có $2$ nghiệm là $x_1 = \dfrac{\pi}{4}$ và $x_2 = \dfrac{7\pi}{12}$. Tổng các nghiệm là $\dfrac{\pi}{4} + \dfrac{7\pi}{12} = \dfrac{5\pi}{6}$.
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> <span class="q-ans">Chọn A.</span><br>
  Ta có $u_3 + u_4 = q^2(u_1 + u_2) \Rightarrow q^2 = \dfrac{48}{12} = 4$. Vì các số hạng đều dương nên $q = 2$.<br>
  Từ $u_1(1 + 2) = 12 \Rightarrow u_1 = 4$. Vậy $u_5 = u_1 q^4 = 4\cdot 2^4 = 64$.
</div>

<div class="q-block">
  <span class="q-title">Câu 7.</span> <span class="q-ans">Chọn D.</span><br>
  Điều kiện: $x^2 - 3x + 2 > 0 \Leftrightarrow x < 1$ hoặc $x > 2$. Vì $0 < 0,5 < 1$ nên bất phương trình tương đương:<br>
  $x^2 - 3x + 2 \le (0,5)^{-1} = 2 \Leftrightarrow x^2 - 3x \le 0 \Leftrightarrow 0 \le x \le 3$. Tập nghiệm là $[0; 1) \cup (2; 3]$, có $2$ nghiệm nguyên là $x \in \{0; 3\}$.
</div>

<!-- ==================== PAGE 2 ==================== -->
<div style="page-break-before: always;"></div>

<div class="q-block">
  <span class="q-title">Câu 8.</span> <span class="q-ans">Chọn B.</span><br>
  Diện tích đáy lớn $B_1 = 4^2 = 16\text{ m}^2$, đáy nhỏ $B_2 = 2^2 = 4\text{ m}^2$, chiều cao $h = 3\text{ m}$.<br>
  Thể tích khối chóp cụt đều là $V = \dfrac{h}{3}\left(B_1 + B_2 + \sqrt{B_1 B_2}\right) = \dfrac{3}{3}\left(16 + 4 + \sqrt{16\cdot 4}\right) = 28\text{ m}^3$.
</div>

<div class="q-block">
  <span class="q-title">Câu 9.</span> <span class="q-ans">Chọn C.</span><br>
  Tách cận tích phân tại $x = 1$: $I = \int_0^1 3x^2\,\mathrm{d}x + \int_1^2 (2x + 1)\,\mathrm{d}x = \left.x^3\right|_0^1 + \left.(x^2 + x)\right|_1^2 = 1 + (6 - 2) = 5$.
</div>

<div class="q-block">
  <span class="q-title">Câu 10.</span> <span class="q-ans">Chọn A.</span><br>
  Diện tích thiết diện tam giác đều cạnh $\sqrt{x^2 + 1}$ là $S(x) = \dfrac{(\sqrt{x^2 + 1})^2\sqrt{3}}{4} = \dfrac{\sqrt{3}}{4}(x^2 + 1)$.<br>
  Thể tích vật thể là $V = \int_0^2 S(x)\,\mathrm{d}x = \dfrac{\sqrt{3}}{4}\left(\dfrac{x^3}{3} + x\right)\Bigg|_0^2 = \dfrac{\sqrt{3}}{4}\left(\dfrac{8}{3} + 2\right) = \dfrac{7\sqrt{3}}{6}$.
</div>

<div class="q-block">
  <span class="q-title">Câu 11.</span> <span class="q-ans">Chọn D.</span><br>
  Cỡ mẫu $n = 40$; tần số tích lũy các nhóm lần lượt là $4; 14; 28; 36; 40$.
  <div style="margin: 3px 0;">• $\dfrac{n}{4} = 10 \Rightarrow Q_1 \in [13; 14)$, suy ra $Q_1 = 13 + \dfrac{10 - 4}{10}\cdot 1 = 13,6$.</div>
  <div style="margin: 3px 0;">• $\dfrac{3n}{4} = 30 \Rightarrow Q_3 \in [15; 16)$, suy ra $Q_3 = 15 + \dfrac{30 - 28}{8}\cdot 1 = 15,25$.</div>
  Khoảng tứ phân vị $\Delta_Q = Q_3 - Q_1 = 15,25 - 13,6 = 1,65$.
</div>

<div class="q-block">
  <span class="q-title">Câu 12.</span> <span class="q-ans">Chọn B.</span><br>
  Mặt cầu $(S)$ có tâm $I(1; -1; 1)$, bán kính $R = 3$. Vì $IA = \sqrt{5} < 3$ nên $A$ nằm trong $(S)$.<br>
  Đường tròn giao tuyến có bán kính $r = \sqrt{R^2 - d^2(I, (P))}$ nhỏ nhất khi $d(I, (P))$ lớn nhất, tức là $(P) \perp IA$.<br>
  Vậy một vectơ pháp tuyến của $(P)$ là $\vec{n} = \overrightarrow{IA} = (1; 0; 2)$.
</div>

<div class="sub-title" style="margin-top: 8px;">PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI</div>

<div class="q-block">
  <span class="q-title">Câu 1.</span> <span class="q-ans">Đáp án: a) Đúng – b) Sai – c) Đúng – d) Đúng.</span><br>
  Tập xác định $D = \mathbb{R} \setminus \{2\}$. Ta có $f(x) = x - 1 + \dfrac{4}{x - 2} \Rightarrow f'(x) = 1 - \dfrac{4}{(x - 2)^2} = \dfrac{x(x - 4)}{(x - 2)^2} = 0 \Leftrightarrow x \in \{0; 4\}$.
  <ul class="solution-list">
    <li><strong>a) Đúng:</strong> Với $x \in (0; 2)$ và $x \in (2; 4)$ thì $f'(x) < 0$, nên hàm số nghịch biến trên các khoảng $(0; 2)$ và $(2; 4)$.</li>
    <li><strong>b) Sai:</strong> Theo bảng biến thiên, $y_{\text{CĐ}} = f(0) = -3$ và $y_{\text{CT}} = f(4) = 5$. Vì $-3 < 5$ nên giá trị cực đại nhỏ hơn giá trị cực tiểu.</li>
    <li><strong>c) Đúng:</strong> Giao điểm tiệm cận đứng $x = 2$ và tiệm cận xiên $y = x - 1$ là tâm đối xứng $I(2; 1)$ của $(C)$. Hai điểm cực trị là $A(0; -3)$ và $B(4; 5)$ có khoảng cách $AB = \sqrt{4^2 + 8^2} = 4\sqrt{5}$.</li>
    <li><strong>d) Đúng:</strong> Phương trình $\dfrac{x^2 - 3x + 6}{x - 2} = m \Leftrightarrow x^2 - (m + 3)x + (2m + 6) = 0$ ($x = 2$ không phải nghiệm vì $4 \ne 0$). Đường thẳng $y = m$ không cắt $(C) \Leftrightarrow \Delta = m^2 - 2m - 15 < 0 \Leftrightarrow -3 < m < 5$. Các số nguyên thỏa mãn là $\{-2; -1; 0; 1; 2; 3; 4\}$ (đúng $7$ giá trị).</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> <span class="q-ans">Đáp án: a) Đúng – b) Đúng – c) Sai – d) Đúng.</span>
  <ul class="solution-list">
    <li><strong>a) Đúng:</strong> $E_{\text{phát}} = \int_0^{12}\left(-\dfrac{1}{4}t^2 + 3t\right)\mathrm{d}t = \left.\left(-\dfrac{t^3}{12} + \dfrac{3t^2}{2}\right)\right|_0^{12} = -144 + 216 = 72\text{ kWh}$.</li>
    <li><strong>b) Đúng:</strong> Giao điểm: $-\dfrac{1}{4}t^2 + 3t = 0,5t + 4 \Leftrightarrow t^2 - 10t + 16 = 0 \Leftrightarrow t = 2$ hoặc $t = 8$.<br>
      Lượng điện dư là $E_{\text{dư}} = \int_2^8\left(-\dfrac{1}{4}t^2 + \dfrac{5}{2}t - 4\right)\mathrm{d}t = \dfrac{1}{4}\cdot\dfrac{(8-2)^3}{6} = 9\text{ kWh}$.</li>
    <li><strong>c) Sai:</strong> $\Delta P(t) = P_{\text{phát}}(t) - P_{\text{tiêu}}(t) = -\dfrac{1}{4}t^2 + \dfrac{5}{2}t - 4 = -\dfrac{1}{4}(t - 5)^2 + 2,25$, đạt cực đại $2,25\text{ kW}$ tại $t = 5\text{ giờ}$ (không phải $t = 6\text{ giờ}$).</li>
    <li><strong>d) Đúng:</strong> Tổng tiêu thụ $E_{\text{tiêu}} = \int_0^{12}(0,5t + 4)\,\mathrm{d}t = \left.(0,25t^2 + 4t)\right|_0^{12} = 84\text{ kWh}$. Pin lưu trữ $9\text{ kWh}$ điện dư (hiệu suất $100\%$) bù cho các giờ thiếu điện ($21\text{ kWh}$), nên toàn bộ $72\text{ kWh}$ phát ra được sử dụng hết. Điện phải mua thêm là $84 - 72 = 12\text{ kWh}$.</li>
  </ul>
</div>

<!-- ==================== PAGE 3 ==================== -->
<div style="page-break-before: always;"></div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> <span class="q-ans">Đáp án: a) Đúng – b) Sai – c) Đúng – d) Sai.</span><br>
  Gọi $B$ là biến cố "Người được chọn thực sự mắc bệnh", $D$ là biến cố "AI trả về kết quả dương tính". Ta có $P(B) = 0,02$, $P(\overline{B}) = 0,98$, $P(D \mid B) = 0,95$, $P(D \mid \overline{B}) = 0,05$.
  <ul class="solution-list">
    <li><strong>a) Đúng:</strong> $P(B \cap D) = P(B)\cdot P(D \mid B) = 0,02 \times 0,95 = 0,019$.</li>
    <li><strong>b) Sai:</strong> Theo công thức xác suất toàn phần: $P(D) = 0,019 + 0,98 \times 0,05 = 0,019 + 0,049 = 0,068 \ne 0,05$.</li>
    <li><strong>c) Đúng:</strong> Theo công thức Bayes: $P(B \mid D) = \dfrac{P(B \cap D)}{P(D)} = \dfrac{0,019}{0,068} = \dfrac{19}{68} \approx 27,94\% < 28\%$.</li>
    <li><strong>d) Sai:</strong> $P(\overline{D}) = 1 - 0,068 = 0,932$. Suy ra $P(B \mid \overline{D}) = \dfrac{P(B \cap \overline{D})}{P(\overline{D})} = \dfrac{0,02 \times 0,05}{0,932} = \dfrac{0,001}{0,932} \approx 0,107\% < 0,2\%$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> <span class="q-ans">Đáp án: a) Sai – b) Đúng – c) Sai – d) Đúng.</span><br>
  Mặt phẳng $(P): x + 2y - 2z - 5 = 0$ có VTPT $\vec{n} = (1; 2; -2)$ với $|\vec{n}| = 3$.
  <ul class="solution-list">
    <li><strong>a) Sai:</strong> Khoảng cách từ $A(2; 4; -2)$ đến $(P)$ là $d(A, (P)) = \dfrac{|2 + 2\cdot 4 - 2(-2) - 5|}{3} = \dfrac{9}{3} = 3\text{ m} \ne 4\text{ m}$.<br>
      <em>(Hình chiếu của $A$ lên $(P)$ là $H(1; 2; 0) \Rightarrow$ điểm đối xứng $A'(0; 0; 2)$, tuy nhiên ý khoảng cách sai nên mệnh đề là Sai).</em></li>
    <li><strong>b) Đúng:</strong> Ta có $\overrightarrow{AM} = (1; -1; 4)$ ($M \in (P)$). Gọi $\varphi$ là góc giữa tia $AM$ và $(P)$:
      $$\sin\varphi = \dfrac{|\overrightarrow{AM}\cdot\vec{n}|}{|\overrightarrow{AM}|\cdot|\vec{n}|} = \dfrac{|1\cdot 1 + (-1)\cdot 2 + 4(-2)|}{\sqrt{1 + 1 + 16}\cdot 3} = \dfrac{9}{3\sqrt{2}\cdot 3} = \dfrac{1}{\sqrt{2}} \Rightarrow \varphi = 45^\circ.$$</li>
    <li><strong>c) Sai:</strong> Tia phản xạ đi qua $M$ nằm trên đường thẳng $A'M$ có VTCP $\overrightarrow{A'M} = (3; 3; 0) \parallel (1; 1; 0)$. Vectơ $\vec{u} = (1; -1; 0)$ không cùng phương với $(1; 1; 0)$ nên không phải VTCP của tia phản xạ.</li>
    <li><strong>d) Đúng:</strong> Đặt $f(x; y; z) = x + 2y - 2z - 5$. Ta có $f(A) = 9 > 0$ và $f(B) = 6 + 12 - 4 - 5 = 9 > 0$, nên $A, B$ cùng phía đối với $(P)$. Với mọi $N \in (P)$ thì $AN + NB = A'N + NB \ge A'B = \sqrt{6^2 + 6^2 + 0^2} = 6\sqrt{2}\text{ m}$ (dấu bằng đạt tại $N = A'B \cap (P) = M(3; 3; 2)$).</li>
  </ul>
</div>

<div class="sub-title" style="margin-top: 8px;">PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN</div>

<div class="q-block">
  <span class="q-title">Câu 1.</span> <span class="q-ans">Đáp số: 96,5.</span><br>
  Elip $(E)$ có $a = 5,\; b = 3$ có phương trình $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1 \Rightarrow y^2 = 9\left(1 - \dfrac{x^2}{25}\right)$.<br>
  Đường sinh mặt trụ $y = \pm 1,8$ cắt $(E)$ tại hoành độ thỏa mãn $1,8^2 = 9\left(1 - \dfrac{x^2}{25}\right) \Leftrightarrow \dfrac{x^2}{25} = 0,64 \Leftrightarrow x = \pm 4$.<br>
  Thể tích phần gỗ còn lại khi quay miền tô đậm quanh trục $Ox$ là:
  $$V = \pi \int_{-4}^4 \left[9\left(1 - \dfrac{x^2}{25}\right) - 1,8^2\right]\mathrm{d}x = 2\pi\int_0^4 \dfrac{9}{25}(16 - x^2)\,\mathrm{d}x = \dfrac{18\pi}{25}\left(16x - \dfrac{x^3}{3}\right)\Bigg|_0^4 = \dfrac{768\pi}{25} \approx 96,5\text{ cm}^3.$$
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> <span class="q-ans">Đáp số: 15,6.</span><br>
  Đặt $BM = x$. Theo tính đối xứng qua nếp gấp $MN$, ta có $EM = BM = x$, $AM = 12 - x$. Vì $M \in AB$ và $EM > AM$ nên $6 < x \le 12$.<br>
  Trong $\triangle AME$ vuông tại $A$: $AE = \sqrt{x^2 - (12 - x)^2} = \sqrt{24x - 144} = 2\sqrt{6(x - 6)}$, suy ra $BE = \sqrt{12^2 + AE^2} = \sqrt{24x} = 2\sqrt{6x}$.<br>
  Vì $MN \perp BE$ nên $\widehat{BMN} = \widehat{ABE}$ (cùng phụ $\widehat{AEB}$), suy ra $\triangle MBN \backsim \triangle BAE$ (g.g). Do đó:
  $$MN = BM \cdot \dfrac{BE}{AE} = x\cdot\dfrac{\sqrt{24x}}{\sqrt{24(x - 6)}} = \sqrt{\dfrac{x^3}{x - 6}}.$$
  Xét $g(x) = \dfrac{x^3}{x - 6}$ trên $(6; 12]$: $g'(x) = \dfrac{x^2(2x - 18)}{(x - 6)^2} = 0 \Leftrightarrow x = 9 \in (6; 12]$.<br>
  Tại $x = 9$ (kiểm tra $AE = 6\sqrt{2} < 20$, $BN = 9\sqrt{2} < 20$, thỏa mãn điều kiện hình học), $g(x)$ đạt GTNN $g(9) = 243$.<br>
  Vậy $MN_{\min} = \sqrt{243} = 9\sqrt{3} \approx 15,6\text{ cm}$.
</div>

<!-- ==================== PAGE 4 ==================== -->
<div style="page-break-before: always;"></div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> <span class="q-ans">Đáp số: 111.</span><br>
  Gọi $O, O'$ là tâm hai đáy ($AB = 8,\; A'B' = 2,\; OO' = 4$); $I, I'$ lần lượt là trung điểm $AB, A'B'$. Ta có $OI = 4$, $O'I' = 1$.<br>
  Chiều cao mặt bên hình thang cân $ABB'A'$ là $II' = \sqrt{OO'^2 + (OI - O'I')^2} = \sqrt{4^2 + 3^2} = 5$.<br>
  Cạnh bên là $BB' = \sqrt{5^2 + \left(\dfrac{8 - 2}{2}\right)^2} = \sqrt{34}$. Kẻ $AK \perp BB'$; do tính đối xứng, $CK \perp BB'$, nên góc nhị diện $[A, BB', C] = \widehat{AKC}$.<br>
  Tính $AK = CK = \dfrac{AB \cdot II'}{BB'} = \dfrac{8 \cdot 5}{\sqrt{34}} = \dfrac{40}{\sqrt{34}}$. Với $AC = 8\sqrt{2}$, theo định lí côsin trong $\triangle AKC$:
  $$\cos\widehat{AKC} = \dfrac{AK^2 + CK^2 - AC^2}{2\cdot AK\cdot CK} = \dfrac{\dfrac{3200}{34} - 128}{\dfrac{3200}{34}} = \dfrac{3200 - 4352}{3200} = -0,36 \Rightarrow \widehat{AKC} \approx 111,1^\circ.$$
  Làm tròn đến hàng đơn vị ta được $111$.
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> <span class="q-ans">Đáp số: 7.</span><br>
  Kiểm tra dấu: $(1 + 1 - 4)(1 - 3 - 4) = (-2)(-6) > 0$ và $z_A\cdot z_B = 2\cdot 1 > 0$, nên $A, B$ nằm cùng phía đối với $(P)$ và đối với $(Oxy)$.<br>
  - Điểm đối xứng của $A(1; 1; 2)$ qua $(P): x + y - 4 = 0$ là $A_1(3; 3; 2)$ (do trung điểm $H(2; 2; 2) \in (P)$ và $\overrightarrow{AA_1} = (2; 2; 0) \perp (P)$).<br>
  - Điểm đối xứng của $B(1; -3; 1)$ qua $(Oxy): z = 0$ là $B_1(1; -3; -1)$.<br>
  Khi đó tổng quãng đường bay là $AM + MN + NB = A_1 M + MN + N B_1 \ge A_1 B_1 = \sqrt{(1-3)^2 + (-3-3)^2 + (-1-2)^2} = \sqrt{49} = 7\text{ m}$.<br>
  <em>(Đoạn $A_1 B_1$ cắt $(P)$ tại $s_M = \frac{1}{4}$ rồi cắt $(Oxy)$ tại $s_N = \frac{2}{3}$, nên dấu bằng đạt được theo đúng thứ tự $A \to M \to N \to B$).</em>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> <span class="q-ans">Đáp số: 0,55.</span><br>
  Mỗi đường đi ngắn nhất từ $O(0; 0)$ đến $A(4; 4)$ gồm $8$ bước ($4$ phải, $4$ lên), nên tổng số đường đi là $C_8^4 = 70$.<br>
  - Số đường đi qua $M(1; 2)$ là $C_3^1 \cdot C_5^2 = 3 \cdot 10 = 30 \Rightarrow$ số đường đi tránh $M$ là $n(\overline{M}) = 70 - 30 = 40$.<br>
  - Số đường đi qua $N(3; 3)$ là $C_6^3 \cdot C_2^1 = 20 \cdot 2 = 40$; số đường đi qua cả $M$ và $N$ là $C_3^1 \cdot C_3^1 \cdot C_2^1 = 3 \cdot 3 \cdot 2 = 18$.<br>
  - Suy ra số đường đi qua $N$ và tránh $M$ là $n(N \cap \overline{M}) = 40 - 18 = 22$.<br>
  Vậy xác suất cần tìm là $P(N \mid \overline{M}) = \dfrac{n(N \cap \overline{M})}{n(\overline{M})} = \dfrac{22}{40} = \dfrac{11}{20} = 0,55$.
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> <span class="q-ans">Đáp số: 56,5.</span><br>
  Tâm $I_n$ của $(C_n)$ nằm trên phân giác góc $\widehat{xOy} = 60^\circ$, nên $\widehat{I_n O x} = 30^\circ \Rightarrow OI_n = \dfrac{R_n}{\sin 30^\circ} = 2R_n$.<br>
  Do $(C_{n+1})$ tiếp xúc ngoài và nhỏ hơn $(C_n)$ nên $OI_n - OI_{n+1} = I_n I_{n+1} \Leftrightarrow 2R_n - 2R_{n+1} = R_n + R_{n+1} \Leftrightarrow R_{n+1} = \dfrac{1}{3}R_n$.<br>
  Diện tích $S_n = \pi R_n^2$ lập thành cấp số nhân lùi vô hạn có $S_1 = \pi R_1^2 = 16\pi$ và công bội $q = \left(\dfrac{1}{3}\right)^2 = \dfrac{1}{9}$.<br>
  Tổng diện tích của tất cả các hình tròn là:
  $$S = \dfrac{S_1}{1 - q} = \dfrac{16\pi}{1 - \dfrac{1}{9}} = 18\pi \approx 56,5\text{ cm}^2.$$
</div>

<div style="text-align: center; font-weight: bold; color: #2b6cb0; margin-top: 14px; font-size: 10pt; border-top: 1px dashed #cbd5e0; padding-top: 6px;">
  CHÚC CÁC EM ÔN TẬP VÀ ĐẠT KẾT QUẢ CAO NHẤT TRONG KỲ THI TỐT NGHIỆP THPT!
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

html_filename = 'dap_an_de_200.html'
pdf_name = 'Bang_Dap_An_Va_HDG_De_200.pdf'

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

print("Running Chrome to generate Bang_Dap_An_Va_HDG_De_200.pdf...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
