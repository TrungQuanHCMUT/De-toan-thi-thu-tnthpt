import os

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề ôn thi giữa kì 1 - Môn Toán 12 (Đề số 03)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin-top: 8mm;
  margin-bottom: 9mm;
  margin-left: 14mm;
  margin-right: 14mm;
  @bottom-right {
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 103";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.2pt;
  line-height: 1.38;
  color: #000;
  margin: 0;
  padding: 0;
}

.header-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1px;
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
}

.subject-title {
  font-size: 11.5pt;
  font-weight: bold;
  margin-top: 1px;
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
  width: 160px;
  margin: 2px auto 0 auto;
}

.left-box .bold-text {
  font-weight: bold;
  font-size: 10pt;
}

.left-box .sub-text {
  font-size: 9pt;
  font-style: italic;
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
  margin: 3px 0 2px 0;
}

.solid-divider-thick {
  border-top: 1.5px solid #000;
  margin: 3px 0 4px 0;
}

.student-info {
  display: flex;
  justify-content: space-between;
  font-size: 10pt;
  font-style: italic;
  margin-bottom: 1px;
}

.section-title {
  font-weight: bold;
  font-size: 10.5pt;
  margin-top: 3px;
  margin-bottom: 4px;
  text-align: justify;
}

.question {
  margin-bottom: 3.5px;
  text-align: justify;
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

.sub-item {
  margin-left: 18px;
  margin-bottom: 1.5px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

.end-exam {
  text-align: center;
  margin-top: 15px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}

.end-note {
  text-align: center;
  font-style: italic;
  font-size: 9pt;
}

.page-break {
  page-break-before: always;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: TOÀN BỘ PHẦN I ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN THI GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12 (ĐỀ SỐ 03)</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 103</div>
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

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 1; padding-right: 10px;">
      <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$. Đồ thị của hàm số đạo hàm $y = f'(x)$ được cho như hình vẽ bên. Hàm số $y = f(x)$ nghịch biến trên khoảng nào dưới đây?
      <div class="options-grid grid-2" style="margin-top: 4px;">
        <div><b>A.</b> $(-\infty; -1)$.</div>
        <div><b>B.</b> $(-1; 2)$.</div>
        <div><b>C.</b> $(2; +\infty)$.</div>
        <div><b>D.</b> $(0; 2)$.</div>
      </div>
    </div>
    <div style="width: 110px; text-align: center; flex-shrink: 0;">
      <img src="assets/de3_dothi_fprime_cau1.png" style="width: 105px;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Điểm cực đại của hàm số $y = x^4 - 2x^2 + 3$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $x = 1$.</div>
    <div><b>B.</b> $x = 0$.</div>
    <div><b>C.</b> $x = -1$.</div>
    <div><b>D.</b> $x = 3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{2x - 3}{x^2 - 4x + 3}$ là
  <div class="options-grid grid-4">
    <div><b>A.</b> $1$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $3$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 4x + 5}{x - 1}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = x - 4$.</div>
    <div><b>B.</b> $y = x - 3$.</div>
    <div><b>C.</b> $y = x + 3$.</div>
    <div><b>D.</b> $y = 2x - 3$.</div>
  </div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 1; padding-right: 10px;">
      <span class="question-title">Câu 5:</span> Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?
      <div class="options-grid grid-2" style="margin-top: 4px;">
        <div><b>A.</b> $y = \dfrac{x^2 - x + 1}{x - 1}.$</div>
        <div><b>B.</b> $y = \dfrac{x^2 + x + 1}{x + 1}.$</div>
        <div><b>C.</b> $y = \dfrac{x^2 - 3x + 1}{x - 1}.$</div>
        <div><b>D.</b> $y = \dfrac{2x - 1}{x - 1}.$</div>
      </div>
    </div>
    <div style="width: 110px; text-align: center; flex-shrink: 0;">
      <img src="assets/de3_dothi_cau5.png" style="width: 105px;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Cho dãy số $(u_n)$ được xác định bởi hệ thức truy hồi: $\begin{cases} u_1 = 3 \\ u_{n+1} = 2u_n - 1, \quad \forall n \ge 1 \end{cases}$. Giá trị của số hạng $u_4$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_4 = 15$.</div>
    <div><b>B.</b> $u_4 = 17$.</div>
    <div><b>C.</b> $u_4 = 33$.</div>
    <div><b>D.</b> $u_4 = 9$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 7:</span> Cho cấp số cộng $(u_n)$ có $u_3 = 8$ và $u_7 = 20$. Công sai $d$ của cấp số cộng đó bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $d = 3$.</div>
    <div><b>B.</b> $d = 4$.</div>
    <div><b>C.</b> $d = 2$.</div>
    <div><b>D.</b> $d = -3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8:</span> Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = -2$ và công bội $q = -3$. Số hạng thứ 5 của cấp số nhân đó là
  <div class="options-grid grid-4">
    <div><b>A.</b> $u_5 = 162$.</div>
    <div><b>B.</b> $u_5 = -162$.</div>
    <div><b>C.</b> $u_5 = 486$.</div>
    <div><b>D.</b> $u_5 = -54$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 9:</span> Cho tứ diện đều $ABCD$. Số đo góc giữa hai đường thẳng $AB$ và $CD$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $45^\circ$.</div>
    <div><b>B.</b> $60^\circ$.</div>
    <div><b>C.</b> $90^\circ$.</div>
    <div><b>D.</b> $30^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10:</span> Cho hình lăng trụ tam giác đều $ABC.A'B'C'$ có tất cả các cạnh đều bằng $a$. Góc giữa đường thẳng $A'B$ và mặt phẳng đáy $(ABC)$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $30^\circ$.</div>
    <div><b>B.</b> $45^\circ$.</div>
    <div><b>C.</b> $60^\circ$.</div>
    <div><b>D.</b> $90^\circ$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = 3a, AD = 4a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$. Khoảng cách từ điểm $B$ đến mặt phẳng $(SAD)$ bằng độ dài đoạn thẳng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $SA$.</div>
    <div><b>B.</b> $AB$.</div>
    <div><b>C.</b> $AD$.</div>
    <div><b>D.</b> $BD$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 12:</span> Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Khoảng cách giữa hai đường thẳng chéo nhau $AA'$ và $BC$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $a$.</div>
    <div><b>B.</b> $a\sqrt{2}$.</div>
    <div><b>C.</b> $a\sqrt{3}$.</div>
    <div><b>D.</b> $\dfrac{a}{2}$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: TOÀN BỘ PHẦN II ==================== -->
<div class="page-break"></div>

<div class="section-title">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = \dfrac{x^2 - 3x + 3}{x - 1}$ có đồ thị $(C)$. Gọi $I$ là giao điểm hai đường tiệm cận của $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có tiệm cận đứng $x = 1$ và tiệm cận xiên $y = x - 2$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho đồng biến trên mỗi khoảng $(-\infty; 0)$ và $(2; +\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tọa độ tâm đối xứng của đồ thị $(C)$ là điểm $I(1; -2)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tích các khoảng cách từ một điểm $M$ bất kỳ thuộc đồ thị $(C)$ đến hai đường tiệm cận của nó luôn bằng $\dfrac{1}{\sqrt{2}}$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Một nguồn điện không đổi có suất điện động $E = 12\text{ V}$ và điện trở trong $r = 2\,\Omega$. Mạch ngoài là một biến trở có điện trở $R > 0$. Công suất tiêu thụ trên mạch ngoài được cho bởi công thức $P(R) = \dfrac{144R}{(R + 2)^2}\text{ (W)}$, có đồ thị như hình vẽ bên dưới.
  <div style="text-align: center; margin: 3px 0;">
    <img src="assets/de3_mach_dien_cau2.png" style="width: 78mm; max-width: 85%;">
  </div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Công suất tiêu thụ trên mạch ngoài tăng khi điện trở $R$ tăng trong khoảng từ $0\,\Omega$ đến $2\,\Omega$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Công suất tiêu thụ lớn nhất trên mạch ngoài đạt giá trị bằng $18\text{ W}$ khi biến trở có giá trị $R = 2\,\Omega$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khi điện trở mạch ngoài tăng lên rất lớn ($R \to +\infty$), công suất tiêu thụ trên mạch ngoài tiến dần về $0\text{ W}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Có đúng hai giá trị của biến trở $R$ để công suất tiêu thụ trên mạch ngoài đạt $16\text{ W}$, trong đó hiệu giữa hai giá trị điện trở này bằng $3\,\Omega$.</div>
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 1; padding-right: 12px;">
      <span class="question-title">Câu 3:</span> Xét tam giác $ABC$ có $AC = 2AB$ và $BC = 10\text{ cm}$. Trên cạnh $AC$ lấy điểm $D$ sao cho $AD = \dfrac{1}{4}AC$, trên cạnh $AB$ lấy điểm $E$ sao cho $AE = \dfrac{1}{4}AB$, trên cạnh $AD$ lấy điểm $F$ sao cho $AF = \dfrac{1}{4}AD$ và tiếp tục lấy các điểm $G, H, I, J...$ (vô hạn lần) theo quy luật đó (như hình vẽ bên).
      <div class="sub-item" style="margin-left: 5px; margin-top: 4px;"><span class="sub-item-label">a)</span> $\dfrac{AB}{AC} = \dfrac{AD}{AB}$.</div>
      <div class="sub-item" style="margin-left: 5px;"><span class="sub-item-label">b)</span> Tam giác $ABD$ đồng dạng với tam giác $ABC$.</div>
      <div class="sub-item" style="margin-left: 5px;"><span class="sub-item-label">c)</span> $BD = 5\text{ cm}; DE = 3\text{ cm}$.</div>
      <div class="sub-item" style="margin-left: 5px;"><span class="sub-item-label">d)</span> Độ dài đường gấp khúc $CBDEFGH...$ bằng $20\text{ cm}$.</div>
    </div>
    <div style="width: 120px; text-align: center; flex-shrink: 0;">
      <img src="assets/de3_tam_giac_gapkhuc.png" style="width: 115px;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $2a$. Tam giác $SAB$ là tam giác đều nằm trong mặt phẳng vuông góc với mặt phẳng đáy $(ABCD)$. Gọi $H$ là trung điểm của cạnh $AB$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đoạn thẳng $SH$ vuông góc với mặt phẳng đáy $(ABCD)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Chiều cao của hình chóp bằng $a\sqrt{3}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tang của góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABCD)$ bằng $\dfrac{\sqrt{3}}{\sqrt{5}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách giữa hai đường thẳng chéo nhau $AB$ và $SC$ bằng $2a$.</div>
</div>

<!-- ==================== TRANG 3: PHẦN III (CÂU 1 ĐẾN CÂU 5) ==================== -->
<div class="page-break"></div>

<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Một doanh nghiệp công nghệ khởi nghiệp (Startup) chuẩn bị mở rộng quy mô và cần thuê một mặt bằng làm trung tâm kho vận phân phối hàng hóa trong thời hạn 15 năm. Sau khi khảo sát, doanh nghiệp nhận được hai phương án hợp đồng từ hai đơn vị cho thuê bất động sản như sau:
  <div style="margin-left: 12px; margin-top: 3px; margin-bottom: 3px;">
    • <b>Phương án 1 (Thanh toán theo quý):</b> Tiền thuê quý đầu tiên là $10\text{ triệu đồng}$; từ quý thứ hai trở đi, tiền thuê mỗi quý tăng thêm $500.000\text{ đồng}$ ($0,5\text{ triệu đồng}$) so với quý trước đó.<br>
    • <b>Phương án 2 (Thanh toán theo năm):</b> Tiền thuê năm đầu tiên là $70\text{ triệu đồng}$; từ năm thứ hai trở đi, tiền thuê mỗi năm tăng thêm $3\text{ triệu đồng}$ so với năm trước đó.
  </div>
  Để tối ưu hóa ngân sách, doanh nghiệp nên chọn phương án nào để tổng chi phí thuê mặt bằng trong 15 năm là thấp nhất? Số tiền chi phí thấp nhất đó bằng bao nhiêu triệu đồng?
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và $SA = a$. Tính số đo góc giữa hai mặt phẳng $(SBC)$ và $(SCD)$ (đơn vị: độ).
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = 6\text{ cm}, BC = 8\text{ cm}$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$ và $SA = 4\text{ cm}$. Gọi $M$ là trung điểm của cạnh $AC$. Tính khoảng cách giữa hai đường thẳng chéo nhau $SM$ và $BC$ (kết quả ghi dưới dạng số thập phân theo đơn vị cm).
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 1)^2 (x^2 - 4)$ với mọi $x \in \mathbb{R}$. Tìm số điểm cực trị của hàm số $g(x) = f(x^2 - 2)$.
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Một bồn chứa nước có dạng một khối nón tròn xoay có đỉnh hướng thẳng đứng xuống dưới. Bán kính miệng bồn là $R = 30\text{ cm}$ và chiều cao của bồn là $H = 60\text{ cm}$. Người ta xả nước vào bồn từ một vòi nước với lưu lượng không đổi $50\pi\text{ cm}^3\text{/s}$ (như hình vẽ bên dưới). Tại thời điểm chiều cao của mực nước trong bồn bằng $20\text{ cm}$, tốc độ dâng lên của mực nước là bao nhiêu cm/s? (kết quả ghi dưới dạng số thập phân).
  <div style="text-align: center; margin: 8px 0 2px 0;">
    <img src="assets/de3_bon_nuoc_cau5.png" style="width: 88mm; max-width: 90%;">
  </div>
</div>

<!-- ==================== TRANG 4: PHẦN III (CÂU 6 CÓ HÌNH VẼ MINH HỌA TO RÕ RÀNG) ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 6:</span> Một bức tranh nghệ thuật có chiều cao $3\text{ m}$ ($AB = 3\text{ m}$) được treo thẳng đứng trên một bức tường phẳng. Mép dưới của bức tranh cách mặt sàn $2,6\text{ m}$. Một người xem tranh có tầm mắt cách mặt sàn $1,6\text{ m}$. Hỏi người đó cần đứng cách bức tường một khoảng cách bằng bao nhiêu mét để góc nhìn bức tranh $\theta$ (góc tạo bởi các tia nhìn từ mắt đến mép trên $A$ và mép dưới $B$ của bức tranh) đạt giá trị lớn nhất? (kết quả ghi dưới dạng số nguyên).
  <div style="text-align: center; margin: 15px 0 10px 0;">
    <img src="assets/de3_ngam_tranh_cau6.png" style="width: 118mm; max-width: 95%;">
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

with open('exam_de3.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("exam_de3.html updated successfully!")
