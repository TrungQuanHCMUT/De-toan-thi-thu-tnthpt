import os, subprocess, pypdf, base64

def get_base64_img(filename):
    with open(filename, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

img_p3_c1 = get_base64_img('de200_p3_c1_ellipsoid.png')
img_p3_c2 = get_base64_img('de200_p3_c2_fold.png')
img_p3_c3 = get_base64_img('de200_p3_c3_frustum.png')
img_p3_c5 = get_base64_img('de200_p3_c5_grid.png')
img_p3_c6 = get_base64_img('de200_p3_c6_circles.png')

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề Thi Thử Kì Thi TNTHPT Quốc Gia - Mã Đề 200</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4 portrait;
  margin: 11mm 13mm 11mm 13mm;
}
* {
  box-sizing: border-box;
}
body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 10.3pt;
  line-height: 1.32;
  color: #000;
  margin: 0;
  padding: 0;
}
.katex {
  font-size: 1.02em;
}
.katex-display {
  margin: 3px 0;
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
  font-size: 10.2pt;
  margin-top: 2px;
  margin-bottom: 2px;
}
.section-title {
  font-weight: bold;
  font-size: 10.6pt;
  margin-top: 3px;
  margin-bottom: 2px;
}
.section-subtitle {
  font-style: italic;
  font-size: 9.6pt;
  margin-bottom: 5px;
}
.question {
  margin-bottom: 5px;
  text-align: justify;
}
.question-title {
  font-weight: bold;
}
.options-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 2px;
  margin-bottom: 2px;
}
.options-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  row-gap: 1.5px;
  margin-top: 2px;
  margin-bottom: 2px;
}
.sub-item {
  margin-left: 10px;
  margin-top: 3.5px;
  margin-bottom: 3.5px;
}
.sub-item-label {
  font-weight: bold;
  display: inline-block;
  width: 18px;
}
.stats-table {
  width: 92%;
  margin: 3px auto 3px auto;
  border-collapse: collapse;
  font-size: 9.5pt;
  text-align: center;
}
.stats-table th, .stats-table td {
  border: 1px solid #000;
  padding: 2px 5px;
}
.end-exam {
  text-align: center;
  font-weight: bold;
  margin-top: 14px;
  font-size: 10.8pt;
}
.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9.3pt;
  margin-top: 3px;
}
.img-center {
  text-align: center;
  margin: 5px 0;
}
.img-p3-c1 {
  max-width: 520px;
  width: 80%;
  height: auto;
  display: inline-block;
}
.img-p3-c2 {
  max-width: 340px;
  width: 52%;
  height: auto;
  display: inline-block;
}
.img-p3-c3 {
  max-width: 280px;
  width: 43%;
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
      <div class="code-box">Mã đề: 200</div>
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
  <div>Họ và tên học sinh: ............................................................................</div>
  <div>Lớp: ............................................................................</div>
</div>
<div class="solid-divider-thick"></div>

<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 (Lớp 12 - Tiệm cận xiên & diện tích tam giác - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 1.</span> Đồ thị hàm số $y = \dfrac{2x^2 - 5x + 1}{x - 1}$ có đường tiệm cận xiên là đường thẳng $\Delta$. Diện tích tam giác tạo bởi đường thẳng $\Delta$ và hai trục tọa độ $Ox, Oy$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{9}{4}$.</div>
    <div><strong>B.</strong> $\dfrac{9}{2}$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $\dfrac{3}{2}$.</div>
  </div>
</div>

<!-- Câu 2 (Lớp 12 - GTNN hàm số chứa logarit - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 2.</span> Giá trị nhỏ nhất của hàm số $f(x) = x - 2\ln x$ trên đoạn $[1; e]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $e - 2$.</div>
    <div><strong>C.</strong> $2 - 2\ln 2$.</div>
    <div><strong>D.</strong> $2 - \ln 2$.</div>
  </div>
</div>

<!-- Câu 3 (Lớp 11/12 - Đạo hàm của hàm số - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 3.</span> Đạo hàm của hàm số $y = \dfrac{e^{2x}}{x + 1}$ (với $x \ne -1$) là
  <div class="options-grid-4">
    <div><strong>A.</strong> $y' = \dfrac{(2x + 3)e^{2x}}{(x + 1)^2}$.</div>
    <div><strong>B.</strong> $y' = \dfrac{(2x + 1)e^{2x}}{(x + 1)^2}$.</div>
    <div><strong>C.</strong> $y' = \dfrac{(2x + 1)e^{2x}}{x + 1}$.</div>
    <div><strong>D.</strong> $y' = \dfrac{x e^{2x}}{(x + 1)^2}$.</div>
  </div>
</div>

<!-- Câu 4 (Lớp 10 - Hệ thức lượng trong tam giác - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 4.</span> Cho tam giác $ABC$ có $AB = 5$, $AC = 8$ và $\widehat{BAC} = 60^\circ$. Bán kính đường tròn ngoại tiếp tam giác $ABC$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{7\sqrt{3}}{2}$.</div>
    <div><strong>B.</strong> $7\sqrt{3}$.</div>
    <div><strong>C.</strong> $\dfrac{7}{3}$.</div>
    <div><strong>D.</strong> $\dfrac{7\sqrt{3}}{3}$.</div>
  </div>
</div>

<!-- Câu 5 (Lớp 11 - Phương trình lượng giác - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 5.</span> Tổng tất cả các nghiệm của phương trình $\sin\left(2x - \dfrac{\pi}{3}\right) = \dfrac{1}{2}$ thuộc đoạn $[0; \pi]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{\pi}{2}$.</div>
    <div><strong>B.</strong> $\dfrac{7\pi}{6}$.</div>
    <div><strong>C.</strong> $\dfrac{5\pi}{6}$.</div>
    <div><strong>D.</strong> $\dfrac{2\pi}{3}$.</div>
  </div>
</div>

<!-- Câu 6 (Lớp 11 - Cấp số nhân - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 6.</span> Cho cấp số nhân $(u_n)$ có tất cả các số hạng đều dương, thỏa mãn $u_1 + u_2 = 12$ và $u_3 + u_4 = 48$. Giá trị của $u_5$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $64$.</div>
    <div><strong>B.</strong> $32$.</div>
    <div><strong>C.</strong> $128$.</div>
    <div><strong>D.</strong> $48$.</div>
  </div>
</div>

<!-- Câu 7 (Lớp 11 - Bất phương trình logarit - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 7.</span> Số nghiệm nguyên của bất phương trình $\log_{0,5}(x^2 - 3x + 2) \ge -1$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $4$.</div>
    <div><strong>B.</strong> $3$.</div>
    <div><strong>C.</strong> $1$.</div>
    <div><strong>D.</strong> $2$.</div>
  </div>
</div>

<!-- Câu 8 (Lớp 11 - Thể tích khối chóp cụt đều - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 8.</span> Một bồn hoa công viên có dạng khối chóp cụt tứ giác đều với cạnh đáy lớn bằng $4\text{ m}$, cạnh đáy nhỏ bằng $2\text{ m}$ và chiều cao bằng $3\text{ m}$. Thể tích của khối chóp cụt đó bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $20\text{ m}^3$.</div>
    <div><strong>B.</strong> $28\text{ m}^3$.</div>
    <div><strong>C.</strong> $24\text{ m}^3$.</div>
    <div><strong>D.</strong> $32\text{ m}^3$.</div>
  </div>
</div>

<!-- Câu 9 (Lớp 12 - Tích phân hàm cho bởi nhiều công thức - Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 9.</span> Cho hàm số $f(x) = \begin{cases} 2x + 1 & \text{khi } x \ge 1 \\ 3x^2 & \text{khi } x < 1 \end{cases}$. Giá trị của tích phân $I = \int_0^2 f(x)\,\mathrm{d}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $4$.</div>
    <div><strong>B.</strong> $7$.</div>
    <div><strong>C.</strong> $5$.</div>
    <div><strong>D.</strong> $6$.</div>
  </div>
</div>

<!-- Câu 10 (Lớp 12 - Thể tích vật thể theo thiết diện S(x) - Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, một vật thể nằm giữa hai mặt phẳng $x = 0$ và $x = 2$. Biết thiết diện của vật thể bị cắt bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ ($0 \le x \le 2$) là một tam giác đều có cạnh bằng $\sqrt{x^2 + 1}$. Thể tích của vật thể đó bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\dfrac{7\sqrt{3}}{6}$.</div>
    <div><strong>B.</strong> $\dfrac{7\sqrt{3}}{3}$.</div>
    <div><strong>C.</strong> $\dfrac{14}{3}$.</div>
    <div><strong>D.</strong> $\dfrac{7\pi\sqrt{3}}{6}$.</div>
  </div>
</div>

<!-- Câu 11 (Lớp 12 - Thống kê mẫu số liệu ghép nhóm - Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 11.</span> Thời gian chạy cự li $100\text{ m}$ (đơn vị: giây) của $40$ học sinh lớp $12$ được thống kê trong bảng ghép nhóm sau:
  <table class="stats-table">
    <tr>
      <th>Thời gian (giây)</th>
      <td>$[12; 13)$</td>
      <td>$[13; 14)$</td>
      <td>$[14; 15)$</td>
      <td>$[15; 16)$</td>
      <td>$[16; 17)$</td>
    </tr>
    <tr>
      <th>Số học sinh</th>
      <td>$4$</td>
      <td>$10$</td>
      <td>$14$</td>
      <td>$8$</td>
      <td>$4$</td>
    </tr>
  </table>
  Khoảng tứ phân vị $\Delta_Q$ của mẫu số liệu ghép nhóm trên bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $1,45$.</div>
    <div><strong>B.</strong> $2,25$.</div>
    <div><strong>C.</strong> $1,85$.</div>
    <div><strong>D.</strong> $1,65$.</div>
  </div>
</div>

<!-- Câu 12 (Lớp 12 - Oxyz: Mặt phẳng cắt mặt cầu đường tròn nhỏ nhất - Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 12.</span> Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(2; -1; 3)$ và mặt cầu $(S): (x - 1)^2 + (y + 1)^2 + (z - 1)^2 = 9$. Mặt phẳng $(P)$ đi qua $A$ và cắt mặt cầu $(S)$ theo giao tuyến là một đường tròn có bán kính nhỏ nhất. Một vectơ pháp tuyến của mặt phẳng $(P)$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $\vec{n} = (1; -2; 2)$.</div>
    <div><strong>B.</strong> $\vec{n} = (1; 0; 2)$.</div>
    <div><strong>C.</strong> $\vec{n} = (3; -2; 4)$.</div>
    <div><strong>D.</strong> $\vec{n} = (2; -1; 3)$.</div>
  </div>
</div>

<!-- ==================== PAGE 2 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 (Lớp 12 - Khảo sát hàm số bình thường - Key: Đ - S - Đ - Đ) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \dfrac{x^2 - 3x + 6}{x - 2}$ có đồ thị $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số đã cho nghịch biến trên các khoảng $(0; 2)$ và $(2; 4)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Giá trị cực đại của hàm số lớn hơn giá trị cực tiểu của hàm số.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đồ thị $(C)$ nhận điểm $I(2; 1)$ làm tâm đối xứng và khoảng cách giữa hai điểm cực trị của $(C)$ bằng $4\sqrt{5}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Có đúng $7$ giá trị nguyên của tham số $m$ để đường thẳng $y = m$ không có điểm chung với đồ thị $(C)$.</div>
</div>

<!-- Câu 2 (Lớp 12 Tích phân & Năng lượng Mặt Trời - Không đồ thị - Key: Đ - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 2.</span> Trong khoảng thời gian $12\text{ giờ}$ ban ngày (tính bằng $t$ giờ, $0 \le t \le 12$), một hệ thống điện mặt trời áp mái của một hộ gia đình phát điện với công suất $P_{\text{phát}}(t) = -\dfrac{1}{4}t^2 + 3t\text{ (kW)}$, trong khi công suất tiêu thụ điện của gia đình là <span style="white-space: nowrap;">$P_{\text{tiêu}}(t) = 0,5t + 4\text{ (kW)}$.</span> Biết rằng điện năng (kWh) là tích phân của công suất theo thời gian. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tổng lượng điện năng mà hệ thống pin mặt trời phát ra trong $12\text{ giờ}$ bằng $72\text{ kWh}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Trong khoảng thời gian từ $t = 2\text{ giờ}$ đến $t = 8\text{ giờ}$, lượng điện dư thu được từ hệ thống bằng $9\text{ kWh}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Công suất phát điện vượt công suất tiêu thụ một lượng lớn nhất tại thời điểm $t = 6\text{ giờ}$ với độ chênh lệch bằng $2\text{ kW}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Nếu toàn bộ phần điện dư thu được được lưu trữ vào pin dự phòng với hiệu suất $100\%$ để dùng bù cho các giờ thiếu điện trong khoảng $12\text{ giờ}$ đó, lượng điện gia đình còn phải mua thêm từ lưới điện bằng $12\text{ kWh}$.</div>
</div>

<!-- Câu 3 (Lớp 12 Xác suất có điều kiện & Bayes - Key: Đ - S - Đ - S) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 3.</span> Một bệnh viện ứng dụng hệ thống trí tuệ nhân tạo (AI) để hỗ trợ sàng lọc một loại bệnh phổi qua ảnh X-quang. Theo thống kê trên nhóm người đến khám sàng lọc, tỉ lệ người thực sự mắc bệnh là $2\%$. Nếu một người thực sự mắc bệnh, mô hình AI chẩn đoán cho kết quả dương tính với xác suất $95\%$. Nếu một người không mắc bệnh, mô hình AI vẫn có thể báo nhầm kết quả dương tính với xác suất $5\%$. Chọn ngẫu nhiên một người đến khám để hệ thống AI sàng lọc. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Xác suất để người được chọn vừa mắc bệnh vừa nhận kết quả dương tính từ AI bằng $0,019$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Xác suất để mô hình AI trả về kết quả dương tính đối với một người đến khám bất kì bằng $0,05$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Nếu hệ thống AI trả về kết quả dương tính, xác suất để người đó thực sự mắc bệnh nhỏ hơn $28\%$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Nếu hệ thống AI trả về kết quả âm tính, xác suất để người đó thực sự mắc bệnh lớn hơn $0,2\%$.</div>
</div>

<!-- Câu 4 (Lớp 12 Oxyz Phản xạ tia laser - Key: S - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là mét), một phòng thí nghiệm quang học đặt một tấm gương phẳng lớn nằm trên mặt phẳng $(P): x + 2y - 2z - 5 = 0$. Một nguồn phát tia laser đặt tại điểm $A(2; 4; -2)$ chiếu một tia sáng tới gặp mặt gương $(P)$ tại điểm $M(3; 3; 2)$ rồi phản xạ theo quy luật phản xạ ánh sáng (tia tới và tia phản xạ nằm trong cùng mặt phẳng chứa pháp tuyến tại $M$, góc tới bằng góc phản xạ). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Khoảng cách từ nguồn phát $A$ đến mặt gương $(P)$ bằng $4\text{ m}$ và tọa độ điểm đối xứng của $A$ qua $(P)$ là $A'(0; 0; 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Góc tạo bởi tia sáng tới $AM$ và mặt phẳng gương $(P)$ bằng $45^\circ$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tia sáng phản xạ đi qua điểm $M$ có một vectơ chỉ phương là $\vec{u} = (1; -1; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đặt một cảm biến thu sáng tại điểm $B(6; 6; 2)$. Nếu tia sáng đi từ $A$ tới chạm mặt gương $(P)$ tại một điểm $N$ thay đổi trên $(P)$ rồi truyền thẳng tới $B$ thì tổng quãng đường truyền $AN + NB$ ngắn nhất bằng $6\sqrt{2}\text{ m}$.</div>
</div>

<!-- ==================== PAGE 3 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 (Lớp 10 Elip + Lớp 12 Tích phân khối tròn xoay - Đáp số: 96,5) -->
<div class="question" style="margin-bottom: 10px;">
  <span class="question-title">Câu 1.</span> Một nghệ nhân chế tác một hạt vòng gỗ mỹ nghệ bằng cách tiện một khối gỗ đặc có hình dạng là khối tròn xoay thu được khi quay hình elip $(E)$ (có độ dài trục lớn bằng $10\text{ cm}$, độ dài trục nhỏ bằng $6\text{ cm}$) quanh trục lớn của nó. Sau đó, nghệ nhân khoan xuyên tâm dọc theo trục lớn một lỗ hình trụ có bán kính đáy $r = 1,8\text{ cm}$ (toàn bộ phần gỗ nằm bên trong mặt trụ bị loại bỏ, phần mặt cắt trên hệ trục $Oxy$ được tô đậm như hình vẽ bên dưới). Thể tích phần gỗ còn lại của hạt vòng bằng bao nhiêu $\text{cm}^3$ (làm tròn kết quả đến hàng phần mười)?
  <div class="img-center">
    <img src="__IMG_P3_C1__" class="img-p3-c1" alt="Hạt vòng elipxoit khoan lỗ trụ">
  </div>
</div>

<!-- Câu 2 (Lớp 12 Đạo hàm Tối ưu Thực tế - Gấp góc tờ giấy - Đáp số: 15,6) -->
<div class="question" style="margin-bottom: 10px;">
  <span class="question-title">Câu 2.</span> Cho một tờ giấy hình chữ nhật $ABCD$ có chiều rộng $AB = 12\text{ cm}$ và chiều dài $BC = 20\text{ cm}$. Người ta gấp góc $B$ của tờ giấy sao cho đỉnh $B$ chạm tới một điểm $E$ nằm trên cạnh đối diện $AD$, tạo thành nếp gấp là đoạn thẳng $MN$ (với $M$ nằm trên đoạn $AB$, $N$ nằm trên đoạn $BC$, tham khảo hình vẽ). Độ dài ngắn nhất của nếp gấp $MN$ bằng bao nhiêu centimét (làm tròn kết quả đến hàng phần mười)?
  <div class="img-center">
    <img src="__IMG_P3_C2__" class="img-p3-c2" alt="Gấp góc tờ giấy chữ nhật">
  </div>
</div>

<!-- Câu 3 (Lớp 11 Hình học không gian - Chóp cụt & Góc nhị diện - Đáp số: 111) -->
<div class="question" style="margin-bottom: 6px;">
  <span class="question-title">Câu 3.</span> Phần bệ đỡ của một tháp quan sát được thiết kế có dạng hình chóp cụt tứ giác đều $ABCD.A'B'C'D'$ với cạnh đáy dưới $AB = 8\text{ m}$, cạnh đáy trên $A'B' = 2\text{ m}$ và chiều cao $OO' = 4\text{ m}$ (tham khảo hình vẽ). Tính số đo của góc nhị diện $[A, BB', C]$ tạo bởi hai mặt bên kề nhau (đơn vị: độ, làm tròn kết quả đến hàng đơn vị).
  <div class="img-center">
    <img src="__IMG_P3_C3__" class="img-p3-c3" alt="Hình chóp cụt tứ giác đều">
  </div>
</div>

<!-- ==================== PAGE 4 ==================== -->
<div style="page-break-before: always;"></div>

<!-- Câu 4 (Lớp 12 Oxyz - Phản xạ kép trên 2 mặt phẳng - Đáp số: 7) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là mét), một phòng thí nghiệm có sàn nhà nằm trên mặt phẳng $(Oxy): z = 0$ và một bức tường kính phẳng nằm trên mặt phẳng $(P): x + y - 4 = 0$. Một thiết bị bay không người lái (drone) xuất phát từ điểm $A(1; 1; 2)$, bay thẳng tới chạm nhẹ vào bức tường kính $(P)$ tại điểm $M$, sau đó bay thẳng tới chạm sàn nhà $(Oxy)$ tại điểm $N$ rồi bay thẳng về trạm sạc $B(1; -3; 1)$. Tổng quãng đường bay ngắn nhất của drone bằng bao nhiêu mét?
</div>

<!-- Câu 5 (Lớp 10 Tổ hợp + Lớp 12 Xác suất có điều kiện trên lưới - Đáp số: 0,55) -->
<div class="question" style="margin-bottom: 14px;">
  <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
    <div style="flex: 1;">
      <span class="question-title">Câu 5.</span> Trên mặt phẳng tọa độ $Oxy$, một robot tự hành xuất phát từ điểm $O(0; 0)$ để di chuyển đến đích $A(4; 4)$ theo các cạnh của lưới ô vuông đơn vị (tham khảo hình vẽ). Ở mỗi bước, robot chỉ được phép đi sang phải $1$ đơn vị hoặc đi lên trên $1$ đơn vị, và tất cả các đường đi ngắn nhất từ $O$ đến $A$ đều có khả năng được chọn như nhau. Biết rằng robot đã tránh được điểm chướng ngại vật $M(1; 2)$ (không đi qua $M$), tính xác suất để robot đi qua trạm tiếp nhiên liệu $N(3; 3)$.
    </div>
    <div style="width: 150px; text-align: right; flex-shrink: 0;">
      <img src="__IMG_P3_C5__" style="width: 145px; height: auto;" alt="Lưới tọa độ Câu 5">
    </div>
  </div>
</div>

<!-- Câu 6 (Lớp 10 Đường tròn + Lớp 11 Cấp số nhân lùi vô hạn - Đáp số: 56,5) -->
<div class="question" style="margin-bottom: 14px;">
  <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
    <div style="flex: 1;">
      <span class="question-title">Câu 6.</span> Trong góc nhọn $\widehat{xOy} = 60^\circ$, người ta vẽ vô hạn các hình tròn $(C_1), (C_2), (C_3), \dots$ sao cho mỗi hình tròn đều tiếp xúc với hai tia $Ox, Oy$; hình tròn lớn nhất $(C_1)$ có bán kính $R_1 = 4\text{ cm}$ và mỗi hình tròn $(C_{n+1})$ có bán kính nhỏ hơn $(C_n)$ đồng thời tiếp xúc ngoài với $(C_n)$ với mọi $n \ge 1$ (tham khảo hình vẽ). Tổng diện tích của tất cả các hình tròn đó bằng bao nhiêu $\text{cm}^2$ (làm tròn kết quả đến hàng phần mười)?
    </div>
    <div style="width: 160px; text-align: right; flex-shrink: 0;">
      <img src="__IMG_P3_C6__" style="width: 155px; height: auto;" alt="Chuỗi đường tròn vô hạn Câu 6">
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
    .replace('__IMG_P3_C3__', img_p3_c3)
    .replace('__IMG_P3_C5__', img_p3_c5)
    .replace('__IMG_P3_C6__', img_p3_c6)
)

html_filename = 'exam_de_thi_thu_tnthpt_ma200.html'
pdf_name = 'De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_200.pdf'

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

print("Running Chrome to generate De 200 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
