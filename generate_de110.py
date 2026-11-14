import base64, subprocess, pypdf

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

b64_c1 = get_b64("assets_110/c1_gonsong.png")
b64_c2 = get_b64("assets_110/c2_congparabol.png")
b64_c3 = get_b64("assets_110/c3_sporthub.png")
b64_c6 = get_b64("assets_110/c6_dentron.png")

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 110)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 5mm;
  margin-bottom: 5mm;
  margin-left: 11.5mm;
  margin-right: 11.5mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 110";
    font-family: 'Times New Roman', serif;
    font-size: 9pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10pt;
  line-height: 1.3;
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

.org-name {
  font-size: 9.5pt;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.2px;
}

.exam-title {
  font-size: 10.5pt;
  font-weight: bold;
  text-transform: uppercase;
  margin-top: 1px;
}

.exam-round {
  font-size: 10.5pt;
  font-weight: bold;
  text-transform: uppercase;
  margin-top: 1px;
}

.author-title {
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
}

.divider-line {
  width: 120px;
  height: 1px;
  background-color: #000;
  margin: 2px auto 0 auto;
}

.right-header {
  width: 56%;
  text-align: center;
}

.main-title {
  font-size: 11pt;
  font-weight: bold;
  text-transform: uppercase;
}

.subject-title {
  font-size: 10pt;
  font-weight: bold;
  margin-top: 1px;
}

.meta-info {
  font-size: 8.5pt;
  font-style: italic;
  margin-top: 1px;
}

.code-box {
  font-size: 9pt;
  font-weight: bold;
  margin-top: 1px;
}

.student-info {
  margin-top: 2px;
  margin-bottom: 3px;
  font-size: 9.5pt;
  display: flex;
  justify-content: space-between;
}

.section-title {
  font-size: 10pt;
  font-weight: bold;
  text-transform: uppercase;
  margin-top: 4px;
  margin-bottom: 1px;
}

.section-subtitle {
  font-size: 9pt;
  font-style: italic;
  margin-bottom: 2px;
}

.question {
  margin-bottom: 2.5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 1px;
  margin-bottom: 1.5px;
}

.options-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  margin-top: 1px;
  margin-bottom: 1.5px;
}

.sub-item {
  margin-left: 12px;
  margin-top: 1px;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  font-weight: bold;
  margin-top: 5px;
  font-size: 9.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 8.5pt;
}
</style>
</head>
<body>

<!-- HEADER -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="org-name">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12</div>
      <div class="exam-round">ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="divider-line"></div>
    </td>
    <td class="right-header">
      <div class="main-title">BÀI THI: TOÁN HỌC</div>
      <div class="subject-title">Thời gian làm bài: 90 phút, không kể thời gian phát đề</div>
      <div class="meta-info">(Đề thi gồm có 03 trang)</div>
      <div class="code-box">MÃ ĐỀ: 110</div>
    </td>
  </tr>
</table>

<div class="student-info">
  <div>Họ và tên học sinh: ............................................................................</div>
  <div>Lớp: .....................................................</div>
</div>
<div style="height: 1px; background-color: #000; margin-bottom: 3px;"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Giá trị lớn nhất của hàm số $f(x) = \dfrac{2x - 1}{x + 2}$ trên đoạn $[0; 2]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{3}{4}$.</div>
    <div><strong>B.</strong> $-\dfrac{1}{2}$.</div>
    <div><strong>C.</strong> $1$.</div>
    <div><strong>D.</strong> $\dfrac{1}{2}$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Hàm số $y = -x^4 + 2x^2 + 3$ nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid-4">
    <div><strong>A.</strong> $(-\infty; -1)$.</div>
    <div><strong>B.</strong> $(0; 1)$.</div>
    <div><strong>C.</strong> $(-1; 0)$.</div>
    <div><strong>D.</strong> $(-1; 1)$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Tìm họ tất cả các nguyên hàm của hàm số $f(x) = 3x^2 + \dfrac{1}{x^2}$ trên khoảng $(0; +\infty)$.
  <div class="options-grid-2">
    <div><strong>A.</strong> $x^3 + \dfrac{1}{x} + C$.</div>
    <div><strong>B.</strong> $6x - \dfrac{2}{x^3} + C$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $x^3 + \ln x + C$.</div>
    <div><strong>D.</strong> $x^3 - \dfrac{1}{x} + C$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Giá trị của tích phân $I = \int_{0}^{\ln 3} e^x\,\mathrm{d}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $3$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $\ln 3$.</div>
    <div><strong>D.</strong> $e^3 - 1$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Cho biết $\int_{0}^{2} f(x)\,\mathrm{d}x = 3$. Giá trị của tích phân $\int_{0}^{2} 4f(x)\,\mathrm{d}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $12$.</div>
    <div><strong>B.</strong> $7$.</div>
    <div><strong>C.</strong> $\dfrac{3}{4}$.</div>
    <div><strong>D.</strong> $1$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Diện tích $S$ của hình phẳng giới hạn bởi đồ thị hàm số $y = \dfrac{1}{x}$, trục hoành và hai đường thẳng $x = 1, x = e^2$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $e^2 - 1$.</div>
    <div><strong>B.</strong> $1$.</div>
    <div><strong>C.</strong> $2$.</div>
    <div><strong>D.</strong> $4$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Thể tích $V$ của khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đường cong $y = \sqrt{\cos x}$, trục hoành và hai đường thẳng $x = 0, x = \dfrac{\pi}{2}$ quanh trục hoành bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $\pi$.</div>
    <div><strong>C.</strong> $\dfrac{\pi}{2}$.</div>
    <div><strong>D.</strong> $2\pi$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian $Oxyz$, cho điểm $M(2; -3; 4)$. Tọa độ của điểm $M'$ đối xứng với điểm $M$ qua mặt phẳng tọa độ $(Oxy)$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $M'(-2; 3; 4)$.</div>
    <div><strong>B.</strong> $M'(2; 3; 4)$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $M'(-2; -3; -4)$.</div>
    <div><strong>D.</strong> $M'(2; -3; -4)$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, cho vectơ $\overrightarrow{u} = 2\vec{i} - 3\vec{j} + 6\vec{k}$ (với $\vec{i}, \vec{j}, \vec{k}$ là các vectơ đơn vị của các trục $Ox, Oy, Oz$). Độ dài của vectơ $\overrightarrow{u}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $7$.</div>
    <div><strong>B.</strong> $5$.</div>
    <div><strong>C.</strong> $49$.</div>
    <div><strong>D.</strong> $\sqrt{11}$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, cho hai vectơ $\overrightarrow{a} = (2; -1; 3)$ và $\overrightarrow{b} = (-4; m; n)$. Biết rằng hai vectơ $\overrightarrow{a}$ và $\overrightarrow{b}$ cùng phương với nhau. Giá trị của tổng $m + n$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $4$.</div>
    <div><strong>B.</strong> $-8$.</div>
    <div><strong>C.</strong> $8$.</div>
    <div><strong>D.</strong> $-4$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Trong không gian $Oxyz$, cho ba điểm $A(1; 2; 0)$, $B(3; -1; 1)$ và $C(1; 1; 2)$. Tích vô hướng $\overrightarrow{AB} \cdot \overrightarrow{AC}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $-1$.</div>
    <div><strong>B.</strong> $1$.</div>
    <div><strong>C.</strong> $5$.</div>
    <div><strong>D.</strong> $3$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Một chất điểm chịu tác dụng của một lực không đổi $\overrightarrow{F} = (4; -2; 5)\text{ (N)}$ làm dịch chuyển chất điểm từ vị trí $M(1; 3; 2)$ đến vị trí $N(3; 0; 4)$ (đơn vị tọa độ tính bằng mét). Công $A$ sinh ra bởi lực $\overrightarrow{F}$ được tính theo công thức $A = \overrightarrow{F} \cdot \overrightarrow{MN}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $14\text{ J}$.</div>
    <div><strong>B.</strong> $24\text{ J}$.</div>
    <div><strong>C.</strong> $4\text{ J}$.</div>
    <div><strong>D.</strong> $28\text{ J}$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div class="section-title" style="margin-top: 5px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <div style="display: flex; gap: 10px; align-items: flex-start;">
    <div style="flex: 1;">
      <span class="question-title">Câu 1.</span> Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ bên. Xét tính đúng sai của các mệnh đề sau:
      <div class="sub-item"><span class="sub-item-label">a)</span> Điểm uốn của đồ thị hàm số là điểm $I(1; 0)$.</div>
      <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho đồng biến trên mỗi khoảng $(-\infty; 0)$ và $(2; +\infty)$.</div>
      <div class="sub-item"><span class="sub-item-label">c)</span> Phương trình của hàm số đã cho là $y = x^3 - 3x^2 + 2$.</div>
      <div class="sub-item"><span class="sub-item-label">d)</span> Phương trình tiếp tuyến của đồ thị tại điểm có hoành độ $x = 3$ đi qua điểm $N(2; -5)$.</div>
    </div>
    <div style="width: 155px; text-align: center; flex-shrink: 0; margin-top: 1px;">
      <svg width="150" height="120" viewBox="0 0 210 165">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000" />
          </marker>
        </defs>
        <!-- x axis -->
        <line x1="25" y1="85" x2="202" y2="85" stroke="#000" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="195" y="78" font-family="Times New Roman" font-size="13" font-style="italic">x</text>
        <!-- y axis -->
        <line x1="80" y1="155" x2="80" y2="12" stroke="#000" stroke-width="1.2" marker-end="url(#arrow)" />
        <text x="88" y="18" font-family="Times New Roman" font-size="13" font-style="italic">y</text>
        <!-- Origin -->
        <text x="68" y="98" font-family="Times New Roman" font-size="12" font-style="italic">O</text>
        <!-- Dashed lines for B(2, -2) -->
        <line x1="152" y1="85" x2="152" y2="137" stroke="#666" stroke-width="1" stroke-dasharray="3,3" />
        <line x1="80" y1="137" x2="152" y2="137" stroke="#666" stroke-width="1" stroke-dasharray="3,3" />
        <!-- Coordinates labels -->
        <text x="68" y="37" font-family="Times New Roman" font-size="11">2</text>
        <text x="61" y="141" font-family="Times New Roman" font-size="11">-2</text>
        <text x="148" y="98" font-family="Times New Roman" font-size="11">2</text>
        <!-- Special Points dots: ONLY A and B -->
        <circle cx="80" cy="33" r="3" fill="#000" />
        <text x="85" y="36" font-family="Times New Roman" font-size="11" font-weight="bold">A</text>
        <circle cx="152" cy="137" r="3" fill="#000" />
        <text x="157" y="142" font-family="Times New Roman" font-size="11" font-weight="bold">B</text>
        <!-- Curve polyline -->
        <polyline fill="none" stroke="#003366" stroke-width="1.8" points="51.2,96.2 54.8,80.1 58.4,66.7 62.0,55.8 65.6,47.1 69.2,40.7 72.8,36.3 76.4,33.8 80.0,33.0 83.6,33.8 87.2,35.9 90.8,39.3 94.4,43.8 98.0,49.2 101.6,55.5 105.2,62.3 108.8,69.6 112.4,77.2 116.0,85.0 119.6,92.8 123.2,100.4 126.8,107.7 130.4,114.5 134.0,120.8 137.6,126.2 141.2,130.7 144.8,134.1 148.4,136.2 152.0,137.0 155.6,136.2 159.2,133.7 162.8,129.3 166.4,122.9 170.0,114.2 173.6,103.3 177.2,89.9 180.8,73.8 184.4,54.9 188.0,33.0" />
      </svg>
    </div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $f(x) = 3x^2 - 2x$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> $F(x) = x^3 - x^2 + C$ là một nguyên hàm của hàm số $f(x)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Biết $F(x)$ là một nguyên hàm của hàm số $f(x)$ thỏa mãn $F(2) = 5$. Khi đó giá trị của $F(5)$ bằng $101$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Giá trị của tích phân $\int_{1}^{3} [f(x) + 2x]\,\mathrm{d}x$ bằng $26$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = 0, x = 1$ bằng $1$.</div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Trong một phòng thí nghiệm sinh học, số lượng vi khuẩn trong một mẻ nuôi cấy tăng trưởng theo thời gian $t$ (giờ, $0 \le t \le 8$) với tốc độ tăng trưởng được mô hình hóa bởi hàm số $N'(t) = 150e^{0,5t}$ (con/giờ). Biết rằng tại thời điểm bắt đầu nuôi cấy ($t = 0$), mẻ cấy có $300$ con vi khuẩn. Gọi $N(t)$ là số lượng vi khuẩn có trong mẻ sau $t$ giờ. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tốc độ tăng trưởng của vi khuẩn tại thời điểm ban đầu $t = 0$ là $150$ con/giờ.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Số lượng vi khuẩn tại thời điểm $t$ giờ ($0 \le t \le 8$) được xác định bởi công thức $N(t) = 300e^{0,5t}$ (con).</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Số lượng vi khuẩn tăng thêm trong $4$ giờ nuôi cấy đầu tiên là $300(e^2 - 1)$ con.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Sau $2$ giờ kể từ lúc bắt đầu nuôi cấy, số lượng vi khuẩn trong mẻ vượt quá $1000$ con.</div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có đỉnh $A$ trùng với gốc tọa độ $O(0; 0; 0)$, ba đỉnh kề với đỉnh $A$ có tọa độ lần lượt là $B(4; 0; 0)$, $D(0; 6; 0)$ và $A'(0; 0; 3)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tọa độ đỉnh $C'$ của hình hộp chữ nhật là $C'(4; 6; 3)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tọa độ trọng tâm $G$ của khối tứ diện $A'BCD$ là $G(1; 2; 1)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Độ dài đường chéo $AC'$ của hình hộp chữ nhật bằng $\sqrt{61}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Thể tích của khối hộp chữ nhật $ABCD.A'B'C'D'$ bằng $72$.</div>
</div>

<!-- ==================== PHẦN III ==================== -->
<!-- NỐI TRỰC TIẾP VÀO CUỐI TRANG 2, KHÔNG CÓ PAGE BREAK -->
<div class="section-title" style="margin-top: 6px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1: Phóng to x2 (width ~210px), hình sạch không thừa chữ -->
<div class="question">
  <div style="display: flex; gap: 14px; align-items: center;">
    <div style="flex: 1;">
      <span class="question-title">Câu 1.</span> Một viên đá được ném xuống mặt hồ phẳng lặng, tạo ra các gợn sóng hình tròn đồng tâm. Bán kính của gợn sóng ngoài cùng tăng với tốc độ không đổi $2\text{ cm/s}$. Diện tích hình tròn tạo bởi gợn sóng này đang tăng với tốc độ bao nhiêu $\text{cm}^2/\text{s}$ tại thời điểm bán kính của nó bằng $10\text{ cm}$? (kết quả làm tròn đến hàng phần mười).
    </div>
    <div style="width: 220px; text-align: center; flex-shrink: 0;">
      <img src="data:image/png;base64,__B64_C1__" style="width: 210px; height: auto; display: block; margin: 0 auto;">
    </div>
  </div>
</div>

<!-- Câu 2: Hình ở ngay DƯỚI câu hỏi, phóng to x2 (~215px) -->
<div class="question">
  <div>
    <span class="question-title">Câu 2.</span> Chị Minh Hiền muốn làm một cái cổng hình parabol như hình vẽ bên dưới. Chiều cao $GH = 4\text{ m}$, chiều rộng $AB = 4\text{ m}$, $AC = BD = 0,9\text{ m}$. Chị Minh Hiền làm hai cánh cổng khi đóng lại là hình chữ nhật $CDEF$ (phần tô màu xám) có đơn giá $1\,200\,000\text{ đồng/m}^2$, còn các phần để trắng làm xiên hoa có đơn giá $900\,000\text{ đồng/m}^2$. Tổng chi phí để làm cổng là bao nhiêu triệu đồng? (kết quả làm tròn đến chữ số thập phân thứ hai).
  </div>
  <div style="text-align: center; margin-top: 3px; margin-bottom: 2px;">
    <img src="data:image/png;base64,__B64_C2__" style="width: 215px; height: auto; display: inline-block;">
  </div>
</div>

<!-- Câu 3: Hình ở ngay DƯỚI câu hỏi, phóng to x2 (~310px) -->
<div class="question">
  <div>
    <span class="question-title">Câu 3.</span> Sân vận động Sport Hub (Singapore) có mái vòm với nền sân là một hình elip $(E)$ có trục lớn dài $150\text{ m}$, trục bé dài $90\text{ m}$. Nếu cắt không gian bên trong sân vận động theo một mặt phẳng vuông góc với trục lớn của $(E)$ và cắt elip tại hai điểm $M, N$ thì thiết diện thu được luôn là một hình viên phân của đường tròn tâm $I$ với $MN$ là dây cung và $\widehat{MIN} = 90^\circ$ (như hình vẽ bên dưới). Thể tích phần không gian bên trong mái che sân vận động bằng bao nhiêu mét khối? (làm tròn kết quả đến hàng đơn vị).
  </div>
  <div style="text-align: center; margin-top: 3px; margin-bottom: 2px;">
    <img src="data:image/png;base64,__B64_C3__" style="width: 310px; height: auto; display: inline-block;">
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trên một mặt hồ phẳng rộng $470\text{ m}^2$, một đợt tảo lam độc hại phát triển với tốc độ tỷ lệ thuận với căn bậc hai diện tích hiện tại của nó: $S'(t) = k\sqrt{S(t)}$ (trong đó $S(t)$ tính bằng $\text{m}^2$, $t$ là số ngày kể từ lúc phát hiện, $k$ là hằng số thực). Khi mới phát hiện ($t = 0$), đợt tảo bao phủ $16\text{ m}^2$ mặt hồ. Sau $3$ ngày, diện tích đợt tảo tăng gấp đôi. Sau bao nhiêu ngày tính từ lúc phát hiện thì đợt tảo này phủ kín toàn bộ mặt hồ? (kết quả làm tròn đến hàng đơn vị).
</div>

<!-- Câu 5: Hình học - Tính góc giữa 2 vector -->
<div class="question">
  <span class="question-title">Câu 5.</span> Cho hình lập phương $ABCD.A'B'C'D'$. Số đo góc giữa hai vectơ $\overrightarrow{AC}$ và $\overrightarrow{A'D}$ bằng bao nhiêu độ?
</div>

<!-- Câu 6: Phóng to x2 (width ~225px), hình sạch không thừa chữ -->
<div class="question">
  <div style="display: flex; gap: 14px; align-items: center;">
    <div style="flex: 1;">
      <span class="question-title">Câu 6.</span> Một chiếc đèn tròn được treo song song với mặt phẳng nằm ngang bởi ba sợi dây không dãn xuất phát từ điểm $O$ trên trần nhà lần lượt buộc vào ba điểm $A, B, C$ trên vành đèn sao cho tam giác $ABC$ đều (như hình vẽ bên). Độ dài của ba sợi dây $OA, OB, OC$ đều bằng $L$. Trọng lượng của chiếc đèn là $27\text{ N}$ và bán kính của đèn tròn là $0,5\text{ m}$. Biết rằng mỗi sợi dây được thiết kế để chịu được lực căng tối đa là $12\text{ N}$. Chiều dài tối thiểu $L$ của mỗi sợi dây bằng bao nhiêu xentimét? (kết quả làm tròn đến chữ số thập phân thứ nhất).
    </div>
    <div style="width: 235px; text-align: center; flex-shrink: 0;">
      <img src="data:image/png;base64,__B64_C6__" style="width: 225px; height: auto; display: block; margin: 0 auto;">
    </div>
  </div>
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

html_content = html_content.replace("__B64_C1__", b64_c1)
html_content = html_content.replace("__B64_C2__", b64_c2)
html_content = html_content.replace("__B64_C3__", b64_c3)
html_content = html_content.replace("__B64_C6__", b64_c6)

with open("exam_de_khao_sat_toan_12_ma110.html", "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "De_Thi_Khao_Sat_Toan_12_Ma_110.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "exam_de_khao_sat_toan_12_ma110.html"
]

print("Running Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
