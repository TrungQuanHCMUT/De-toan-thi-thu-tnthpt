#!/usr/bin/env python3
"""Generate Bang_Dap_An_Va_HDG_De_202.pdf matching De 201 solution sheet layout."""
import os
import subprocess
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 202</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4 portrait;
  margin: 10mm 12mm 10mm 12mm;
}
* { box-sizing: border-box; }
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 9.8pt;
  line-height: 1.32;
  color: #111;
  margin: 0;
  padding: 0;
}
.katex { font-size: 1.0em; }
.katex-display { margin: 3px 0; }
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
  page-break-inside: avoid;
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
  <h2>ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA – MÔN TOÁN (MÃ ĐỀ 202)</h2>
  <div class="meta">Chương trình GDPT 2018 (Toán lớp 10, 11, 12) – Thời gian làm bài: 90 phút &nbsp;|&nbsp; Biên soạn: Trần Trung Quân</div>
</div>

<h3>A. BẢNG ĐÁP ÁN</h3>

<h4>PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (3,0 điểm)</h4>
<table class="key-table">
  <tr>
    <th>Câu</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <th>Đáp án</th><td><strong>B</strong></td><td><strong>D</strong></td><td><strong>A</strong></td><td><strong>C</strong></td><td><strong>A</strong></td><td><strong>C</strong></td><td><strong>B</strong></td><td><strong>D</strong></td><td><strong>A</strong></td><td><strong>C</strong></td><td><strong>B</strong></td><td><strong>D</strong></td>
  </tr>
</table>

<div class="grid-2">
  <div>
    <h4>PHẦN II. Trắc nghiệm đúng sai (4,0 điểm)</h4>
    <table class="key-table">
      <tr><th>Câu</th><th>Ý a)</th><th>Ý b)</th><th>Ý c)</th><th>Ý d)</th></tr>
      <tr><th>Câu 1</th><td><strong>Đúng</strong></td><td><strong>Sai</strong></td><td><strong>Đúng</strong></td><td><strong>Sai</strong></td></tr>
      <tr><th>Câu 2</th><td><strong>Sai</strong></td><td><strong>Đúng</strong></td><td><strong>Đúng</strong></td><td><strong>Sai</strong></td></tr>
      <tr><th>Câu 3</th><td><strong>Đúng</strong></td><td><strong>Sai</strong></td><td><strong>Sai</strong></td><td><strong>Đúng</strong></td></tr>
      <tr><th>Câu 4</th><td><strong>Sai</strong></td><td><strong>Đúng</strong></td><td><strong>Đúng</strong></td><td><strong>Sai</strong></td></tr>
    </table>
  </div>
  <div>
    <h4>PHẦN III. Trắc nghiệm trả lời ngắn (3,0 điểm)</h4>
    <table class="key-table" style="margin-top: 8px;">
      <tr><th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th></tr>
      <tr><th>Đáp án</th><td><strong>40,1</strong></td><td><strong>12,5</strong></td><td><strong>192</strong></td><td><strong>13</strong></td><td><strong>0,18</strong></td><td><strong>0,48</strong></td></tr>
    </table>
  </div>
</div>

<h3>B. HƯỚNG DẪN GIẢI CHI TIẾT</h3>

<h4>PHẦN I. Trắc nghiệm nhiều phương án lựa chọn</h4>

<div class="solution-block"><span class="q-head">Câu 1 (Chọn B):</span> Số hạng tổng quát $C_4^k (2x)^{4-k}(-1)^k$. Ứng với $x^2$ ta có $4 - k = 2 \iff k = 2$, hệ số bằng $C_4^2 \cdot 2^2 \cdot (-1)^2 = 6 \cdot 4 = 24.$</div>

<div class="solution-block"><span class="q-head">Câu 2 (Chọn D):</span> $\displaystyle\int_1^4 \big[2f(x) - 3g(x)\big]\,dx = 2\int_1^4 f(x)\,dx - 3\int_1^4 g(x)\,dx = 2(6) - 3(-2) = 18$.</div>

<div class="solution-block"><span class="q-head">Câu 3 (Chọn A):</span> Áp dụng công thức $(a^u)' = u' \cdot a^u \ln a$: $y' = 2 \cdot 5^{2x - 1} \ln 5$.</div>

<div class="solution-block"><span class="q-head">Câu 4 (Chọn C):</span> $\cos(\vec{u}, \vec{v}) = \dfrac{1\cdot 0 + 1\cdot 1 + 0\cdot 1}{\sqrt{1^2+1^2}\cdot\sqrt{1^2+1^2}} = \dfrac{1}{2} \implies (\vec{u}, \vec{v}) = 60^\circ$.</div>

<div class="solution-block"><span class="q-head">Câu 5 (Chọn A):</span> $P = \log_a(a^3) + \log_a(b^2) = 3 + 2\log_a b = 3 + 2 \cdot 4 = 11$.</div>

<div class="solution-block"><span class="q-head">Câu 6 (Chọn C):</span> $y' = 1 - \dfrac{4}{x^2} = 0 \iff x = 2 \in [1; 3]$. Ta có $y(1) = 5$, $y(2) = 4$, $y(3) = \dfrac{13}{3}$, nên $\min_{[1;3]} y = 4$.</div>

<div class="solution-block"><span class="q-head">Câu 7 (Chọn B):</span> $\cos 2x = \dfrac{\sqrt{2}}{2} \iff 2x = \pm \dfrac{\pi}{4} + k2\pi \iff x = \pm \dfrac{\pi}{8} + k\pi \ (k \in \mathbb{Z})$.</div>

<div class="solution-block"><span class="q-head">Câu 8 (Chọn D):</span> $S_{ABC} = \dfrac{1}{2} \cdot 2a \cdot 2a = 2a^2 \implies V = S_{ABC} \cdot AA' = 2a^2 \cdot 3a = 6a^3$.</div>

<div class="solution-block"><span class="q-head">Câu 9 (Chọn A):</span> Mặt phẳng qua $M(1; -2; 3)$ có VTPT $\vec{n} = (2; -3; 1)$: $2(x - 1) - 3(y + 2) + (z - 3) = 0 \iff 2x - 3y + z - 11 = 0$.</div>

<div class="solution-block"><span class="q-head">Câu 10 (Chọn C):</span> Nhóm chứa mốt là $[160; 165)$ ($n_m = 16$). $M_o = 160 + \dfrac{16 - 10}{(16 - 10) + (16 - 12)} \cdot 5 = 160 + \dfrac{6}{10} \cdot 5 = 163$.</div>

<div class="solution-block"><span class="q-head">Câu 11 (Chọn B):</span> $P(A \cap B) = P(B)P(A|B) = 0{,}4 \cdot 0{,}3 = 0{,}12$. Suy ra $P(A \cup B) = 0{,}5 + 0{,}4 - 0{,}12 = 0{,}78$.</div>

<div class="solution-block"><span class="q-head">Câu 12 (Chọn D):</span> $\dfrac{3n - 2}{n + 1} = \dfrac{19}{8} \iff 24n - 16 = 19n + 19 \iff 5n = 35 \iff n = 7$.</div>

<h4>PHẦN II. Trắc nghiệm đúng sai</h4>

<div class="solution-block">
  <span class="q-head">Câu 1:</span> $f(x) = (x^2 - 3x + 1)e^x$.
  <ul class="sub-sol">
    <li><strong>a) Đúng:</strong> $f'(x) = (2x - 3 + x^2 - 3x + 1)e^x = (x^2 - x - 2)e^x = (x + 1)(x - 2)e^x$.</li>
    <li><strong>b) Sai:</strong> $f'(x)$ đổi dấu $+$ sang $-$ qua $x = -1$ (cực đại) và $-$ sang $+$ qua $x = 2$ (cực tiểu).</li>
    <li><strong>c) Đúng:</strong> $f(0) = 1$, $f(2) = -e^2$, $f(3) = e^3 \implies \max_{[0; 3]} f(x) = e^3$.</li>
    <li><strong>d) Sai:</strong> $x^2 - 3x + 1 = 0$ có $\Delta = 5 > 0$ nên phương trình $f(x) = 0$ có $2$ nghiệm phân biệt.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 2:</span> $V(0) = 100\text{ m}^3$, $V'(t) = v_1(t) - v_2(t) = -0{,}03t^2 + 0{,}3t + 6 = -0{,}03(t - 20)(t + 10)$.
  <ul class="sub-sol">
    <li><strong>a) Sai:</strong> Lượng nước bơm vào trong $10$ phút đầu bằng $\int_0^{10} (0{,}3t + 8)\,dt = [0{,}15t^2 + 8t]_0^{10} = 95\text{ m}^3$.</li>
    <li><strong>b) Đúng:</strong> Với $t \in [0; 20)$, $V'(t) > 0$ nên lượng nước tăng liên tục.</li>
    <li><strong>c) Đúng:</strong> $V(t)$ đạt cực đại duy nhất trên $[0; 30]$ tại $t = 20$: $V(20) = 100 + [-0{,}01t^3 + 0{,}15t^2 + 6t]_0^{20} = 100 - 80 + 60 + 120 = 200\text{ m}^3$.</li>
    <li><strong>d) Sai:</strong> $V(30) = 100 - 270 + 135 + 180 = 145\text{ m}^3 < 150\text{ m}^3$.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 3:</span> Bước 1 chọn $2$ bi từ $11$ bi ($C_{11}^2 = 55$). Gọi $A_0, A_1, A_2$ là biến cố chuyển được $0, 1, 2$ bi trắng sang Hộp II: $P(A_0) = \dfrac{C_5^2}{55} = \dfrac{2}{11},$ $P(A_1) = \dfrac{C_6^1 C_5^1}{55} = \dfrac{6}{11},$ $P(A_2) = \dfrac{C_6^2}{55} = \dfrac{3}{11}.$ Bước 2 chọn $2$ bi từ $9$ bi ($C_9^2 = 36$).
  <ul class="sub-sol">
    <li><strong>a) Đúng:</strong> $P(A_0 \cup A_2) = \dfrac{10 + 15}{55} = \dfrac{25}{55} = \dfrac{5}{11}$.</li>
    <li><strong>b) Sai:</strong> Với $A_2$, Hộp II có $5$ trắng, $4$ đen $\implies P(T|A_2) = \dfrac{C_5^2}{C_9^2} = \dfrac{10}{36} = \dfrac{5}{18} \ne \dfrac{1}{3}$.</li>
    <li><strong>c) Sai:</strong> Xác suất $2$ bi khác màu là $P(M) = \dfrac{2}{11}\cdot\dfrac{18}{36} + \dfrac{6}{11}\cdot\dfrac{20}{36} + \dfrac{3}{11}\cdot\dfrac{20}{36} = \dfrac{6}{11} \implies P(\text{cùng màu}) = 1 - \dfrac{6}{11} = \dfrac{5}{11}$.</li>
    <li><strong>d) Đúng:</strong> $P(T) = \dfrac{2}{11}\cdot\dfrac{3}{36} + \dfrac{6}{11}\cdot\dfrac{6}{36} + \dfrac{3}{11}\cdot\dfrac{10}{36} = \dfrac{72}{11\cdot 36} = \dfrac{2}{11} \implies P(A_1|T) = \dfrac{\frac{6}{11}\cdot\frac{6}{36}}{\frac{2}{11}} = \dfrac{1}{2}$.</li>
  </ul>
</div>

<div class="solution-block">
  <span class="q-head">Câu 4:</span> $(\alpha): x + 2y + 2z - 48 = 0$ có $\vec{n} = (1; 2; 2)$ ($|\vec{n}| = 3$); $(Oxy)$ có $\vec{k} = (0; 0; 1)$.
  <ul class="sub-sol">
    <li><strong>a) Sai:</strong> $\cos\varphi = \dfrac{2}{3} < \dfrac{\sqrt{2}}{2} \implies \varphi \approx 48{,}2^\circ > 45^\circ$.</li>
    <li><strong>b) Đúng:</strong> $d(S, (\alpha)) = \dfrac{|10 + 18 + 38 - 48|}{3} = \dfrac{18}{3} = 6\text{ m}$.</li>
    <li><strong>c) Đúng:</strong> Hình chiếu của $S(10; 9; 19)$ lên $(\alpha)$ là $K = S - \dfrac{18}{9}(1; 2; 2) = (8; 5; 15)$.</li>
    <li><strong>d) Sai:</strong> $A(4; 9; 13) \in (\alpha)$ và $KA = \sqrt{(-4)^2 + 4^2 + (-2)^2} = 6 = SK \implies \widehat{SAK} = 45^\circ$.</li>
  </ul>
</div>

<h4>PHẦN III. Trắc nghiệm trả lời ngắn</h4>

<div class="solution-block">
  <span class="q-head">Câu 1 (Đáp số: 40,1):</span> Đặt hệ trục $Oxy$ tâm $O(0; 0)$, đường tròn $x^2 + y^2 = 25$, $C(0; -5)$, $A(-3; 4)$, $B(3; 4)$. Parabol $(P)$ đỉnh $C(0; -5)$ qua $B(3; 4)$ là $y = x^2 - 5$.
  $$S = 2\int_0^3 \left(\sqrt{25 - x^2} - (x^2 - 5)\right)dx = 25\arcsin\frac{3}{5} + 24 \approx 40{,}0875 \approx 40{,}1\text{ dm}^2.$$
</div>

<div class="solution-block">
  <span class="q-head">Câu 2 (Đáp số: 12,5):</span> Xét góc $\theta \in \left(0; \frac{\pi}{2}\right)$ giữa thanh thép và tường nhánh $2{,}7\text{ m}$: $L(\theta) = \dfrac{2{,}7}{\sin\theta} + \dfrac{6{,}4}{\cos\theta}$.
  $$L'(\theta) = 0 \iff \tan^3\theta = \frac{2{,}7}{6{,}4} = \frac{27}{64} \iff \tan\theta = \frac{3}{4} \implies \sin\theta = 0{,}6,\ \cos\theta = 0{,}8.$$
  Suy ra $L_{\max} = \min L(\theta) = \dfrac{2{,}7}{0{,}6} + \dfrac{6{,}4}{0{,}8} = 4{,}5 + 8 = 12{,}5\text{ m}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 3 (Đáp số: 192):</span> $\triangle ABC$ cân tại $A$ có $BH = 6 \implies AH = \sqrt{10^2 - 6^2} = 8$, $S_{ABC} = 48$. Do $BC \perp (AA'H)$, kẻ $HK \perp AA'$ tại $K$ thì $HK = d(AA', BC) = 4{,}8$.
  Trong $\triangle AA'H$ vuông tại $H$: $\dfrac{1}{A'H^2} = \dfrac{1}{4{,}8^2} - \dfrac{1}{8^2} = \dfrac{1}{36} \implies A'H = 6$. Vậy $V_{A'.BCC'B'} = \dfrac{2}{3} V_{ABC.A'B'C'} = \dfrac{2}{3} \cdot 48 \cdot 6 = 192$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 4 (Đáp số: 13):</span> $(S)$ có tâm $I(1; 4; 6)$, $R = 5$. $d(I, (P)) = \dfrac{|1 + 8 + 12 - 12|}{3} = 3 \implies$ bán kính đường tròn $(C)$ là $r = \sqrt{5^2 - 3^2} = 4$, tâm $K = I - (1; 2; 2) = (0; 2; 4)$.
  Hình chiếu của $A(10; 4; 15)$ lên $(P)$ là $H = A - 4(1; 2; 2) = (6; -4; 7)$, $AH = 12$, $HK = \sqrt{6^2 + (-6)^2 + 3^2} = 9$.
  Suy ra $AM_{\min} = \sqrt{AH^2 + (HK - r)^2} = \sqrt{12^2 + (9 - 4)^2} = \sqrt{144 + 25} = 13\text{ m}$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 5 (Đáp số: 0,18):</span> Không gian mẫu $n(\Omega) = 7! = 5040$. Xếp $4$ cuốn Lí, Hóa trước để tạo $5$ khe đặt $3$ cuốn Toán. Xét các cấu hình môn của $4$ cuốn Lí – Hóa:
  LHLH/HLHL ($2$ kiểu $\times C_5^3 = 20$); LLHH/HHLL ($2$ kiểu $\times 3 = 6$, do buộc chèn Toán vào $2$ khe giữa L–L và H–H); LHHL/HLLH ($2$ kiểu $\times C_4^2 = 12$). Tổng $20 + 6 + 12 = 38$ cấu hình môn.
  Nhân $3!2!2! = 24$ hoán vị sách cho $n(A) = 38 \cdot 24 = 912 \implies P = \dfrac{912}{5040} = \dfrac{19}{105} \approx 0{,}18$.
</div>

<div class="solution-block">
  <span class="q-head">Câu 6 (Đáp số: 0,48):</span> Gọi $H_k$ ($k \in \{0; 1; 2; 3\}$) là biến cố Đội A có $k$ nữ; $M$ là biến cố cặp chọn được là nam – nữ ($C_9^3 = 84$).
  Ta có: $P(H_0) = \dfrac{20}{84},\ P(M|H_0) = \dfrac{1}{2}$; $P(H_1) = \dfrac{45}{84},\ P(M|H_1) = \dfrac{4}{9}$; $P(H_2) = \dfrac{18}{84},\ P(M|H_2) = \dfrac{11}{18}$; $P(H_3) = \dfrac{1}{84},\ P(M|H_3) = 1$.
  $$P(M) = \frac{10 + 20 + 11 + 1}{84} = \frac{42}{84} = \frac{1}{2} \implies P(H_1|M) = \frac{20/84}{42/84} = \frac{10}{21} \approx 0{,}48.$$
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

html_path = os.path.join(BASE_DIR, "_tmp_hdg202.html")
pdf_path = os.path.join(BASE_DIR, "Bang_Dap_An_Va_HDG_De_202.pdf")

try:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path,
    ]
    print("Running Chrome to generate HDG 202 PDF...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Chrome exit code:", res.returncode)
finally:
    if os.path.exists(html_path):
        os.remove(html_path)

reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
