import os

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề ôn thi giữa kì 1 - Môn Toán 12 (ĐỀ SỐ 02 - Mã đề: 102)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 7mm;
  margin-bottom: 7.5mm;
  margin-left: 13.5mm;
  margin-right: 13.5mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 102";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.8pt;
  line-height: 1.38;
  color: #000;
  margin: 0;
  padding: 0;
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
  font-size: 10.5pt;
  font-weight: bold;
  line-height: 1.25;
}

.subject-title {
  font-size: 11.5pt;
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
  padding: 2.5px 6px;
  text-align: center;
  width: 165px;
  margin: 2px auto 0 auto;
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
  margin: 2.5px 0 1.5px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 2.5px 0 3px 0;
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
  margin-top: 3px;
  margin-bottom: 3.5px;
  text-align: justify;
}

.question {
  margin-bottom: 3px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 1px;
  margin-bottom: 1px;
  padding-left: 4px;
}

.grid-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.grid-2 {
  grid-template-columns: 1fr 1fr;
}

.grid-1 {
  grid-template-columns: 1fr;
}

.sub-item {
  margin-left: 18px;
  margin-bottom: 2px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 18px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.8pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9.5pt;
}

.page-break {
  page-break-before: always;
}

/* Flex layout for questions with images */
.flex-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
}
.flex-col-text {
  flex: 1;
}
.flex-col-img {
  text-align: center;
  flex-shrink: 0;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: PHẦN I (CÂU 1 ĐẾN CÂU 8) ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN THI GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP<br>CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12 (ĐỀ SỐ 02)</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 102</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên thí sinh: ............................................................................</div>
  <div>Số báo danh: .............................</div>
</div>
<div class="solid-divider-thick"></div>

<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có bảng xét dấu của đạo hàm $f'(x)$ như sau:
  <div style="text-align: center; margin: 2px 0 3px 0;">
    <img src="assets/de2_khao_sat_bxd_cau1.png" style="max-height: 52px;" alt="Bảng xét dấu f'(x)">
  </div>
  Hàm số đã cho đạt cực đại tại điểm nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = -1$.</div>
    <div><b>B.</b> $x = 2$.</div>
    <div><b>C.</b> $x = 0$.</div>
    <div><b>D.</b> $x = 3$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$ và $f'(x) = x(x - 1)^2(x + 2)^3$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3:</span> Giá trị nhỏ nhất của hàm số $y = x + \dfrac{4}{x}$ trên đoạn $[1; 3]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $4$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $\dfrac{13}{3}$.</div>
    <div><b>D.</b> $2$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4:</span> Tiếp tuyến của đồ thị hàm số $y = x^3 - 3x + 2$ tại điểm có hoành độ $x_0 = 2$ có hệ số góc bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $9$.</div>
    <div><b>B.</b> $3$.</div>
    <div><b>C.</b> $6$.</div>
    <div><b>D.</b> $12$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5:</span> Đường tiệm cận đứng của đồ thị hàm số $y = \dfrac{2x + 1}{x - 3}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = 3$.</div>
    <div><b>B.</b> $x = -3$.</div>
    <div><b>C.</b> $y = 2$.</div>
    <div><b>D.</b> $y = 3$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6:</span> Tọa độ giao điểm của đồ thị hàm số $y = x^3 - 3x^2 + 2$ với trục tung $Oy$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $(0; 2)$.</div>
    <div><b>B.</b> $(2; 0)$.</div>
    <div><b>C.</b> $(0; -2)$.</div>
    <div><b>D.</b> $(1; 0)$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 7:</span> Đường cong trong hình vẽ bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-1" style="margin-top: 4px;">
        <div><b>A.</b> $y = x^3 - 3x + 1$.</div>
        <div><b>B.</b> $y = -x^3 + 3x + 1$.</div>
        <div><b>C.</b> $y = x^3 - 3x^2 + 1$.</div>
        <div><b>D.</b> $y = x^4 - 2x^2 + 1$.</div>
      </div>
    </div>
    <div class="flex-col-img" style="width: 265px;">
      <img src="assets/de2_khao_sat_dothi_cau7.png" style="max-height: 218px;" alt="Đồ thị Câu 7">
    </div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8:</span> Điểm cực đại của hàm số $y = x^4 - 2x^2 + 3$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = 0$.</div>
    <div><b>B.</b> $x = 1$.</div>
    <div><b>C.</b> $x = -1$.</div>
    <div><b>D.</b> $y = 3$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: CÂU 9-12 PHẦN I & CÂU 1-2 PHẦN II ==================== -->
<div class="page-break"></div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9:</span> Đường tiệm cận ngang của đồ thị hàm số $y = \dfrac{3x + 2}{1 - x}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = -3$.</div>
    <div><b>B.</b> $y = 3$.</div>
    <div><b>C.</b> $x = 1$.</div>
    <div><b>D.</b> $y = 1$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10:</span> Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \dfrac{x - 2}{x - m}$ đồng biến trên từng khoảng xác định.
  <div class="options-grid grid-4">
    <div><b>A.</b> $m < 2$.</div>
    <div><b>B.</b> $m > 2$.</div>
    <div><b>C.</b> $m \le 2$.</div>
    <div><b>D.</b> $m \ne 2$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11:</span> Tọa độ tâm đối xứng của đồ thị hàm số bậc ba $y = x^3 - 3x^2 + 4$ là điểm
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 2)$.</div>
    <div><b>B.</b> $I(0; 4)$.</div>
    <div><b>C.</b> $I(2; 0)$.</div>
    <div><b>D.</b> $I(-1; 0)$.</div>
  </div>
</div>

<!-- Câu 12: Đồ thị hàm số bậc 1 / bậc 1 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 12:</span> Đường cong trong hình vẽ bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-1" style="margin-top: 4px;">
        <div><b>A.</b> $y = \dfrac{x - 2}{x - 1}$.</div>
        <div><b>B.</b> $y = \dfrac{x + 2}{x - 1}$.</div>
        <div><b>C.</b> $y = \dfrac{2x - 1}{x - 1}$.</div>
        <div><b>D.</b> $y = \dfrac{x - 2}{x + 1}$.</div>
      </div>
    </div>
    <div class="flex-col-img" style="width: 270px;">
      <img src="assets/de2_khao_sat_dothi_cau12.png" style="max-height: 218px;" alt="Đồ thị Câu 12">
    </div>
  </div>
</div>

<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<!-- Câu 1 Phần II (Theo ảnh 1 upload) -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = \dfrac{x^2 + 2x + 2}{x + 1}$ có đồ thị $(C)$. Gọi $I$ là giao điểm hai đường tiệm cận của $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có tiệm cận đứng $x = -1$ và tiệm cận xiên $y = x + 1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho nghịch biến trên khoảng $(-2; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Có đúng hai giá trị nguyên của tham số $m$ để đường thẳng $y = m$ không có điểm chung với $(C)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tiếp tuyến tại điểm $M$ bất kỳ thuộc $(C)$ cắt tiệm cận đứng và tiệm cận xiên lần lượt tại $A$ và $B$. Khi đó diện tích tam giác $IAB$ luôn bằng $2$.</div>
</div>

<!-- Câu 2 Phần II (Theo ảnh 2 upload) -->
<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $f(x) = \dfrac{x^3}{3} - 3x - 6\ln(2 - x) + 1$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đạo hàm của hàm số đã cho là $f'(x) = \dfrac{x^3 - 2x^2 - 3x}{x - 2}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho đồng biến trong khoảng $(-\infty; -1)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tổng các giá trị cực đại và cực tiểu của đồ thị hàm số bằng $\dfrac{14}{3} - 6\ln 6$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Hàm số $g(x) = \dfrac{f(x)}{x^2 + 2x + 2}$ có đường tiệm cận xiên có dạng $y = ax + b$. Khi đó $a + b = \dfrac{1}{3}$.</div>
</div>

<!-- ==================== TRANG 3: CÂU 3-4 PHẦN II & CÂU 1-3 PHẦN III ==================== -->
<div class="page-break"></div>

<!-- Câu 3 Phần II: Dạng bài tìm m để hàm số -->
<div class="question">
  <span class="question-title">Câu 3:</span> Cho hàm số $y = f(x) = \dfrac{1}{3}x^3 - x^2 - mx + 1$ với $m$ là tham số thực.
  <div class="sub-item"><span class="sub-item-label">a)</span> Khi $m = 3$, hàm số đã cho nghịch biến trên khoảng $(-1; 3)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị hàm số đã cho có hai điểm cực trị khi và chỉ khi $m > -1$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khi $m = 3$, hàm số đạt cực đại tại điểm $x = 3$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tập hợp tất cả các giá trị của tham số $m$ để hàm số đồng biến trên khoảng $(2; +\infty)$ là nửa khoảng $(-\infty; 0]$.</div>
</div>

<!-- Câu 4 Phần II (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 4:</span> Một nguồn điện một chiều không đổi có suất điện động $E = 12\text{ V}$ và điện trở trong $r = 2\,\Omega$. Mạch ngoài là một biến trở có điện trở $R > 0$. Công suất tiêu thụ trên mạch ngoài được xác định bởi hàm số:
      $$P(R) = \dfrac{144R}{(R + 2)^2}\quad (R > 0),$$
      có đồ thị như hình vẽ bên.
      <div class="sub-item" style="margin-top: 6px;"><span class="sub-item-label">a)</span> Tập xác định của hàm số công suất là nửa khoảng $[0; +\infty)$.</div>
      <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số là $P'(R) = \dfrac{144(2 - R)}{(R + 2)^3}$ với mọi $R > 0$.</div>
      <div class="sub-item"><span class="sub-item-label">c)</span> Khi điện trở mạch ngoài tăng trong khoảng từ $0\,\Omega$ đến $2\,\Omega$ thì công suất tiêu thụ mạch ngoài tăng dần.</div>
      <div class="sub-item"><span class="sub-item-label">d)</span> Công suất tiêu thụ trên mạch ngoài đạt giá trị lớn nhất bằng $18\text{ W}$ khi điện trở mạch ngoài $R = 2\,\Omega$.</div>
    </div>
    <div class="flex-col-img" style="width: 290px;">
      <img src="assets/de2_khao_sat_mach_dien_cau4.png" style="max-height: 220px; width: 100%;" alt="Đồ thị công suất">
    </div>
  </div>
</div>

<div class="section-title" style="margin-top: 5px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu trả lời đúng thí sinh được 0,5 điểm.</div>

<!-- Câu 1 Phần III -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số bậc ba $f(x) = x^3 - 3x^2 + 2$. Phương trình $f(f(x)) = 0$ có bao nhiêu nghiệm thực phân biệt?
</div>

<!-- Câu 2 Phần III -->
<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 1)^2 (x^2 - 4)$ với mọi $x \in \mathbb{R}$. Tìm số điểm cực trị của hàm số $g(x) = f(x^2 - 2)$.
</div>

<!-- Câu 3 Phần III (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 3:</span> Trong một tiết học Toán, giáo viên phát cho 4 tổ một tấm bìa hình vuông $ABCD$ cạnh bằng $10\text{ cm}$. Giáo viên yêu cầu 4 tổ sử dụng tấm bìa này và cắt tấm bìa theo các tam giác cân $AEB, BFC, CGD, DHA$ để sau đó gấp các tam giác $AEH, BEF, CFG, DGH$ sao cho bốn đỉnh $A, B, C, D$ trùng nhau tạo thành khối chóp tứ giác đều (tham khảo hình vẽ bên). Khi đó thể tích lớn nhất của khối chóp tứ giác đều tạo thành bằng $\dfrac{a\sqrt{b}}{c}\text{ (cm}^3\text{)}$ với $a, b, c$ là các số nguyên dương và phân số tối giản. Tính giá trị của biểu thức $P = a + b + c$.
    </div>
    <div class="flex-col-img" style="width: 320px;">
      <img src="assets/de2_khao_sat_gap_bia_cau3.png" style="max-height: 175px; width: 100%;" alt="Gấp tấm bìa hình chóp">
    </div>
  </div>
</div>

<!-- ==================== TRANG 4: CÂU 4-6 PHẦN III & HẾT ==================== -->
<div class="page-break"></div>

<!-- Câu 4 Phần III (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 4:</span> Một cái ao nuôi cá hình chữ nhật của nhà ông An, tại một góc của ao ông An đóng một cái cọc ở vị trí $K$ cách bờ $AB$ là $1\text{ m}$ và cách bờ $AC$ là $8\text{ m}$, rồi dùng một dây phao căng thẳng ngăn một góc của ao để làm nơi cho cá ăn (phần tô màu như hình vẽ bên) sao cho dây phao có thể đồng thời chạm vào hai bờ $AB, AC$ và vào cái cọc $K$. Biết mỗi mét dây phao ông An cần mua có giá $130$ nghìn đồng. Hỏi ông An phải bỏ ra ít nhất bao nhiêu nghìn đồng để mua dây phao đó? <i>(Bỏ qua đường kính của dây phao và cái cọc, làm tròn kết quả đến hàng đơn vị)</i>.
    </div>
    <div class="flex-col-img" style="width: 290px;">
      <img src="assets/de2_khao_sat_ao_ca_cau4.png" style="max-height: 235px; width: 100%;" alt="Ao cá có cọc K">
    </div>
  </div>
</div>

<!-- Câu 5 Phần III (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 8px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 5:</span> Một bồn chứa nước sinh hoạt có dạng một khối nón tròn xoay có đỉnh hướng thẳng đứng xuống dưới. Bán kính miệng bồn là $R = 30\text{ cm}$ và chiều sâu (chiều cao) của bồn là $H = 60\text{ cm}$. Người ta xả nước vào bồn từ một vòi nước với lưu lượng không đổi bằng $50\pi\text{ cm}^3\text{/s}$ (như hình vẽ bên). Tại thời điểm chiều cao của khối nước trong bồn đạt $h = 20\text{ cm}$, tốc độ dâng lên của mực nước trong bồn bằng bao nhiêu cm/s? <i>(Kết quả ghi dưới dạng số thập phân)</i>.
    </div>
    <div class="flex-col-img" style="width: 280px;">
      <img src="assets/de2_khao_sat_bon_nuoc_cau5.png" style="max-height: 235px; width: 100%;" alt="Bồn nước hình nón">
    </div>
  </div>
</div>

<!-- Câu 6 Phần III (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 8px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 6:</span> Một bờ hồ hình bán nguyệt có bán kính bằng $2\text{ km}$, đường kính $AB$ (tham khảo hình vẽ bên). Từ điểm $A$ anh Tài chèo một chiếc thuyền với vận tốc $3\text{ km/h}$ đến điểm $C$ trên hồ, rồi chạy dọc theo thành hồ đến vị trí $B$ với vận tốc $6\text{ km/h}$ ($C$ không trùng với $A$ và $B$). Thời gian ngắn nhất mà anh Tài di chuyển từ $A$ đến $B$ là bao nhiêu giờ? <i>(Kết quả làm tròn đến hàng phần chục)</i>.
    </div>
    <div class="flex-col-img" style="width: 320px;">
      <img src="assets/de2_khao_sat_ho_ban_nguyet_cau6.png" style="max-height: 215px; width: 100%;" alt="Bờ hồ bán nguyệt">
    </div>
  </div>
</div>

<div class="end-exam" style="margin-top: 30px;">----------------------- HẾT -----------------------</div>
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

with open('exam_de2_khao_sat.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("exam_de2_khao_sat.html updated with deg 1/1 graph and parameter m problem successfully!")
