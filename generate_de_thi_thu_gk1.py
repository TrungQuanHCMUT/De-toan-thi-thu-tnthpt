import os, subprocess, pypdf

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề thi thử giữa kì 1 - Môn Toán 12 (ĐỀ SỐ 01 - Mã đề: 105)</title>
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
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 105";
    font-family: 'Times New Roman', serif;
    font-size: 10pt;
    color: #000;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 10.8pt;
  line-height: 1.36;
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

.section-subtitle {
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 3px;
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
  margin-bottom: 2px;
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
  font-size: 9.2pt;
}

.page-break {
  page-break-before: always;
}

.bbt-table {
  border-collapse: collapse;
  margin: 2px auto;
  font-size: 9.8pt;
  text-align: center;
}

.bbt-table td {
  padding: 1px 6px;
}
</style>
</head>
<body>

<!-- ==================== TRANG 1: PHẦN I (CÂU 1 ĐẾN CÂU 8) ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ THI THỬ GIỮA KÌ 1</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ THI THỬ<br>CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>NĂM HỌC 2026 - 2027</div>
      <div class="subject-title">Môn: TOÁN - Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 105</div>
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

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 3px 0 2px 0;">
    <img src="assets/gk1_clean_bbt_cau1.png" style="max-height: 52px;" alt="Bảng biến thiên Câu 1">
  </div>
  Hàm số đã cho đồng biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(-2; 2)$.</div>
    <div><b>B.</b> $(-\infty; -2)$.</div>
    <div><b>C.</b> $(-3; 4)$.</div>
    <div><b>D.</b> $(-2; +\infty)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = f(x)$ có bảng xét dấu của đạo hàm $f'(x)$ như sau:
  <div style="text-align: center; margin: 2px 0 2px 0;">
    <img src="assets/gk1_clean_bxd_cau2.png" style="max-height: 36px;" alt="Bảng xét dấu Câu 2">
  </div>
  Số điểm cực tiểu của hàm số đã cho là
  <div class="options-grid grid-4">
    <div><b>A.</b> $0$.</div>
    <div><b>B.</b> $2$.</div>
    <div><b>C.</b> $1$.</div>
    <div><b>D.</b> $3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 3:</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 5$ trên đoạn $[0; 2]$ bằng
  <div class="options-grid grid-4">
    <div><b>A.</b> $3$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $7$.</div>
    <div><b>D.</b> $1$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Đường tiệm cận đứng của đồ thị hàm số $y = \dfrac{2x + 1}{x - 3}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = 2$.</div>
    <div><b>B.</b> $x = -3$.</div>
    <div><b>C.</b> $x = 3$.</div>
    <div><b>D.</b> $y = 3$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 - 3x + 5}{x - 1}$ là đường thẳng
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = x + 2$.</div>
    <div><b>B.</b> $y = x - 2$.</div>
    <div><b>C.</b> $y = x - 3$.</div>
    <div><b>D.</b> $y = -x + 2$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Tọa độ tâm đối xứng của đồ thị hàm số $y = \dfrac{3x - 2}{x + 1}$ là điểm
  <div class="options-grid grid-4">
    <div><b>A.</b> $I(1; 3)$.</div>
    <div><b>B.</b> $I(-1; -2)$.</div>
    <div><b>C.</b> $I(3; -1)$.</div>
    <div><b>D.</b> $I(-1; 3)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 7:</span> Hàm số $y = \sqrt{4 - x^2}$ nghịch biến trên khoảng nào dưới đây?
  <div class="options-grid grid-4">
    <div><b>A.</b> $(0; 2)$.</div>
    <div><b>B.</b> $(-2; 0)$.</div>
    <div><b>C.</b> $(-2; 2)$.</div>
    <div><b>D.</b> $(-\infty; 0)$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 8:</span> Có bao nhiêu giá trị nguyên của tham số $m \in [-5; 5]$ để hàm số $y = \dfrac{x - 3}{x - m}$ đồng biến trên khoảng $(0; +\infty)$?
  <div class="options-grid grid-4">
    <div><b>A.</b> $6$.</div>
    <div><b>B.</b> $5$.</div>
    <div><b>C.</b> $7$.</div>
    <div><b>D.</b> $4$.</div>
  </div>
</div>

<!-- ==================== TRANG 2: CÂU 9-12 PHẦN I & CÂU 1-2 PHẦN II ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 9:</span> Gọi $m$ là giá trị nhỏ nhất của hàm số $f(x) = (x^2 - 2)e^{2x}$ trên đoạn $[-1; 2]$. Khi đó $m$ có dạng $m = a + be^2$ với $a, b \in \mathbb{Z}$. Tính $2a + b$.
  <div class="options-grid grid-4">
    <div><b>A.</b> $2$.</div>
    <div><b>B.</b> $1$.</div>
    <div><b>C.</b> $-1$.</div>
    <div><b>D.</b> $-2$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 10:</span> Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên dưới:
  <div style="text-align: center; margin: 2px 0 1px 0;">
    <img src="assets/gk1_dothi_cau10.png" style="width: 145px; max-width: 100%;">
  </div>
  Biểu thức $f(x)$ là biểu thức nào sau đây?
  <div class="options-grid grid-4" style="margin-top: 2px;">
    <div><b>A.</b> $-x^3 + 3x - 1$.</div>
    <div><b>B.</b> $\dfrac{2x - 1}{x + 1}$.</div>
    <div><b>C.</b> $x + \dfrac{1}{x}$.</div>
    <div><b>D.</b> $\dfrac{x - 1}{x + 1}$.</div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 11:</span> Cho hàm số $y = f(x)$ liên tục trên tập số thực, có bảng biến thiên như hình vẽ sau:
  <div style="text-align: center; margin: 3px 0 2px 0;">
    <img src="assets/gk1_clean_bbt_cau11.png" style="max-height: 52px;" alt="Bảng biến thiên Câu 11">
  </div>
  Điểm cực đại của hàm số là
  <div class="options-grid grid-4">
    <div><b>A.</b> $y = 3$.</div>
    <div><b>B.</b> $M(0; 3)$.</div>
    <div><b>C.</b> $N(1; -2)$.</div>
    <div><b>D.</b> $x = 0$.</div>
  </div>
</div>

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

<div class="question">
  <span class="question-title">Câu 1:</span> Cho hàm số bậc ba $y = f(x)$ có bảng biến thiên như sau:
  <div style="text-align: center; margin: 3px 0 2px 0;">
    <img src="assets/gk1_clean_bbt_p2_cau1.png" style="max-height: 52px;" alt="Bảng biến thiên Phần II Câu 1">
  </div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số $y = f(x)$ đạt cực đại tại điểm $x = 1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số $y = f(x)$ đồng biến trên khoảng $(-5; +\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đồ thị hàm số $y = f(x)$ đi qua điểm có tọa độ $(0; -1)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> $f(-1) = f(2)$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Cho hàm số $y = \dfrac{-x^2 - 3x + 4}{x - 3}$ có đồ thị là $(C)$.
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị $(C)$ có tiệm cận xiên là đường thẳng $y = -x - 6$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ nhận giao điểm $I(3; -9)$ của hai đường tiệm cận làm tâm đối xứng.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đồ thị $(C)$ có hai điểm cực trị nằm về 2 phía đối với trục tung $Oy$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đồ thị $(C)$ không cắt trục hoành $Ox$.</div>
</div>

<!-- ==================== TRANG 3: CÂU 3-4 PHẦN II & CÂU 1-2 PHẦN III ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 3:</span> Số dân của một thị trấn sau $t$ năm ($t \ge 0$) kể từ năm 1970 được ước tính bởi công thức:
  <div style="text-align: center; margin: 2px 0;">
    $f(t) = \dfrac{26t + 10}{t + 5}\quad (f(t)\text{ được tính bằng nghìn người}).$
  </div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Số dân của thị trấn giảm trong những năm từ 1975 đến 1980.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm của hàm số $f$ biểu thị tốc độ tăng dân số của thị trấn (tính bằng nghìn người/năm). Vào năm 1998 thì tốc độ tăng dân số là $0{,}125\text{ nghìn người/năm}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Đạo hàm $f'(t) = \dfrac{120}{(t + 5)^2},\ (t \ge 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Số dân của thị trấn vào đầu năm 1980 là $18\text{ nghìn người}$.</div>
</div>

<div class="question">
  <span class="question-title">Câu 4:</span> Một tàu đổ bộ tiếp cận Mặt Trăng theo cách tiếp cận thẳng đứng và đốt cháy các tên lửa hãm ở độ cao $250\text{ km}$ so với bề mặt của Mặt Trăng. Trong khoảng 50 giây đầu tiên kể từ khi đốt cháy các tên lửa hãm, độ cao $h$ của con tàu so với bề mặt của Mặt Trăng được tính (gần đúng) bởi hàm $h(t) = -0{,}01t^3 + 1{,}1t^2 - 30t + 250$; trong đó $t$ là thời gian tính bằng giây và $h$ là độ cao tính bằng kilômét.
  <div style="font-size: 9.2pt; font-style: italic; margin-left: 15px; margin-bottom: 2px;">(Nguồn: A. Bigalke et al., Mathematik, Grundkurs ma-1, Cornelsen 2016)</div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Vận tốc tức thời của con tàu ở thời điểm $t$ (giây) kể từ khi đốt cháy các tên lửa hãm được xác định bởi $v(t) = -0{,}03t^2 + 2{,}2t - 30,\ (0 \le t \le 50)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vận tốc tức thời của con tàu tại thời điểm $t = 25$ (giây) là $6{,}25\text{ (km/s)}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tại thời điểm $t = 25$ (giây), vận tốc tức thời của con tàu tiếp tục giảm.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Trong khoảng 50 giây đầu tiên kể từ khi đốt cháy các tên lửa hãm, con tàu đạt khoảng cách nhỏ nhất so với bề mặt Mặt Trăng là $10\text{ km}$.</div>
</div>

<div class="solid-divider" style="margin-top: 4px;"></div>
<div class="section-title">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<div class="question">
  <span class="question-title">Câu 1:</span> Trong một buổi tập luyện của lính đặc công, một chiến sỹ cần phối hợp bơi và chạy bộ từ điểm $A$ ở bờ sông bên này đến điểm $B$ về phía hạ lưu của bờ sông bên kia (tham khảo hình vẽ bên dưới). Bờ sông thẳng, hai bờ song song và cách nhau một khoảng $AH = 300\text{ m}$ và $HB = 900\text{ m}$. Dòng nước chảy từ $H$ về phía $B$ với vận tốc không đổi là $1\text{ m/s}$. Chiến sỹ dự định bơi thẳng từ điểm $A$ đến một điểm thuộc đoạn $HB$, sau đó tiếp tục chạy bộ từ điểm đó về điểm $B$. Biết vận tốc bơi của chiến sỹ đối với dòng nước là $1\text{ m/s}$ và vận tốc chạy trên bờ của chiến sỹ là $3\text{ m/s}$. Hỏi chiến sỹ cần ít nhất bao nhiêu giây để hoàn thành kế hoạch trên? *(kết quả làm tròn đến hàng đơn vị)*.
  <div style="text-align: center; margin: 3px 0 1px 0;">
    <img src="assets/gk1_song_cau1.png" style="width: 82mm; max-width: 90%;">
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 2:</span> Công ty du lịch Hòa Bình muốn mở một tour du lịch bằng du thuyền trên biển và giám đốc công ty đang tính toán các chi phí cần thiết để vận hành du thuyền. Để tính toán chi phí, giám đốc Hòa Bình đã mô hình hóa lượng dầu diesel tiêu thụ ước tính theo hàm số $G(x) = \dfrac{250}{x} + \dfrac{x}{10}\ (\text{lít/km})$, với $x$ là vận tốc của du thuyền (giả định rằng vận tốc này duy trì không đổi trong suốt quá trình di chuyển). Biết rằng giá dầu diesel là $17{,}5\text{ nghìn đồng/lít}$. Ngoài ra, công ty cần tuyển thuyền trưởng với mức lương $1{,}5\text{ triệu đồng}$ mỗi giờ để lái du thuyền này trong toàn bộ chuyến du lịch dài $640\text{ km}$. Hỏi thuyền trưởng phải duy trì vận tốc của du thuyền bằng bao nhiêu $\text{km/h}$ để tổng chi phí của công ty là thấp nhất? *(kết quả làm tròn đến hàng phần mười)*.
</div>

<!-- ==================== TRANG 4: CÂU 3-6 PHẦN III & HẾT ==================== -->
<div class="page-break"></div>

<div class="question">
  <span class="question-title">Câu 3:</span> Tìm số đường tiệm cận (bao gồm cả tiệm cận đứng, tiệm cận ngang và tiệm cận xiên) của đồ thị hàm số $y = \dfrac{\sqrt{x^2 - 9}}{x^3 - 16x}$.
</div>

<div class="question">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; padding-right: 20px;">
      <span class="question-title">Câu 4:</span> Từ hình vuông có cạnh bằng $6\text{ cm}$, người ta cắt bỏ các tam giác vuông cân tạo thành hình tô đậm như hình vẽ bên. Sau đó người ta gập thành hình hộp chữ nhật không nắp. Thể tích lớn nhất của khối hộp đó bằng bao nhiêu $\text{cm}^3$? *(làm tròn kết quả đến hàng phần chục)*.
    </div>
    <div style="width: 130px; text-align: center; flex-shrink: 0;">
      <img src="assets/gk1_hop_cau4.png" style="width: 115px; max-width: 100%;">
    </div>
  </div>
</div>

<div class="question">
  <span class="question-title">Câu 5:</span> Cho hàm số bậc ba $y = \dfrac{1}{3}x^3 - (m + 1)x^2 + (m^2 + 2m)x - 4$ với $m$ là tham số thực. Tìm giá trị của $m$ để hàm số đã cho đạt cực đại tại điểm $x = 2$.
</div>

<div class="question">
  <span class="question-title">Câu 6:</span> Cho một đường tròn $(C)$ có bán kính bằng $4$, vẽ một hình chữ nhật nội tiếp đường tròn $(C)$. Khi diện tích của hình chữ nhật đạt giá trị lớn nhất thì chu vi của hình chữ nhật là bao nhiêu? <em>(Làm tròn kết quả đến hàng phần mười)</em>.
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

with open('exam_de_thi_thu_gk1.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'De_Thi_Thu_Giua_Ki_1_Toan_12.pdf'
cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=6000',
    f'--print-to-pdf={output_pdf}',
    'exam_de_thi_thu_gk1.html'
]

print('Running Chrome...')
res = subprocess.run(cmd, capture_output=True, text=True)
print('Chrome code:', res.returncode)
reader = pypdf.PdfReader(output_pdf)
print('Page count:', len(reader.pages))
