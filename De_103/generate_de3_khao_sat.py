import os

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Đề Ôn Thi Khảo Sát Toán 12 - Đề Số 03</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
<style>
@page {
  size: A4 portrait;
  margin: 10mm 12mm 12mm 12mm;
  @bottom-right {
    content: "Trang " counter(page) "/4 – Mã đề: 103";
    font-family: 'Times New Roman', Times, serif;
    font-size: 9.5pt;
  }
}

*, *:before, *:after {
  box-sizing: border-box;
}

body {
  font-family: 'Times New Roman', Times, serif;
  font-size: 10.8pt;
  line-height: 1.38;
  color: #000;
  margin: 0;
  padding: 0;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 4px;
}

.header-table td {
  vertical-align: top;
  text-align: center;
  padding: 1px 4px;
}

.exam-box {
  border: 1.5px solid #000;
  padding: 3px 6px;
  margin-top: 3px;
  font-weight: bold;
  display: inline-block;
}

.code-box {
  border: 1.5px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  display: inline-block;
  margin-top: 2px;
}

.info-bar {
  margin-top: 4px;
  margin-bottom: 4px;
  padding-bottom: 3px;
  border-bottom: 1px solid #000;
  font-size: 10.5pt;
  display: flex;
  justify-content: space-between;
}

.section-title {
  font-weight: bold;
  font-size: 11pt;
  margin-top: 4px;
  margin-bottom: 3px;
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
  margin-top: 2px;
  margin-bottom: 2px;
  column-gap: 8px;
  row-gap: 2px;
}

.grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

.grid-1 {
  grid-template-columns: 1fr;
}

.sub-item {
  margin-left: 12px;
  margin-top: 2px;
  margin-bottom: 2px;
}

.sub-item-label {
  font-weight: bold;
}

.page-footer {
  position: fixed;
  bottom: 0;
  right: 0;
  font-size: 9.5pt;
  font-style: italic;
}

.exam-end {
  text-align: center;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 2px;
}

.exam-sub-end {
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
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.flex-col-text {
  flex: 1;
}

.flex-col-img {
  flex-shrink: 0;
  text-align: center;
}

.table-bbt {
  border-collapse: collapse;
  margin: 3px auto;
  font-size: 10pt;
}

.table-bbt td {
  border: 1px solid #000;
  padding: 2px 7px;
  text-align: center;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: HEADER & CÂU 1-8 PHẦN I ==================== -->
<table class="header-table">
  <tr>
    <td style="width: 45%;">
      <div style="font-size: 11pt; font-weight: bold;">ĐỀ ÔN THI GIỮA KÌ 1</div>
      <div style="font-size: 10pt; font-style: italic;">Biên soạn: Trần Trung Quân</div>
      <div class="exam-box">
        ĐỀ ÔN TẬP<br>CHÍNH THỨC<br>
        <span style="font-size: 9pt; font-weight: normal; font-style: italic;">(Đề thi gồm có 04 trang)</span>
      </div>
    </td>
    <td style="width: 55%;">
      <div style="font-size: 11pt; font-weight: bold;">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12</div>
      <div style="font-size: 11pt; font-weight: bold;">NĂM HỌC 2026 - 2027</div>
      <div style="font-size: 11pt; font-weight: bold; margin-top: 2px;">Môn: TOÁN - Lớp 12 (ĐỀ SỐ 03)</div>
      <div style="font-size: 9.5pt; font-style: italic;">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="code-box">Mã đề: 103</div>
    </td>
  </tr>
</table>

<div class="info-bar">
  <span>Họ và tên thí sinh: ............................................................................</span>
  <span>Số báo danh: ............................................................</span>
</div>

<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>

<!-- Câu 1: Bảng biến thiên hàm số bậc ba -->
<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ xác định trên $\mathbb{R}$ và có bảng biến thiên như sau:
  <div style="text-align: center; margin: 3px 0;">
    <img src="assets/de3_khao_sat_bbt_cau1.png" style="height: 68px;" alt="Bảng biến thiên Câu 1">
  </div>
  Hàm số đã cho đồng biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-\infty; -1)$.</div>
    <div><b>B.</b> $(-1; 1)$.</div>
    <div><b>C.</b> $(0; 2)$.</div>
    <div><b>D.</b> $(-1; +\infty)$.</div>
  </div>
</div>

<!-- Câu 2: Tiệm cận đứng và tiệm cận ngang -->
<div class="question">
  <span class="question-title">Câu 2:</span> Đường tiệm cận đứng của đồ thị hàm số $y = \dfrac{3x - 1}{x + 2}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = -2$.</div>
    <div><b>B.</b> $x = 2$.</div>
    <div><b>C.</b> $y = 3$.</div>
    <div><b>D.</b> $y = -2$.</div>
  </div>
</div>

<!-- Câu 3: GTLN hàm phân thức trên đoạn -->
<div class="question">
  <span class="question-title">Câu 3:</span> Giá trị lớn nhất của hàm số $y = \dfrac{x^2 - 3x + 6}{x - 1}$ trên đoạn $[2; 4]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $4$.</div>
    <div><b>B.</b> $3$.</div>
    <div><b>C.</b> $\dfrac{10}{3}$.</div>
    <div><b>D.</b> $6$.</div>
  </div>
</div>

<!-- Câu 4: Giao điểm với trục hoành -->
<div class="question">
  <span class="question-title">Câu 4:</span> Tọa độ giao điểm của đồ thị hàm số $y = \dfrac{2x - 4}{x + 1}$ với trục hoành là
  <div class="options-grid grid-4">
    <div><b>A.</b> $(2; 0)$.</div>
    <div><b>B.</b> $(0; -4)$.</div>
    <div><b>C.</b> $(-1; 0)$.</div>
    <div><b>D.</b> $(0; 2)$.</div>
  </div>
</div>

<!-- Câu 5: Số điểm cực trị từ biểu thức f'(x) -->
<div class="question">
  <span class="question-title">Câu 5:</span> Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$ và $f'(x) = x(x + 2)^2(x - 3)^3$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số $y = f(x)$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $2$.</div>
    <div><b>B.</b> $3$.</div>
    <div><b>C.</b> $1$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<!-- Câu 6: Tiệm cận xiên -->
<div class="question">
  <span class="question-title">Câu 6:</span> Phương trình đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 + 2x - 1}{x + 2}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = x$.</div>
    <div><b>B.</b> $y = x + 2$.</div>
    <div><b>C.</b> $y = 2x - 1$.</div>
    <div><b>D.</b> $y = x - 1$.</div>
  </div>
</div>

<!-- Câu 7: Đồ thị hàm trùng phương (Phóng to 50%) -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 7:</span> Đường cong trong hình vẽ bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-1" style="margin-top: 4px;">
        <div><b>A.</b> $y = -x^4 + 2x^2 + 1$.</div>
        <div><b>B.</b> $y = x^4 - 2x^2 + 1$.</div>
        <div><b>C.</b> $y = -x^4 + 4x^2 + 1$.</div>
        <div><b>D.</b> $y = -x^3 + 3x + 1$.</div>
      </div>
    </div>
    <div class="flex-col-img" style="width: 260px;">
      <img src="assets/de3_khao_sat_dothi_cau7.png" style="max-height: 215px;" alt="Đồ thị Câu 7">
    </div>
  </div>
</div>

<!-- Câu 8: Tâm đối xứng đồ thị bậc 2/ bậc 1 -->
<div class="question">
  <span class="question-title">Câu 8:</span> Tọa độ tâm đối xứng của đồ thị hàm số $y = \dfrac{x^2 - 3x + 3}{x - 2}$ là điểm
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(2; 1)$.</div>
    <div><b>B.</b> $I(1; 2)$.</div>
    <div><b>C.</b> $I(2; -1)$.</div>
    <div><b>D.</b> $I(-2; -3)$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: CÂU 9-12 PHẦN I & CÂU 1-2 PHẦN II ==================== -->
<div class="page-break"></div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9:</span> Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \dfrac{mx - 4}{x - m}$ đồng biến trên từng khoảng xác định.
  <div class="options-grid grid-4">
    <div><b>A.</b> $-2 < m < 2$.</div>
    <div><b>B.</b> $m < -2$ hoặc $m > 2$.</div>
    <div><b>C.</b> $-2 \le m \le 2$.</div>
    <div><b>D.</b> $m \ne \pm 2$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question" style="margin-top: 4px;">
  <span class="question-title">Câu 10:</span> Tiếp tuyến của đồ thị hàm số $y = \dfrac{2x - 1}{x + 1}$ tại điểm có tung độ $y_0 = 1$ có hệ số góc bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $\dfrac{1}{3}$.</div>
    <div><b>B.</b> $3$.</div>
    <div><b>C.</b> $\dfrac{1}{9}$.</div>
    <div><b>D.</b> $-\dfrac{1}{3}$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question" style="margin-top: 4px;">
  <span class="question-title">Câu 11:</span> Điểm cực tiểu của hàm số $y = x^4 - 4x^2 + 3$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = \pm\sqrt{2}$.</div>
    <div><b>B.</b> $x = 0$.</div>
    <div><b>C.</b> $x = 2$.</div>
    <div><b>D.</b> $y = -1$.</div>
  </div>
</div>

<!-- Câu 12: Đồ thị hàm bậc 2 / bậc 1 (Phóng to 50%) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 12:</span> Đường cong trong hình vẽ bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-1" style="margin-top: 4px;">
        <div><b>A.</b> $y = \dfrac{x^2 - 2x + 2}{x - 1}$.</div>
        <div><b>B.</b> $y = \dfrac{x^2 + 2x + 2}{x - 1}$.</div>
        <div><b>C.</b> $y = \dfrac{x^2 - 2x - 2}{x - 1}$.</div>
        <div><b>D.</b> $y = \dfrac{x^2 - 2x + 2}{x + 1}$.</div>
      </div>
    </div>
    <div class="flex-col-img" style="width: 270px;">
      <img src="assets/de3_khao_sat_dothi_cau12.png" style="max-height: 218px;" alt="Đồ thị Câu 12">
    </div>
  </div>
</div>

<div class="section-title" style="margin-top: 8px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<!-- Câu 1 Phần II: Hàm căn thức -->
<div class="question" style="margin-top: 4px;">
  <span class="question-title">Câu 1:</span> Cho hàm số chứa căn thức $f(x) = \sqrt{2x - x^2}$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Tập xác định của hàm số là đoạn $[0; 2]$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số trên khoảng $(0; 2)$ là $f'(x) = \dfrac{1 - x}{\sqrt{2x - x^2}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số nghịch biến trên khoảng $(0; 1)$ và đồng biến trên khoảng $(1; 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Giá trị lớn nhất của hàm số trên đoạn $[0; 2]$ bằng $1$ đạt được tại $x = 1$.</div>
</div>

<!-- Câu 2 Phần II: Hàm phân thức bậc 2 / bậc 1 -->
<div class="question" style="margin-top: 6px;">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = \dfrac{x^2 - 3x + 3}{x - 2}$ có đồ thị $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có đường tiệm cận đứng là $x = 2$ và đường tiệm cận xiên là $y = x - 1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Giao điểm của hai đường tiệm cận là điểm $I(2; 1)$, đồng thời điểm $I$ là tâm đối xứng của đồ thị $(C)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số đã cho đồng biến trên khoảng $(1; 3)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đồ thị $(C)$ có hai điểm cực trị $A$ và $B$. Khoảng cách giữa hai điểm cực trị $A, B$ bằng $2\sqrt{5}$.</div>
</div>

<!-- ==================== TRANG 3: CÂU 3-4 PHẦN II & CÂU 1-3 PHẦN III ==================== -->
<div class="page-break"></div>

<!-- Câu 3 Phần II: Toán thực tế kinh tế (Chi phí trung bình) -->
<div class="question">
  <span class="question-title">Câu 3:</span> Một xưởng cơ khí sản xuất một loại chi tiết máy. Chi phí sản xuất $x$ chi tiết máy mỗi ngày ($x > 0$) được mô hình hóa bởi hàm tổng chi phí $C(x) = x^2 + 20x + 400$ (nghìn đồng). Hàm chi phí trung bình để sản xuất một chi tiết máy là $\bar{C}(x) = \dfrac{C(x)}{x} = x + 20 + \dfrac{400}{x}$ với $x > 0$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đạo hàm của hàm chi phí trung bình là $\bar{C}'(x) = 1 - \dfrac{400}{x^2}$ với mọi $x > 0$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Khi quy mô sản xuất tăng từ $1$ đến $20$ chi tiết máy mỗi ngày thì chi phí trung bình cho mỗi chi tiết máy tăng dần.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Để chi phí sản xuất trung bình cho một chi tiết máy là thấp nhất thì xưởng cần sản xuất $20$ chi tiết máy mỗi ngày.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Chi phí sản xuất trung bình thấp nhất cho mỗi chi tiết máy bằng $60$ nghìn đồng.</div>
</div>

<!-- Câu 4 Phần II: Toán thực tế kỹ thuật (Máng nước - Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 4:</span> Một người thợ gò một tấm tôn phẳng dài có bề rộng $60\text{ cm}$ thành một máng dẫn nước có mặt cắt ngang là hình thang cân với đáy nhỏ và hai thành máng đều có độ dài bằng $20\text{ cm}$. Gọi $\alpha$ ($0^\circ < \alpha < 90^\circ$) là góc nghiêng của hai thành máng so với phương ngang (tham khảo hình vẽ bên).
      <div class="sub-item" style="margin-top: 4px;"><span class="sub-item-label">a)</span> Khi hai thành máng vuông góc với đáy ($\alpha = 90^\circ$), diện tích mặt cắt ngang của máng bằng $400\text{ cm}^2$.</div>
      <div class="sub-item"><span class="sub-item-label">b)</span> Diện tích mặt cắt ngang của máng được xác định bởi hàm số:
      $$S(\alpha) = 400(1 + \cos \alpha)\sin \alpha\text{ (cm}^2\text{)}.$$</div>
      <div class="sub-item"><span class="sub-item-label">c)</span> Trên khoảng $(0^\circ; 90^\circ)$, phương trình $S'(\alpha) = 0$ có nghiệm duy nhất là $\alpha = 45^\circ$.</div>
      <div class="sub-item"><span class="sub-item-label">d)</span> Diện tích mặt cắt ngang của máng đạt giá trị lớn nhất bằng $300\sqrt{3}\text{ cm}^2$ khi góc nghiêng $\alpha = 60^\circ$.</div>
    </div>
    <div class="flex-col-img" style="width: 290px;">
      <img src="assets/de3_khao_sat_mang_nuoc_cau4.png" style="max-height: 235px; width: 100%;" alt="Máng nước hình thang">
    </div>
  </div>
</div>

<div class="section-title" style="margin-top: 6px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu trả lời đúng thí sinh được 0,5 điểm.</div>

<!-- Câu 1 Phần III: Cực trị hàm trị tuyệt đối (không chứa m) -->
<div class="question">
  <span class="question-title">Câu 1:</span> Tìm số điểm cực trị của hàm số $y = |x^3 - 3x + 1|$.
</div>

<!-- Câu 2 Phần III: Cực trị hàm bậc 3 và diện tích tam giác OAB -->
<div class="question" style="margin-top: 4px;">
  <span class="question-title">Câu 2:</span> Cho hàm số bậc ba $y = x^3 - 3mx^2 + 2$ với $m$ là tham số thực. Có bao nhiêu giá trị của tham số $m$ để đồ thị hàm số có hai điểm cực trị $A$ và $B$ sao cho diện tích tam giác $OAB$ bằng $4$ (với $O$ là gốc tọa độ)?
</div>

<!-- Câu 3 Phần III: Lon nước ngọt (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 3:</span> Một nhà máy sản xuất lon nước ngọt hình trụ bằng nhôm có thể tích không đổi $V = 128\pi\text{ cm}^3$ (tham khảo hình vẽ bên). Để tiết kiệm chi phí nguyên liệu sản xuất vỏ lon nhất, nhà máy thiết kế lon sao cho diện tích toàn phần của lon hình trụ là nhỏ nhất. Bán kính đáy $R$ của lon nước khi đó bằng bao nhiêu centimét?
    </div>
    <div class="flex-col-img" style="width: 260px;">
      <img src="assets/de3_khao_sat_lon_nuoc_cau3.png" style="max-height: 210px; width: 100%;" alt="Lon nước hình trụ">
    </div>
  </div>
</div>

<!-- ==================== TRANG 4: CÂU 4-6 PHẦN III & HẾT ==================== -->
<div class="page-break"></div>

<!-- Câu 4 Phần III: Đường ống dẫn dầu (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 4px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 4:</span> Một trạm nghiên cứu biển $S$ nằm ngoài khơi, cách bờ biển thẳng một khoảng $SH = 6\text{ km}$ ($H$ là hình chiếu vuông góc của $S$ lên bờ biển). Một trạm tiếp nhận trên bờ biển $T$ cách $H$ một khoảng $HT = 16\text{ km}$. Người ta lắp đặt đường ống dẫn từ $S$ đến một điểm $P$ trên bờ biển nằm giữa $H$ và $T$, rồi kéo thẳng từ $P$ đến $T$ (tham khảo hình vẽ bên). Chi phí lắp đặt ống dưới biển là $130\text{ triệu đồng/km}$, chi phí lắp đặt trên đất liền là $50\text{ triệu đồng/km}$. Hỏi khoảng cách $HP$ bằng bao nhiêu kilômét để tổng chi phí lắp đặt toàn bộ đường ống là thấp nhất? <i>(Kết quả ghi dưới dạng số thập phân)</i>.
    </div>
    <div class="flex-col-img" style="width: 290px;">
      <img src="assets/de3_khao_sat_duong_ong_cau4.png" style="max-height: 235px; width: 100%;" alt="Đường ống dẫn từ biển">
    </div>
  </div>
</div>

<!-- Câu 5 Phần III: Cửa sổ vòm Norman (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 8px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 5:</span> Một cửa sổ hình vòm Norman gồm một hình chữ nhật phía dưới và một nửa hình tròn phía trên có đường kính bằng chiều rộng $x$ của hình chữ nhật (tham khảo hình vẽ bên). Chu vi của toàn bộ khung cửa sổ bằng $10\text{ m}$. Tìm chiều rộng $x$ của cửa sổ (tính theo mét) để diện tích của cửa sổ đón được nhiều ánh sáng nhất. <i>(Làm tròn kết quả đến hàng phần mười)</i>.
    </div>
    <div class="flex-col-img" style="width: 270px;">
      <img src="assets/de3_khao_sat_cua_so_cau5.png" style="max-height: 230px; width: 100%;" alt="Cửa sổ vòm Norman">
    </div>
  </div>
</div>

<!-- Câu 6 Phần III: Hải đăng và Ca nô (Hình vẽ phóng to gấp đôi) -->
<div class="question" style="margin-top: 8px;">
  <div class="flex-row">
    <div class="flex-col-text">
      <span class="question-title">Câu 6:</span> Một ngọn hải đăng cao $40\text{ m}$ ($AB = 40\text{ m}$ với $A$ là chân ngọn hải đăng trên mặt biển, $B$ là đèn hải đăng). Một chiếc ca nô di chuyển thẳng trên mặt nước về phía chân hải đăng $A$ với tốc độ không đổi $v = 15\text{ m/s}$ (tham khảo hình vẽ bên). Tại thời điểm ca nô cách chân hải đăng $30\text{ m}$ (điểm $M$ sao cho $AM = 30\text{ m}$), khoảng cách $BM$ giữa đèn hải đăng và chiếc ca nô đang giảm với tốc độ bằng bao nhiêu mét trên giây?
    </div>
    <div class="flex-col-img" style="width: 290px;">
      <img src="assets/de3_khao_sat_hai_dang_cau6.png" style="max-height: 230px; width: 100%;" alt="Hải đăng và ca nô">
    </div>
  </div>
</div>

<div class="exam-end">----------------------- HẾT -----------------------</div>
<div class="exam-sub-end">Học sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

</body>
</html>
"""

with open("exam_de3_khao_sat.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("exam_de3_khao_sat.html generated successfully!")
