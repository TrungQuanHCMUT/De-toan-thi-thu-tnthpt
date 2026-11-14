import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (CHUYÊN ĐỀ KHẢO SÁT HÀM SỐ - Mã đề: 107)</title>
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
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 107";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.75pt;
  line-height: 1.35;
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
  margin-bottom: 3px;
  text-align: justify;
}

.section-subtitle {
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 2.5px;
}

.question {
  margin-bottom: 3.5px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}

.question-title {
  font-weight: bold;
}

.options-grid {
  display: grid;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  padding-left: 4px;
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
  margin-top: 3px;
  margin-bottom: 3.5px;
  line-height: 1.45;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.flex-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.flex-col-text {
  flex: 1;
  text-align: justify;
}

.flex-col-img {
  text-align: center;
  flex-shrink: 0;
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
  font-size: 9.2pt;
}

.page-break {
  page-break-before: always;
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
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 03 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12 (CHUYÊN ĐỀ HÀM SỐ)</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 107</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 3px 0 3px 0;">
    <img src="assets/bbt_cau1_sgk.png" style="width: 105mm; max-width: 95%;" alt="Bảng biến thiên Câu 1">
  </div>
  Hàm số đã cho nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-1; 2)$.</div>
    <div><b>B.</b> $(-\infty; -1)$.</div>
    <div><b>C.</b> $(2; +\infty)$.</div>
    <div><b>D.</b> $(-1; 3)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 1)^2(x + 2)^3$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3:</span> Đạo hàm của hàm số $y = \dfrac{2x - 1}{x + 1}$ trên từng khoảng xác định là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y' = \dfrac{3}{(x + 1)^2}$.</div>
    <div><b>B.</b> $y' = \dfrac{1}{(x + 1)^2}$.</div>
    <div><b>C.</b> $y' = \dfrac{-3}{(x + 1)^2}$.</div>
    <div><b>D.</b> $y' = \dfrac{3}{x + 1}$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4:</span> Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{x + 2}{x^2 - 4}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $0$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 5:</span> Đường cong trong hình bên là đồ thị của hàm số nào sau đây?
      <div class="options-grid grid-2" style="margin-top: 8px;">
        <div><b>A.</b> $y = -x^3 + 3x$.</div>
        <div><b>B.</b> $y = x^3 - 3x + 1$.</div>
        <div><b>C.</b> $y = x^3 - 3x$.</div>
        <div><b>D.</b> $y = x^4 - 2x^2$.</div>
      </div>
    </div>
    <div class="flex-col-img" style="width: 195px;">
      <img src="assets/dothi_cau5.png" style="width: 185px; max-width: 100%;" alt="Đồ thị hàm số bậc 3">
    </div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6:</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 3x + 5}{x - 1}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = x + 2$.</div>
    <div><b>B.</b> $y = x - 2$.</div>
    <div><b>C.</b> $y = x - 3$.</div>
    <div><b>D.</b> $y = -x + 2$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7:</span> Tọa độ tâm đối xứng của đồ thị hàm số $y = \dfrac{3x - 2}{x + 1}$ là điểm
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 3)$.</div>
    <div><b>B.</b> $I(-1; -2)$.</div>
    <div><b>C.</b> $I(3; -1)$.</div>
    <div><b>D.</b> $I(-1; 3)$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8:</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 5$ trên đoạn $[0; 2]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $7$.</div>
    <div><b>D.</b> $1$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: CÂU 9-12 PHẦN I & CÂU 1 PHẦN II ==================== -->
<!-- break 1 removed -->


<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9:</span> Hàm số $y = \sqrt{4 - x^2}$ nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(0; 2)$.</div>
    <div><b>B.</b> $(-2; 0)$.</div>
    <div><b>C.</b> $(-2; 2)$.</div>
    <div><b>D.</b> $(-\infty; 0)$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10:</span> Có bao nhiêu giá trị nguyên của tham số $m \in [-5; 5]$ để hàm số $y = \dfrac{x - 3}{x - m}$ đồng biến trên khoảng $(0; +\infty)$?
  <div class="options-grid grid-4">
    <div><b>A.</b> $6$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $7$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11:</span> Cho hàm số $y = f(x)$ liên tục trên tập số thực, có bảng biến thiên như hình vẽ sau:
  <div style="text-align: center; margin: 3px 0 3px 0;">
    <img src="assets/gk1_clean_bbt_cau11.png" style="width: 95mm; max-width: 92%;" alt="Bảng biến thiên Câu 11">
  </div>
  Điểm cực đại của hàm số là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = 3$.</div>
    <div><b>B.</b> $M(0; 3)$.</div>
    <div><b>C.</b> $N(1; -2)$.</div>
    <div><b>D.</b> $x = 0$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12:</span> Hàm số $f(x)$ có đạo hàm $f'(x) = x^2(x - 1)(x - 2)^3, \forall x \in \mathbb{R}$. Hàm số $f(x)$ có bao nhiêu điểm cực đại?
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $1$.</div>
    <div><b>C.</b> $0$.</div>
    <div><b>D.</b> $2$.</div>
  </div>
</div>

<div class="solid-divider" style="margin-top: 5px;"></div>
<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 Phần II: Hồ nước nhân tạo trong công viên -->
<div class="question" style="margin-top: 8px; line-height: 1.45;">
  <div class="flex-row">
    <div class="flex-col-text" style="line-height: 1.45;">
      <span class="question-title">Câu 1:</span> Một hồ nước nhân tạo được xây dựng trong một công viên giải trí. Trong mô hình minh hoạ (hình vẽ), nó được giới hạn bởi các trục toạ độ và đường bờ hồ là một phần đồ thị của hàm số bậc ba:
      $$y = f(x) = \dfrac{1}{10}(-x^3 + 9x^2 - 15x + 56), \text{ với } 0 \le x \le 8$$
      đơn vị đo độ dài trên mỗi trục toạ độ là $100\text{ m}$. Xét tính đúng sai của các mệnh đề sau:
      <div class="sub-item"><span class="sub-item-label">a)</span> Chiều dài của đường đi dạo ven hồ chạy dọc theo trục hoành $Ox$ trên thực tế bằng $800\text{ m}$.</div>
      <div class="sub-item"><span class="sub-item-label">b)</span> Trên đoạn đường đi dạo ứng với $0 \le x \le 1$, khoảng cách theo phương thẳng đứng đến bờ hồ đối diện tăng dần.</div>
      <div class="sub-item"><span class="sub-item-label">c)</span> Tại những điểm trên đường đi dạo ven hồ (dọc theo trục $Ox$), khoảng cách lớn nhất theo phương thẳng đứng đến bờ hồ đối diện bằng $800\text{ m}$.</div>
      <div class="sub-item"><span class="sub-item-label">d)</span> Trong công viên có một con đường thẳng chạy dọc theo đồ thị hàm số $y = -x + 15$ (kí hiệu là đường thẳng $d$). Người ta dự định xây một bến thuyền đạp nước tại vị trí điểm $M$ trên bờ hồ sao cho khoảng cách từ bến thuyền đến con đường $d$ là ngắn nhất. Khoảng cách ngắn nhất đó trên thực tế lớn hơn $90\text{ m}$.</div>
    </div>
    <div class="flex-col-img" style="width: 355px;">
      <img src="assets/hinh_ho_nuoc_dep.png" style="width: 345px; max-width: 100%;" alt="Hồ nước nhân tạo">
    </div>
  </div>
</div>

<!-- ==================== TRANG 3: CÂU 2-4 PHẦN II & CÂU 1-2 PHẦN III ==================== -->



<!-- Câu 2 Phần II: Hàm phân thức bậc 2/1 -->
<div class="question" style="line-height: 1.45;">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = \dfrac{-x^2 - 3x + 4}{x - 3}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số có tập xác định $D = \mathbb{R} \setminus \{3\}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ có tiệm cận xiên là $y = -x - 6$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số $y = f(x)$ đồng biến trên khoảng $(3; 7)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đồ thị $(C)$ có hai điểm cực trị nằm $2$ phía đối với trục $Oy$.</div>
</div>

<!-- Câu 3 Phần II: Hàm phân thức bậc 1/1 -->
<div class="question" style="margin-top: 8px; line-height: 1.45;">
  <span class="question-title">Câu 3:</span> Cho hàm số $y = \dfrac{x + 2}{x - 2}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có đường tiệm cận ngang $y = 2$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ nhận điểm $I(1; 1)$ làm tâm đối xứng.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đường thẳng $d: y = x - 1$ cắt đồ thị $(C)$ tại 2 điểm phân biệt.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Gọi $M$ là điểm bất kì thuộc đồ thị $(C)$. Khi đó tổng khoảng cách từ điểm $M$ đến hai đường tiệm cận của đồ thị $(C)$ đạt giá trị nhỏ nhất bằng $4$.</div>
</div>

<!-- Câu 4 Phần II: Toán kinh tế cho thuê căn hộ -->
<div class="question" style="margin-top: 8px; line-height: 1.45;">
  <span class="question-title">Câu 4:</span> Một công ty bất động sản có 100 căn hộ cho thuê, biết rằng nếu cho thuê mỗi căn hộ với giá 3 triệu đồng mỗi tháng thì mỗi căn hộ đều có người thuê và cứ mỗi lần tăng giá cho thuê mỗi căn hộ thêm 100.000 đồng mỗi tháng thì có thêm 2 căn hộ bị bỏ trống. Gọi $p$ (triệu đồng) là giá mỗi căn hộ cho thuê và $x$ là số căn hộ được thuê.
  <div class="sub-item"><span class="sub-item-label">a)</span> Khi giá cho thuê mỗi căn hộ là 5 triệu đồng thì có 40 căn hộ bị bỏ trống.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm cầu là $p = -\dfrac{1}{20}x + 9\text{ (triệu đồng)}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tổng doanh thu từ tiền thuê nhà là $R(p) = -20p^2 + 140p\text{ (triệu đồng)}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng doanh thu từ tiền thuê nhà lớn nhất là 320 triệu đồng.</div>
</div>

<div class="solid-divider" style="margin-top: 8px;"></div>
<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 Phần III: Đường đi khinh khí cầu -->
<div class="question" style="margin-top: 8px;">
  <span class="question-title">Câu 1:</span> Đường đi của một khinh khí cầu được gắn trong hệ trục toạ độ là một đường cong bậc hai trên bậc nhất có đồ thị cắt trục hoành tại hai điểm có toạ độ là $(1; 0)$ và $(8; 0)$ với đơn vị trên hệ trục toạ độ là $1\text{ km}$. Biết rằng điểm cực đại của đồ thị hàm số là điểm $(6; 5)$. Hỏi khi khí cầu đi qua điểm cực đại và cách mặt đất $3875\text{ m}$ thì khí cầu cách gốc toạ độ theo phương ngang bao nhiêu kilômét?
</div>

<!-- Câu 2 Phần III: Lát cắt ven biển (Đồi và Hồ) -->
<div class="question" style="margin-top: 10px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 2:</span> Lát cắt ngang của một vùng đất ven biển được mô hình hóa thành một hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ (đơn vị độ dài trên các trục là km). Biết khoảng cách hai bên chân đồi $OA = 2\text{ km}$, độ rộng của hồ $AB = 1\text{ km}$ và ngọn đồi cao $550\text{ m}$. Tìm độ sâu của hồ (tính bằng mét) tại điểm sâu nhất? <i>(làm tròn đến hàng đơn vị)</i>.
    </div>
    <div class="flex-col-img" style="width: 315px;">
      <img src="assets/hinh_cat_doi_ho_cau2.png" style="width: 305px; max-width: 100%;" alt="Lát cắt ven biển đồi và hồ">
    </div>
  </div>
</div>

<!-- ==================== TRANG 4: CÂU 3-6 PHẦN III & HẾT ==================== -->



<!-- Câu 3 Phần III: Tham số m đồng biến -->
<div class="question">
  <span class="question-title">Câu 3:</span> Có bao nhiêu giá trị nguyên dương của tham số $m$ để hàm số $f(x) = \dfrac{x^2 + 3x + m - 1}{x + 2}$ đồng biến trên từng khoảng xác định?
</div>

<!-- Câu 4 Phần III: Trang sách giáo khoa Toán -->
<div class="question" style="margin-top: 6px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 4:</span> Mỗi trang của một quyển sách giáo khoa Toán được thiết kế thoả mãn các tiêu chí sau (trang sách có dạng hình chữ nhật $ABCD$, phần diện tích dùng để trình bày là $MNPQ$):
      <div style="margin-left: 8px; margin-top: 2px;">
        • Diện tích của trang sách $ABCD$ bằng $491,04\text{ cm}^2$.<br>
        • Lề trên và lề dưới bằng nhau và bằng $22\text{ mm}$.<br>
        • Lề trái và phải lần lượt là $15\text{ mm}$ và $16\text{ mm}$.
      </div>
      Phần diện tích dùng để trình bày (sau căn chỉnh lề) đạt giá trị lớn nhất, khi đó chu vi mỗi trang sách bằng bao nhiêu? <i>(đơn vị: mm)</i>.
    </div>
    <div class="flex-col-img" style="width: 195px;">
      <img src="assets/hinh_trang_sach_cau4.png" style="width: 185px; max-width: 100%;" alt="Trang sách giáo khoa Toán">
    </div>
  </div>
</div>

<!-- Câu 5 Phần III: Quần thể tảo -->
<div class="question" style="margin-top: 6px;">
  <span class="question-title">Câu 5:</span> Giả sử số lượng cá thể của một quần thể tảo trong bể nuôi được mô hình hoá bằng hàm số:
  $$P(t) = \dfrac{a}{b + e^{-0,6t}}\quad (\text{nghìn cá thể})$$
  trong đó thời gian $t$ được tính bằng ngày. Hàm số $P'(t)$ biểu thị tốc độ gia tăng của quần thể tại thời điểm $t$. Biết rằng $P(0) = 40$ và $P'(0) = 12$. Theo mô hình này, khi thời gian nuôi càng kéo dài ($t$ rất lớn) thì số lượng cá thể tảo trong bể sẽ không vượt quá bao nhiêu? <i>(đơn vị: nghìn cá thể)</i>.
</div>

<!-- Câu 6 Phần III: Gợn sóng đồng tâm -->
<div class="question" style="margin-top: 6px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 6:</span> Một viên đá được ném xuống mặt hồ phẳng lặng, tạo ra các gợn sóng hình tròn đồng tâm. Bán kính của gợn sóng ngoài cùng tăng với tốc độ không đổi $2\text{ cm/s}$. Hỏi diện tích hình tròn tạo bởi gợn sóng này đang tăng với tốc độ bao nhiêu tại thời điểm bán kính của nó bằng $10\text{ cm}$? <i>(kết quả làm tròn đến hàng phần mười theo đơn vị $\text{cm}^2/\text{s}$)</i>.
    </div>
    <div class="flex-col-img" style="width: 195px;">
      <img src="assets/hinh_gon_song_cau6.png" style="width: 185px; max-width: 100%;" alt="Gợn sóng đồng tâm">
    </div>
  </div>
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

html_path = 'exam_de_chuyen_de_ham_so_ma107.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'De_Chuyen_De_Khao_Sat_Ham_So_Ma_107.pdf'
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
