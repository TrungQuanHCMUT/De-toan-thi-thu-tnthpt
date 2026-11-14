import base64
import subprocess
import pypdf

with open('assets_111/cau3_graph.png', 'rb') as f:
    cau3_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets_111/cau5_phong.png', 'rb') as f:
    cau5_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets_111/cau6_cancau.png', 'rb') as f:
    cau6_b64 = base64.b64encode(f.read()).decode('utf-8')

html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 111)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {{
  size: A4;
  margin-top: 5mm;
  margin-bottom: 5mm;
  margin-left: 11.5mm;
  margin-right: 11.5mm;
  @bottom-right {{
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 111";
    font-family: 'Times New Roman', serif;
    font-size: 9pt;
    color: #000;
  }}
}}

body {{
  font-family: 'Times New Roman', serif;
  font-size: 10pt;
  line-height: 1.25;
  color: #000;
  margin: 0;
  padding: 0;
}}

.katex .accent-vec > svg {{
  transform: scale(1.4);
  transform-origin: center bottom;
}}
.katex .svg-align > svg {{
  transform: scale(1.25);
  transform-origin: center bottom;
}}

.header-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2px;
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
  padding: 2px 6px;
  text-align: center;
  width: 175px;
  margin: 3px auto 0 auto;
  line-height: 1.22;
}}
.left-box .bold-text {{
  font-weight: bold;
  font-size: 10pt;
}}
.left-box .sub-text {{
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
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
  margin: 3px 0 1.5px 0;
}}
.solid-divider-thick {{
  border-top: 1.5px solid #000;
  margin: 2.5px 0 4px 0;
}}
.student-info {{
  display: flex;
  justify-content: space-between;
  font-size: 10pt;
  font-style: italic;
  margin-bottom: 2px;
}}
.section-title {{
  font-weight: bold;
  font-size: 10.5pt;
  margin-top: 3.5px;
  margin-bottom: 2px;
  text-align: justify;
}}
.section-subtitle {{
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 2.5px;
}}
.question {{
  margin-bottom: 3.0px;
  text-align: justify;
  page-break-inside: avoid;
  break-inside: avoid;
}}
.question-title {{
  font-weight: bold;
}}
.options-grid-4 {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4px;
  margin-top: 2px;
  margin-bottom: 2px;
}}
.options-grid-2 {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 4px;
  margin-top: 2px;
  margin-bottom: 2px;
}}
.sub-item {{
  margin-left: 18px;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  line-height: 1.32;
  text-align: justify;
}}
.sub-item-label {{
  font-weight: bold;
}}
.end-exam {{
  text-align: center;
  margin-top: 6px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}}
.end-note {{
  text-align: center;
  font-style: italic;
  font-size: 9.5pt;
}}
</style>
</head>
<body>

<!-- HEADER (Y CHANG ĐỀ 108) -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 03 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 111</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Đường tiệm cận đứng của đồ thị hàm số $y = \\dfrac{{2x + 3}}{{x - 1}}$ là đường thẳng có phương trình
  <div class="options-grid-4">
    <div><strong>A.</strong> $x = 2$.</div>
    <div><strong>B.</strong> $x = 1$.</div>
    <div><strong>C.</strong> $y = 2$.</div>
    <div><strong>D.</strong> $y = 1$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 2)^2(x + 3)^3$ với mọi $x \\in \\mathbb{{R}}$. Số điểm cực trị của hàm số đã cho là
  <div class="options-grid-4">
    <div><strong>A.</strong> $1$.</div>
    <div><strong>B.</strong> $3$.</div>
    <div><strong>C.</strong> $2$.</div>
    <div><strong>D.</strong> $4$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 5$ trên đoạn $[0; 2]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $3$.</div>
    <div><strong>B.</strong> $5$.</div>
    <div><strong>C.</strong> $1$.</div>
    <div><strong>D.</strong> $7$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Họ tất cả các nguyên hàm của hàm số $f(x) = \\sin 2x + e^{{3x}}$ trên $\\mathbb{{R}}$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $\\dfrac{{1}}{{2}}\\cos 2x + \\dfrac{{1}}{{3}}e^{{3x}} + C$.</div>
    <div><strong>B.</strong> $-\\cos 2x + 3e^{{3x}} + C$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $-2\\cos 2x + \\dfrac{{1}}{{3}}e^{{3x}} + C$.</div>
    <div><strong>D.</strong> $-\\dfrac{{1}}{{2}}\\cos 2x + \\dfrac{{1}}{{3}}e^{{3x}} + C$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Cho $\\int_{{1}}^{{2}} f(x)\\,\\mathrm{{d}}x = 2$ và $\\int_{{2}}^{{4}} f(x)\\,\\mathrm{{d}}x = -5$. Giá trị của tích phân $\\int_{{1}}^{{4}} [2f(x) - 3]\\,\\mathrm{{d}}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $-15$.</div>
    <div><strong>B.</strong> $-3$.</div>
    <div><strong>C.</strong> $3$.</div>
    <div><strong>D.</strong> $-9$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Diện tích hình phẳng giới hạn bởi hai đường cong parabol $y = x^2$ và $y = 2 - x^2$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{4}}{{3}}$.</div>
    <div><strong>B.</strong> $\\dfrac{{8}}{{3}}$.</div>
    <div><strong>C.</strong> $2$.</div>
    <div><strong>D.</strong> $\\dfrac{{16}}{{3}}$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Cho hình phẳng giới hạn bởi đường cong $y = x e^x$, trục hoành và hai đường thẳng $x = 0, x = 1$. Thể tích $V$ của khối tròn xoay tạo thành khi quay hình phẳng trên quanh trục hoành được tính theo công thức nào dưới đây?
  <div class="options-grid-2">
    <div><strong>A.</strong> $V = \\pi \\int_{{0}}^{{1}} x e^x\\,\\mathrm{{d}}x$.</div>
    <div><strong>B.</strong> $V = \\int_{{0}}^{{1}} x^2 e^{{2x}}\\,\\mathrm{{d}}x$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $V = \\pi \\int_{{0}}^{{1}} x^2 e^{{2x}}\\,\\mathrm{{d}}x$.</div>
    <div><strong>D.</strong> $V = \\pi^2 \\int_{{0}}^{{1}} x^2 e^{{2x}}\\,\\mathrm{{d}}x$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Trong không gian $Oxyz$, cho điểm $A(3; -2; 5)$. Hình chiếu vuông góc của điểm $A$ lên trục tung $Oy$ là điểm có tọa độ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $(3; 0; 0)$.</div>
    <div><strong>B.</strong> $(0; -2; 0)$.</div>
    <div><strong>C.</strong> $(0; 0; 5)$.</div>
    <div><strong>D.</strong> $(3; 0; 5)$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, cho hai điểm $P(1; 4; -3)$ và $Q(-3; 2; 1)$. Tọa độ trung điểm $I$ của đoạn thẳng $PQ$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $I(-2; 6; -2)$.</div>
    <div><strong>B.</strong> $I(2; -1; 2)$.</div>
    <div><strong>C.</strong> $I(-1; 3; 2)$.</div>
    <div><strong>D.</strong> $I(-1; 3; -1)$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, cho hai vectơ $\\overrightarrow{{u}} = (1; 2; -2)$ và $\\overrightarrow{{v}} = (2; -1; 2)$. Độ dài của vectơ $\\overrightarrow{{u}} + \\overrightarrow{{v}}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\sqrt{{10}}$.</div>
    <div><strong>B.</strong> $10$.</div>
    <div><strong>C.</strong> $\\sqrt{{26}}$.</div>
    <div><strong>D.</strong> $4$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Trong không gian $Oxyz$, cho hai vectơ $\\overrightarrow{{a}} = (1; 0; 1)$ và $\\overrightarrow{{b}} = (0; 1; 1)$. Côsin của góc giữa hai vectơ $\\overrightarrow{{a}}$ và $\\overrightarrow{{b}}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{\\sqrt{{2}}}}{{2}}$.</div>
    <div><strong>B.</strong> $-\\dfrac{{1}}{{2}}$.</div>
    <div><strong>C.</strong> $\\dfrac{{1}}{{2}}$.</div>
    <div><strong>D.</strong> $1$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Trong không gian $Oxyz$, vectơ nào dưới đây cùng hướng với vectơ $\\overrightarrow{{a}} = (2; -4; 6)$?
  <div class="options-grid-2">
    <div><strong>A.</strong> $\\overrightarrow{{u}}_1 = (-1; 2; -3)$.</div>
    <div><strong>B.</strong> $\\overrightarrow{{u}}_2 = (1; 2; 3)$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $\\overrightarrow{{u}}_3 = (2; 4; 6)$.</div>
    <div><strong>D.</strong> $\\overrightarrow{{u}}_4 = (1; -2; 3)$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1: BỎ HOÀN TOÀN ĐỒ THỊ -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \\dfrac{{x^2 - x + 1}}{{x - 1}}$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Đồ thị hàm số có đường tiệm cận đứng là $x = 1$ và đường tiệm cận xiên là $y = x$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số đã cho đồng biến trên mỗi khoảng $(-\\infty; 0)$ và $(2; +\\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tọa độ tâm đối xứng của đồ thị hàm số là giao điểm của hai đường tiệm cận $I(1; 1)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Khoảng cách nhỏ nhất giữa hai điểm bất kì thuộc hai nhánh khác nhau của đồ thị hàm số bằng $2\\sqrt{{2}}$.</div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Cho hàm số $f(x) = 4x^3 - 3x^2 + 2x$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số $F(x) = x^4 - x^3 + x^2 + 5$ là một nguyên hàm của hàm số $f(x)$ trên $\\mathbb{{R}}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Biết $F(x)$ là một nguyên hàm của hàm số $f(x)$ thỏa mãn $F(1) = 3$. Khi đó giá trị của $F(2)$ bằng $16$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Giá trị của tích phân $\\int_{{0}}^{{1}} [f(x) + e^x]\\,\\mathrm{{d}}x$ bằng $e$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Gọi $D$ là hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$ và đồ thị hàm số $y = g(x) = 4x^3 - 5x^2 + 4x$. Khi quay hình phẳng $D$ quanh trục hoành $Ox$, thể tích khối tròn xoay tạo thành bằng $\\dfrac{{11\\pi}}{{15}}$.</div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Một đoàn tàu hỏa đang chạy với vận tốc $v_0 = 72\\text{{ km/h}}$ (tương ứng với $20\\text{{ m/s}}$) thì người lái tàu phát hiện chướng ngại vật và bắt đầu hãm phanh. Kể từ thời điểm bắt đầu hãm phanh ($t = 0$), đoàn tàu chuyển động chậm dần đều với vận tốc giảm dần theo thời gian $t$ (giây) theo quy luật $v(t) = 20 - 2t\\text{{ (m/s)}}$ cho đến khi dừng hẳn. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Kể từ lúc bắt đầu hãm phanh, đoàn tàu chuyển động thêm $10\\text{{ giây}}$ thì dừng hẳn.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Vận tốc của đoàn tàu sau $4\\text{{ giây}}$ kể từ lúc bắt đầu hãm phanh là $12\\text{{ m/s}}$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Quãng đường đoàn tàu đi được trong $5\\text{{ giây}}$ đầu tiên kể từ lúc hãm phanh bằng $75\\text{{ m}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Quãng đường tổng cộng mà đoàn tàu di chuyển từ lúc bắt đầu hãm phanh đến khi dừng hẳn là $120\\text{{ m}}$.</div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho hình chóp $S.ABCD$ có đỉnh chóp $S(0; 0; 3)$ và đáy $ABCD$ là hình vuông nằm trong mặt phẳng $(Oxy)$ với ba đỉnh có tọa độ là $A(0; 0; 0), B(2; 0; 0)$ và $D(0; 2; 0)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tọa độ đỉnh $C$ của hình vuông đáy là $C(2; 2; 0)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tọa độ trọng tâm $G$ của tam giác $SAB$ là $G\\left(\\dfrac{{2}}{{3}}; 0; 1\\right)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tích vô hướng của hai vectơ $\\overrightarrow{{SB}} \\cdot \\overrightarrow{{SD}}$ bằng $9$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Thể tích của khối chóp $S.ABCD$ bằng $6$.</div>
</div>

<!-- ==================== PHẦN III ==================== -->
<div class="section-title" style="margin-top: 4px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1: R=4cm, kết quả làm tròn đến hàng phần trăm, hình phóng to 50%, bỏ R=4cm và h=7cm -->
<div class="question" style="margin-bottom: 2px;">
  <div style="display: flex; gap: 14px; align-items: center;">
    <div style="flex: 1;">
      <span class="question-title">Câu 1.</span> Một chiếc hộp hình trụ có bán kính đường tròn đáy $R = 4\\text{{ cm}}$ và chiều cao $h = 7\\text{{ cm}}$. Người ta quấn một sợi dây từ một điểm $A$ thuộc đường tròn đáy trên quanh thân hình trụ đúng một vòng đến điểm $B$ thuộc đường tròn đáy dưới sao cho $B$ nằm thẳng đứng phía dưới điểm $A$ (như hình vẽ bên). Độ dài ngắn nhất của sợi dây đó bằng bao nhiêu xentimét? (kết quả làm tròn đến hàng phần trăm).
    </div>
    <div style="width: 255px; text-align: center; flex-shrink: 0;">
      <svg width="250" height="195" viewBox="10 10 145 130">
        <ellipse cx="90" cy="30" rx="55" ry="15" fill="#eef4fb" stroke="#000" stroke-width="1.6" />
        <path d="M 35 120 A 55 15 0 0 1 145 120" fill="none" stroke="#000" stroke-width="1.3" stroke-dasharray="3,3" />
        <path d="M 35 120 A 55 15 0 0 0 145 120" fill="none" stroke="#000" stroke-width="1.6" />
        <line x1="35" y1="30" x2="35" y2="120" stroke="#000" stroke-width="1.6" />
        <line x1="145" y1="30" x2="145" y2="120" stroke="#000" stroke-width="1.6" />
        <line x1="90" y1="30" x2="90" y2="120" stroke="#888" stroke-width="1.0" stroke-dasharray="4,3" />
        <circle cx="90" cy="30" r="2.5" fill="#000" />
        <circle cx="90" cy="120" r="2.5" fill="#000" />
        <!-- Helical wire -->
        <path d="M 35 30 Q 90 55 145 75" fill="none" stroke="#cc0000" stroke-width="2.0" stroke-dasharray="4,3" />
        <path d="M 145 75 Q 90 110 35 120" fill="none" stroke="#cc0000" stroke-width="2.6" />
        <circle cx="35" cy="30" r="3.5" fill="#cc0000" />
        <text x="18" y="35" font-family="Times New Roman" font-size="14" font-weight="bold" fill="#cc0000">A</text>
        <circle cx="35" cy="120" r="3.5" fill="#cc0000" />
        <text x="18" y="125" font-family="Times New Roman" font-size="14" font-weight="bold" fill="#cc0000">B</text>
      </svg>
    </div>
  </div>
</div>

<!-- Câu 2: Bỏ R=1m, L=4m, chỉ giữ 0.5m, làm tròn hàng phần trăm -->
<div class="question" style="margin-bottom: 2px;">
  <div>
    <span class="question-title">Câu 2.</span> Một bồn chứa nước hình trụ đặt nằm ngang có bán kính đáy $R = 1\\text{{ m}}$ và chiều dài $L = 4\\text{{ m}}$. Mực nước trong bồn hiện tại ngập đến độ cao $0,5\\text{{ m}}$ tính từ điểm thấp nhất của đáy (như hình vẽ bên dưới). Thể tích lượng nước có trong bồn xấp xỉ bằng bao nhiêu mét khối? (kết quả làm tròn đến hàng phần trăm).
  </div>
  <div style="text-align: center; margin-top: 2px; margin-bottom: 1px;">
    <svg width="310" height="95" viewBox="0 0 280 95">
      <ellipse cx="65" cy="48" rx="25" ry="44" fill="none" stroke="#003366" stroke-width="1.5" />
      <line x1="65" y1="4" x2="225" y2="4" stroke="#003366" stroke-width="1.5" />
      <line x1="65" y1="92" x2="225" y2="92" stroke="#003366" stroke-width="1.5" />
      <path d="M 225 4 A 25 44 0 0 1 225 92" fill="none" stroke="#003366" stroke-width="1.5" />
      <!-- Water body inside -->
      <path d="M 43 71 A 25 44 0 0 0 65 92 A 25 44 0 0 0 87 71 Z" fill="#66b2ff" opacity="0.8" stroke="#003366" stroke-width="1" />
      <polygon points="43,71 87,71 247,71 203,71" fill="#99ccff" opacity="0.7" />
      <line x1="43" y1="71" x2="203" y2="71" stroke="#004080" stroke-width="1.2" />
      <line x1="87" y1="71" x2="247" y2="71" stroke="#004080" stroke-width="1.2" />
      <!-- ONLY 0,5 m marker -->
      <line x1="26" y1="71" x2="26" y2="92" stroke="#cc0000" stroke-width="1.2" />
      <line x1="20" y1="71" x2="32" y2="71" stroke="#cc0000" stroke-width="1.2" />
      <line x1="20" y1="92" x2="32" y2="92" stroke="#cc0000" stroke-width="1.2" />
      <text x="3" y="85" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#cc0000">0,5 m</text>
    </svg>
  </div>
</div>

<div style="page-break-before: always;"></div>

<!-- Câu 3: Hình tăng 50%, để dưới câu hỏi -->
<div class="question" style="margin-top: 3px; margin-bottom: 3.5px;">
  <div>
    <span class="question-title">Câu 3.</span> Cho hai hàm số $f(x) = ax^3 + bx^2 + cx + \\dfrac{{3}}{{4}}$ và $g(x) = dx^2 + ex - \\dfrac{{3}}{{4}}$ ($a, b, c, d, e \\in \\mathbb{{R}}$). Biết rằng đồ thị của hàm số $y = f(x)$ và $y = g(x)$ cắt nhau tại ba điểm có hoành độ lần lượt là $-2; 1; 3$ (như hình vẽ bên dưới). Hình phẳng giới hạn bởi hai đồ thị đã cho có diện tích bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười).
  </div>
  <div style="text-align: center; margin-top: 2px; margin-bottom: 2px;">
    <img src="data:image/png;base64,{cau3_b64}" style="width: 280px; height: auto;" />
  </div>
</div>

<!-- Câu 4: Không hình -->
<div class="question" style="margin-bottom: 3.5px;">
  <span class="question-title">Câu 4.</span> Một chất điểm $A$ xuất phát từ $O$, chuyển động thẳng với vận tốc biến thiên theo thời gian bởi quy luật $v(t) = \\dfrac{{1}}{{100}}t^2 + \\dfrac{{13}}{{30}}t\\text{{ (m/s)}}$, trong đó $t$ là khoảng thời gian tính từ lúc $A$ bắt đầu chuyển động. Từ trạng thái nghỉ, một chất điểm $B$ cũng xuất phát từ $O$, chuyển động thẳng cùng hướng với $A$ nhưng chậm hơn $10\\text{{ giây}}$ so với $A$ và có gia tốc bằng $a\\text{{ (m/s}}^2\\text{{)}}$ ($a$ là hằng số). Sau khi $B$ xuất phát được $15\\text{{ giây}}$ thì đuổi kịp $A$. Vận tốc của $B$ tại thời điểm đuổi kịp $A$ bằng bao nhiêu mét trên giây?
</div>

<!-- Câu 5: Hình ở DƯỚI câu hỏi, tăng 50% -->
<div class="question" style="margin-bottom: 3.5px;">
  <div>
    <span class="question-title">Câu 5.</span> Một căn phòng có dạng hình hộp chữ nhật với chiều dài $4\\text{{ m}}$, chiều rộng $3\\text{{ m}}$ và chiều cao $3\\text{{ m}}$. Xét hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với một góc phòng và mặt phẳng $(Oxy)$ trùng với mặt sàn (như hình vẽ bên dưới), đơn vị đo được lấy theo mét. Trên bức tường thuộc mặt phẳng $(Oyz)$ có một cột dạng hình hộp chữ nhật nhô ra với chiều dài $0,4\\text{{ m}}$, chiều rộng $0,2\\text{{ m}}$. Bác Nam lắp một bóng đèn trên tường tại vị trí điểm $A\\left(1; 0; \\dfrac{{5}}{{2}}\\right)$ và công tắc bóng đèn đặt tại điểm $B\\left(\\dfrac{{1}}{{2}}; 4; 1\\right)$. Dây cáp điện cho bóng đèn được đấu từ công tắc điện dọc theo các bức tường (không đi qua trần nhà, sàn nhà) và nối đến bóng đèn. Hỏi bác Nam phải dùng đoạn dây điện có độ dài tối thiểu là bao nhiêu mét? (kết quả làm tròn đến hàng phần trăm).
  </div>
  <div style="text-align: center; margin-top: 3px; margin-bottom: 2px;">
    <img src="data:image/png;base64,{cau5_b64}" style="width: 350px; height: auto;" />
  </div>
</div>

<!-- Câu 6: Hình tăng 50% -->
<div class="question" style="margin-bottom: 3px;">
  <div style="display: flex; gap: 14px; align-items: center;">
    <div style="flex: 1;">
      <span class="question-title">Câu 6.</span> Một chiếc ô tô được đặt trên mặt đáy dưới của một khung sắt dạng hình hộp chữ nhật với đáy trên là hình chữ nhật $ABCD$, mặt phẳng $(ABCD)$ song song với mặt phẳng nằm ngang. Khung sắt đó được đặt vào móc $E$ của chiếc cần cẩu sao cho các đoạn dây cáp $EA, EB, EC, ED$ bằng nhau và cùng tạo với mặt phẳng $(ABCD)$ một góc $\\alpha$ (như hình vẽ bên). Chiếc cần cẩu kéo khung sắt lên theo phương thẳng đứng. Biết các lực căng $\\overrightarrow{{F}}_1, \\overrightarrow{{F}}_2, \\overrightarrow{{F}}_3, \\overrightarrow{{F}}_4$ đều có cường độ là $4800\\text{{ N}}$, trọng lượng của cả khung sắt chứa xe ô tô là $7200\\sqrt{{6}}\\text{{ N}}$. Tính $\\sin\\alpha$ (kết quả làm tròn đến hàng phần trăm).
    </div>
    <div style="width: 160px; text-align: center; flex-shrink: 0;">
      <img src="data:image/png;base64,{cau6_b64}" style="width: 155px; height: auto;" />
    </div>
  </div>
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

with open('exam_de_khao_sat_toan_12_ma111.html', 'w', encoding='utf-8') as f:
    f.write(html)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_name = "De_Thi_Khao_Sat_Toan_12_Ma_111.pdf"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    "exam_de_khao_sat_toan_12_ma111.html"
]

print("Running Chrome to generate De 111 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
    if i == 1:
        print("  Page 2 has Cau 2:", "Câu 2. Một bồn chứa" in txt)
    if i == 2:
        print("  Page 3 has HET:", "HẾT" in txt)
