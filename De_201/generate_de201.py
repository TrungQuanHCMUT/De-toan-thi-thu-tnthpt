import os, subprocess, pypdf, base64

def get_base64_img(filename):
    with open(filename, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

img_p3_c1 = get_base64_img('assets/de201_p3_c1_cylinders.png')
img_p3_c2 = get_base64_img('assets/de201_p3_c2_trapezoid.png')
img_p3_c6 = get_base64_img('assets/de201_p3_c6_boxes.png')

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề Thi Thử Kì Thi TNTHPT Quốc Gia - Mã Đề 201</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4 portrait;
  margin: 14mm 15mm 14mm 15mm;
}
* {
  box-sizing: border-box;
}
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 11.5pt;
  line-height: 1.40;
  color: #000;
  margin: 0;
  padding: 0;
}
.katex {
  font-size: 1.0em;
}
.katex-display {
  margin: 4px 0;
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
  width: 48.5%;
  text-align: center;
}
.right-header {
  width: 51.5%;
  text-align: center;
}
.title-main {
  font-size: 11.2pt;
  font-weight: bold;
  text-transform: uppercase;
  line-height: 1.25;
  white-space: nowrap;
}
.author-title {
  font-size: 10.5pt;
  font-style: italic;
  margin-top: 2px;
}
.pages-note {
  font-size: 9.2pt;
  font-style: italic;
  margin-top: 2px;
}
.code-box {
  border: 1.3px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 3px;
}
.exam-title {
  font-size: 11.2pt;
  font-weight: bold;
  line-height: 1.25;
  text-transform: uppercase;
  white-space: nowrap;
}
.subject-title {
  font-size: 11.2pt;
  font-weight: bold;
  margin-top: 3px;
}
.time-title {
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 2px;
}
.solid-divider {
  border-top: 1px solid #000;
  margin: 4px 0 2px 0;
}
.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 4px 0 4px 0;
}
.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 11pt;
  margin-top: 3px;
  margin-bottom: 3px;
}
.section-title {
  font-weight: bold;
  font-size: 11.5pt;
  margin-top: 12px;
  margin-bottom: 3px;
  break-after: avoid;
  page-break-after: avoid;
}
.section-subtitle {
  font-style: italic;
  font-size: 10.5pt;
  margin-bottom: 8px;
  break-after: avoid;
  page-break-after: avoid;
}
.question {
  margin-bottom: 9.5px;
  text-align: justify;
  break-inside: avoid;
  page-break-inside: avoid;
}
.question-title {
  font-weight: bold;
}
.options-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 3.5px;
  margin-bottom: 2px;
}
.options-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  row-gap: 2.5px;
  margin-top: 3.5px;
  margin-bottom: 2px;
}
.sub-item {
  margin-left: 12px;
  margin-top: 4.5px;
  margin-bottom: 4.5px;
}
.sub-item-label {
  font-weight: bold;
  display: inline-block;
  width: 20px;
}
.stats-table {
  width: 92%;
  margin: 5px auto 5px auto;
  border-collapse: collapse;
  font-size: 10.5pt;
  text-align: center;
}
.stats-table th, .stats-table td {
  border: 1px solid #000;
  padding: 3px 6px;
}
.end-exam {
  text-align: center;
  font-weight: bold;
  margin-top: 16px;
  font-size: 11.5pt;
  break-after: avoid;
}
.end-note {
  text-align: center;
  font-style: italic;
  font-size: 10.3pt;
  margin-top: 3px;
}
.img-center {
  text-align: center;
  margin: 8px 0;
}
.img-p3-c1 {
  max-width: 390px;
  width: 62%;
  height: auto;
  display: inline-block;
}
.img-p3-c2 {
  max-width: 345px;
  width: 55%;
  height: auto;
  display: inline-block;
}
</style>
</head>
<body>

<!-- ==================== PAGE 1 ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="pages-note">(Đề thi gồm có 04 trang)</div>
      <div class="code-box">Mã đề: 201</div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div style="flex: 1.5; display: flex; align-items: baseline; margin-right: 18px;">
    <span>Họ và tên học sinh:&nbsp;</span><span style="flex: 1; border-bottom: 1.1px dotted #000;"></span>
  </div>
  <div style="flex: 1; display: flex; align-items: baseline;">
    <span>Lớp:&nbsp;</span><span style="flex: 1; border-bottom: 1.1px dotted #000;"></span>
  </div>
</div>
<div class="solid-divider-thick"></div>

<div class="section-title" style="margin-top: 4px;">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 (Lớp 12 - Đường tiệm cận xiên của hàm phân thức - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 1.</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 4x + 5}{x - 2}$ có phương trình là
  <div class="options-grid-4">
    <div><strong>A.</strong> $y = x + 2$.</div>
    <div><strong>B.</strong> $y = x - 4$.</div>
    <div><strong>C.</strong> $y = x - 2$.</div>
    <div><strong>D.</strong> $y = 2x - 2$.</div>
  </div>
</div>

<!-- Câu 2 (Lớp 12 - Nguyên hàm thỏa mãn điều kiện - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 2.</span> Biết $F(x)$ là một nguyên hàm của hàm số $f(x) = \sin 2x + e^{3x}$ trên $\mathbb{R}$ thỏa mãn $F(0) = \dfrac{5}{6}$. Giá trị của $F\left(\dfrac{\pi}{4}\right)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{1}{3}e^{\frac{3\pi}{4}} + 1$.</div>
    <div><strong>B.</strong> $\dfrac{1}{3}e^{\frac{3\pi}{4}} + \dfrac{1}{2}$.</div>
    <div><strong>C.</strong> $e^{\frac{3\pi}{4}} + 1$.</div>
    <div><strong>D.</strong> $\dfrac{1}{3}e^{\frac{3\pi}{4}} - \dfrac{1}{6}$.</div>
  </div>
</div>

<!-- Câu 3 (Lớp 11/12 - Đạo hàm của hàm số - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 3.</span> Đạo hàm của hàm số $y = \log_2(x^2 + 2x + 5)$ trên $\mathbb{R}$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $y' = \dfrac{1}{(x^2 + 2x + 5)\ln 2}$.</div>
    <div><strong>B.</strong> $y' = \dfrac{(2x + 2)\ln 2}{x^2 + 2x + 5}$.</div>
    <div><strong>C.</strong> $y' = \dfrac{2x + 2}{x^2 + 2x + 5}$.</div>
    <div><strong>D.</strong> $y' = \dfrac{2x + 2}{(x^2 + 2x + 5)\ln 2}$.</div>
  </div>
</div>

<!-- Câu 4 (Lớp 10 - Phương trình đường tròn cơ bản - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong mặt phẳng tọa độ $Oxy$, đường tròn tâm $I(2; -3)$ và đi qua điểm $A(-1; 1)$ có phương trình là
  <div class="options-grid-2">
    <div><strong>A.</strong> $(x + 2)^2 + (y - 3)^2 = 25$.</div>
    <div><strong>B.</strong> $(x - 2)^2 + (y + 3)^2 = 25$.</div>
    <div><strong>C.</strong> $(x - 2)^2 + (y + 3)^2 = 5$.</div>
    <div><strong>D.</strong> $(x + 2)^2 + (y - 3)^2 = 5$.</div>
  </div>
</div>

<!-- Câu 5 (Lớp 11 - Cấp số cộng - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 5.</span> Một khán phòng được thiết kế gồm $20$ hàng ghế, trong đó hàng đầu tiên có $18$ ghế và mỗi hàng ghế phía sau có nhiều hơn hàng ngay trước nó $3$ ghế. Tổng số ghế có trong khán phòng đó bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $930$.</div>
    <div><strong>B.</strong> $900$.</div>
    <div><strong>C.</strong> $960$.</div>
    <div><strong>D.</strong> $870$.</div>
  </div>
</div>

<!-- Câu 6 (Lớp 11 - Hình học không gian: góc giữa đường thẳng và mặt đáy - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 6.</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$, cạnh bên $SA \perp (ABC)$ và $SA = a\sqrt{3}$. Góc giữa đường thẳng $SB$ và mặt phẳng $(ABC)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $30^\circ$.</div>
    <div><strong>B.</strong> $45^\circ$.</div>
    <div><strong>C.</strong> $60^\circ$.</div>
    <div><strong>D.</strong> $90^\circ$.</div>
  </div>
</div>

<!-- Câu 7 (Lớp 12 - Oxyz: Côsin góc giữa đường thẳng và mặt phẳng - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 7.</span> Trong không gian với hệ tọa độ $Oxyz$, cho đường thẳng $d: \dfrac{x - 1}{2} = \dfrac{y + 2}{-1} = \dfrac{z}{2}$ và mặt phẳng $(P): 2x + y - 2z + 5 = 0$. Côsin của góc tạo bởi đường thẳng $d$ và mặt phẳng $(P)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{1}{9}$.</div>
    <div><strong>B.</strong> $\dfrac{4\sqrt{5}}{9}$.</div>
    <div><strong>C.</strong> $\dfrac{2\sqrt{5}}{9}$.</div>
    <div><strong>D.</strong> $\dfrac{8}{9}$.</div>
  </div>
</div>

<!-- Câu 8 (Lớp 11 - Bất phương trình mũ - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 8.</span> Tập nghiệm của bất phương trình $3^{x^2 - 2x} < 27$ là khoảng $(a; b)$. Giá trị của biểu thức $a + 2b$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $4$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $5$.</div>
  </div>
</div>

<!-- Câu 9 (Lớp 12 - Ứng dụng tích phân tính diện tích hình phẳng - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 9.</span> Diện tích hình phẳng giới hạn bởi các đường $y = e^x$, $y = e^{-x}$, $x = 0$ và $x = 1$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $e + e^{-1} - 2$.</div>
    <div><strong>B.</strong> $e - e^{-1} - 2$.</div>
    <div><strong>C.</strong> $e + e^{-1}$.</div>
    <div><strong>D.</strong> $e - e^{-1}$.</div>
  </div>
</div>

<!-- Câu 10 (Lớp 12 - Thống kê mẫu số liệu ghép nhóm: Phương sai - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 10.</span> Kết quả đo thời gian hoàn thành một bài kiểm tra trực tuyến (đơn vị: phút) của $20$ học sinh được thống kê trong bảng tần số ghép nhóm sau:
  <table class="stats-table">
    <tr>
      <th>Thời gian (phút)</th>
      <td>$[2; 4)$</td>
      <td>$[4; 6)$</td>
      <td>$[6; 8)$</td>
      <td>$[8; 10)$</td>
    </tr>
    <tr>
      <th>Số học sinh</th>
      <td>$4$</td>
      <td>$6$</td>
      <td>$8$</td>
      <td>$2$</td>
    </tr>
  </table>
  Phương sai $s^2$ của mẫu số liệu ghép nhóm trên bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $5{,}8$.</div>
    <div><strong>B.</strong> $3{,}16$.</div>
    <div><strong>C.</strong> $4{,}24$.</div>
    <div><strong>D.</strong> $3{,}36$.</div>
  </div>
</div>

<!-- Câu 11 (Lớp 12 - Xác suất có điều kiện cơ bản - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 11.</span> Cho hai biến cố $A$ và $B$ thỏa mãn $P(A) = 0{,}6$, $P(B) = 0{,}5$ và $P(B|A) = 0{,}3$. Giá trị của $P(A|B)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $0{,}18$.</div>
    <div><strong>B.</strong> $0{,}25$.</div>
    <div><strong>C.</strong> $0{,}36$.</div>
    <div><strong>D.</strong> $0{,}15$.</div>
  </div>
</div>

<!-- Câu 12 (Lớp 11 - Dãy số cho bởi công thức truy hồi - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 12.</span> Cho dãy số $(u_n)$ biết $u_1 = 2$ và $u_{n+1} = 3u_n - 1$ với mọi $n \ge 1$. Giá trị của $u_3$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $5$.</div>
    <div><strong>B.</strong> $14$.</div>
    <div><strong>C.</strong> $41$.</div>
    <div><strong>D.</strong> $17$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 (Lớp 12 - Khảo sát hàm số bình thường, không đồ thị - Key: Đ - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = x^3 - 3x^2 - 9x + 11$ có đồ thị $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số đã cho đồng biến trên khoảng $(-\infty; -1)$ và nghịch biến trên khoảng $(-1; 3)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Giá trị lớn nhất của hàm số $f(x)$ trên đoạn $[0; 4]$ bằng $11$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đường thẳng đi qua hai điểm cực trị của đồ thị $(C)$ có phương trình là $y = -8x - 8$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Có đúng $26$ giá trị nguyên của tham số $m$ để phương trình $f(|x|) = m$ có $4$ nghiệm thực phân biệt.</div>
</div>

<!-- Câu 2 (Lớp 12 - Tích phân chuyển động hai giai đoạn, không đồ thị - Key: S - Đ - Đ - S) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 2.</span> Một đoàn tàu cao tốc thử nghiệm rời ga từ trạng thái đứng yên ($v(0) = 0$) và chuyển động thẳng trong $20\text{ giây}$ với vận tốc biến thiên liên tục theo hai giai đoạn: trong $10\text{ giây}$ đầu tiên ($0 \le t \le 10$), gia tốc của tàu là $a(t) = 0{,}6t\text{ (m/s}^2)$; trong $10\text{ giây}$ tiếp theo ($10 < t \le 20$), tàu chuyển động chậm dần đều rồi dừng hẳn tại thời điểm $t = 20\text{ s}$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Vận tốc lớn nhất của đoàn tàu trong suốt $20\text{ giây}$ thử nghiệm đạt được tại $t = 10\text{ s}$ và bằng $120\text{ km/h}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Quãng đường đoàn tàu đi được trong $10\text{ giây}$ đầu tiên bằng $100\text{ m}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Gia tốc của đoàn tàu trong khoảng thời gian từ $t = 10\text{ s}$ đến $t = 20\text{ s}$ bằng $-3\text{ m/s}^2$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng quãng đường đoàn tàu đi được trong $20\text{ giây}$ thử nghiệm lớn hơn $260\text{ m}$.</div>
</div>

<!-- Câu 3 (Lớp 12 - Xác suất có điều kiện & Bayes - Key: Đ - S - S - Đ) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 3.</span> Một nhà máy sản xuất chip điện tử có hai dây chuyền I và II. Dây chuyền I sản xuất $60\%$ tổng sản lượng với tỉ lệ chip đạt chuẩn là $96\%$. Dây chuyền II sản xuất $40\%$ tổng sản lượng với tỉ lệ chip đạt chuẩn là $91\%$. Toàn bộ chip từ hai dây chuyền được đưa chung vào một kho lưu trữ lớn. Chọn ngẫu nhiên một con chip từ kho để kiểm tra chất lượng. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tỉ lệ chip bị lỗi của toàn bộ nhà máy bằng $6\%$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Xác suất để con chip được chọn vừa đạt chuẩn vừa do dây chuyền II sản xuất bằng $0{,}36$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Biết rằng con chip được chọn bị lỗi, xác suất để con chip đó do dây chuyền I sản xuất lớn hơn xác suất nó do dây chuyền II sản xuất.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Nếu chọn ngẫu nhiên độc lập $2$ con chip từ kho (coi số lượng chip trong kho rất lớn), xác suất để có đúng $1$ con chip đạt chuẩn lớn hơn $11\%$.</div>
</div>

<!-- Câu 4 (Lớp 12 - Oxyz: Mặt cầu radar & quỹ đạo bay - Key: S - S - Đ - Đ) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên mỗi trục là kilômét), mặt đất được xem là mặt phẳng $(Oxy): z = 0$. Một trạm radar kiểm soát không lưu đặt tại vị trí $I(2; 1; 9)$ có phạm vi quét tối đa trong hình cầu $(S)$ tâm $I$, bán kính $R = 15\text{ km}$. Tại thời điểm $t = 0\text{ (s)}$, một máy bay bắt đầu bay thẳng đều từ điểm $A(-16; -8; 9)$ với vectơ vận tốc không đổi $\vec{v} = (0{,}2;\; 0{,}2;\; 0{,}1)\text{ (km/s)}$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Phương trình mặt cầu $(S)$ giới hạn vùng phủ sóng của radar là $(x - 2)^2 + (y - 1)^2 + (z - 9)^2 = 15$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vùng phủ sóng của radar cắt mặt đất $(Oxy)$ theo giao tuyến là một hình tròn có diện tích bằng $120\pi\text{ km}^2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khoảng cách ngắn nhất từ trạm radar $I$ đến đường bay của máy bay bằng $9\text{ km}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng thời gian máy bay nằm trong phạm vi phát hiện của radar bằng $80\text{ giây}$.</div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 (Lớp 12 - Tích phân thể tích giao hai hình trụ vuông góc - Đáp số: 144) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 1.</span> Hai ống trụ tròn xoay đặc giống hệt nhau có cùng bán kính đáy $R = 3\text{ cm}$ được đặt sao cho hai trục đối xứng của chúng cắt và vuông góc với nhau tại tâm $O$ (tham khảo hình vẽ bên dưới). Thể tích phần chung của hai khối trụ đó bằng bao nhiêu $\text{cm}^3$?
  <div class="img-center">
    <img src="__IMG_P3_C1__" class="img-p3-c1" alt="Giao hai hình trụ vuông góc">
  </div>
</div>

<!-- Câu 2 (Lớp 12 - Đạo hàm Tối ưu Hình thang nội tiếp nửa đường tròn - Đáp số: 46,8) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 2.</span> Một nhà thiết kế chế tạo khung đèn trang trí có dạng hình thang cân $ABCD$ nội tiếp trong nửa đường tròn tâm $O$, đường kính $AD = 12\text{ dm}$ với hai đỉnh $B, C$ nằm trên nửa đường tròn (tham khảo hình vẽ). Diện tích lớn nhất của khung hình thang $ABCD$ bằng bao nhiêu $\text{dm}^2$ (làm tròn kết quả đến hàng phần mười)?
  <div class="img-center">
    <img src="__IMG_P3_C2__" class="img-p3-c2" alt="Hình thang cân nội tiếp nửa đường tròn">
  </div>
</div>

<!-- Câu 3 (Lớp 11 - Hình không gian lăng trụ đứng & khoảng cách 2 đường chéo nhau - Đáp số: 2,81) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 3.</span> Một giàn giáo khung thép có dạng hình lăng trụ đứng $ABC.A'B'C'$ với đáy $ABC$ là tam giác đều cạnh $AB = 6\text{ m}$ và chiều cao $AA' = 8\text{ m}$. Khoảng cách giữa hai thanh giằng chéo nhau $AB'$ và $BC'$ bằng bao nhiêu mét (làm tròn kết quả đến hàng phần trăm)?
</div>

<!-- Câu 4 (Lớp 12 - Oxyz Khoảng cách ngắn nhất giữa 2 UAV chuyển động - Đáp số: 6) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị trên mỗi trục là mét), tại thời điểm $t = 0\text{ (s)}$, hai thiết bị bay không người lái (UAV) cùng xuất phát chuyển động thẳng đều với vận tốc không đổi: UAV thứ nhất xuất phát từ điểm $A(-4; -2; 7)$ với vectơ vận tốc $\vec{v}_1 = (3; 2; 0)\text{ m/s}$, UAV thứ hai xuất phát từ điểm $B(4; 5; 5)$ với vectơ vận tốc $\vec{v}_2 = (1; 1; 2)\text{ m/s}$. Khoảng cách ngắn nhất giữa hai UAV trong quá trình bay (với $t \ge 0$) bằng bao nhiêu mét?
</div>

<!-- Câu 5 (Lớp 10/11/12 - Tổ hợp & Xác suất có điều kiện trên đa giác đều 12 đỉnh - Đáp số: 0,04) -->
<div class="question" style="margin-bottom: 11px;">
  <span class="question-title">Câu 5.</span> Cho đa giác đều $12$ đỉnh nội tiếp trong một đường tròn. Chọn ngẫu nhiên đồng thời $4$ đỉnh trong số $12$ đỉnh của đa giác để tạo thành một tứ giác lồi. Biết rằng tứ giác tạo thành có hai đường chéo vuông góc với nhau, tính xác suất để tứ giác đó là một hình vuông.
</div>

<!-- Câu 6 (Lớp 11 & 12 - Xác suất kết hợp cổ điển (tổ hợp) và có điều kiện / Bayes - Đáp số: 0,31) -->
<div class="question" style="margin-bottom: 12px;">
  <div style="display: flex; justify-content: space-between; align-items: center; gap: 12px;">
    <div style="flex: 1;">
      <span class="question-title">Câu 6.</span> Có hai hộp chứa các viên bi cùng kích thước và khối lượng: hộp I chứa $5$ viên bi đỏ và $4$ viên bi xanh; hộp II chứa $6$ viên bi đỏ và $3$ viên bi xanh (tham khảo hình vẽ). Lấy ngẫu nhiên đồng thời $2$ viên bi từ hộp I bỏ sang hộp II, sau đó lấy ngẫu nhiên đồng thời $2$ viên bi từ hộp II. Biết rằng $2$ viên bi lấy ra từ hộp II có cùng màu, tính xác suất để $2$ viên bi chuyển từ hộp I sang hộp II trước đó đều là bi đỏ.
    </div>
    <div style="width: 275px; text-align: right; flex-shrink: 0;">
      <img src="__IMG_P3_C6__" style="width: 268px; height: auto;" alt="Hai hộp bi đỏ và xanh">
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

html_content = (
    html_content
    .replace('__IMG_P3_C1__', img_p3_c1)
    .replace('__IMG_P3_C2__', img_p3_c2)
    .replace('__IMG_P3_C6__', img_p3_c6)
)

html_filename = 'exam_de_thi_thu_tnthpt_ma201.html'
pdf_name = 'De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_201.pdf'

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

print("Running Chrome to generate De 201 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
