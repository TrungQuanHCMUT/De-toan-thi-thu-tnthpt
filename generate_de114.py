import os, subprocess, pypdf, base64

def get_base64_img(filename):
    with open(filename, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

img1_b64 = get_base64_img('cau1_diagram.png')
img2_b64 = get_base64_img('cau2_diagram.png')
img3_b64 = get_base64_img('cau3_diagram.png')
img_p2_c3_b64 = get_base64_img('cau3_p2_graph.png')

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề Khảo Sát Toán 12 - Mã Đề 114</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {{
  size: A4 portrait;
  margin: 11mm 13mm 11mm 13mm;
}}
* {{
  box-sizing: border-box;
}}
body {{
  font-family: 'Times New Roman', Times, serif;
  font-size: 10.3pt;
  line-height: 1.32;
  color: #000;
  margin: 0;
  padding: 0;
}}
.katex {{
  font-size: 1.02em;
}}
.katex-display {{
  margin: 3px 0;
}}

/* Vector accent styling */
.katex .accent > .vlist-t > .vlist-r:first-child {{
  transform: scale(1.25);
  transform-origin: center bottom;
}}
.katex .svg-align > svg {{
  transform: scale(1.25);
  transform-origin: center bottom;
}}

.header-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 3px;
}}
.header-table td {{
  vertical-align: top;
  padding: 0;
}}
.left-header {{
  width: 44%;
  text-align: center;
}}
.right-header {{
  width: 56%;
  text-align: center;
}}
.title-main {{
  font-size: 11.5pt;
  font-weight: bold;
  text-transform: uppercase;
}}
.author-title {{
  font-size: 10.5pt;
  font-style: italic;
  margin-top: 1px;
}}
.exam-title {{
  font-size: 11.5pt;
  font-weight: bold;
  line-height: 1.25;
  text-transform: uppercase;
}}
.subject-title {{
  font-size: 11.2pt;
  font-weight: bold;
  margin-top: 2px;
}}
.time-title {{
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 1px;
}}
.left-box {{
  border: 1px solid #000;
  padding: 2.5px 10px;
  text-align: center;
  width: fit-content;
  min-width: 185px;
  margin: 3px auto 0 auto;
  line-height: 1.25;
}}
.left-box .bold-text {{
  font-weight: bold;
  font-size: 10pt;
  white-space: nowrap;
}}
.left-box .sub-text {{
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
  white-space: nowrap;
}}
.right-box {{
  border: 1.3px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 2px;
}}
.solid-divider {{
  border-top: 1px solid #000;
  margin: 4px 0 2px 0;
}}
.solid-divider-thick {{
  border-top: 1.5px solid #000;
  margin: 4px 0 4px 0;
}}
.student-info {{
  display: flex;
  justify-content: space-between;
  font-size: 10.2pt;
  margin-top: 2px;
  margin-bottom: 2px;
}}
.section-title {{
  font-weight: bold;
  font-size: 10.6pt;
  margin-top: 3px;
  margin-bottom: 2px;
}}
.section-subtitle {{
  font-style: italic;
  font-size: 9.6pt;
  margin-bottom: 4px;
}}
.question {{
  margin-bottom: 6px;
  text-align: justify;
}}
.question-title {{
  font-weight: bold;
}}
.options-grid-4 {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 2px;
  margin-bottom: 3px;
}}
.sub-item {{
  margin-left: 10px;
  margin-top: 2.5px;
  margin-bottom: 2.5px;
}}
.sub-item-label {{
  font-weight: bold;
  display: inline-block;
  width: 18px;
}}
.end-exam {{
  text-align: center;
  font-weight: bold;
  margin-top: 16px;
  font-size: 10.8pt;
}}
.end-note {{
  text-align: center;
  font-style: italic;
  font-size: 9.3pt;
  margin-top: 3px;
}}
.img-center {{
  text-align: center;
  margin: 8px 0;
}}
.img-cau1 {{
  max-width: 530px;
  width: 80%;
  height: auto;
  display: inline-block;
}}
.img-cau2 {{
  max-width: 570px;
  width: 86%;
  height: auto;
  display: inline-block;
}}
.img-cau3 {{
  max-width: 290px;
  width: 44%;
  height: auto;
  display: inline-block;
}}
</style>
</head>
<body>

<!-- ==================== PAGE 1 ==================== -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 04 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12<br>ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 114</div>
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

<!-- Câu 1 (Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 1)^2 (x + 2)^3$ với mọi $x \\in \\mathbb{{R}}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid-4">
    <div><strong>A.</strong> $3$.</div>
    <div><strong>B.</strong> $1$.</div>
    <div><strong>C.</strong> $2$.</div>
    <div><strong>D.</strong> $6$.</div>
  </div>
</div>

<!-- Câu 2 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x)$ xác định trên $\\mathbb{{R}} \\setminus \\{{2\\}}$ thỏa mãn $\\lim_{{x \\to -\\infty}} f(x) = 1$, $\\lim_{{x \\to +\\infty}} f(x) = 3$, $\\lim_{{x \\to 2^+}} f(x) = +\\infty$ và $\\lim_{{x \\to 2^-}} f(x) = -1$. Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số đã cho là
  <div class="options-grid-4">
    <div><strong>A.</strong> $3$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $4$.</div>
    <div><strong>D.</strong> $1$.</div>
  </div>
</div>

<!-- Câu 3 (Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 3.</span> Có bao nhiêu giá trị nguyên của tham số $m \\in [-5; 5]$ để hàm số $y = \\dfrac{{x - 2}}{{x + m}}$ đồng biến trên từng khoảng xác định?
  <div class="options-grid-4">
    <div><strong>A.</strong> $5$.</div>
    <div><strong>B.</strong> $8$.</div>
    <div><strong>C.</strong> $6$.</div>
    <div><strong>D.</strong> $7$.</div>
  </div>
</div>

<!-- Câu 4 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 4.</span> Cho tứ diện đều $ABCD$ có cạnh bằng $a$. Góc giữa hai vectơ $\\overrightarrow{{AB}}$ và $\\overrightarrow{{CD}}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $60^\\circ$.</div>
    <div><strong>B.</strong> $90^\\circ$.</div>
    <div><strong>C.</strong> $45^\\circ$.</div>
    <div><strong>D.</strong> $120^\\circ$.</div>
  </div>
</div>

<!-- Câu 5 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 5.</span> Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(1; 2; 3)$ và mặt phẳng $(P): 2x + y - 2z + 11 = 0$. Tọa độ hình chiếu vuông góc $H$ của điểm $A$ trên mặt phẳng $(P)$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $H(-1; 1; 5)$.</div>
    <div><strong>B.</strong> $H(3; 3; 1)$.</div>
    <div><strong>C.</strong> $H(-1; 3; 5)$.</div>
    <div><strong>D.</strong> $H(1; -1; 5)$.</div>
  </div>
</div>

<!-- Câu 6 (Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1; 0; 0)$, $B(0; 2; 0)$, $C(0; 0; 3)$ và $D(2; 2; 3)$. Thể tích của khối tứ diện $ABCD$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $6$.</div>
    <div><strong>B.</strong> $18$.</div>
    <div><strong>C.</strong> $1$.</div>
    <div><strong>D.</strong> $3$.</div>
  </div>
</div>

<!-- Câu 7 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 7.</span> Trong không gian với hệ tọa độ $Oxyz$, cho mặt cầu $(S): (x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 9$ và mặt phẳng $(\\alpha): 2x - 2y + z + m = 0$. Giá trị của tham số $m$ để mặt phẳng $(\\alpha)$ tiếp xúc với mặt cầu $(S)$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $m = 0$ hoặc $m = 18$.</div>
    <div><strong>B.</strong> $m = 0$ hoặc $m = -18$.</div>
    <div><strong>C.</strong> $m = 9$ hoặc $m = -9$.</div>
    <div><strong>D.</strong> $m = 3$ hoặc $m = -15$.</div>
  </div>
</div>

<!-- Câu 8 (Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian với hệ tọa độ $Oxyz$, tọa độ giao điểm $M$ của đường thẳng $d: \\dfrac{{x - 1}}{{2}} = \\dfrac{{y + 2}}{{-1}} = \\dfrac{{z - 3}}{{1}}$ và mặt phẳng $(P): x + 2y + z - 1 = 0$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $M(1; -2; 3)$.</div>
    <div><strong>B.</strong> $M(-1; -1; 2)$.</div>
    <div><strong>C.</strong> $M(3; -3; 4)$.</div>
    <div><strong>D.</strong> $M(5; -4; 5)$.</div>
  </div>
</div>

<!-- Câu 9 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian với hệ tọa độ $Oxyz$, sin của góc giữa đường thẳng $d: \\dfrac{{x - 1}}{{2}} = \\dfrac{{y + 1}}{{1}} = \\dfrac{{z}}{{-2}}$ và mặt phẳng $(P): 2x + 2y - z - 5 = 0$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{4}}{{9}}$.</div>
    <div><strong>B.</strong> $\\dfrac{{8}}{{9}}$.</div>
    <div><strong>C.</strong> $\\dfrac{{\\sqrt{{17}}}}{{9}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{2}}{{3}}$.</div>
  </div>
</div>

<!-- Câu 10 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 10.</span> Cho hàm số $f(x)$ liên tục trên đoạn $[0; 4]$ thỏa mãn $\\int_0^4 f(x)\\,\\mathrm{{d}}x = 8$. Giá trị của tích phân $I = \\int_0^2 f(2x)\\,\\mathrm{{d}}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $4$.</div>
    <div><strong>B.</strong> $16$.</div>
    <div><strong>C.</strong> $8$.</div>
    <div><strong>D.</strong> $2$.</div>
  </div>
</div>

<!-- Câu 11 (Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 11.</span> Giá trị của tích phân $I = \\int_0^1 (2x + 1) e^x\\,\\mathrm{{d}}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $e - 1$.</div>
    <div><strong>B.</strong> $2e + 1$.</div>
    <div><strong>C.</strong> $3e - 1$.</div>
    <div><strong>D.</strong> $e + 1$.</div>
  </div>
</div>

<!-- Câu 12 (Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 12.</span> Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = 3x - x^2$ và trục hoành $Ox$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{9}}{{4}}$.</div>
    <div><strong>B.</strong> $9$.</div>
    <div><strong>C.</strong> $\\dfrac{{9}}{{2}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{27}}{{2}}$.</div>
  </div>
</div>

<!-- ==================== PAGE 2 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 (Key: Đ - S - Đ - S) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 1.</span> Trong một nghiên cứu dịch tễ học, tổng số ca mắc một bệnh truyền nhiễm trong một cộng đồng dân cư sau $t$ ngày (kể từ khi ca bệnh đầu tiên xuất hiện) được mô hình hóa bởi hàm số Logistic: $N(t) = \\dfrac{{1000}}{{1 + 9e^{{-0,2t}}}}$ ($0 \\le t \\le 60$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Số người bị nhiễm bệnh ban đầu tại thời điểm $t = 0$ là $100$ người.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đạo hàm $N'(t) < 0$ với mọi $t \\ge 0$, tức là tổng số ca nhiễm luôn giảm theo thời gian.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tốc độ lây lan dịch bệnh (số ca nhiễm mới gia tăng mỗi ngày $N'(t)$) đạt giá trị lớn nhất khi tổng số ca nhiễm đạt $500$ người.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khi thời gian bùng phát dịch kéo dài ($t \\to +\\infty$), tổng số ca nhiễm bệnh trong cộng đồng có thể vượt quá $1200$ người.</div>
</div>

<!-- Câu 2 (Key: Đ - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 2.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là kilômét), một ngọn hải đăng đặt tại đảo có tọa độ $A(2; 3; 1)$. Một tàu ngầm di chuyển dưới mặt nước biển theo đường thẳng $d$ có phương trình tham số: $\\begin{{cases}} x = 6 - 2t \\\\ y = -1 + 2t \\\\ z = -2 + t \\end{{cases}}$ ($t \\ge 0$, $t$ tính bằng giờ). Mặt biển được lấy trùng với mặt phẳng tọa độ $(Oxy): z = 0$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tàu ngầm nổi lên mặt biển tại điểm có tọa độ $M(2; 3; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vận tốc di chuyển của tàu ngầm bằng $3\\text{{ km/h}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Sin của góc tạo bởi đường di chuyển $d$ của tàu ngầm và mặt biển $(Oxy)$ bằng $\\dfrac{{2}}{{3}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách từ ngọn hải đăng $A(2; 3; 1)$ đến vị trí tàu ngầm tại thời điểm tàu nổi lên mặt biển bằng $1\\text{{ km}}$.</div>
</div>

<!-- Câu 3 (Key: Đ - S - Đ - S) -->
<div class="question" style="margin-bottom: 10px;">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 8px;">
    <div style="flex: 1;">
      <span class="question-title">Câu 3.</span> Hình vẽ bên mô tả hiệu suất làm việc của hai công nhân trong một nhà máy trong thời gian $6\\text{{ giờ}}$. Công nhân A đang sản xuất với hiệu suất $Q_1'(t) = -2t^2 + 4t + 58$ sản phẩm mỗi giờ, trong khi công nhân B đang sản xuất với hiệu suất $Q_2'(t) = 53 + at$ sản phẩm mỗi giờ ($a \\in \\mathbb{{R}}$). Biết rằng hàm $Q_1(t)$ và $Q_2(t)$ mô phỏng số lượng sản phẩm mới làm được của công nhân A và công nhân B sau $t\\text{{ giờ}}$. Xét tính đúng sai của các mệnh đề sau:
    </div>
    <div style="width: 260px; text-align: right; flex-shrink: 0;">
      <img src="{img_p2_c3_b64}" style="width: 252px; height: auto;" alt="Đồ thị Câu 3">
    </div>
  </div>
  <div class="sub-item"><span class="sub-item-label">a)</span> Hiệu suất cực đại của công nhân A là $60$ sản phẩm mỗi giờ.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Phần diện tích tô đậm biểu diễn cho tổng số lượng sản phẩm mới mà 2 công nhân làm được trong $6\\text{{ giờ}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Sau $5\\text{{ giờ}}$ số lượng sản phẩm mới mà công nhân A hoàn thành nhiều hơn công nhân B là $54$ sản phẩm (kết quả làm tròn đến hàng đơn vị).</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Sau $6\\text{{ giờ}}$ làm việc tổng số lượng sản phẩm mới mà 2 công nhân hoàn thành là $502$ sản phẩm.</div>
</div>

<!-- Câu 4 (Key: Đ - S - Đ - Đ) -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là mét), một mái che sân khấu ngoài trời được thiết kế dạng hình chóp tứ giác đều $S.ABCD$ với đỉnh $S$ hướng lên trên. Mặt phẳng đáy $(ABCD)$ nằm trên mặt đất $(Oxy): z = 0$ có tâm trùng với gốc tọa độ $O(0; 0; 0)$ và các cạnh song song với các trục tọa độ ($AB \\parallel Ox$). Độ dài cạnh đáy bằng $12\\text{{ m}}$ và chiều cao của mái che là $SO = 8\\text{{ m}}$ (đỉnh $S$ nằm trên phần dương của trục $Oz$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tọa độ của đỉnh $S$ là $S(0; 0; 8)$ và điểm $C$ có tọa độ là $(6; 6; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Độ dài đường cao của mặt bên $(SCD)$ kẻ từ đỉnh $S$ bằng $12\\text{{ m}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Cosin của góc $\\alpha$ tạo bởi mặt bên $(SCD)$ và mặt phẳng đáy $(ABCD)$ bằng $\\dfrac{{3}}{{5}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Gọi $M$ là trung điểm của $SA$, khoảng cách từ điểm $B$ đến mặt phẳng $(MCD)$ bằng $\\dfrac{{48}}{{\\sqrt{{97}}}}\\text{{ m}}$.</div>
</div>

<!-- ==================== PAGE 3 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 (TẤM BÌA LỤC GIÁC ĐỀU CẮT GẬP CHÓP LỤC GIÁC ĐỀU) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 1.</span> Từ một tấm bìa lục giác đều cạnh bằng $30\\text{{ cm}}$, bạn Bình muốn làm một hình chóp lục giác đều bằng cách cắt bỏ phần tô đậm và dán các mép lại với nhau (các mối ghép nối có kích thước không đáng kể, tham khảo hình vẽ). Để thể tích khối chóp lục giác đều tạo thành lớn nhất thì phần diện tích bạn Bình cắt đi là bao nhiêu $\\text{{cm}}^2$ (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng đơn vị)?
  <div class="img-center">
    <img src="{img1_b64}" class="img-cau1" alt="Hình minh họa Câu 1">
  </div>
</div>

<!-- Câu 2 (VIÊN GẠCH HOA VĂN HYPERBOL) -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 2.</span> Một viên gạch hình vuông cạnh $10\\text{{ dm}}$ có trang trí và sơn màu hồng ở phần tô đậm như hình 1. Hình 2 là bản vẽ thiết kế viên gạch đó trong hệ tọa độ $Oxy$ với một đơn vị của mỗi trục ứng với $1\\text{{ dm}}$, $O$ là tâm hình vuông, các trục tọa độ lần lượt song song với các cạnh của hình vuông. Lúc này, mỗi hình $(C_1), (C_2), (C_3), (C_4)$ là một phần của một trong hai đường hypebol $y = -\\dfrac{{5}}{{x}}$, $y = \\dfrac{{5}}{{x}}$. Diện tích phần sơn màu hồng là bao nhiêu $\\text{{dm}}^2$ (làm tròn kết quả đến hàng phần mười)?
  <div class="img-center">
    <img src="{img2_b64}" class="img-cau2" alt="Hình minh họa Câu 2">
  </div>
</div>

<!-- ==================== PAGE 4 ==================== -->
<div style="page-break-before: always;"></div>

<!-- Câu 3 (CHIẾC LU ĐỰNG NƯỚC CẮT TỪ KHỐI CẦU) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 3.</span> Một khối cầu có bán kính là $5\\text{{ (dm)}}$, người ta cắt bỏ hai phần của khối cầu bằng hai mặt phẳng song song cùng vuông góc đường kính và cách tâm một khoảng $3\\text{{ (dm)}}$ để làm một chiếc lu đựng nước (như hình vẽ). Tính thể tích mà chiếc lu chứa được (kết quả làm tròn đến hàng đơn vị).
  <div class="img-center">
    <img src="{img3_b64}" class="img-cau3" alt="Hình minh họa Câu 3">
  </div>
</div>

<!-- Câu 4 (CỰC TRỊ TÂM TỈ CỰ OXYZ VỚI MẶT CẦU) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho mặt cầu $(S): (x - 1)^2 + (y - 2)^2 + (z + 1)^2 = 9$ và hai điểm $A(3; 2; 1)$, $B(-1; 0; 0)$. Điểm $M$ di động trên mặt cầu $(S)$. Tìm giá trị lớn nhất của biểu thức $P = 2MA^2 - MB^2$.
</div>

<!-- Câu 5 (ĐÀI KIỂM SOÁT KHÔNG LƯU BÁM SÁT HAI MÁY BAY) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 5.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục tọa độ là kilômét), đài kiểm soát không lưu theo dõi hai máy bay thương mại $A$ và $B$ đang bay thẳng đều ở cùng độ cao $10\\text{{ km}}$. Tại thời điểm $t = 0\\text{{ (phút)}}$, máy bay $A$ ở vị trí $A_0(10; 40; 10)$ và bay với vectơ vận tốc $\\overrightarrow{{v_A}} = (12; 6; 0)\\text{{ (km/phút)}}$. Cùng thời điểm đó, máy bay $B$ ở vị trí $B_0(26; 27; 10)$ và bay với vectơ vận tốc $\\overrightarrow{{v_B}} = (6; 14; 0)\\text{{ (km/phút)}}$. Khoảng cách ngắn nhất giữa hai máy bay trong quá trình bay bằng bao nhiêu kilômét?
</div>

<!-- Câu 6 (BÁN KÍNH ĐƯỜNG TRÒN TIẾP XÚC MẶT CẦU) -->
<div class="question" style="margin-bottom: 16px;">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, cho mặt cầu $(S): (x - 1)^2 + (y - 2)^2 + (z + 1)^2 = 9$ và điểm $A(4; 6; -1)$. Từ điểm $A$ kẻ các đường thẳng tiếp xúc với mặt cầu $(S)$, tập hợp tất cả các tiếp điểm tạo thành một đường tròn $(C)$. Bán kính của đường tròn $(C)$ bằng bao nhiêu?
</div>

<div class="end-exam">---------- HẾT ----------</div>
<div class="end-note">Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

<script>
document.addEventListener("DOMContentLoaded", function() {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "$$", right: "$$", display: true}},
      {{left: "$", right: "$", display: false}}
    ],
    throwOnError: false
  }});
}});
</script>
</body>
</html>
"""

html_filename = 'exam_de_khao_sat_toan_12_ma114.html'
pdf_name = "De_Thi_Khao_Sat_Toan_12_Ma_114.pdf"

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

print("Running Chrome to generate De 114 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
