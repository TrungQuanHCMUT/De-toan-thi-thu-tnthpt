import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 108)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 6.5mm;
  margin-bottom: 6.5mm;
  margin-left: 13mm;
  margin-right: 13mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 108";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.75pt;
  line-height: 1.36;
  color: #000;
  margin: 0;
  padding: 0;
}

/* Tinh chỉnh dấu mũi tên chỉ vectơ to, rõ và trùm đỉnh */
.katex .accent-vec > svg {
  transform: scale(1.4);
  transform-origin: center bottom;
}
.katex .svg-align > svg {
  transform: scale(1.25);
  transform-origin: center bottom;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2px;
}

.header-table td {
  vertical-align: top;
  padding: 0;
}

.left-header {
  width: 44%;
  text-align: center;
}

.right-header {
  width: 56%;
  text-align: center;
}

.title-main {
  font-size: 11.5pt;
  font-weight: bold;
  text-transform: uppercase;
}

.author-title {
  font-size: 10.5pt;
  font-style: italic;
  margin-top: 1px;
}

.exam-title {
  font-size: 11.5pt;
  font-weight: bold;
  line-height: 1.25;
  text-transform: uppercase;
}

.subject-title {
  font-size: 11.2pt;
  font-weight: bold;
  margin-top: 2px;
}

.time-title {
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 1px;
}

.left-box {
  border: 1px solid #000;
  padding: 2px 6px;
  text-align: center;
  width: 175px;
  margin: 3px auto 0 auto;
  line-height: 1.22;
}

.left-box .bold-text {
  font-weight: bold;
  font-size: 10pt;
}

.left-box .sub-text {
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
}

.right-box {
  border: 1.3px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 2px;
}

.solid-divider {
  border-top: 1px solid #000;
  margin: 3px 0 1.5px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 2.5px 0 4px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 10pt;
  font-style: italic;
  margin-bottom: 2px;
}

.section-title {
  font-weight: bold;
  font-size: 10.8pt;
  margin-top: 4px;
  margin-bottom: 2px;
  text-align: justify;
}

.section-subtitle {
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 3.5px;
}

.question {
  margin-bottom: 4.5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 2px;
  margin-bottom: 2.5px;
  padding-left: 5px;
  align-items: center;
}

.options-grid div {
  display: flex;
  align-items: center;
  gap: 3.5px;
}

.grid-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.grid-2 {
  grid-template-columns: 1fr 1fr;
}

.sub-item {
  margin-left: 18px;
  margin-top: 2.5px;
  margin-bottom: 3px;
  line-height: 1.4;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 12px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9.5pt;
}

.bbt-table {
  margin: 4px auto;
  border-collapse: collapse;
  text-align: center;
  font-size: 10pt;
  border: 1px solid #000;
}

.bbt-table td {
  padding: 2.5px 11px;
}

.bbt-border-r {
  border-right: 1px solid #000;
  font-weight: bold;
}

.bbt-border-b {
  border-bottom: 1px solid #000;
}
</style>
</head>
<body>

<!-- HEADER -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 03 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 108</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <table class="bbt-table">
    <tr class="bbt-border-b">
      <td class="bbt-border-r">$x$</td>
      <td>$-\infty$</td>
      <td></td>
      <td>$-2$</td>
      <td></td>
      <td>$1$</td>
      <td></td>
      <td>$+\infty$</td>
    </tr>
    <tr class="bbt-border-b">
      <td class="bbt-border-r">$f'(x)$</td>
      <td></td>
      <td>$+$</td>
      <td>$0$</td>
      <td>$-$</td>
      <td>$0$</td>
      <td>$+$</td>
      <td></td>
    </tr>
    <tr>
      <td class="bbt-border-r">$f(x)$</td>
      <td>$-\infty$</td>
      <td>$\nearrow$</td>
      <td>$3$</td>
      <td>$\searrow$</td>
      <td>$-2$</td>
      <td>$\nearrow$</td>
      <td>$+\infty$</td>
    </tr>
  </table>
  Hàm số đã cho đồng biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-2; 1)$.</div>
    <div><b>B.</b> $(1; 3)$.</div>
    <div><b>C.</b> $(-\infty; -2)$.</div>
    <div><b>D.</b> $(-2; +\infty)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x^2 + 2$ trên đoạn $[0; 3]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $2$.</div>
    <div><b>B.</b> $0$.</div>
    <div><b>C.</b> $-4$.</div>
    <div><b>D.</b> $-2$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Biết $F(x) = x^3$ là một nguyên hàm của hàm số $f(x)$ trên $\mathbb{R}$. Giá trị của $\int_{1}^{2} [2 + f(x)]\,\mathrm{d}x$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $9$.</div>
    <div><b>B.</b> $7$.</div>
    <div><b>C.</b> $11$.</div>
    <div><b>D.</b> $5$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Họ tất cả các nguyên hàm của hàm số $f(x) = e^{2x} + \cos x$ là
  <div class="options-grid grid-2">
    <div><b>A.</b> $2e^{2x} - \sin x + C$.</div>
    <div><b>B.</b> $\dfrac{1}{2}e^{2x} - \sin x + C$.</div>
    <div><b>C.</b> $\dfrac{1}{2}e^{2x} + \sin x + C$.</div>
    <div><b>D.</b> $e^{2x} + \sin x + C$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Cho $\int_{0}^{2} f(x)\,\mathrm{d}x = 3$ và $\int_{0}^{2} g(x)\,\mathrm{d}x = -1$. Khi đó $\int_{0}^{2} [2f(x) - 3g(x)]\,\mathrm{d}x$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $-9$.</div>
    <div><b>D.</b> $9$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Thể tích $V$ của khối tròn xoay sinh ra khi quay hình phẳng giới hạn bởi đồ thị hàm số $y = e^x$, trục hoành $y = 0$ và hai đường thẳng $x = 0, x = 1$ quanh trục hoành bằng
  <div class="options-grid grid-2">
    <div><b>A.</b> $\dfrac{\pi(e^2 + 1)}{2}$.</div>
    <div><b>B.</b> $\dfrac{\pi(e^2 - 1)}{2}$.</div>
    <div><b>C.</b> $\pi(e^2 - 1)$.</div>
    <div><b>D.</b> $\dfrac{e^2 - 1}{2}$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2 - 2x$ và trục hoành bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $-\dfrac{4}{3}$.</div>
    <div><b>B.</b> $\dfrac{8}{3}$.</div>
    <div><b>C.</b> $\dfrac{4}{3}$.</div>
    <div><b>D.</b> $\dfrac{2}{3}$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian $Oxyz$, cho hai điểm $A(1; 2; -1)$ và $B(3; 0; 2)$. Tọa độ của vectơ $\overrightarrow{AB}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-2; 2; -3)$.</div>
    <div><b>B.</b> $(4; 2; 1)$.</div>
    <div><b>C.</b> $(2; -1; 1)$.</div>
    <div><b>D.</b> $(2; -2; 3)$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(2; -1; 3)$, $B(4; 0; 1)$ và $C(0; 4; -1)$. Tọa độ trọng tâm $G$ của tam giác $ABC$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $G(2; 1; 1)$.</div>
    <div><b>B.</b> $G(6; 3; 3)$.</div>
    <div><b>C.</b> $G(1; 1; 2)$.</div>
    <div><b>D.</b> $G(2; 3; 1)$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, cho hai vectơ $\overrightarrow{u} = (1; 0; -2)$ và $\overrightarrow{v} = (2; -1; 1)$. Tích vô hướng $\overrightarrow{u} \cdot \overrightarrow{v}$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $4$.</div>
    <div><b>B.</b> $0$.</div>
    <div><b>C.</b> $-2$.</div>
    <div><b>D.</b> $1$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Trong không gian, cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Giá trị của $|\overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AA'}|$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $a\sqrt{3}$.</div>
    <div><b>B.</b> $a\sqrt{2}$.</div>
    <div><b>C.</b> $3a$.</div>
    <div><b>D.</b> $a$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Một chiếc đèn chùm có khối lượng $m = 6\text{ kg}$ được treo cân bằng trên trần nhà bởi ba sợi dây cáp không giãn. Gọi các lực căng tác dụng lên đèn bởi ba sợi dây lần lượt là $\overrightarrow{F}_1, \overrightarrow{F}_2, \overrightarrow{F}_3$, và trọng lực của đèn là $\overrightarrow{P}$ (lấy gia tốc trọng trường $g = 9,8\text{ m/s}^2$). Do đèn ở trạng thái cân bằng nên độ lớn của hợp lực $\overrightarrow{F}_1 + \overrightarrow{F}_2 + \overrightarrow{F}_3$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $19,6\text{ N}$.</div>
    <div><b>B.</b> $58,8\text{ N}$.</div>
    <div><b>C.</b> $0\text{ N}$.</div>
    <div><b>D.</b> $117,6\text{ N}$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div class="section-title" style="margin-top: 8px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \sqrt{e^{2x} - 2e^x + 2}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tập xác định của hàm số là $D = \mathbb{R}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số đã cho là $f'(x) = \dfrac{e^x - 1}{\sqrt{e^{2x} - 2e^x + 2}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số đã cho có một điểm cực đại.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đồ thị $(C)$ có đường tiệm cận ngang là $y = \sqrt{2}$.</div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x)$ liên tục và không âm trên $\mathbb{R}$ thoả mãn $f(2) = 4$ và $\int_{0}^{2} f(x)\,\mathrm{d}x = 3$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> $\int_{0}^{2} [3f(x) - 2x]\,\mathrm{d}x = 5$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> $\int_{0}^{1} f(2x)\,\mathrm{d}x = 3$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Thể tích khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đồ thị hàm số $y = \sqrt{f(x)}$, trục hoành và hai đường thẳng $x = 0, x = 2$ quanh trục $Ox$ bằng $3\pi$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Nếu $F(x)$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$ thoả mãn $F(0) = 1$ thì $F(2) = 4$.</div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Một vật chuyển động thẳng với gia tốc $a(t) = 3t^2 + 2t\text{ (m/s}^2\text{)}$, trong đó $t$ là thời gian tính bằng giây ($t \ge 0$). Vận tốc ban đầu của vật là $v(0) = 5\text{ m/s}$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Vận tốc của vật tại thời điểm $t$ là $v(t) = t^3 + t^2 + 5\text{ (m/s)}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tại thời điểm $t = 2\text{ s}$, vận tốc của vật đạt $15\text{ m/s}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Quãng đường vật đi được từ thời điểm $t = 0\text{ s}$ đến thời điểm $t = 3\text{ s}$ là $44,25\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Vận tốc trung bình của vật trong khoảng thời gian từ $t = 0\text{ s}$ đến $t = 3\text{ s}$ là $15\text{ m/s}$.</div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1; 0; 2)$, $B(-1; 1; 3)$, $C(3; 2; 1)$ và $D(3; -2; 3)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tọa độ của vectơ $\overrightarrow{AB}$ là $(-2; 1; 1)$ và độ dài đoạn thẳng $AB$ bằng $\sqrt{6}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vectơ $\overrightarrow{AC} = (2; 2; -1)$ và côsin của góc giữa hai vectơ $\overrightarrow{AB}$ và $\overrightarrow{AC}$ là $\cos(\overrightarrow{AB}, \overrightarrow{AC}) = -\dfrac{\sqrt{6}}{6}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Gọi $M$ là chân đường phân giác trong kẻ từ đỉnh $A$ của tam giác $ACD$. Khi đó tọa độ của điểm $M$ là $M(3; 0; 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Bốn điểm $A, B, C, D$ đồng phẳng.</div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div class="section-title" style="margin-top: 8px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Một xưởng sản xuất cần chế tạo một chiếc hộp đựng quà có nắp dạng hình hộp chữ nhật có đáy là hình vuông, thể tích bằng $432\text{ cm}^3$. Chi phí làm nắp và đáy là $8.000\text{ đồng/cm}^2$, trong khi chi phí làm bốn mặt xung quanh là $4.000\text{ đồng/cm}^2$. Để tổng chi phí vật liệu làm chiếc hộp là nhỏ nhất thì chiều cao của chiếc hộp đó phải bằng bao nhiêu centimét?
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Trên bức tường cần trang trí một hình phẳng dạng parabol đỉnh $S$ như hình vẽ, biết $OS = AB = 4\text{ m}$, $O$ là trung điểm $AB$. Parabol trên được chia thành ba phần để sơn ba màu khác nhau với mức chi phí: phần trên là phần kẻ sọc $140.000\text{ đồng/m}^2$, phần giữa là hình quạt tâm $O$, bán kính $2\text{ m}$ được tô đậm $150.000\text{ đồng/m}^2$, phần còn lại $160.000\text{ đồng/m}^2$. Tổng chi phí để sơn cả ba phần bằng bao nhiêu nghìn đồng? <i>(kết quả làm tròn đến hàng đơn vị)</i>.
  <div style="text-align: center; margin: 2px auto;">
    <img src="assets/hinh_cau2_phan3.png" style="width: 74mm; max-width: 90%;" alt="Minh hoạ Câu 2">
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Có một cốc thủy tinh hình trụ, bán kính trong lòng đáy cốc là $6\text{ cm}$, chiều cao trong lòng cốc là $10\text{ cm}$ đang đựng một lượng nước. Biết rằng khi nghiêng cốc nước sao cho mép nước vừa lúc chạm miệng cốc thì mặt nước ở đáy cốc trùng với một đường kính đáy cốc (như hình vẽ minh hoạ). Tính thể tích lượng nước có trong cốc (theo đơn vị $\text{cm}^3$).
  <div style="text-align: center; margin: 2px auto;">
    <img src="assets/hinh_cau3_phan3.png" style="width: 96mm; max-width: 95%;" alt="Minh hoạ Câu 3">
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Một đoàn tàu cao tốc đang di chuyển với vận tốc $48\text{ m/s}$ thì người lái tàu bắt đầu hãm phanh. Kể từ thời điểm đó, tàu chuyển động chậm dần với gia tốc biến thiên theo thời gian là $a(t) = -2t - 2\text{ (m/s}^2\text{)}$ (với $t$ tính bằng giây). Hỏi từ lúc bắt đầu hãm phanh đến khi tàu dừng hẳn, tàu đã di chuyển được một quãng đường bằng bao nhiêu mét?
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Trong không gian $Oxyz$ (đơn vị trên mỗi trục toạ độ là $1\text{ km}$), một đài kiểm soát không lưu được đặt tại gốc toạ độ $O(0; 0; 0)$. Một máy bay dân dụng bay theo đường thẳng từ vị trí $A(1; 8; 12)$ đến vị trí $B(7; 4; 12)$. Hỏi trong suốt chặng bay thẳng từ $A$ đến $B$, khoảng cách ngắn nhất từ máy bay đến đài kiểm soát không lưu $O$ bằng bao nhiêu kilômét?
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(2; 1; -1)$, $B(0; 3; 1)$ và $C(4; -1; 3)$. Điểm $M(a; b; 0)$ thuộc mặt phẳng toạ độ $(Oxy)$ sao cho biểu thức $|\overrightarrow{MA} + \overrightarrow{MB} + \overrightarrow{MC}|$ đạt giá trị nhỏ nhất. Giá trị của $a + b$ bằng bao nhiêu?
</div>

<div class="end-exam">----------------------- HẾT -----------------------</div>
<div class="end-note">Học sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

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

html_path = 'exam_de_khao_sat_toan_12_ma108.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'De_Thi_Khao_Sat_Toan_12_Ma_108.pdf'
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
