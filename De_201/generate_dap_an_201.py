import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 201</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4 portrait;
  margin: 10mm 12mm 10mm 12mm;
}
* {
  box-sizing: border-box;
}
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 9.8pt;
  line-height: 1.32;
  color: #111;
  margin: 0;
  padding: 0;
}
.katex {
  font-size: 1.0em;
}
.katex-display {
  margin: 3px 0;
}
.header {
  text-align: center;
  border-bottom: 2px solid #000;
  padding-bottom: 5px;
  margin-bottom: 8px;
}
.header h1 {
  font-size: 13pt;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.header h2 {
  font-size: 10.8pt;
  margin: 2px 0;
}
.header .meta {
  font-size: 9.2pt;
  font-style: italic;
}
h3 {
  font-size: 10.5pt;
  text-transform: uppercase;
  margin: 8px 0 4px 0;
  border-left: 3.5px solid #1a365d;
  padding-left: 6px;
  color: #1a365d;
  break-after: avoid;
  page-break-after: avoid;
}
h4 {
  font-size: 10pt;
  margin: 6px 0 3px 0;
  color: #000;
  break-after: avoid;
  page-break-after: avoid;
}
table.key-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 6px;
  font-size: 9.4pt;
  text-align: center;
}
table.key-table th, table.key-table td {
  border: 1px solid #444;
  padding: 3px 5px;
}
table.key-table th {
  background-color: #edf2f7;
  font-weight: bold;
}
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 6px;
}
.solution-block {
  margin-bottom: 6px;
  text-align: justify;
  break-inside: avoid;
}
.q-head {
  font-weight: bold;
  color: #1a365d;
}
ul.sub-sol {
  margin: 2px 0 0 0;
  padding-left: 16px;
}
ul.sub-sol li {
  margin-bottom: 2px;
}
</style>
</head>
<body>

<div class="header">
  <h1>BẢNG ĐÁP ÁN &amp; HƯỚNG DẪN GIẢI CHI TIẾT</h1>
  <h2>ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA – MÔN TOÁN (MÃ ĐỀ 201)</h2>
  <div class="meta">Chương trình GDPT 2018 (Toán lớp 10, 11, 12) – Thời gian làm bài: 90 phút &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</div>
</div>

<h3>A. BẢNG ĐÁP ÁN</h3>

<h4>PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (3,0 điểm)</h4>
<table class="key-table">
  <tr>
    <th>Câu</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <th>Đáp án</th><td><strong>C</strong></td><td><strong>A</strong></td><td><strong>D</strong></td><td><strong>B</strong></td><td><strong>A</strong></td><td><strong>C</strong></td><td><strong>B</strong></td><td><strong>D</strong></td><td><strong>A</strong></td><td><strong>D</strong></td><td><strong>C</strong></td><td><strong>B</strong></td>
  </tr>
</table>

<div class="grid-2">
  <div>
    <h4>PHẦN II. Trắc nghiệm đúng sai (4,0 điểm)</h4>
    <table class="key-table">
      <tr><th>Câu</th><th>Ý a)</th><th>Ý b)</th><th>Ý c)</th><th>Ý d)</th></tr>
      <tr><th>Câu 1</th><td><strong>Đúng</strong></td><td><strong>Đúng</strong></td><td><strong>Sai</strong></td><td><strong>Đúng</strong></td></tr>
      <tr><th>Câu 2</th><td><strong>Sai</strong></td><td><strong>Đúng</strong></td><td><strong>Đúng</strong></td><td><strong>Sai</strong></td></tr>
      <tr><th>Câu 3</th><td><strong>Đúng</strong></td><td><strong>Sai</strong></td><td><strong>Sai</strong></td><td><strong>Đúng</strong></td></tr>
      <tr><th>Câu 4</th><td><strong>Sai</strong></td><td><strong>Sai</strong></td><td><strong>Đúng</strong></td><td><strong>Đúng</strong></td></tr>
    </table>
  </div>
  <div>
    <h4>PHẦN III. Trắc nghiệm trả lời ngắn (3,0 điểm)</h4>
    <table class="key-table" style="margin-top: 8px;">
      <tr><th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th></tr>
      <tr><th>Đáp án</th><td><strong>144</strong></td><td><strong>46,8</strong></td><td><strong>2,81</strong></td><td><strong>6</strong></td><td><strong>0,04</strong></td><td><strong>0,31</strong></td></tr>
    </table>
    <div style="font-size: 8.8pt; font-style: italic; color: #444; margin-top: 4px; text-align: center;">
      Quy ước chấm Phần II: đúng 1 ý = 0,1đ; 2 ý = 0,25đ; 3 ý = 0,5đ; 4 ý = 1,0đ.
    </div>
  </div>
</div>

<h3>B. HƯỚNG DẪN GIẢI CHI TIẾT</h3>

<h4>PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN</h4>

<div class="solution-block">
  <span class="q-head">Câu 1. Chọn C.</span> Thực hiện phép chia đa thức: $y = \dfrac{x^2 - 4x + 5}{x - 2} = x - 2 + \dfrac{1}{x - 2}$. Do $\lim\limits_{x \to \pm\infty}[y - (x - 2)] = 0$, đường tiệm cận xiên của đồ thị hàm số là $y = x - 2$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 2. Chọn A.</span> Ta có $F(x) = \displaystyle\int \left(\sin 2x + e^{3x}\right)\mathrm{d}x = -\dfrac{1}{2}\cos 2x + \dfrac{1}{3}e^{3x} + C$. Do $F(0) = \dfrac{5}{6} \Rightarrow -\dfrac{1}{2} + \dfrac{1}{3} + C = \dfrac{5}{6} \Leftrightarrow C = 1$. Vậy $F\left(\dfrac{\pi}{4}\right) = -\dfrac{1}{2}\cos\dfrac{\pi}{2} + \dfrac{1}{3}e^{\frac{3\pi}{4}} + 1 = \dfrac{1}{3}e^{\frac{3\pi}{4}} + 1$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 3. Chọn D.</span> Vì $x^2 + 2x + 5 = (x + 1)^2 + 4 > 0\;\forall x \in \mathbb{R}$, áp dụng $(\log_2 u)' = \dfrac{u'}{u\ln 2}$ ta được $y' = \dfrac{2x + 2}{(x^2 + 2x + 5)\ln 2}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 4. Chọn B.</span> Bán kính đường tròn là $R = IA = \sqrt{(-1 - 2)^2 + (1 + 3)^2} = \sqrt{9 + 16} = 5$. Phương trình đường tròn tâm $I(2; -3)$, bán kính $R = 5$ là $(x - 2)^2 + (y + 3)^2 = 25$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 5. Chọn A.</span> Số ghế mỗi hàng lập thành cấp số cộng với $u_1 = 18$, $d = 3$, $n = 20$. Tổng số ghế là $S_{20} = \dfrac{20}{2}\left[2\cdot 18 + 19\cdot 3\right] = 10\cdot 93 = 930$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 6. Chọn C.</span> Vì $SA \perp (ABC)$ nên $AB$ là hình chiếu vuông góc của $SB$ lên $(ABC)$, suy ra $\widehat{(SB, (ABC))} = \widehat{SBA}$. Trong $\triangle SAB$ vuông tại $A$: $\tan\widehat{SBA} = \dfrac{SA}{AB} = \dfrac{a\sqrt{3}}{a} = \sqrt{3} \Rightarrow \widehat{SBA} = 60^\circ$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 7. Chọn B.</span> Đường thẳng $d$ có VTCP $\vec{u} = (2; -1; 2)$, mặt phẳng $(P)$ có VTPT $\vec{n} = (2; 1; -2)$. Gọi $\varphi$ là góc giữa $d$ và $(P)$, ta có $\sin\varphi = \dfrac{|\vec{u}\cdot\vec{n}|}{|\vec{u}|\cdot|\vec{n}|} = \dfrac{|4 - 1 - 4|}{3\cdot 3} = \dfrac{1}{9} \Rightarrow \cos\varphi = \sqrt{1 - \dfrac{1}{81}} = \dfrac{4\sqrt{5}}{9}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 8. Chọn D.</span> $3^{x^2 - 2x} < 27 \Leftrightarrow x^2 - 2x < 3 \Leftrightarrow -1 < x < 3$. Suy ra $a = -1$, $b = 3 \Rightarrow a + 2b = 5$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 9. Chọn A.</span> Với $x \in [0; 1]$, $e^x \ge e^{-x}$. Diện tích hình phẳng là $S = \displaystyle\int_0^1 \left(e^x - e^{-x}\right)\mathrm{d}x = \left.(e^x + e^{-x})\right|_0^1 = e + e^{-1} - 2$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 10. Chọn D.</span> Giá trị đại diện các nhóm là $3; 5; 7; 9$, cỡ mẫu $n = 20$. Số trung bình $\bar{x} = \dfrac{4\cdot 3 + 6\cdot 5 + 8\cdot 7 + 2\cdot 9}{20} = 5{,}8$. Phương sai $s^2 = \dfrac{4\cdot 9 + 6\cdot 25 + 8\cdot 49 + 2\cdot 81}{20} - 5{,}8^2 = 37 - 33{,}64 = 3{,}36$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 11. Chọn C.</span> Áp dụng công thức nhân xác suất: $P(A \cap B) = P(A)\cdot P(B|A) = 0{,}6\cdot 0{,}3 = 0{,}18$. Suy ra $P(A|B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{0{,}18}{0{,}5} = 0{,}36$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 12. Chọn B.</span> Áp dụng công thức truy hồi $u_{n+1} = 3u_n - 1$: với $n = 1 \Rightarrow u_2 = 3\cdot 2 - 1 = 5$; với $n = 2 \Rightarrow u_3 = 3\cdot 5 - 1 = 14$.
</div>

<h4>PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI</h4>

<div class="solution-block">
  <span class="q-head">Câu 1. (Đ – Đ – S – Đ)</span> Ta có $f'(x) = 3x^2 - 6x - 9 = 3(x + 1)(x - 3)$, có hai nghiệm $x = -1$ và $x = 3$.
  <ul class="sub-sol">
    <li><strong>a) Đúng:</strong> $f'(x) > 0$ trên $(-\infty; -1)$ và $(3; +\infty)$; $f'(x) < 0$ trên $(-1; 3)$.</li>
    <li><strong>b) Đúng:</strong> Trên $[0; 4]$, $f'(x) = 0 \Leftrightarrow x = 3$. Tính $f(0) = 11$, $f(3) = -16$, $f(4) = -9 \Rightarrow \max\limits_{[0; 4]} f(x) = 11$.</li>
    <li><strong>c) Sai:</strong> Hai điểm cực trị là $(-1; 16)$ và $(3; -16)$. Đường thẳng đi qua hai điểm này có phương trình $y = -8x + 8 \ne -8x - 8$.</li>
    <li><strong>d) Đúng:</strong> Đồ thị hàm chẵn $y = f(|x|)$ có điểm cực đại tại $(0; 11)$, hai điểm cực tiểu tại $(\pm 3; -16)$ và tiến về $+\infty$ khi $x \to \pm\infty$. Để phương trình có $4$ nghiệm phân biệt thì $-16 < m < 11$, gồm $10 - (-15) + 1 = 26$ số nguyên.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 2. (S – Đ – Đ – S)</span>
  <ul class="sub-sol">
    <li><strong>a) Sai:</strong> Với $0 \le t \le 10$, $v(t) = \int_0^t 0{,}6u\,\mathrm{d}u = 0{,}3t^2$. Vận tốc cực đại tại $t = 10\text{ s}$ là $v(10) = 30\text{ m/s} = 108\text{ km/h} \ne 120\text{ km/h}$.</li>
    <li><strong>b) Đúng:</strong> $s_1 = \displaystyle\int_0^{10} 0{,}3t^2\,\mathrm{d}t = \left.0{,}1t^3\right|_0^{10} = 100\text{ m}$.</li>
    <li><strong>c) Đúng:</strong> Giai đoạn $10 < t \le 20$ chậm dần đều từ $30\text{ m/s}$ về $0$ trong $10\text{ s} \Rightarrow a_2 = \dfrac{0 - 30}{10} = -3\text{ m/s}^2$.</li>
    <li><strong>d) Sai:</strong> $s_2 = \dfrac{30 + 0}{2}\cdot 10 = 150\text{ m}$. Tổng quãng đường $S = 100 + 150 = 250\text{ m} < 260\text{ m}$.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 3. (Đ – S – S – Đ)</span> Đặt $P(D_1) = 0{,}6$, $P(D_2) = 0{,}4$, $P(C|D_1) = 0{,}96$, $P(C|D_2) = 0{,}91$.
  <ul class="sub-sol">
    <li><strong>a) Đúng:</strong> $P(C) = 0{,}6\cdot 0{,}96 + 0{,}4\cdot 0{,}91 = 0{,}94 \Rightarrow P(\overline{C}) = 1 - 0{,}94 = 0{,}06 = 6\%$.</li>
    <li><strong>b) Sai:</strong> $P(C \cap D_2) = 0{,}4 \cdot 0{,}91 = 0{,}364 \ne 0{,}36$.</li>
    <li><strong>c) Sai:</strong> $P(D_1|\overline{C}) = \dfrac{0{,}6\cdot 0{,}04}{0{,}06} = 0{,}4 < P(D_2|\overline{C}) = \dfrac{0{,}4\cdot 0{,}09}{0{,}06} = 0{,}6$.</li>
    <li><strong>d) Đúng:</strong> Xác suất đúng $1$ chip đạt chuẩn trong $2$ chip độc lập là $C_2^1 \cdot 0{,}94 \cdot 0{,}06 = 0{,}1128 = 11{,}28\% > 11\%$.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 4. (S – S – Đ – Đ)</span>
  <ul class="sub-sol">
    <li><strong>a) Sai:</strong> Phương trình đúng phải có vế phải $R^2 = 15^2 = 225 \ne 15$.</li>
    <li><strong>b) Sai:</strong> $d(I, (Oxy)) = 9 \Rightarrow r = \sqrt{15^2 - 9^2} = 12\text{ km} \Rightarrow S = \pi r^2 = 144\pi\text{ km}^2 \ne 120\pi\text{ km}^2$.</li>
    <li><strong>c) Đúng:</strong> Tọa độ máy bay tại thời điểm $t$: $M(-16 + 0{,}2t;\; -8 + 0{,}2t;\; 9 + 0{,}1t)$. Đặt $u = 0{,}1t \Rightarrow \overrightarrow{IM} = (2u - 18;\; 2u - 9;\; u)$, nên $IM^2 = 9u^2 - 108u + 405 = 9(u - 6)^2 + 81 \ge 81 \Rightarrow IM_{\min} = 9\text{ km}$.</li>
    <li><strong>d) Đúng:</strong> $IM \le 15 \Leftrightarrow 9(u - 6)^2 + 81 \le 225 \Leftrightarrow (u - 6)^2 \le 16 \Leftrightarrow 2 \le u \le 10 \Leftrightarrow 20 \le t \le 100$. Thời gian máy bay nằm trong vùng radar là $100 - 20 = 80\text{ giây}$.</li>
  </ul>
</div>

<h4>PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN</h4>

<div class="solution-block">
  <span class="q-head">Câu 1. Đáp số: 144.</span> Chọn hệ trục $Oxyz$ với gốc $O$ là giao điểm hai trục trụ (trùng $Ox, Oy$). Hai khối trụ xác định bởi $y^2 + z^2 \le 9$ và $x^2 + z^2 \le 9$. Thiết diện vuông góc $Oz$ tại cao độ $z \in [-3; 3]$ là hình vuông cạnh $2\sqrt{9 - z^2}$, diện tích $S(z) = 4(9 - z^2)$. Thể tích phần chung:
  $$V = \int_{-3}^3 4(9 - z^2)\,\mathrm{d}z = 8\left.\left(9z - \dfrac{z^3}{3}\right)\right|_0^3 = 8(27 - 9) = 144\text{ cm}^3.$$
</div>

<div class="solution-block">
  <span class="q-head">Câu 2. Đáp số: 46,8.</span> Bán kính $R = \dfrac{AD}{2} = 6\text{ dm}$. Đặt $\widehat{COD} = \theta \in \left(0; \dfrac{\pi}{2}\right)$. Ta có đường cao $CH = R\sin\theta$, đáy nhỏ $BC = 2R\cos\theta$, đáy lớn $AD = 2R$. Diện tích hình thang:
  $$S(\theta) = \dfrac{AD + BC}{2}\cdot CH = R^2(1 + \cos\theta)\sin\theta \Rightarrow S'(\theta) = R^2(2\cos^2\theta + \cos\theta - 1) = R^2(2\cos\theta - 1)(\cos\theta + 1).$$
  Giải $S'(\theta) = 0$ trên $\left(0; \dfrac{\pi}{2}\right)$ được $\cos\theta = \dfrac{1}{2} \Rightarrow \theta = \dfrac{\pi}{3}$. Khi đó $S_{\max} = \dfrac{3\sqrt{3}}{4}R^2 = 27\sqrt{3} \approx 46{,}765 \to 46{,}8\text{ dm}^2$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 3. Đáp số: 2,81.</span> Chọn hệ trục $Oxyz$ sao cho $A(0; 0; 0)$, $B(6; 0; 0)$, $C(3; 3\sqrt{3}; 0)$, $B'(6; 0; 8)$, $C'(3; 3\sqrt{3}; 8)$. Ta có $\overrightarrow{AB'} = (6; 0; 8)$, $\overrightarrow{BC'} = (-3; 3\sqrt{3}; 8)$, $\overrightarrow{AB} = (6; 0; 0)$. Tính tích có hướng:
  $$\left[\overrightarrow{AB'}, \overrightarrow{BC'}\right] = \left(-24\sqrt{3};\; -72;\; 18\sqrt{3}\right) = 6\left(-4\sqrt{3};\; -12;\; 3\sqrt{3}\right).$$
  Chọn $\vec{n} = (-4\sqrt{3}; -12; 3\sqrt{3})$, suy ra $d(AB', BC') = \dfrac{|\vec{n}\cdot \overrightarrow{AB}|}{|\vec{n}|} = \dfrac{|-24\sqrt{3}|}{\sqrt{48 + 144 + 27}} = \dfrac{24\sqrt{3}}{\sqrt{219}} = \dfrac{24}{\sqrt{73}} \approx 2{,}8090 \to 2{,}81\text{ m}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 4. Đáp số: 6.</span> Tại thời điểm $t \ge 0$, vị trí hai UAV là $M(-4 + 3t;\; -2 + 2t;\; 7)$ và $N(4 + t;\; 5 + t;\; 5 + 2t)$, suy ra $\overrightarrow{MN} = (8 - 2t;\; 7 - t;\; -2 + 2t)$. Bình phương khoảng cách:
  $$MN^2 = (8 - 2t)^2 + (7 - t)^2 + (-2 + 2t)^2 = 9t^2 - 54t + 117 = 9(t - 3)^2 + 36 \ge 36.$$
  Đạt dấu bằng tại $t = 3\text{ s} > 0$, do đó khoảng cách ngắn nhất giữa hai UAV bằng $\sqrt{36} = 6\text{ m}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 5. Đáp số: 0,04.</span> Bốn đỉnh lập thành tứ giác chia đường tròn thành $4$ cung liên tiếp có độ dài (đơn vị cung $30^\circ$) là $x_1, x_2, x_3, x_4 \ge 1$ với $x_1 + x_2 + x_3 + x_4 = 12$. Hai đường chéo vuông góc khi và chỉ khi $x_1 + x_3 = 6$ ($5$ cặp) và $x_2 + x_4 = 6$ ($5$ cặp). Chọn đỉnh xuất phát có $12$ cách, mỗi tứ giác lặp lại $4$ lần nên số tứ giác có hai đường chéo vuông góc là $\dfrac{12 \times 5 \times 5}{4} = 75$. Trong đó có $3$ hình vuông ($x_1 = x_2 = x_3 = x_4 = 3$), vậy xác suất cần tìm là $\dfrac{3}{75} = \dfrac{1}{25} = 0{,}04$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 6. Đáp số: 0,31.</span> Gọi $H_0, H_1, H_2$ lần lượt là biến cố $2$ viên bi lấy từ hộp I có: $0$ bi đỏ ($2$ bi xanh); $1$ bi đỏ và $1$ bi xanh; $2$ bi đỏ. Theo xác suất cổ điển ($C_9^2 = 36$):
  $$P(H_0) = \dfrac{C_4^2}{36} = \dfrac{6}{36}, \qquad P(H_1) = \dfrac{C_5^1 C_4^1}{36} = \dfrac{20}{36}, \qquad P(H_2) = \dfrac{C_5^2}{36} = \dfrac{10}{36}.$$
  Gọi $A$ là biến cố $2$ viên bi lấy từ hộp II có cùng màu ($C_{11}^2 = 55$). Ở từng trường hợp ta có $P(A|H_0) = \dfrac{C_6^2 + C_5^2}{55} = \dfrac{25}{55}$, $P(A|H_1) = \dfrac{C_7^2 + C_4^2}{55} = \dfrac{27}{55}$, $P(A|H_2) = \dfrac{C_8^2 + C_3^2}{55} = \dfrac{31}{55}$. Theo công thức xác suất toàn phần và công thức Bayes:
  $$P(A) = \dfrac{6\cdot 25 + 20\cdot 27 + 10\cdot 31}{36\cdot 55} = \dfrac{1000}{36\cdot 55} \implies P(H_2|A) = \dfrac{10\cdot 31}{1000} = 0{,}31.$$
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

html_filename = 'hdg_de_201.html'
pdf_name = 'Bang_Dap_An_Va_HDG_De_201.pdf'

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

print("Running Chrome to generate HDG 201 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
