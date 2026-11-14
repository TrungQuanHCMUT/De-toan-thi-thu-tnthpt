import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 112</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 11mm 13mm 13mm 13mm;
  @bottom-right {
    content: "Trang " counter(page) " – Mã đề: 112";
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
  margin-bottom: 12px;
}
.header h2 {
  margin: 0 0 3px 0;
  font-size: 13.5pt;
  text-transform: uppercase;
  color: #1a365d;
}
.header h3 {
  margin: 0 0 3px 0;
  font-size: 11.5pt;
  font-weight: normal;
  color: #2b4c7e;
}
.header p {
  margin: 0;
  font-size: 10pt;
  font-style: italic;
  color: #555;
}

h2.sec-title {
  font-size: 11.5pt;
  color: #1a365d;
  background-color: #f0f4f8;
  padding: 4px 8px;
  border-left: 4px solid #2b4c7e;
  margin-top: 12px;
  margin-bottom: 7px;
  text-transform: uppercase;
}

h3.sub-title {
  font-size: 10.5pt;
  color: #2b4c7e;
  margin-top: 9px;
  margin-bottom: 5px;
}

table.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
  text-align: center;
}
table.ans-table th, table.ans-table td {
  border: 1px solid #777;
  padding: 4px 3px;
  font-size: 10pt;
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
  margin-bottom: 9px;
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
  margin-top: 2px;
  margin-bottom: 2px;
}
ul.solution-list {
  margin: 3px 0 5px 16px;
  padding: 0;
}
ul.solution-list li {
  margin-bottom: 2.5px;
}
</style>
</head>
<body>

<div class="header">
  <h2>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết</h2>
  <h3>KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 – ĐỀ ÔN TẬP GIỮA KỲ I</h3>
  <p>Môn: TOÁN – Lớp 12 &nbsp;|&nbsp; Mã đề: 112 &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</p>
</div>

<!-- ==================== A. BẢNG ĐÁP ÁN ==================== -->
<h2 class="sec-title">A. Bảng Đáp Án Toàn Bộ Đề Thi (Mã đề: 112)</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp án</td>
    <td class="bold-ans">B</td><td class="bold-ans">B</td><td class="bold-ans">C</td><td class="bold-ans">A</td><td class="bold-ans">A</td><td class="bold-ans">B</td>
    <td class="bold-ans">C</td><td class="bold-ans">A</td><td class="bold-ans">B</td><td class="bold-ans">B</td><td class="bold-ans">A</td><td class="bold-ans">A</td>
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
    <td style="text-align: left; font-weight: bold; padding-left: 6px;">Câu 1 (Khảo sát $y = \frac{x^2-3x+3}{x-1}$)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 6px;">Câu 2 (Tìm $m$ hàm bậc ba)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 6px;">Câu 3 (Nồng độ thuốc trong máu)</td>
    <td class="bold-ans">ĐÚNG</td>
    <td class="bold-ans">ĐÚNG</td>
    <td style="color: #2b6cb0; font-weight: bold;">SAI</td>
    <td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; font-weight: bold; padding-left: 6px;">Câu 4 (Dây cáp hai trụ đèn)</td>
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
    <td style="font-weight: bold;">Chủ đề</td>
    <td>Tổng $m \in S$ đồng biến</td><td>Tối ưu thuế Nhà nước</td><td>GTLN trên đoạn</td><td>Lợi nhuận trừ thuế VAT 10%</td><td>Con đường 4 ngôi nhà</td><td>Chi phí làm bể nước</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp số</td>
    <td class="bold-ans">-15</td><td class="bold-ans">180</td><td class="bold-ans">1</td><td class="bold-ans">2150</td><td class="bold-ans">1600</td><td class="bold-ans">27</td>
  </tr>
</table>

<!-- ==================== B. HƯỚNG DẪN GIẢI CHI TIẾT ==================== -->
<h2 class="sec-title">B. Hướng Dẫn Giải Chi Tiết</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> <span class="q-ans">Chọn B.</span>
  <div class="step">Dựa vào bảng biến thiên, trên khoảng $(-1; 3)$ thì đạo hàm $f'(x) < 0$, do đó hàm số đã cho nghịch biến trên khoảng $(-1; 3)$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> <span class="q-ans">Chọn B.</span>
  <div class="step">Phương trình $f'(x) = 0 \Leftrightarrow (x - 1)^2(x + 2)(x - 3)^3 = 0 \Leftrightarrow x = 1$ (nghiệm bội 2), $x = -2$ (nghiệm đơn – lẻ), $x = 3$ (nghiệm bội 3 – lẻ). Vì $f'(x)$ chỉ đổi dấu qua các nghiệm bội lẻ nên hàm số có đúng $2$ điểm cực trị là $x = -2$ và $x = 3$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> <span class="q-ans">Chọn C.</span>
  <div class="step">Đạo hàm $f'(x) = 3x^2 - 6x - 9 = 3(x + 1)(x - 3)$. Trên đoạn $[0; 4]$, $f'(x) = 0 \Leftrightarrow x = 3$.<br>
  Ta tính các giá trị: $f(0) = 5$, $f(3) = 27 - 27 - 27 + 5 = -22$, $f(4) = 64 - 48 - 36 + 5 = -15$.<br>
  Vậy giá trị nhỏ nhất của hàm số trên đoạn $[0; 4]$ bằng $-22$ (đạt tại $x = 3$).</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> <span class="q-ans">Chọn A.</span>
  <div class="step">Ta có $\lim_{x \to (-3)^+} \dfrac{2x - 5}{x + 3} = -\infty$ do mẫu tiến về $0^+$ và tử tiến về $-11 < 0$. Suy ra đường thẳng $x = -3$ là đường tiệm cận đứng của đồ thị hàm số.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> <span class="q-ans">Chọn A.</span>
  <div class="step">Chia đa thức: $\dfrac{x^2 - 3x + 5}{x - 2} = x - 1 + \dfrac{3}{x - 2}$.<br>
  Vì $\lim_{x \to \pm\infty} [y - (x - 1)] = \lim_{x \to \pm\infty} \dfrac{3}{x - 2} = 0$, nên đường thẳng $y = x - 1$ là đường tiệm cận xiên của đồ thị hàm số.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> <span class="q-ans">Chọn B.</span>
  <div class="step">Đồ thị là đường cong bậc ba có nhánh phải đi lên nên $a > 0$. Đồ thị đi qua điểm $(0; 1)$, đạt cực đại tại $(-1; 3)$ và cực tiểu tại $(1; -1)$. Xét hàm số $y = x^3 - 3x + 1$ có $y' = 3x^2 - 3 = 0 \Leftrightarrow x = \pm 1$; $y(-1) = 3, y(1) = -1, y(0) = 1$ hoàn toàn thỏa mãn.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 7.</span> <span class="q-ans">Chọn C.</span>
  <div class="step">Phương trình $2f(x) - 1 = 0 \Leftrightarrow f(x) = \dfrac{1}{2}$. Từ bảng biến thiên, ta thấy giá trị cực tiểu là $-2$ và cực đại là $3$. Do $-2 < \dfrac{1}{2} < 3$ nên đường thẳng $y = \dfrac{1}{2}$ cắt đồ thị tại đúng $3$ điểm phân biệt.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 8.</span> <span class="q-ans">Chọn A.</span>
  <div class="step">Giao điểm của đồ thị với trục tung $Oy$ ứng với hoành độ $x = 0 \Rightarrow y = \dfrac{0 - 3}{0 + 1} = -3$. Do đó toạ độ giao điểm là $(0; -3)$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 9.</span> <span class="q-ans">Chọn B.</span>
  <div class="step">Hàm số rút gọn: với $x \ne 1$ thì $y = \dfrac{x - 1}{(x - 1)(x - 2)} = \dfrac{1}{x - 2}$.<br>
  - Tại $x = 1$: $\lim_{x \to 1} y = -1$ (hữu hạn, không là TCĐ).<br>
  - Tại $x = 2$: $\lim_{x \to 2^+} y = +\infty \Rightarrow x = 2$ là tiệm cận đứng duy nhất.<br>
  - Tại $\pm\infty$: $\lim_{x \to \pm\infty} y = 0 \Rightarrow y = 0$ là tiệm cận ngang duy nhất.<br>
  Tổng số tiệm cận đứng và tiệm cận ngang là $1 + 1 = 2$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 10.</span> <span class="q-ans">Chọn B.</span>
  <div class="step">Hàm số $y = -x^3 + 3x^2 + 2$ có $y' = -3x^2 + 6x = -3x(x - 2) = 0 \Leftrightarrow x = 0$ hoặc $x = 2$.<br>
  Ta có $y'' = -6x + 6 \Rightarrow y''(2) = -6 < 0$ nên $x = 2$ là điểm cực đại của hàm số. Tung độ cực đại $y(2) = 6$. Vậy điểm cực đại của đồ thị là $(2; 6)$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 11.</span> <span class="q-ans">Chọn A.</span>
  <div class="step">Vận tốc tức thời: $v(t) = s'(t) = -3t^2 + 12t + 15 = -3(t - 2)^2 + 27 \le 27$. Dấu bằng đạt được khi $t = 2\text{ s}$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 12.</span> <span class="q-ans">Chọn A.</span>
  <div class="step">Tập xác định: $D = \mathbb{R} \setminus \{m\}$.<br>
  Đạo hàm: $y' = \dfrac{1 \cdot (-m) - (-3) \cdot 1}{(x - m)^2} = \dfrac{-m + 3}{(x - m)^2}$.<br>
  Hàm số đồng biến trên khoảng $(4; +\infty) \Leftrightarrow \begin{cases} y' > 0, \forall x \in (4; +\infty) \\ m \notin (4; +\infty) \end{cases} \Leftrightarrow \begin{cases} -m + 3 > 0 \\ m \le 4 \end{cases} \Leftrightarrow \begin{cases} m < 3 \\ m \le 4 \end{cases} \Leftrightarrow m < 3$.<br>
  Vì $m \in \mathbb{Z}$ và $m \in [-100; 100]$ nên $m \in \{-100; -99; \dots; 1; 2\}$.<br>
  Số giá trị nguyên thỏa mãn là: $2 - (-100) + 1 = 103$. Do đó chọn đáp án <b>A</b>.</div>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 3}{x - 1}$ có đồ thị là $(C)$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG.</b> Ta có $y = x - 2 + \dfrac{1}{x - 1} \Rightarrow y' = 1 - \dfrac{1}{(x - 1)^2} = \dfrac{x(x - 2)}{(x - 1)^2}$. Cho $y' = 0 \Leftrightarrow x = 0$ hoặc $x = 2$. Bảng xét dấu cho thấy $y' > 0$ khi $x \in (-\infty; 0) \cup (2; +\infty)$ nên hàm số đồng biến trên các khoảng đó.</li>
    <li><b>b) ĐÚNG.</b> Vì $\lim_{x \to 1^+} y = +\infty$ nên $x = 1$ là tiệm cận đứng; và $\lim_{x \to \pm\infty} [y - (x - 2)] = \lim_{x \to \pm\infty} \dfrac{1}{x - 1} = 0$ nên $y = x - 2$ là tiệm cận xiên.</li>
    <li><b>c) SAI.</b> Giao điểm hai đường tiệm cận là nghiệm của hệ $\begin{cases} x = 1 \\ y = x - 2 \end{cases} \Rightarrow I(1; -1)$. Điểm $I(1; -1)$ mới là tâm đối xứng.</li>
    <li><b>d) ĐÚNG.</b> Hai điểm cực trị của $(C)$ là cực đại $A(0; -3)$ và cực tiểu $B(2; 1)$. Khoảng cách giữa hai điểm cực trị: $AB = \sqrt{(2 - 0)^2 + (1 - (-3))^2} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Cho hàm số $y = f(x) = \dfrac{1}{3}x^3 - mx^2 + (m^2 - 4)x + 1$.
  <ul class="solution-list">
    <li><b>a) ĐÚNG.</b> Đạo hàm $f'(x) = x^2 - 2mx + m^2 - 4$. Ta có $\Delta' = m^2 - (m^2 - 4) = 4 > 0, \forall m \in \mathbb{R}$. Do đó phương trình $f'(x) = 0$ luôn có hai nghiệm phân biệt với mọi $m$.</li>
    <li><b>b) ĐÚNG.</b> Hai nghiệm phân biệt của $f'(x) = 0$ là $x_1 = m - \sqrt{4} = m - 2$ và $x_2 = m + \sqrt{4} = m + 2$.</li>
    <li><b>c) ĐÚNG.</b> Vì hệ số bậc cao nhất $a = 1 > 0$ nên hàm số đồng biến trên $(-\infty; x_1)$ và $(x_2; +\infty)$. Để hàm số đồng biến trên $(5; +\infty)$ thì $(5; +\infty) \subset (x_2; +\infty) \Leftrightarrow x_2 \le 5 \Leftrightarrow m + 2 \le 5 \Leftrightarrow m \le 3$.</li>
    <li><b>d) ĐÚNG.</b> Ta có $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = (2m)^2 - 2(m^2 - 4) = 2m^2 + 8$. Theo giả thiết: $2m^2 + 8 = 20 \Leftrightarrow 2m^2 = 12 \Leftrightarrow m^2 = 6 \Leftrightarrow m = \pm\sqrt{6}$. Có đúng $2$ giá trị $m$ thỏa mãn.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Nồng độ thuốc $C(t) = \dfrac{8t}{t^2 + 4}\text{ (mg/L)}$ ($t \ge 0$).
  <ul class="solution-list">
    <li><b>a) ĐÚNG.</b> Tại $t = 0$: $C(0) = \dfrac{8 \cdot 0}{0 + 4} = 0\text{ mg/L}$.</li>
    <li><b>b) ĐÚNG.</b> Đạo hàm $C'(t) = \dfrac{8(t^2 + 4) - 8t(2t)}{(t^2 + 4)^2} = \dfrac{32 - 8t^2}{(t^2 + 4)^2} = \dfrac{8(4 - t^2)}{(t^2 + 4)^2}$. Với $t \ge 0$, $C'(t) = 0 \Leftrightarrow t = 2$ giờ. Bảng biến thiên cho thấy $C(t)$ đạt cực đại và lớn nhất tại $t = 2\text{ giờ}$.</li>
    <li><b>c) SAI.</b> Nồng độ thuốc lớn nhất trong máu là $C(2) = \dfrac{8 \cdot 2}{2^2 + 4} = \dfrac{16}{8} = 2\text{ mg/L} \ne 4\text{ mg/L}$.</li>
    <li><b>d) ĐÚNG.</b> Với $t > 2$, ta có $C'(t) < 0$ nên nồng độ thuốc giảm dần theo thời gian.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Giăng dây cáp hai trụ đèn $AH = 6\text{ m}, BK = 12\text{ m}, HK = 24\text{ m}$. Đặt $HM = x$ ($0 \le x \le 24$).
  <ul class="solution-list">
    <li><b>a) ĐÚNG.</b> Đoạn $KM = 24 - x$, tam giác $BKM$ vuông tại $K \Rightarrow BM = \sqrt{(24 - x)^2 + 12^2} = \sqrt{(24 - x)^2 + 144}\text{ (m)}$.</li>
    <li><b>b) SAI.</b> Khi $x = 12\text{ m} \Rightarrow AM = \sqrt{12^2 + 6^2} = \sqrt{180} = 6\sqrt{5}$; $BM = \sqrt{12^2 + 12^2} = 12\sqrt{2}$. Tổng chiều dài là $6\sqrt{5} + 12\sqrt{2} \approx 30,39\text{ m} \ne 18\sqrt{2}\text{ m} \approx 25,46\text{ m}$.</li>
    <li><b>c) ĐÚNG.</b> Xét véc-tơ $\vec{u} = (x; 6)$ và $\vec{v} = (24 - x; 12)$. Ta có chiều dài cáp $L(x) = |\vec{u}| + |\vec{v}| \ge |\vec{u} + \vec{v}| = \sqrt{24^2 + (6 + 12)^2} = \sqrt{24^2 + 18^2} = 30\text{ m}$. Đẳng thức xảy ra khi hai véc-tơ cùng hướng: $\dfrac{x}{24 - x} = \dfrac{6}{12} = \dfrac{1}{2} \Leftrightarrow 2x = 24 - x \Leftrightarrow 3x = 24 \Leftrightarrow x = 8\text{ m}$.</li>
    <li><b>d) ĐÚNG.</b> Chiều dài ngắn nhất bằng chính $30\text{ m}$.</li>
  </ul>
</div>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> <span class="q-ans">Đáp số: -15</span>
  <div class="step">Hàm số $y = x^3 - 3(m + 1)x^2 + 3m(m + 2)x + 2026$ có đạo hàm:<br>
  $y' = 3x^2 - 6(m + 1)x + 3m(m + 2) = 3[x^2 - 2(m + 1)x + m(m + 2)] = 3(x - m)[x - (m + 2)]$.<br>
  Hai nghiệm của $y' = 0$ là $x = m$ và $x = m + 2$. Vì $a = 3 > 0$ nên hàm số nghịch biến trên khoảng $(m; m + 2)$ và đồng biến trên các khoảng $(-\infty; m)$, $(m + 2; +\infty)$.<br>
  Để hàm số đồng biến trên khoảng $(2; 6)$ thì khoảng $(2; 6)$ không được chứa điểm nào của khoảng nghịch biến $(m; m + 2)$, tức là:<br>
  $\left[\begin{array}{l} (2; 6) \subseteq (-\infty; m] \\ (2; 6) \subseteq [m + 2; +\infty) \end{array}\right. \Leftrightarrow \left[\begin{array}{l} m \ge 6 \\ m + 2 \le 2 \end{array}\right. \Leftrightarrow \left[\begin{array}{l} m \ge 6 \\ m \le 0 \end{array}\right.$<br>
  Do $m \in \mathbb{Z}$ và $m \in [-100; 100]$ nên tập hợp $S = \{-100; -99; \dots; 0\} \cup \{6; 7; \dots; 100\}$.<br>
  Nhận xét các số nguyên từ $-100$ đến $100$ có tổng bằng $0$. Các giá trị không thuộc $S$ là $m \in \{1; 2; 3; 4; 5\}$.<br>
  Vậy tổng tất cả các phần tử của $S$ là: $\sum_{m \in S} m = 0 - (1 + 2 + 3 + 4 + 5) = -15$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> <span class="q-ans">Đáp số: 180</span>
  <div class="step">
    <b>Bước 1: Thiết lập hàm lợi nhuận sau thuế của doanh nghiệp theo sản lượng $x$ và mức thuế $t$:</b><br>
    Hàm doanh thu khi bán $x$ sản phẩm ($0 < x \le 200$) là:<br>
    $R(x) = x \cdot p(x) = x(400 - x) = 400x - x^2\text{ (nghìn đồng)}$.<br>
    Tổng chi phí của doanh nghiệp bao gồm chi phí sản xuất và thuế phụ thu $t\text{ nghìn đồng/sản phẩm}$ nộp cho Nhà nước:<br>
    $C_{\text{toàn bộ}}(x) = C(x) + t \cdot x = (x^2 + 40x + 2000) + tx = x^2 + (40 + t)x + 2000\text{ (nghìn đồng)}$.<br>
    Lợi nhuận sau thuế của doanh nghiệp là:<br>
    $P(x) = R(x) - C_{\text{toàn bộ}}(x) = (400x - x^2) - [x^2 + (40 + t)x + 2000] = -2x^2 + (360 - t)x - 2000\text{ (nghìn đồng)}$.<br>
    <br>
    <b>Bước 2: Tìm mức sản lượng $x(t)$ để doanh nghiệp đạt lợi nhuận lớn nhất:</b><br>
    Hàm $P(x)$ là tam thức bậc hai theo $x$ với hệ số $a = -2 < 0$, đạo hàm:<br>
    $P'(x) = -4x + 360 - t = 0 \Leftrightarrow x(t) = \dfrac{360 - t}{4}$.<br>
    Với $0 < t < 360$, ta có $0 < x(t) = \dfrac{360 - t}{4} < \dfrac{360}{4} = 90 \le 200$, do đó doanh nghiệp luôn chọn sản xuất mức sản lượng $x(t) = \dfrac{360 - t}{4}$ để tối đa hóa lợi nhuận.<br>
    <br>
    <b>Bước 3: Tối ưu hóa tổng số tiền thuế Nhà nước thu được theo $t$:</b><br>
    Tổng số tiền thuế Nhà nước thu được trong một ngày theo mức thuế $t$ là:<br>
    $T(t) = t \cdot x(t) = t \cdot \dfrac{360 - t}{4} = \dfrac{1}{4}(360t - t^2)\text{ (nghìn đồng)}$.<br>
    Xét hàm số $T(t)$ trên khoảng $(0; 360)$:<br>
    $T'(t) = \dfrac{1}{4}(360 - 2t) = 90 - \dfrac{1}{2}t$.<br>
    $T'(t) = 0 \Leftrightarrow 90 - \dfrac{1}{2}t = 0 \Leftrightarrow t = 180\text{ (nghìn đồng)}$.<br>
    Vì $T''(t) = -\dfrac{1}{2} < 0$ nên $T(t)$ đạt giá trị lớn nhất tại $t = 180$.<br>
    (Khi đó doanh nghiệp sản xuất $x = 45$ sản phẩm, tiền thuế Nhà nước thu về lớn nhất là $T(180) = 8\,100\text{ nghìn đồng} = 8,1\text{ triệu đồng}$).<br>
    Vậy Nhà nước cần ấn định mức thuế $t = 180\text{ nghìn đồng}$.
  </div>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> <span class="q-ans">Đáp số: 1</span>
  <div class="step">Trên đoạn $[2; 4]$, đạo hàm $f'(x) = \dfrac{-2 - m}{(x - 1)^2}$.<br>
  - Nếu $-2 - m > 0 \Leftrightarrow m < -2$: hàm số đồng biến trên $[2; 4] \Rightarrow \max f(x) = f(4) = \dfrac{8 + m}{3} = 5 \Leftrightarrow m = 7$ (loại).<br>
  - Nếu $-2 - m < 0 \Leftrightarrow m > -2$: hàm số nghịch biến trên $[2; 4] \Rightarrow \max f(x) = f(2) = 4 + m = 5 \Leftrightarrow m = 1$ (thỏa mãn $m > -2$).<br>
  - Nếu $m = -2 \Rightarrow f(x) = 2$ hằng số (loại). Vậy $m = 1$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> <span class="q-ans">Đáp số: 2150</span>
  <div class="step">
    Số lượng đặt hàng $x$ (tấn sản phẩm) với $0 \le x \le 90$.<br>
    Tổng doanh thu bán hàng mỗi tháng là:<br>
    $R(x) = x \cdot P(x) = x(90 - 0{,}01x^2) = 90x - 0{,}01x^3\text{ (triệu đồng)}$.<br>
    Số tiền thuế giá trị gia tăng (VAT) nhà máy A phải nộp là $10\%$ tổng doanh thu:<br>
    $T_{\text{VAT}}(x) = 0{,}1 \cdot R(x) = 0{,}1(90x - 0{,}01x^3) = 9x - 0{,}001x^3\text{ (triệu đồng)}$.<br>
    Doanh thu thực tế sau khi trừ thuế VAT là:<br>
    $R_{\text{sau VAT}}(x) = R(x) - T_{\text{VAT}}(x) = 0{,}9 \cdot R(x) = 0{,}9(90x - 0{,}01x^3) = 81x - 0{,}009x^3\text{ (triệu đồng)}$.<br>
    Chi phí sản xuất $x$ tấn sản phẩm trong một tháng là:<br>
    $C(x) = \dfrac{1}{2}(200 + 27x) = 100 + 13{,}5x\text{ (triệu đồng)}$.<br>
    Lợi nhuận mỗi tháng của nhà máy A sau khi trừ thuế VAT là:<br>
    $L(x) = R_{\text{sau VAT}}(x) - C(x) = (81x - 0{,}009x^3) - (100 + 13{,}5x) = -0{,}009x^3 + 67{,}5x - 100\text{ (triệu đồng)}$.<br>
    Xét hàm số $L(x)$ trên đoạn $[0; 90]$:<br>
    $L'(x) = -0{,}027x^2 + 67{,}5 = -\dfrac{27}{1000}x^2 + \dfrac{135}{2}$.<br>
    $L'(x) = 0 \Leftrightarrow x^2 = \dfrac{135}{2} \cdot \dfrac{1000}{27} = 2500 \Leftrightarrow x = 50\text{ (do } 0 \le x \le 90\text{)}$.<br>
    Giá trị của hàm số tại các điểm đầu mút và điểm tới hạn:<br>
    $L(0) = -100$;<br>
    $L(50) = -0{,}009 \cdot (50)^3 + 67{,}5 \cdot 50 - 100 = -1125 + 3375 - 100 = 2150\text{ (triệu đồng)}$;<br>
    $L(90) = -0{,}009 \cdot (90)^3 + 67{,}5 \cdot 90 - 100 = -6561 + 6075 - 100 = -586\text{ (triệu đồng)}$.<br>
    Vậy lợi nhuận mỗi tháng cao nhất mà nhà máy A thu được là $2150\text{ triệu đồng}$.
  </div>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> <span class="q-ans">Đáp số: 1600</span>
  <div class="step">Tam giác $ABC$ đều cạnh $4\text{ km} \Rightarrow \widehat{ABC} = 60^\circ$. Tam giác $DAB$ cân tại $D$ có $\widehat{ADB} = 120^\circ \Rightarrow \widehat{DBA} = 30^\circ$ và $DB = \dfrac{4 \sin 30^\circ}{\sin 120^\circ} = \dfrac{4}{\sqrt{3}}\text{ km}$.<br>
  Ta có $\widehat{DBC} = \widehat{DBA} + \widehat{ABC} = 30^\circ + 60^\circ = 90^\circ \Rightarrow \triangle DBC$ vuông tại $B$.<br>
  Đặt $BM = x\text{ (km)}$ ($0 \le x \le 4$). Chiều dài đoạn đường trên $BC$ là $MC = 4 - x$, chi phí là $200(4 - x)$ (triệu đồng).<br>
  Chiều dài đoạn đường $MD = \sqrt{DB^2 + BM^2} = \sqrt{x^2 + \dfrac{16}{3}}$, chi phí là $400\sqrt{x^2 + \dfrac{16}{3}}$ (triệu đồng).<br>
  Tổng chi phí: $f(x) = 200\left[4 - x + 2\sqrt{x^2 + \dfrac{16}{3}}\right]$. Xét hàm $g(x) = 2\sqrt{x^2 + \dfrac{16}{3}} - x + 4$.<br>
  $g'(x) = \dfrac{2x}{\sqrt{x^2 + \frac{16}{3}}} - 1 = 0 \Leftrightarrow 4x^2 = x^2 + \dfrac{16}{3} \Leftrightarrow x^2 = \dfrac{16}{9} \Rightarrow x = \dfrac{4}{3}\text{ km}$.<br>
  Tại $x = \dfrac{4}{3}$, ta có $\sqrt{x^2 + \dfrac{16}{3}} = \dfrac{8}{3}$ và $g\left(\dfrac{4}{3}\right) = 2 \cdot \dfrac{8}{3} - \dfrac{4}{3} + 4 = 8$.<br>
  Chi phí nhỏ nhất là $f\left(\dfrac{4}{3}\right) = 200 \times 8 = 1600\text{ (triệu đồng)}$.</div>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> <span class="q-ans">Đáp số: 27</span>
  <div class="step">Gọi chiều rộng đáy bể là $x\text{ (m)}$ ($x > 0$), chiều dài đáy là $2x\text{ (m)}$. Diện tích đáy bể $S_đ = 2x^2\text{ (m}^2\text{)}$.<br>
  Thể tích bể $V = 60\text{ m}^3 \Rightarrow$ Chiều cao bể $h = \dfrac{60}{2x^2} = \dfrac{30}{x^2}\text{ (m)}$.<br>
  Diện tích bốn mặt thành xung quanh: $S_{xq} = 2(x + 2x) \cdot \dfrac{30}{x^2} = \dfrac{180}{x}\text{ (m}^2\text{)}$.<br>
  Tổng chi phí (triệu đồng): $C(x) = 0,5 \cdot (2x^2) + 0,3 \cdot \dfrac{180}{x} = x^2 + \dfrac{54}{x}$.<br>
  Đạo hàm $C'(x) = 2x - \dfrac{54}{x^2} = 0 \Leftrightarrow x^3 = 27 \Leftrightarrow x = 3\text{ (m)}$.<br>
  Hàm số đạt giá trị nhỏ nhất tại $x = 3$. Chi phí nhỏ nhất là $C(3) = 3^2 + \dfrac{54}{3} = 9 + 18 = 27\text{ (triệu đồng)}$.</div>
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

html_path = 'dap_an_112.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'Bang_Dap_An_Va_HDG_De_112.pdf'
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

print('Running Chrome for answer key PDF...')
res = subprocess.run(cmd, capture_output=True, text=True)
print('Chrome exit code:', res.returncode)

reader = pypdf.PdfReader(output_pdf)
print('Total pages of answer key PDF:', len(reader.pages))
