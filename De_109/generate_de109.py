import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 109)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 8mm;
  margin-bottom: 8mm;
  margin-left: 13mm;
  margin-right: 13mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 109";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.75pt;
  line-height: 1.38;
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
  margin-bottom: 3px;
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
  padding: 3px 6px;
  display: inline-block;
  margin-top: 5px;
  width: 82%;
  text-align: center;
}

.right-box {
  border: 1px solid #000;
  padding: 3px 6px;
  display: inline-block;
  margin-top: 5px;
  width: 58%;
  text-align: center;
}

.bold-text {
  font-weight: bold;
}

.sub-text {
  font-size: 9.5pt;
  font-style: italic;
}

.student-info {
  margin-top: 5px;
  margin-bottom: 7px;
  display: flex;
  justify-content: space-between;
  font-size: 10.5pt;
}

.separator {
  border-top: 1px dashed #000;
  margin: 4px 0 6px 0;
}

.section-title {
  font-weight: bold;
  font-size: 10.75pt;
  margin-top: 7px;
  margin-bottom: 1px;
  text-align: justify;
}

.section-subtitle {
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 4px;
}

.question {
  margin-bottom: 5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 2.5px;
  margin-bottom: 3px;
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
  margin-top: 14px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9.5pt;
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
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="subject-title">MÔN: TOÁN – LỚP 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian phát đề</div>
      <div class="right-box">
        <span class="bold-text">Mã đề thi: 109</span>
      </div>
    </td>
  </tr>
</table>

<div class="student-info">
  <div>Họ và tên thí sinh: ....................................................................................</div>
  <div>Số báo danh: .............................</div>
</div>

<div class="separator"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = \dfrac{2x - 1}{x + 1}$. Tọa độ giao điểm $I$ của đường tiệm cận đứng và đường tiệm cận ngang của đồ thị hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 2)$.</div>
    <div><b>B.</b> $I(-1; 2)$.</div>
    <div><b>C.</b> $I(-1; -1)$.</div>
    <div><b>D.</b> $I(2; -1)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x)$ xác định và liên tục trên $\mathbb{R}$, có đạo hàm $f'(x) = (x + 1)^2(x - 2)(x - 5)$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $1$.</div>
    <div><b>C.</b> $0$.</div>
    <div><b>D.</b> $2$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Tìm họ tất cả các nguyên hàm của hàm số $f(x) = \dfrac{1}{2x + 1}$ trên khoảng $\left(-\dfrac{1}{2}; +\infty\right)$.
  <div class="options-grid grid-2">
    <div><b>A.</b> $\dfrac{1}{2}\ln(2x + 1) + C$.</div>
    <div><b>B.</b> $\ln(2x + 1) + C$.</div>
    <div><b>C.</b> $-\dfrac{1}{(2x + 1)^2} + C$.</div>
    <div><b>D.</b> $2\ln(2x + 1) + C$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Giá trị của tích phân $I = \int_{0}^{\frac{\pi}{2}} \sin x\,\mathrm{d}x$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $-1$.</div>
    <div><b>B.</b> $0$.</div>
    <div><b>C.</b> $1$.</div>
    <div><b>D.</b> $\dfrac{1}{2}$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Cho $\int_{1}^{3} f(x)\,\mathrm{d}x = 5$ và $\int_{2}^{3} f(x)\,\mathrm{d}x = 2$. Khi đó $\int_{1}^{2} f(x)\,\mathrm{d}x$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $7$.</div>
    <div><b>B.</b> $3$.</div>
    <div><b>C.</b> $-3$.</div>
    <div><b>D.</b> $10$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Diện tích $S$ của hình phẳng giới hạn bởi đồ thị của parabol $y = x^2$ và đường thẳng $y = 2x$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $\dfrac{2}{3}$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $\dfrac{8}{3}$.</div>
    <div><b>D.</b> $\dfrac{4}{3}$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Thể tích $V$ của khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đồ thị hàm số $y = \sqrt{2x + 1}$, trục hoành và hai đường thẳng $x = 0, x = 4$ quanh trục hoành bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $20\pi$.</div>
    <div><b>B.</b> $16\pi$.</div>
    <div><b>C.</b> $24\pi$.</div>
    <div><b>D.</b> $20$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian $Oxyz$, cho hai điểm $A(2; -3; 5)$ và $B(4; 1; -1)$. Tọa độ trung điểm $M$ của đoạn thẳng $AB$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $M(6; -2; 4)$.</div>
    <div><b>B.</b> $M(1; 2; -3)$.</div>
    <div><b>C.</b> $M(3; -1; 2)$.</div>
    <div><b>D.</b> $M(2; 4; -6)$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, cho hai vectơ $\overrightarrow{a} = (1; 2; -2)$ và $\overrightarrow{b} = (-1; 0; 3)$. Tọa độ của vectơ $\overrightarrow{u} = 2\overrightarrow{a} - \overrightarrow{b}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $\overrightarrow{u} = (1; 4; -1)$.</div>
    <div><b>B.</b> $\overrightarrow{u} = (3; 4; -1)$.</div>
    <div><b>C.</b> $\overrightarrow{u} = (1; 4; -7)$.</div>
    <div><b>D.</b> $\overrightarrow{u} = (3; 4; -7)$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, cho hai vectơ $\overrightarrow{u} = (1; 0; 1)$ và $\overrightarrow{v} = (0; 1; -1)$. Côsin của góc giữa hai vectơ $\overrightarrow{u}$ và $\overrightarrow{v}$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $-\dfrac{1}{2}$.</div>
    <div><b>B.</b> $\dfrac{1}{2}$.</div>
    <div><b>C.</b> $-\dfrac{\sqrt{2}}{2}$.</div>
    <div><b>D.</b> $0$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(1; 1; 2)$, $B(2; -1; 1)$ và $C(3; 2; -1)$. Để tứ giác $ABCD$ là hình bình hành thì tọa độ đỉnh $D$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $D(4; 0; 0)$.</div>
    <div><b>B.</b> $D(2; 4; 0)$.</div>
    <div><b>C.</b> $D(0; 4; 2)$.</div>
    <div><b>D.</b> $D(2; -2; 4)$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Một chất điểm chịu tác dụng của ba lực $\overrightarrow{F}_1, \overrightarrow{F}_2, \overrightarrow{F}_3$ cùng đặt tại điểm $O$. Biết hai lực $\overrightarrow{F}_1$ và $\overrightarrow{F}_2$ có phương vuông góc với nhau với độ lớn lần lượt là $|\overrightarrow{F}_1| = 30\text{ N}$ và $|\overrightarrow{F}_2| = 40\text{ N}$. Lực $\overrightarrow{F}_3$ có phương vuông góc với mặt phẳng chứa hai lực $\overrightarrow{F}_1, \overrightarrow{F}_2$ và có độ lớn $|\overrightarrow{F}_3| = 50\text{ N}$. Độ lớn hợp lực $\overrightarrow{F} = \overrightarrow{F}_1 + \overrightarrow{F}_2 + \overrightarrow{F}_3$ tác dụng lên chất điểm bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $120\text{ N}$.</div>
    <div><b>B.</b> $100\text{ N}$.</div>
    <div><b>C.</b> $50\sqrt{2}\text{ N}$.</div>
    <div><b>D.</b> $50\text{ N}$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div class="section-title" style="margin-top: 8px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 3}{x - 1}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị hàm số $(C)$ có đường tiệm cận xiên là đường thẳng $y = x - 2$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho đồng biến trên mỗi khoảng $(-\infty; 0)$ và $(2; +\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Điểm cực đại của đồ thị hàm số $(C)$ là điểm $M(2; 1)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Giao điểm của hai đường tiệm cận là tâm đối xứng của đồ thị $(C)$ có tọa độ là $I(1; 1)$.</div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho tích phân $I = \int_{0}^{1} (2x + 1)e^x\,\mathrm{d}x$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Nếu sử dụng phương pháp tích phân từng phần bằng cách đặt $u = 2x + 1$ và $\mathrm{d}v = e^x\,\mathrm{d}x$ thì ta có $\mathrm{d}u = 2\,\mathrm{d}x$ và chọn $v = e^x$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Giá trị của tích phân $I$ bằng $e + 1$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Áp dụng phương pháp đổi biến số với $t = \ln x$ cho tích phân $J = \int_{1}^{e} \dfrac{\ln x}{x}\,\mathrm{d}x$, ta tính được giá trị $J = \dfrac{1}{2}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Giá trị của tích phân $I$ nhỏ hơn $3$.</div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Một bồn chứa nước hình trụ ban đầu có chứa $200$ lít nước. Người ta bắt đầu bơm thêm nước vào bồn với tốc độ thay đổi theo thời gian được mô hình hóa bởi hàm số $v(t) = 30 + 6t$ (đơn vị: lít/phút), trong đó $t$ là thời gian tính bằng phút kể từ lúc bắt đầu bơm ($0 \le t \le 10$). Gọi $V(t)$ là tổng thể tích nước có trong bồn tại thời điểm $t$ phút ($0 \le t \le 10$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Lượng nước được bơm thêm vào bồn trong khoảng thời gian từ thời điểm $t = 0$ đến thời điểm $t = t_0$ ($0 \le t_0 \le 10$) được xác định bởi công thức $\int_{0}^{t_0} v(t)\,\mathrm{d}t$ (lít).</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tốc độ bơm nước vào bồn tại thời điểm $t = 5$ phút là $60$ lít/phút.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Sau $10$ phút bơm, lượng nước được bơm thêm vào bồn là $500$ lít.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tại thời điểm $t = 10$ phút kể từ lúc bắt đầu bơm, tổng thể tích nước có trong bồn là $800$ lít.</div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(1; 2; -1)$, $B(2; 3; 1)$, $C(0; 1; 2)$ và điểm $D(2; 1; 3)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Vectơ tích có hướng $[\overrightarrow{AB}, \overrightarrow{AC}]$ cùng phương với vectơ $\overrightarrow{n} = (1; -1; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tam giác $ABC$ là tam giác vuông tại đỉnh $A$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Diện tích của tam giác $ABC$ bằng $\dfrac{5\sqrt{2}}{2}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Bốn điểm $A, B, C, D$ tạo thành bốn đỉnh của một khối tứ diện có thể tích bằng $\dfrac{5}{3}$.</div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div class="section-title" style="margin-top: 8px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Một người nông dân có $120\text{ m}$ hàng rào thép gai muốn rào một khu đất hình chữ nhật sát bờ một con sông thẳng để chăn nuôi (bờ sông không cần rào). Giả sử hàng rào bao bọc ba cạnh còn lại của hình chữ nhật: chiều dài song song với bờ sông là $x$ (mét) và hai chiều rộng vuông góc với bờ sông là $y$ (mét) (với $x, y > 0$). Hỏi diện tích lớn nhất của khu đất mà người nông dân có thể rào được bằng bao nhiêu mét vuông ($\text{m}^2$)?
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Một vật thể có chiều cao bằng $12\text{ cm}$ nằm dọc theo trục thẳng đứng. Khi cắt vật thể bởi một mặt phẳng vuông góc với trục tại vị trí có khoảng cách $x\text{ (cm)}$ tính từ đáy dưới ($0 \le x \le 12$), thiết diện thu được luôn là một hình vuông có độ dài cạnh bằng $\sqrt{36 - 3x}\text{ (cm)}$. Thể tích của vật thể đó bằng bao nhiêu centimét khối ($\text{cm}^3$)?
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Một bình hoa pha lê nghệ thuật có lòng trong là một khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đường cong $y = \sqrt{x + 4}$, trục hoành và hai đường thẳng $x = 0, x = 12$ (đơn vị trên các trục tọa độ là centimét) quanh trục hoành. Biết thể tích lòng trong của bình hoa có dạng $V = k\pi\text{ (cm}^3)$. Giá trị của hệ số $k$ bằng bao nhiêu?
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Một chiếc ô tô đang chuyển động thẳng đều với vận tốc $10\text{ m/s}$ thì người lái xe nhấn chân ga để tăng tốc. Kể từ thời điểm đó, ô tô chuyển động nhanh dần với gia tốc phụ thuộc vào thời gian là $a(t) = 2 + 0,6t\text{ (m/s}^2)$, trong đó $t$ là thời gian tính bằng giây ($t \ge 0$). Quãng đường chiếc ô tô đi được trong $10$ giây đầu tiên kể từ lúc bắt đầu tăng tốc bằng bao nhiêu mét?
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(1; 2; 4)$, $B(3; 4; 2)$ và $C(5; 3; 6)$. Điểm $M(x; y; 0)$ di động trên mặt phẳng tọa độ $(Oxy)$. Tìm giá trị nhỏ nhất của biểu thức $T = MA^2 + MB^2 + MC^2$.
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(1; 2; 3)$ và $B(5; 4; -1)$. Điểm $M$ di động trên mặt phẳng tọa độ $(Oxy)$. Giá trị nhỏ nhất của tổng khoảng cách $MA + MB$ bằng bao nhiêu?
</div>

<div class="end-exam">---------- HẾT ----------</div>
<div class="end-note">Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

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

with open("exam_de_khao_sat_toan_12_ma109.html", "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "De_Thi_Khao_Sat_Toan_12_Ma_109.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "exam_de_khao_sat_toan_12_ma109.html"
]

print("Running Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
