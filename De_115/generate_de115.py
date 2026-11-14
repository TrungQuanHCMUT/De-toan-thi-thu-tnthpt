import os, subprocess, pypdf, base64

def get_base64_img(filename):
    with open(filename, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

img1_b64 = get_base64_img('assets/de115_cau1_cone.png')
img2_b64 = get_base64_img('assets/de115_cau2.png')
img5_b64 = get_base64_img('assets/de115_cau5_integral.png')

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề Khảo Sát Toán 12 - Mã Đề 115</title>
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
  font-size: 10.1pt;
  line-height: 1.28;
  color: #000;
  margin: 0;
  padding: 0;
}}
.katex {{
  font-size: 1.01em;
}}
.katex-display {{
  margin: 2px 0;
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
  margin-bottom: 4px;
  text-align: justify;
}}
.question-title {{
  font-weight: bold;
}}
.options-grid-4 {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 1.5px;
  margin-bottom: 2px;
}}
.options-grid-2 {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  row-gap: 1.5px;
  margin-top: 1.5px;
  margin-bottom: 2px;
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
  margin-top: 14px;
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
  margin: 4px 0;
}}
.img-cau1 {{
  max-width: 480px;
  width: 72%;
  height: auto;
  display: inline-block;
}}
.img-cau2 {{
  max-width: 270px;
  width: 42%;
  height: auto;
  display: inline-block;
}}
.img-cau5 {{
  max-width: 320px;
  width: 50%;
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
      <div class="right-box">Mã đề: 115</div>
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
  <span class="question-title">Câu 1.</span> Cho hàm số $y = \\dfrac{{2x^2 - 3x + 5}}{{x - 1}}$. Đường tiệm cận xiên của đồ thị hàm số có phương trình là $y = ax + b$. Giá trị của biểu thức $a + b$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $-1$.</div>
    <div><strong>B.</strong> $3$.</div>
    <div><strong>C.</strong> $1$.</div>
    <div><strong>D.</strong> $2$.</div>
  </div>
</div>

<!-- Câu 2 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 2.</span> Một doanh nghiệp sản xuất một loại sản phẩm với tổng chi phí sản xuất $x$ tấn sản phẩm được mô hình hóa bởi hàm số $C(x) = x^2 + 40x + 1600$ (triệu đồng), với $x > 0$. Chi phí trung bình để sản xuất một tấn sản phẩm là $\\bar{{C}}(x) = \\dfrac{{C(x)}}{{x}}$. Để chi phí trung bình trên mỗi tấn sản phẩm là nhỏ nhất thì doanh nghiệp cần sản xuất bao nhiêu tấn sản phẩm?
  <div class="options-grid-4">
    <div><strong>A.</strong> $40$ tấn.</div>
    <div><strong>B.</strong> $50$ tấn.</div>
    <div><strong>C.</strong> $30$ tấn.</div>
    <div><strong>D.</strong> $20$ tấn.</div>
  </div>
</div>

<!-- Câu 3 (Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 3.</span> Cho hàm số $y = \\dfrac{{x^2 - 2x + 3}}{{x + 1}}$. Tọa độ tâm đối xứng $I$ của đồ thị hàm số (giao điểm của hai đường tiệm cận) là
  <div class="options-grid-4">
    <div><strong>A.</strong> $I(1; -2)$.</div>
    <div><strong>B.</strong> $I(-1; 4)$.</div>
    <div><strong>C.</strong> $I(1; 2)$.</div>
    <div><strong>D.</strong> $I(-1; -4)$.</div>
  </div>
</div>

<!-- Câu 4 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 4.</span> Ba lực $\\overrightarrow{{F_1}}, \\overrightarrow{{F_2}}, \\overrightarrow{{F_3}}$ cùng tác dụng vào một chất điểm cân bằng tại gốc $O$. Biết rằng $|\\overrightarrow{{F_1}}| = 10\\text{{ N}}$, $|\\overrightarrow{{F_2}}| = 10\\text{{ N}}$ và góc giữa hai lực $\\overrightarrow{{F_1}}$ và $\\overrightarrow{{F_2}}$ bằng $120^\\circ$. Độ lớn của lực $\\overrightarrow{{F_3}}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $10\\sqrt{{3}}\\text{{ N}}$.</div>
    <div><strong>B.</strong> $10\\text{{ N}}$.</div>
    <div><strong>C.</strong> $20\\text{{ N}}$.</div>
    <div><strong>D.</strong> $5\\sqrt{{3}}\\text{{ N}}$.</div>
  </div>
</div>

<!-- Câu 5 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 5.</span> Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(1; 0; 0)$, $B(0; 2; 0)$, $C(0; 0; 4)$. Diện tích của tam giác $ABC$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\sqrt{{21}}$.</div>
    <div><strong>B.</strong> $\\sqrt{{42}}$.</div>
    <div><strong>C.</strong> $2\\sqrt{{21}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{\\sqrt{{21}}}}{{2}}$.</div>
  </div>
</div>

<!-- Câu 6 (Đáp án D) - Đã sửa format options-grid-2 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, phương trình mặt cầu có tâm $I(2; -1; 3)$ và tiếp xúc với trục $Oz$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $(x + 2)^2 + (y - 1)^2 + (z + 3)^2 = 5$.</div>
    <div><strong>B.</strong> $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 13$.</div>
    <div><strong>C.</strong> $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 9$.</div>
    <div><strong>D.</strong> $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 5$.</div>
  </div>
</div>

<!-- Câu 7 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 7.</span> Trong không gian với hệ tọa độ $Oxyz$, cho hai đường thẳng $d_1: \\dfrac{{x - 1}}{{2}} = \\dfrac{{y + 1}}{{1}} = \\dfrac{{z - 2}}{{-1}}$ và $d_2: \\dfrac{{x + 1}}{{1}} = \\dfrac{{y - 2}}{{2}} = \\dfrac{{z + 1}}{{1}}$. Vị trí tương đối của hai đường thẳng $d_1$ và $d_2$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> Song song.</div>
    <div><strong>B.</strong> Chéo nhau.</div>
    <div><strong>C.</strong> Cắt nhau.</div>
    <div><strong>D.</strong> Trùng nhau.</div>
  </div>
</div>

<!-- Câu 8 (Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian với hệ tọa độ $Oxyz$, cho điểm $M(1; -2; 3)$. Hình chiếu vuông góc của điểm $M$ lên trục tọa độ $Oy$ có tọa độ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $(1; 0; 0)$.</div>
    <div><strong>B.</strong> $(0; 0; 3)$.</div>
    <div><strong>C.</strong> $(0; -2; 0)$.</div>
    <div><strong>D.</strong> $(1; 0; 3)$.</div>
  </div>
</div>

<!-- Câu 9 (Đáp án B) -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(3; 3; -3)$ và đường thẳng $d: \\dfrac{{x - 1}}{{1}} = \\dfrac{{y - 2}}{{2}} = \\dfrac{{z + 1}}{{2}}$. Khoảng cách từ điểm $A$ đến đường thẳng $d$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $2$.</div>
    <div><strong>B.</strong> $3$.</div>
    <div><strong>C.</strong> $\\sqrt{{5}}$.</div>
    <div><strong>D.</strong> $\\sqrt{{13}}$.</div>
  </div>
</div>

<!-- Câu 10 (Đáp án A) -->
<div class="question">
  <span class="question-title">Câu 10.</span> Cho hàm số $f(x)$ liên tục trên $\\mathbb{{R}}$ thỏa mãn $\\int_0^3 f(x)\\,\\mathrm{{d}}x = 7$ và $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = 2$. Giá trị của $F(3)$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $9$.</div>
    <div><strong>B.</strong> $5$.</div>
    <div><strong>C.</strong> $-5$.</div>
    <div><strong>D.</strong> $14$.</div>
  </div>
</div>

<!-- Câu 11 (Đáp án D) -->
<div class="question">
  <span class="question-title">Câu 11.</span> Một vật chuyển động với gia tốc $a(t) = 6t - 2\\text{{ (m/s}}^2\\text{{)}}$. Vận tốc ban đầu của vật tại thời điểm $t = 0$ là $v(0) = 4\\text{{ m/s}}$. Quãng đường vật đi được sau $3\\text{{ giây}}$ đầu tiên bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $36\\text{{ m}}$.</div>
    <div><strong>B.</strong> $24\\text{{ m}}$.</div>
    <div><strong>C.</strong> $28\\text{{ m}}$.</div>
    <div><strong>D.</strong> $30\\text{{ m}}$.</div>
  </div>
</div>

<!-- Câu 12 (Đáp án C) -->
<div class="question">
  <span class="question-title">Câu 12.</span> Thể tích của khối tròn xoay sinh ra khi quay hình phẳng giới hạn bởi đường cong $y = \\sqrt{{x}}e^x$, trục hoành $Ox$ và hai đường thẳng $x = 0, x = 1$ quanh trục hoành $Ox$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{\\pi(e^2 - 1)}}{{4}}$.</div>
    <div><strong>B.</strong> $\\dfrac{{\\pi(e^2 + 1)}}{{2}}$.</div>
    <div><strong>C.</strong> $\\dfrac{{\\pi(e^2 + 1)}}{{4}}$.</div>
    <div><strong>D.</strong> $\\pi(e^2 + 1)$.</div>
  </div>
</div>

<!-- ==================== PAGE 2 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 (Key: Đ - S - Đ - S) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 1.</span> Trong một trang trại nuôi tôm công nghệ cao, nồng độ oxy hòa tan trong nước $C(t)$ (đơn vị: mg/L) sau khi bật máy sục khí $t$ giờ ($0 \\le t \\le 12$) được mô tả bởi hàm số:
  $$C(t) = 4 + \\dfrac{{8t}}{{t^2 + 4}}$$
  Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Nồng độ oxy hòa tan ban đầu khi chưa bật máy sục khí ($t = 0$) là $4\\text{{ mg/L}}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Nồng độ oxy hòa tan trong nước luôn tăng trong suốt thời gian $12\\text{{ giờ}}$ sục khí.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Sau khi bật máy sục khí $2\\text{{ giờ}}$, nồng độ oxy hòa tan trong nước đạt giá trị cực đại bằng $6\\text{{ mg/L}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Trong suốt $12\\text{{ giờ}}$ theo dõi, nồng độ oxy hòa tan trong hồ luôn duy trì ở mức trên $4,8\\text{{ mg/L}}$.</div>
</div>

<!-- Câu 2 (Key: Đ - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 2.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là mét), một cần cẩu tháp có chân đế đặt tại gốc tọa độ $O(0; 0; 0)$ trên mặt đất phẳng $(Oxy): z = 0$. Trục tháp thẳng đứng trùng với phần dương trục $Oz$. Cần cẩu có tay cần quay ngang, đầu mút tay cần tại thời điểm ban đầu ở vị trí $M(12; 16; 30)$. Cáp tải của cần cẩu móc vào một kiện hàng đặt tại vị trí $B(12; 16; 0)$ trên mặt đất. Cần cẩu nâng kiện hàng thẳng đứng từ $B$ lên vị trí $C(12; 16; 10)$, sau đó di chuyển đều kiện hàng theo phương ngang đến vị trí $D(0; 25; 10)$ với vận tốc $1,5\\text{{ m/s}}$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Khoảng cách từ đầu mút tay cần $M$ đến trục quay thẳng đứng $Oz$ của cần cẩu bằng $20\\text{{ m}}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Thời gian để cần cẩu di chuyển kiện hàng từ vị trí $C$ sang vị trí $D$ là $10\\text{{ giây}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Trên trục tháp ở độ cao $10\\text{{ m}}$ có gắn một đèn tín hiệu $E(0; 0; 10)$. Trong quá trình kiện hàng di chuyển thẳng từ $C$ đến $D$, khoảng cách ngắn nhất từ đèn tín hiệu $E$ đến kiện hàng bằng $15\\text{{ m}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Sin của góc tạo bởi sợi dây cáp nối từ đầu cần $M$ đến kiện hàng tại vị trí $D$ và mặt phẳng nằm ngang $(Oxy)$ bằng $\\dfrac{{4}}{{5}}$.</div>
</div>

<!-- Câu 3 (Key: S - Đ - S - Đ) -->
<div class="question" style="margin-bottom: 14px;">
  <span class="question-title">Câu 3.</span> Lưu lượng nước đổ về một hồ chứa thủy điện trong đợt mưa lũ kéo dài $8\\text{{ ngày}}$ được xác định bởi hàm số $f(t) = 15 + 6t - \\dfrac{{3}}{{4}}t^2$ (triệu $\\text{{m}}^3/\\text{{ngày}}$), với $0 \\le t \\le 8$ ($t$ tính bằng ngày). Ban quản lý hồ mở cửa xả đáy với lưu lượng xả cố định không đổi là $g(t) = 24$ (triệu $\\text{{m}}^3/\\text{{ngày}}$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tại thời điểm bắt đầu theo dõi ($t = 0$), lượng nước đổ về hồ là $20\\text{{ triệu m}}^3/\\text{{ngày}}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Lưu lượng nước đổ về hồ đạt giá trị lớn nhất tại ngày thứ 4 với giá trị là $27\\text{{ triệu m}}^3/\\text{{ngày}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Sau $8\\text{{ ngày}}$, tổng lượng nước tích thêm trong hồ tăng thêm $16\\text{{ triệu m}}^3$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Trong khoảng thời gian lưu lượng nước về hồ lớn hơn lưu lượng xả ($2 \\le t \\le 6$), tổng lượng nước hồ tích lũy thêm bằng $8\\text{{ triệu m}}^3$.</div>
</div>

<!-- Câu 4 (Key: Đ - S - S - Đ) -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là kilômét), một trạm radar đặt tại điểm $H(2; 3; 1)$ có bán kính phát hiện mục tiêu tối đa là $R = 10\\text{{ km}}$. Một thiết bị bay không người lái (drone) bay thẳng đều theo đường thẳng $d$ có phương trình tham số: $\\begin{{cases}} x = -6 + 4t \\\\ y = -3 + 3t \\\\ z = 7 \\end{{cases}}$ ($t$ tính bằng phút, $t \\ge 0$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Drone luôn bay ở độ cao ổn định $7\\text{{ km}}$ so với mặt đất $(Oxy)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vận tốc bay của drone bằng $10\\text{{ km/phút}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khoảng cách ngắn nhất từ trạm radar $H$ đến quỹ đạo bay của drone bằng $8\\text{{ km}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Drone nằm trong tầm quan sát của radar trong thời gian $3,2\\text{{ phút}}$ và bay được quãng đường $16\\text{{ km}}$ trong vùng phủ sóng radar.</div>
</div>

<!-- ==================== PAGE 3 ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 (Cây thông nón & trải phẳng hình) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 1.</span> Một cây thông trang trí Noel có dạng hình nón với bán kính đường tròn đáy $r = 2\text{{ m}}$ và đường cao là $4\text{{ m}}$. Người ta quấn quanh thân cây thông một sợi dây kim tuyến từ một điểm $A$ nằm trên đường tròn đáy, quấn đúng một vòng quanh mặt nón rồi nối tới trung điểm $M$ của đường sinh $SA$ (sợi dây luôn bám sát mặt xung quanh của hình nón, tham khảo hình vẽ). Độ dài ngắn nhất của sợi dây đó bằng bao nhiêu mét (làm tròn kết quả đến hàng phần mười)?
  <div class="img-center">
    <img src="{img1_b64}" class="img-cau1" alt="Mô hình cây thông nón">
  </div>
</div>

<!-- Câu 2 (Thùng rượu gỗ sồi) -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 2.</span> Một thùng rượu làm bằng gỗ sồi có chiều cao $80\\text{{ cm}}$. Bán kính của hai đáy thùng đều bằng $30\\text{{ cm}}$, bán kính ở phần bụng giữa thùng là $40\\text{{ cm}}$. Thân thùng rượu có dạng mặt cong sinh ra khi quay một cung parabol quanh trục đối xứng của nó nối tâm hai đáy (tham khảo hình vẽ). Hỏi thùng rượu đó có thể chứa được tối đa bao nhiêu lít rượu (làm tròn kết quả đến hàng đơn vị)?
  <div class="img-center">
    <img src="{img2_b64}" class="img-cau2" alt="Thùng rượu gỗ sồi">
  </div>
</div>

<!-- ==================== PAGE 4 ==================== -->
<div style="page-break-before: always;"></div>

<!-- Câu 3 (Cáp treo & đường điện cao thế) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 3.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục là mét), một tuyến cáp treo di chuyển dọc theo đường thẳng $d_1: \\dfrac{{x - 1}}{{2}} = \\dfrac{{y - 3}}{{2}} = \\dfrac{{z - 2}}{{1}}$ và một đường dây điện cao thế chạy thẳng dọc theo đường thẳng $d_2: \\dfrac{{x - 11}}{{1}} = \\dfrac{{y - 5}}{{-2}} = \\dfrac{{z - 2}}{{2}}$. Khoảng cách ngắn nhất giữa tuyến cáp treo và đường dây điện cao thế bằng bao nhiêu mét?
</div>

<!-- Câu 4 (Tâm tỉ cự T_min trên (P)) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(1; 2; -1)$, $B(3; 0; 1)$, $C(2; 1; 3)$ và mặt phẳng $(P): x + 2y - 2z + 7 = 0$. Điểm $M$ di động trên mặt phẳng $(P)$. Tìm giá trị nhỏ nhất của biểu thức $T = MA^2 + MB^2 + MC^2$.
</div>

<!-- Câu 5 (Tích phân phân thức hữu tỉ có chứa logarit) -->
<div class="question" style="margin-bottom: 12px;">
  <span class="question-title">Câu 5.</span> Biết $\displaystyle\int_{1}^{2} \dfrac{{2x^2 + 3x + 2}}{{x + 1}}\,\mathrm{{d}}x = a + \ln\left(\dfrac{{b}}{{c}}{chr(92)}right)$ với $a \in \mathbb{{Z}}$, $b, c \in \mathbb{{Z}}^+$ và $\dfrac{{b}}{{c}}$ tối giản. Tính giá trị của biểu thức<br>$T = a - b + c$.
</div>

<!-- Câu 6 (Góc giữa 2 vectơ trong hình chóp S.ABCD đáy hình thoi) -->
<div class="question" style="margin-top: 14px; margin-bottom: 16px; line-height: 1.55; letter-spacing: 0.2px;">
  <span class="question-title">Câu 6.</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi cạnh $a$, $\widehat{{ABC}} = 60^\circ$. Hình chiếu vuông góc của $S$ lên mặt phẳng đáy $(ABCD)$ là trọng tâm $G$ của tam giác $ACD$, biết $SA = a$. Gọi $M$ là trung điểm của cạnh $SB$, và $N$ là điểm thuộc cạnh $SC$ sao cho $SN = \dfrac{{1}}{{2}}NC$. Tính số đo của góc giữa hai vectơ $\overrightarrow{{AM}}$ &nbsp;và&nbsp; $\overrightarrow{{BN}}$ theo độ.
</div>

<div class="solid-divider" style="margin-top: 18px;"></div>
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

with open('test_de115.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML written to test_de115.html")
cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--print-to-pdf=De_Thi_Khao_Sat_Toan_12_Ma_115.pdf',
    '--no-pdf-header-footer',
    'test_de115.html'
]

print("Running Chrome to generate De 115 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader('De_Thi_Khao_Sat_Toan_12_Ma_115.pdf')
print("Total pages:", len(reader.pages))
for i, p in enumerate(reader.pages):
    txt = p.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
