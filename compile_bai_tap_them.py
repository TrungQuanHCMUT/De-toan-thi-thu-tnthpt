import subprocess

html_content = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bài Tập Luyện Thêm - Chuyên Đề Khảo Sát Hàm Số (Nâng Cao)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {
  size: A4;
  margin: 12mm 15mm 15mm 15mm;
  @bottom-right {
    content: "Trang " counter(page);
    font-family: 'Times New Roman', serif;
    font-size: 9pt;
    font-style: italic;
  }
}

body {
  font-family: 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #111;
  margin: 0;
  padding: 0;
}

h1.main-title {
  text-align: center;
  font-size: 16pt;
  text-transform: uppercase;
  color: #1a365d;
  margin-bottom: 4px;
}

h2.sub-title {
  text-align: center;
  font-size: 12pt;
  font-weight: normal;
  color: #2b4c7e;
  margin-top: 0;
  margin-bottom: 12px;
}

.divider {
  border-top: 1.5px solid #2b4c7e;
  margin: 10px 0 14px 0;
}

.sec-title {
  font-size: 11.5pt;
  font-weight: bold;
  color: #1a365d;
  background-color: #f0f4f8;
  padding: 4px 8px;
  border-left: 4px solid #2b4c7e;
  margin-top: 14px;
  margin-bottom: 8px;
}

.question {
  margin-bottom: 10px;
  text-align: justify;
  page-break-inside: avoid;
}

.q-title {
  font-weight: bold;
  color: #1a365d;
}

.sub-item {
  margin-left: 18px;
  margin-top: 2.5px;
  margin-bottom: 2.5px;
  text-align: justify;
}

.sub-item-label {
  font-weight: bold;
}

table.ans-table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0 14px 0;
  text-align: center;
}

table.ans-table th, table.ans-table td {
  border: 1px solid #666;
  padding: 5px 6px;
  font-size: 10pt;
}

table.ans-table th {
  background-color: #e9eef4;
  color: #1a365d;
}

.bold-ans {
  font-weight: bold;
  color: #c53030;
}

.page-break {
  page-break-before: always;
}
</style>
</head>
<body>

<h1 class="main-title">Bài tập luyện thêm</h1>
<h2 class="sub-title">CHUYÊN ĐỀ: KHẢO SÁT HÀM SỐ & ỨNG DỤNG ĐẠO HÀM (NÂNG CAO)</h2>
<div class="divider"></div>

<div class="sec-title">PHẦN II. CÂU HỎI TRẮC NGHIỆM ĐÚNG / SAI</div>
<div style="font-size: 9.5pt; font-style: italic; margin-bottom: 8px;">Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>

<div class="question">
  <span class="q-title">Câu 1:</span> Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$ và thỏa mãn $f'(x) = (x + 1)(x - 2)^2(x - 3)$ với mọi $x \in \mathbb{R}$. Xét hàm số $g(x) = f(x^2 - 2x)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Đạo hàm của hàm số $g(x)$ là $g'(x) = 2(x - 1)f'(x^2 - 2x)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm số $g(x)$ có đúng $5$ điểm cực trị.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Hàm số $g(x)$ nghịch biến trên khoảng $(1; 3)$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Hàm số $g(x)$ đạt cực tiểu tại điểm $x = 1$.</div>
</div>

<div class="question">
  <span class="q-title">Câu 2:</span> Cho hàm số $y = \dfrac{x^2 + mx - 1}{x - 1}$ (với $m$ là tham số thực) có đồ thị là $(C_m)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Với mọi giá trị của tham số $m \in \mathbb{R}$, đồ thị $(C_m)$ luôn có đường tiệm cận đứng là $x = 1$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Khi $m \ne 0$, đường tiệm cận xiên của đồ thị $(C_m)$ luôn có hệ số góc bằng $1$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khi $m = 1$, khoảng cách giữa hai điểm cực trị của đồ thị hàm số bằng $2\sqrt{5}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tồn tại giá trị của tham số $m$ để đồ thị $(C_m)$ có hai điểm cực trị nằm về hai phía khác nhau đối với trục hoành $Ox$.</div>
</div>

<div class="question">
  <span class="q-title">Câu 3:</span> Cho hàm số $f(x) = x^4 - 4x^3 + 4x^2 + a$ (với $a$ là tham số thực). Xét hàm số $g(x) = |f(x)|$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Đạo hàm $f'(x) = 4x(x - 1)(x - 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Khi $a = -1$, hàm số $g(x)$ có đúng $7$ điểm cực trị.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Khi $a = 2$, giá trị nhỏ nhất của hàm số $g(x)$ trên $\mathbb{R}$ bằng $2$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Có tất cả $6$ giá trị nguyên của tham số $a \in [-5; 5]$ để hàm số $g(x)$ có đúng $3$ điểm cực trị.</div>
</div>

<div class="question">
  <span class="q-title">Câu 4:</span> Một công ty dự định xây dựng một đường ống dẫn dầu từ giàn khoan trên biển ở vị trí $A$ cách bờ biển một khoảng $AH = 9\text{ km}$ đến nhà máy lọc dầu ở vị trí $B$ trên đất liền. Khoảng cách từ hình chiếu $H$ của $A$ trên bờ biển đến nhà máy $B$ là $HB = 15\text{ km}$ (bờ biển được xem là một đường thẳng). Chi phí lắp đặt mỗi kilômét đường ống dưới biển là $500$ triệu đồng, chi phí lắp đặt mỗi kilômét đường ống trên đất liền là $300$ triệu đồng. Đường ống sẽ đi từ $A$ dưới biển đến một điểm nối $C$ trên bờ biển ($C$ nằm giữa $H$ và $B$), sau đó đi tiếp trên đất liền từ $C$ đến $B$. Đặt khoảng cách $HC = x\text{ km}$ ($0 \le x \le 15$). Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Chi phí lắp đặt đoạn đường ống dưới biển $AC$ là $500\sqrt{x^2 + 81}$ (triệu đồng).</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Hàm tổng chi phí lắp đặt đường ống theo biến $x$ là $T(x) = 500\sqrt{x^2 + 81} + 300(15 - x)$ (triệu đồng).</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Để tổng chi phí lắp đặt thấp nhất, vị trí điểm nối $C$ phải cách $H$ một khoảng $x = 6,75\text{ km}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tổng chi phí lắp đặt thấp nhất của công ty vượt quá $8$ tỷ đồng (tức lớn hơn $8000$ triệu đồng).</div>
</div>

<div class="sec-title" style="margin-top: 14px;">PHẦN III. CÂU HỎI TRẮC NGHIỆM TRẢ LỜI NGẮN</div>
<div style="font-size: 9.5pt; font-style: italic; margin-bottom: 8px;">Thí sinh trả lời từ câu 1 đến câu 6.</div>

<div class="question">
  <span class="q-title">Câu 1:</span> Cho hàm số bậc ba $f(x) = x^3 - 3x$. Có bao nhiêu giá trị thực của $x$ thỏa mãn phương trình:
  $$f(f(x) - 1) = 2$$
</div>

<div class="question">
  <span class="q-title">Câu 2:</span> Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để hàm số $y = x^3 - 3mx^2 + 3(m^2 - 1)x + 2026$ đồng biến trên khoảng $(2; +\infty)$?
</div>

<div class="question">
  <span class="q-title">Câu 3:</span> Cho hàm số $f(x) = \left|x^3 - 3x^2 + m\right|$. Gọi $M$ là giá trị lớn nhất của hàm số $f(x)$ trên đoạn $[0; 3]$. Có bao nhiêu giá trị của tham số $m$ để $M = 5$?
</div>

<div class="question">
  <span class="q-title">Câu 4:</span> Cho hàm số $y = \dfrac{2x + 1}{x - 1}$ có đồ thị là $(C)$. Gọi $I$ là giao điểm của hai đường tiệm cận của đồ thị $(C)$. Tiếp tuyến bất kỳ của đồ thị $(C)$ cắt hai đường tiệm cận tại hai điểm phân biệt $A$ và $B$. Diện tích tam giác $IAB$ bằng bao nhiêu?
</div>

<div class="question">
  <span class="q-title">Câu 5:</span> Một bức tranh cao $3\text{ m}$ được treo trên một bức tường thẳng đứng sao cho mép dưới của bức tranh cách sàn nhà $2,6\text{ m}$. Một người quan sát có tầm mắt cách sàn nhà $1,6\text{ m}$. Hỏi người đó phải đứng cách bức tường bao nhiêu mét để góc nhìn bức tranh theo phương thẳng đứng (góc tạo bởi tia nhìn đến mép trên và tia nhìn đến mép dưới của bức tranh) là lớn nhất?
</div>

<div class="question">
  <span class="q-title">Câu 6:</span> Từ một tấm tôn hình vuông có độ dài cạnh bằng $60\text{ cm}$, người ta cắt bỏ bốn hình vuông bằng nhau ở bốn góc rồi gập các mép lại để tạo thành một chiếc hộp hình hộp chữ nhật không có nắp. Để thể tích của chiếc hộp đạt giá trị lớn nhất, cạnh của mỗi hình vuông bị cắt bỏ bằng bao nhiêu centimét?
</div>

<div class="page-break"></div>

<h1 class="main-title">Bảng đáp án & Hướng dẫn giải chi tiết</h1>
<div class="divider"></div>

<div class="sec-title">A. BẢNG ĐÁP ÁN</div>

<div style="font-weight: bold; margin-top: 6px;">PHẦN II. Trắc nghiệm Đúng / Sai</div>
<table class="ans-table">
  <tr>
    <th style="width: 35%;">Câu hỏi</th>
    <th style="width: 16%;">Lệnh a)</th>
    <th style="width: 16%;">Lệnh b)</th>
    <th style="width: 16%;">Lệnh c)</th>
    <th style="width: 16%;">Lệnh d)</th>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 1</strong> <i>(Hàm hợp $g(x) = f(x^2 - 2x)$)</i></td>
    <td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 2</strong> <i>(Hàm phân thức $y = \frac{x^2+mx-1}{x-1}$)</i></td>
    <td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 3</strong> <i>(Hàm trị tuyệt đối $g(x) = |f(x)|$)</i></td>
    <td class="bold-ans">ĐÚNG</td><td style="color:#2b6cb0; font-weight:bold;">SAI</td><td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td>
  </tr>
  <tr>
    <td style="text-align: left; padding-left: 8px;"><strong>Câu 4</strong> <i>(Chi phí đường ống dẫn dầu)</i></td>
    <td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td><td class="bold-ans">ĐÚNG</td>
  </tr>
</table>

<div style="font-weight: bold; margin-top: 10px;">PHẦN III. Trắc nghiệm trả lời ngắn</div>
<table class="ans-table">
  <tr>
    <th>Câu</th><th>Câu 1</th><th>Câu 2</th><th>Câu 3</th><th>Câu 4</th><th>Câu 5</th><th>Câu 6</th>
  </tr>
  <tr>
    <td><strong>Đáp số</strong></td>
    <td class="bold-ans">4</td>
    <td class="bold-ans">12</td>
    <td class="bold-ans">2</td>
    <td class="bold-ans">6</td>
    <td class="bold-ans">2</td>
    <td class="bold-ans">10</td>
  </tr>
</table>

<div class="sec-title" style="margin-top: 16px;">B. HƯỚNG DẪN GIẢI CHI TIẾT</div>

<div class="question">
  <span class="q-title">PHẦN II – Câu 1:</span>
  <div>$g(x) = f(x^2 - 2x)$.</div>
  <div>• <b>a) ĐÚNG:</b> $g'(x) = (x^2 - 2x)' f'(x^2 - 2x) = 2(x - 1)f'(x^2 - 2x)$.</div>
  <div>• <b>b) SAI:</b> $f'(u) = (u + 1)(u - 2)^2(u - 3) = 0 \Leftrightarrow u = -1$ (đơn), $u = 3$ (đơn), $u = 2$ (kép).<br>
  $g'(x) = 0 \Leftrightarrow 2(x - 1) = 0 \Leftrightarrow x = 1$ (bội 1).<br>
  $x^2 - 2x = -1 \Leftrightarrow (x - 1)^2 = 0 \implies x = 1$ (kết hợp cho nghiệm bội 3).<br>
  $x^2 - 2x = 3 \Leftrightarrow x = -1$ hoặc $x = 3$ (2 nghiệm đơn).<br>
  Vậy $g'(x)$ chỉ đổi dấu qua 3 nghiệm bội lẻ $\{-1; 1; 3\} \implies$ hàm số có đúng 3 điểm cực trị.</div>
  <div>• <b>c) ĐÚNG:</b> Khi $x > 3 \implies g'(x) > 0$. Qua các nghiệm lẻ, $g'(x)$ đan dấu: trên $(1; 3)$ có $g'(x) < 0$ nên hàm số nghịch biến.</div>
  <div>• <b>d) SAI:</b> $g'(x)$ đổi dấu từ $+$ sang $-$ khi qua $x = 1$ nên $x = 1$ là điểm cực đại.</div>
</div>

<div class="question">
  <span class="q-title">PHẦN II – Câu 2:</span>
  <div>• <b>a) SAI:</b> Khi $m = 0$, $y = \frac{x^2 - 1}{x - 1} = x + 1$ (với $x \ne 1$), đồ thị không có tiệm cận đứng.</div>
  <div>• <b>b) ĐÚNG:</b> Chia đa thức: $y = x + m + 1 + \frac{m}{x - 1} \implies$ TCX là $y = x + m + 1$ luôn có hệ số góc bằng $1$.</div>
  <div>• <b>c) ĐÚNG:</b> Khi $m = 1 \implies y' = \frac{x^2 - 2x}{(x - 1)^2} = 0 \Leftrightarrow x = 0 \implies A(0; 1)$, $x = 2 \implies B(2; 5)$. Khoảng cách $AB = \sqrt{2^2 + 4^2} = 2\sqrt{5}$.</div>
  <div>• <b>d) SAI:</b> Đồ thị có 2 cực trị $\Leftrightarrow m > 0$. Tung độ 2 cực trị là $y = 2x + m \implies y_1 y_2 = m^2 + 4 > 0, \forall m$. Hai điểm cực trị luôn nằm cùng phía so với $Ox$.</div>
</div>

<div class="question">
  <span class="q-title">PHẦN II – Câu 3:</span>
  <div>$f(x) = x^2(x - 2)^2 + a$.</div>
  <div>• <b>a) ĐÚNG:</b> $f'(x) = 4x(x - 1)(x - 2)$.</div>
  <div>• <b>b) SAI:</b> Các điểm cực trị của $f(x)$ là $x = 0, 1, 2$ với $f(0) = f(2) = a$, $f(1) = a + 1$. Khi $a = -1$, $f(x) = 0$ có nghiệm kép $x = 1$ và 2 nghiệm đơn $1 \pm \sqrt{2}$. Số cực trị của $|f(x)|$ là $3 + 2 = 5$.</div>
  <div>• <b>c) ĐÚNG:</b> Khi $a = 2$, $f(x) \ge 2 > 0, \forall x \implies \min |f(x)| = 2$.</div>
  <div>• <b>d) ĐÚNG:</b> Vì $\lim_{x \to \pm\infty} f(x) = +\infty$, nếu $a < 0$ thì $f(0) = a < 0 \implies$ luôn có ít nhất 2 nghiệm đơn $\implies$ số cực trị $\ge 5$. Do đó $g(x)$ có 3 cực trị $\Leftrightarrow a \ge 0$. Với $a \in [-5; 5]$, có 6 giá trị nguyên $\{0; 1; 2; 3; 4; 5\}$.</div>
</div>

<div class="question">
  <span class="q-title">PHẦN II – Câu 4:</span>
  <div>• <b>a) ĐÚNG:</b> $AC = \sqrt{9^2 + x^2} = \sqrt{x^2 + 81}\text{ km} \implies$ chi phí là $500\sqrt{x^2 + 81}$ triệu đồng.</div>
  <div>• <b>b) ĐÚNG:</b> $CB = 15 - x\text{ km} \implies$ tổng chi phí $T(x) = 500\sqrt{x^2 + 81} + 300(15 - x)$ triệu đồng.</div>
  <div>• <b>c) ĐÚNG:</b> $T'(x) = \frac{500x}{\sqrt{x^2 + 81}} - 300 = 0 \Leftrightarrow 5x = 3\sqrt{x^2 + 81} \Leftrightarrow 16x^2 = 729 \implies x = 6,75\text{ km}$.</div>
  <div>• <b>d) ĐÚNG:</b> $T_{\min} = T(6,75) = 500 \times 11,25 + 300 \times 8,25 = 8100\text{ triệu đồng} = 8,1\text{ tỷ đồng} > 8\text{ tỷ đồng}$.</div>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 1:</span> $f(t) = 2 \Leftrightarrow t^3 - 3t - 2 = 0 \Leftrightarrow (t - 2)(t + 1)^2 = 0 \Leftrightarrow t = 2$ hoặc $t = -1$.<br>
  $\implies f(x) - 1 = 2 \Leftrightarrow f(x) = 3$ (có 1 nghiệm vì $3 > y_{\text{CĐ}} = 2$).<br>
  $\implies f(x) - 1 = -1 \Leftrightarrow f(x) = 0$ (có 3 nghiệm phân biệt $0, \pm\sqrt{3}$).<br>
  Tổng số nghiệm thực là $1 + 3 = 4$. $\implies$ <b>Đáp số: 4</b>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 2:</span> $y' = 3(x - m - 1)(x - m + 1) \ge 0 \Leftrightarrow x \le m - 1$ hoặc $x \ge m + 1$.<br>
  Để đồng biến trên $(2; +\infty) \Leftrightarrow m + 1 \le 2 \Leftrightarrow m \le 1$.<br>
  Với $m \in [-10; 10], m \in \mathbb{Z} \implies m \in \{-10; -9; \dots; 1\}$ (gồm 12 giá trị). $\implies$ <b>Đáp số: 12</b>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 3:</span> Xét $u(x) = x^3 - 3x^2 + m$ trên $[0; 3]$. Ta có $u'(x) = 3x(x - 2) = 0 \Leftrightarrow x = 0, x = 2$.<br>
  $u(0) = u(3) = m$, $u(2) = m - 4$.<br>
  $\max_{[0; 3]} |u(x)| = \max(|m - 4|, |m|) = 5 \Leftrightarrow m = -1$ hoặc $m = 5$. Có đúng 2 giá trị. $\implies$ <b>Đáp số: 2</b>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 4:</span> Giao điểm hai tiệm cận $I(1; 2)$. Với điểm $M\left(x_0; 2 + \frac{3}{x_0 - 1}\right) \in (C)$, tiếp tuyến cắt TCĐ tại $A\left(1; 2 + \frac{6}{x_0 - 1}\right) \implies IA = \frac{6}{|x_0 - 1|}$ và cắt TCN tại $B(2x_0 - 1; 2) \implies IB = 2|x_0 - 1|$.<br>
  Diện tích tam giác vuông $IAB$: $S = \frac{1}{2} IA \cdot IB = \frac{1}{2} \cdot \frac{6}{|x_0 - 1|} \cdot 2|x_0 - 1| = 6$. $\implies$ <b>Đáp số: 6</b>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 5:</span> Chiều cao mép dưới so với mắt: $h_1 = 2,6 - 1,6 = 1\text{ m}$. Chiều cao mép trên so với mắt: $h_2 = 5,6 - 1,6 = 4\text{ m}$.<br>
  Góc nhìn $\alpha = \beta_2 - \beta_1 \implies \tan \alpha = \frac{\frac{4}{x} - \frac{1}{x}}{1 + \frac{4}{x^2}} = \frac{3}{x + \frac{4}{x}}$.<br>
  Góc $\alpha$ lớn nhất khi $x + \frac{4}{x}$ nhỏ nhất $\Leftrightarrow x = \sqrt{1 \times 4} = 2\text{ m}$. $\implies$ <b>Đáp số: 2</b>
</div>

<div class="question">
  <span class="q-title">PHẦN III – Câu 6:</span> Hộp có đáy vuông cạnh $60 - 2x\text{ cm}$, chiều cao $x\text{ cm}$ ($0 < x < 30$).<br>
  Thể tích $V(x) = x(60 - 2x)^2 = 4(x^3 - 60x^2 + 900x)$.<br>
  $V'(x) = 12(x^2 - 40x + 300) = 12(x - 10)(x - 30) = 0 \Leftrightarrow x = 10\text{ cm}$.<br>
  Thể tích đạt cực đại khi $x = 10\text{ cm}$. $\implies$ <b>Đáp số: 10</b>
</div>

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

with open("bai_tap_them.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved bai_tap_them.html. Compiling PDF...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=6000",
    "--print-to-pdf=Bai_Tap_Luyen_Them_Ham_So.pdf",
    "bai_tap_them.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)
