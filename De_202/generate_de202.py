#!/usr/bin/env python3
"""Generate De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_202.pdf matching De 201 (11.5pt continuous flow)."""
import os
import base64
import subprocess
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


def b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


img_p3_c1 = b64(os.path.join(ASSETS_DIR, "de202_p3_c1_parabola_circle.png"))
img_p3_c2 = b64(os.path.join(ASSETS_DIR, "de202_p3_c2_corridor.png"))

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề Thi Thử TNTHPT Quốc Gia Môn Toán - Mã Đề 202</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4 portrait;
  margin: 14mm 15mm 14mm 15mm;
}
* { box-sizing: border-box; }
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 11.5pt;
  line-height: 1.40;
  color: #000;
  margin: 0;
  padding: 0;
}
.katex { font-size: 1.0em; }
.katex-display { margin: 4px 0; }

/* Header matching De 201 standard */
.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 5px;
}
.header-table td {
  vertical-align: top;
  padding: 0;
}
.header-left {
  width: 44%;
  text-align: center;
}
.header-right {
  width: 56%;
  text-align: center;
}
.title-main {
  font-weight: bold;
  font-size: 11.2pt;
  text-transform: uppercase;
  line-height: 1.25;
}
.author-title {
  font-style: italic;
  font-size: 10.5pt;
  margin-top: 2px;
}
.pages-note {
  font-style: italic;
  font-size: 9.2pt;
  margin-top: 2px;
}
.code-box {
  display: inline-block;
  border: 1.5px solid #000;
  padding: 1.5px 10px;
  font-weight: bold;
  font-size: 11pt;
  margin-top: 4px;
}
.exam-title {
  font-weight: bold;
  font-size: 11.2pt;
  text-transform: uppercase;
  line-height: 1.25;
}
.subject-title {
  font-weight: bold;
  font-size: 11.2pt;
  margin-top: 2px;
}
.time-title {
  font-style: italic;
  font-size: 9.5pt;
  margin-top: 2px;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 11pt;
  margin-top: 4px;
  margin-bottom: 3px;
}
.student-field {
  display: flex;
  align-items: baseline;
}
.student-field-name {
  flex-grow: 1;
  margin-right: 18px;
}
.dots {
  flex-grow: 1;
  border-bottom: 1px dotted #000;
  margin-left: 4px;
  height: 0.9em;
}
.dots-short {
  display: inline-block;
  width: 82px;
  border-bottom: 1px dotted #000;
  margin-left: 4px;
  height: 0.9em;
}
.header-divider {
  border-bottom: 1.5px solid #000;
  margin-top: 3px;
  margin-bottom: 8px;
}

.section-title {
  font-weight: bold;
  font-size: 11.5pt;
  margin-top: 10px;
  margin-bottom: 3px;
  break-after: avoid;
  page-break-after: avoid;
}
.section-subtitle {
  font-style: italic;
  font-size: 10.5pt;
  margin-bottom: 7px;
  text-align: justify;
  break-after: avoid;
  page-break-after: avoid;
}
.question {
  margin-bottom: 9px;
  text-align: justify;
  break-inside: avoid;
  page-break-inside: avoid;
}
.question-title { font-weight: bold; }

.options-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 5px 10px;
  margin-top: 3.5px;
  margin-left: 12px;
}
.options-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 4px 18px;
  margin-top: 3.5px;
  margin-left: 12px;
}
.tf-list {
  margin-top: 3.5px;
  margin-left: 12px;
}
.tf-item {
  margin-bottom: 3px;
  text-align: justify;
}

.stats-table {
  width: 90%;
  margin: 5px auto;
  border-collapse: collapse;
  font-size: 10.5pt;
  text-align: center;
}
.stats-table th, .stats-table td {
  border: 1px solid #000;
  padding: 2.5px 6px;
}
.stats-table th {
  background-color: #f4f6f9;
  font-weight: bold;
}

.img-center {
  text-align: center;
  margin: 6px 0;
}
.end-exam {
  text-align: center;
  font-weight: bold;
  margin-top: 14px;
  font-size: 11.5pt;
  break-after: avoid;
  page-break-after: avoid;
}
.end-note {
  text-align: center;
  font-style: italic;
  font-size: 10.3pt;
  margin-top: 3px;
}
</style>
</head>
<body>

<table class="header-table">
  <tr>
    <td class="header-left">
      <div class="title-main">ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="pages-note">(Đề thi gồm có 04 trang)</div>
      <div class="code-box">Mã đề: 202</div>
    </td>
    <td class="header-right">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
    </td>
  </tr>
</table>

<div class="student-info">
  <div class="student-field student-field-name">
    <span>Họ và tên học sinh:</span><span class="dots"></span>
  </div>
  <div class="student-field">
    <span>Lớp:</span><span class="dots-short"></span>
  </div>
</div>
<div class="header-divider"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn.</div>
<div class="section-subtitle">Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>

<div class="question">
  <span class="question-title">Câu 1.</span> Hệ số của $x^2$ trong khai triển nhị thức Newton $(2x - 1)^4$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $6$.</div>
    <div><strong>B.</strong> $24$.</div>
    <div><strong>C.</strong> $-24$.</div>
    <div><strong>D.</strong> $12$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2.</span> Cho $\displaystyle\int_1^4 f(x)\,dx = 6$ và $\displaystyle\int_1^4 g(x)\,dx = -2$. Giá trị của $\displaystyle\int_1^4 \big[2f(x) - 3g(x)\big]\,dx$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $6$.</div>
    <div><strong>B.</strong> $14$.</div>
    <div><strong>C.</strong> $10$.</div>
    <div><strong>D.</strong> $18$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3.</span> Đạo hàm của hàm số $y = 5^{2x - 1}$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $y' = 2 \cdot 5^{2x - 1} \ln 5$.</div>
    <div><strong>B.</strong> $y' = 5^{2x - 1} \ln 5$.</div>
    <div><strong>C.</strong> $y' = \dfrac{2 \cdot 5^{2x - 1}}{\ln 5}$.</div>
    <div><strong>D.</strong> $y' = (2x - 1)5^{2x - 2}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian $Oxyz$, góc giữa hai vectơ $\vec{u} = (1; 1; 0)$ và $\vec{v} = (0; 1; 1)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $30^\circ$.</div>
    <div><strong>B.</strong> $45^\circ$.</div>
    <div><strong>C.</strong> $60^\circ$.</div>
    <div><strong>D.</strong> $90^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 5.</span> Với $a, b$ là các số thực dương tùy ý, $a \ne 1$ và $\log_a b = 4$. Giá trị của biểu thức $P = \log_a(a^3 b^2)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $11$.</div>
    <div><strong>B.</strong> $24$.</div>
    <div><strong>C.</strong> $14$.</div>
    <div><strong>D.</strong> $9$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 6.</span> Giá trị nhỏ nhất của hàm số $y = x + \dfrac{4}{x}$ trên đoạn $[1; 3]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{13}{3}$.</div>
    <div><strong>B.</strong> $5$.</div>
    <div><strong>C.</strong> $4$.</div>
    <div><strong>D.</strong> $2$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 7.</span> Phương trình $\cos 2x = \dfrac{\sqrt{2}}{2}$ có họ nghiệm là
  <div class="options-grid-2">
    <div><strong>A.</strong> $x = \pm \dfrac{\pi}{4} + k\pi \ (k \in \mathbb{Z})$.</div>
    <div><strong>B.</strong> $x = \pm \dfrac{\pi}{8} + k\pi \ (k \in \mathbb{Z})$.</div>
    <div><strong>C.</strong> $x = \pm \dfrac{\pi}{8} + k2\pi \ (k \in \mathbb{Z})$.</div>
    <div><strong>D.</strong> $x = \dfrac{\pi}{8} + k\pi \ (k \in \mathbb{Z})$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8.</span> Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông cân tại $B$ với $AB = 2a$ và cạnh bên $AA' = 3a$. Thể tích của khối lăng trụ đã cho bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $2a^3$.</div>
    <div><strong>B.</strong> $4a^3$.</div>
    <div><strong>C.</strong> $12a^3$.</div>
    <div><strong>D.</strong> $6a^3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, mặt phẳng đi qua điểm $M(1; -2; 3)$ và song song với mặt phẳng $(Q): 2x - 3y + z - 5 = 0$ có phương trình là
  <div class="options-grid-2">
    <div><strong>A.</strong> $2x - 3y + z - 11 = 0$.</div>
    <div><strong>B.</strong> $2x - 3y + z + 11 = 0$.</div>
    <div><strong>C.</strong> $2x - 3y + z - 5 = 0$.</div>
    <div><strong>D.</strong> $x - 2y + 3z - 11 = 0$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10.</span> Kết quả đo chiều cao (đơn vị: cm) của $50$ cây giống trong vườn ươm được thống kê trong bảng tần số ghép nhóm sau:
  <table class="stats-table">
    <tr>
      <th>Chiều cao (cm)</th>
      <td>$[150; 155)$</td>
      <td>$[155; 160)$</td>
      <td>$[160; 165)$</td>
      <td>$[165; 170)$</td>
      <td>$[170; 175)$</td>
    </tr>
    <tr>
      <th>Số cây</th>
      <td>$4$</td>
      <td>$10$</td>
      <td>$16$</td>
      <td>$12$</td>
      <td>$8$</td>
    </tr>
  </table>
  Mốt $M_o$ của mẫu số liệu ghép nhóm trên bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $162$.</div>
    <div><strong>B.</strong> $162{,}5$.</div>
    <div><strong>C.</strong> $163$.</div>
    <div><strong>D.</strong> $164$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11.</span> Cho hai biến cố $A$ và $B$ thỏa mãn $P(A) = 0{,}5$, $P(B) = 0{,}4$ và $P(A|B) = 0{,}3$. Giá trị của $P(A \cup B)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $0{,}9$.</div>
    <div><strong>B.</strong> $0{,}78$.</div>
    <div><strong>C.</strong> $0{,}12$.</div>
    <div><strong>D.</strong> $0{,}75$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 12.</span> Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = \dfrac{3n - 2}{n + 1}$ ($n \in \mathbb{N}^*$). Số $\dfrac{19}{8}$ là số hạng thứ bao nhiêu của dãy số đã cho?
  <div class="options-grid-4">
    <div><strong>A.</strong> Thứ $5$.</div>
    <div><strong>B.</strong> Thứ $6$.</div>
    <div><strong>C.</strong> Thứ $8$.</div>
    <div><strong>D.</strong> Thứ $7$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div class="section-title">PHẦN II. Câu trắc nghiệm đúng sai.</div>
<div class="section-subtitle">Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $f(x) = (x^2 - 3x + 1)e^x$.
  <div class="tf-list">
    <div class="tf-item"><strong>a)</strong> Đạo hàm của hàm số đã cho là $f'(x) = (x^2 - x - 2)e^x$.</div>
    <div class="tf-item"><strong>b)</strong> Hàm số đạt cực tiểu tại $x = -1$ và đạt cực đại tại $x = 2$.</div>
    <div class="tf-item"><strong>c)</strong> Giá trị lớn nhất của hàm số trên đoạn $[0; 3]$ bằng $e^3$.</div>
    <div class="tf-item"><strong>d)</strong> Phương trình $f(x) = 0$ vô nghiệm trên $\mathbb{R}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2.</span> Một bể chứa ban đầu đang có $100\text{ m}^3$ nước sạch. Từ thời điểm $t = 0$ phút đến $t = 30$ phút, người ta mở đồng thời vòi bơm nước vào bể với lưu lượng $v_1(t) = 0{,}3t + 8$ ($\text{m}^3/\text{phút}$) và mở van xả nước phục vụ tưới tiêu với lưu lượng $v_2(t) = 0{,}03t^2 + 2$ ($\text{m}^3/\text{phút}$), với $0 \le t \le 30$. Gọi $V(t)$ là lượng nước có trong bể tại thời điểm $t$ phút.
  <div class="tf-list">
    <div class="tf-item"><strong>a)</strong> Tổng lượng nước bơm vào bể trong $10$ phút đầu tiên bằng $105\text{ m}^3$.</div>
    <div class="tf-item"><strong>b)</strong> Lượng nước trong bể tăng liên tục trong $20$ phút đầu tiên.</div>
    <div class="tf-item"><strong>c)</strong> Lượng nước lớn nhất có trong bể trong khoảng thời gian $30$ phút trên bằng $200\text{ m}^3$.</div>
    <div class="tf-item"><strong>d)</strong> Tại thời điểm $t = 30$ phút, lượng nước còn lại trong bể nhiều hơn $150\text{ m}^3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3.</span> Có hai hộp đựng các viên bi có cùng kích thước và khối lượng: Hộp I chứa $6$ viên bi trắng và $5$ viên bi đen; Hộp II chứa $3$ viên bi trắng và $4$ viên bi đen. Thực hiện liên tiếp hai bước ngẫu nhiên sau: ở bước 1, lấy ngẫu nhiên đồng thời $2$ viên bi từ Hộp I bỏ sang Hộp II; ở bước 2, trộn đều rồi lấy ngẫu nhiên đồng thời $2$ viên bi từ Hộp II ra ngoài.
  <div class="tf-list">
    <div class="tf-item"><strong>a)</strong> Xác suất để $2$ viên bi lấy ra từ Hộp I ở bước 1 có cùng màu bằng $\dfrac{5}{11}$.</div>
    <div class="tf-item"><strong>b)</strong> Biết rằng ở bước 1 đã chuyển sang Hộp II hai viên bi cùng màu trắng, xác suất để $2$ viên bi lấy ra từ Hộp II ở bước 2 đều có màu trắng bằng $\dfrac{1}{3}$.</div>
    <div class="tf-item"><strong>c)</strong> Xác suất để $2$ viên bi lấy ra từ Hộp II ở bước 2 có cùng màu bằng $\dfrac{6}{11}$.</div>
    <div class="tf-item"><strong>d)</strong> Giả sử kết quả ở bước 2 lấy được $2$ viên bi đều màu trắng; khi đó xác suất để ở bước 1 đã chuyển sang Hộp II đúng $1$ viên bi trắng và $1$ viên bi đen bằng $\dfrac{1}{2}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian $Oxyz$ (đơn vị trên mỗi trục là mét), mặt đất được mô hình hóa bởi mặt phẳng $(Oxy)$ với trục $Oz$ hướng thẳng đứng lên trên. Một nhà kho có phần mái dốc phẳng nằm trong mặt phẳng $(\alpha): x + 2y + 2z - 48 = 0$. Trên đỉnh một cột thu phát thẳng đứng, người ta đặt thiết bị cảm biến tại điểm $S(10; 9; 19)$.
  <div class="tf-list">
    <div class="tf-item"><strong>a)</strong> Góc tạo bởi mặt phẳng mái $(\alpha)$ và mặt đất $(Oxy)$ nhỏ hơn $45^\circ$.</div>
    <div class="tf-item"><strong>b)</strong> Khoảng cách từ vị trí đặt cảm biến $S$ đến mặt phẳng mái $(\alpha)$ bằng $6\text{ m}$.</div>
    <div class="tf-item"><strong>c)</strong> Điểm trên mặt phẳng mái $(\alpha)$ gần cảm biến $S$ nhất có tọa độ là $K(8; 5; 15)$.</div>
    <div class="tf-item"><strong>d)</strong> Dựng một thanh giằng thẳng nối từ $S$ tới điểm $A(4; 9; 13)$ thuộc mặt mái $(\alpha)$; khi đó góc tạo bởi thanh giằng $SA$ và mặt mái $(\alpha)$ bằng $60^\circ$.</div>
  </div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div class="section-title">PHẦN III. Câu trắc nghiệm trả lời ngắn.</div>
<div class="section-subtitle">Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="question-title">Câu 1.</span> Một chi tiết trang trí hình tròn tâm $O$, bán kính $R = 5\text{ dm}$. Người ta thiết kế phần tô màu bên trong hình tròn được giới hạn bởi cung nhỏ $\widehat{AB}$ có độ dài dây cung $AB = 6\text{ dm}$ và một đường parabol $(P)$ nhận điểm thấp nhất $C$ của đường tròn làm đỉnh, đi qua hai điểm $A, B$ (như hình vẽ, trục đối xứng của $(P)$ là đường kính $OC$ vuông góc với $AB$, trong đó $A$ và $B$ nằm về nửa đường tròn đối diện với $C$ qua $O$). Tính diện tích của phần tô màu (đơn vị: $\text{dm}^2$, kết quả làm tròn đến hàng phần chục).
  <div class="img-center">
    <img src="data:image/png;base64,__IMG_P3_C1__" style="width: 245px; height: auto;" alt="Logo tròn và parabol">
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2.</span> Một hành lang chữ L trong nhà xưởng có bề rộng hai nhánh vuông góc với nhau lần lượt là $2{,}7\text{ m}$ và $6{,}4\text{ m}$ (như hình vẽ). Người ta cần di chuyển một thanh thép thẳng cứng nằm ngang (coi độ dày không đáng kể) đi vòng qua góc vuông của hành lang đó mà không bị vướng. Hỏi chiều dài lớn nhất có thể của thanh thép bằng bao nhiêu mét?
  <div class="img-center">
    <img src="data:image/png;base64,__IMG_P3_C2__" style="width: 300px; height: auto;" alt="Hành lang chữ L">
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3.</span> Cho hình lăng trụ $ABC.A'B'C'$ có đáy $ABC$ là tam giác cân tại $A$ với $AB = AC = 10$ và $BC = 12$. Biết hình chiếu vuông góc của đỉnh $A'$ lên mặt phẳng $(ABC)$ là trung điểm $H$ của cạnh $BC$ và khoảng cách giữa hai đường thẳng chéo nhau $AA'$ và $BC$ bằng $4{,}8$. Tính thể tích khối chóp $A'.BCC'B'$.
</div>

<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian $Oxyz$ (đơn vị trên mỗi trục là mét), người ta thiết kế một vòng tròn ánh sáng $(C)$ là giao tuyến của mặt cầu $(S): (x - 1)^2 + (y - 4)^2 + (z - 6)^2 = 25$ và mặt phẳng $(P): x + 2y + 2z - 12 = 0.$ Một cảm biến thu nhận đặt cố định tại vị trí $A(10; 4; 15)$. Khi một nguồn sáng $M$ di chuyển dọc theo đường tròn $(C)$, khoảng cách ngắn nhất từ cảm biến $A$ đến nguồn sáng $M$ bằng bao nhiêu mét?
</div>

<div class="question">
  <span class="question-title">Câu 5.</span> Trên một giá sách có $7$ cuốn sách đôi một khác nhau gồm $3$ cuốn sách Toán, $2$ cuốn sách Vật lí và $2$ cuốn sách Hóa học. Xếp ngẫu nhiên tất cả $7$ cuốn sách đó thành một hàng ngang trên giá. Tính xác suất để không có hai cuốn sách cùng môn nào đứng cạnh nhau (kết quả làm tròn đến hàng phần trăm).
</div>

<div class="question">
  <span class="question-title">Câu 6.</span> Một câu lạc bộ thể thao có $9$ vận động viên gồm $6$ nam và $3$ nữ. Ban huấn luyện thực hiện hai bước phân chia và chọn ghép cặp ngẫu nhiên liên tiếp như sau: ở bước 1, chọn ngẫu nhiên đồng thời $3$ vận động viên để lập Đội A, $6$ vận động viên còn lại thuộc Đội B; ở bước 2, chọn ngẫu nhiên $1$ vận động viên từ Đội A và $1$ vận động viên từ Đội B để ghép thành một cặp thi đấu đôi. Biết rằng cặp thi đấu ghép được ở bước 2 là một cặp nam – nữ. Tính xác suất để ở bước 1 đã chọn vào Đội A đúng $1$ vận động viên nữ và $2$ vận động viên nam (kết quả làm tròn đến hàng phần trăm).
</div>

<div class="end-exam">---------- HẾT ----------</div>
<div class="end-note">- Thí sinh không được sử dụng tài liệu. - Cán bộ coi thi không giải thích gì thêm.</div>

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
    .replace("__IMG_P3_C1__", img_p3_c1)
    .replace("__IMG_P3_C2__", img_p3_c2)
)

html_path = os.path.join(BASE_DIR, "_tmp_de202.html")
pdf_path = os.path.join(BASE_DIR, "De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_202.pdf")

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
    print("Running Chrome to generate De 202 PDF...")
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
