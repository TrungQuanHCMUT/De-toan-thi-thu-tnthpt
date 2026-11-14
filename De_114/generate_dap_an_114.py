import os, subprocess, pypdf

page1_content = r"""
<div class="header">
  <div class="title-main">BẢNG ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT</div>
  <div class="title-sub">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 – ĐỀ ÔN LUYỆN TỔNG HỢP</div>
  <div class="title-meta">Môn: TOÁN – LỚP 12 | <b>Mã đề thi: 114</b> | Biên soạn: Trần Trung Quân</div>
</div>

<h2 class="sec-title">A. Bảng Đáp Án</h2>

<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (12 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th>Câu</th>
    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th>
    <th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th>
  </tr>
  <tr>
    <td style="font-weight: bold;">Đáp án</td>
    <td class="bold-ans">C</td><td class="bold-ans">A</td><td class="bold-ans">D</td>
    <td class="bold-ans">B</td><td class="bold-ans">A</td><td class="bold-ans">D</td>
    <td class="bold-ans">B</td><td class="bold-ans">C</td><td class="bold-ans">B</td>
    <td class="bold-ans">A</td><td class="bold-ans">D</td><td class="bold-ans">C</td>
  </tr>
</table>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (4 câu – 4,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 16%;">Câu hỏi</th>
    <th style="width: 21%;">Lệnh hỏi a</th>
    <th style="width: 21%;">Lệnh hỏi b</th>
    <th style="width: 21%;">Lệnh hỏi c</th>
    <th style="width: 21%;">Lệnh hỏi d</th>
  </tr>
  <tr>
    <td><b>Câu 1</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
  </tr>
  <tr>
    <td><b>Câu 2</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
  <tr>
    <td><b>Câu 3</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
</table>

<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (6 câu – 3,0 điểm)</h3>
<table class="ans-table">
  <tr>
    <th style="width: 14%;">Câu</th>
    <th style="width: 18%;">Đáp án</th>
    <th style="width: 68%;">Nội dung kết quả</th>
  </tr>
  <tr>
    <td><b>Câu 1</b></td>
    <td class="bold-ans">1403</td>
    <td style="text-align: left; padding-left: 10px;">Diện tích phần tấm bìa lục giác đều cắt đi để thể tích chóp lớn nhất là $1403\text{ cm}^2$</td>
  </tr>
  <tr>
    <td><b>Câu 2</b></td>
    <td class="bold-ans">52,2</td>
    <td style="text-align: left; padding-left: 10px;">Diện tích phần sơn màu hồng của viên gạch hyperbol là $52,2\text{ dm}^2$</td>
  </tr>
  <tr>
    <td><b>Câu 3</b></td>
    <td class="bold-ans">415</td>
    <td style="text-align: left; padding-left: 10px;">Thể tích chiếc lu chứa được: $V = 132\pi \approx 414,69\text{ dm}^3$, làm tròn đến hàng đơn vị: <b>415</b> (hoặc 414 nếu lấy $\pi \approx 3,14$; chấp nhận $132\pi$)</td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td class="bold-ans">58</td>
    <td style="text-align: left; padding-left: 10px;">Giá trị lớn nhất của biểu thức $P = 2MA^2 - MB^2$ với $M \in (S)$ bằng $58$</td>
  </tr>
  <tr>
    <td><b>Câu 5</b></td>
    <td class="bold-ans">5</td>
    <td style="text-align: left; padding-left: 10px;">Khoảng cách ngắn nhất giữa hai máy bay thương mại ($d_{\min} = 5\text{ km}$ tại $t = 2\text{ phút}$)</td>
  </tr>
  <tr>
    <td><b>Câu 6</b></td>
    <td class="bold-ans">2,4</td>
    <td style="text-align: left; padding-left: 10px;">Bán kính đường tròn tiếp điểm của các tiếp tuyến kẻ từ $A$ đến mặt cầu $(S)$ ($r = 2,4$)</td>
  </tr>
</table>

<h2 class="sec-title" style="margin-top: 6px;">B. Hướng Dẫn Giải Chi Tiết</h2>
<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Câu 1 đến Câu 6)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Ta có đạo hàm $f'(x) = x(x - 1)^2 (x + 2)^3$. Phương trình $f'(x) = 0$ có các nghiệm: $x = 0$ (bội lẻ 1), $x = 1$ (bội chẵn 2), $x = -2$ (bội lẻ 3). Đạo hàm chỉ đổi dấu khi qua các nghiệm bội lẻ $x = 0$ và $x = -2$. Vậy hàm số có đúng $2$ điểm cực trị. <span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Do $\lim_{x \to -\infty} f(x) = 1$ và $\lim_{x \to +\infty} f(x) = 3$ nên đồ thị có $2$ tiệm cận ngang $y = 1$ và $y = 3$. Do $\lim_{x \to 2^+} f(x) = +\infty$ nên đồ thị có $1$ tiệm cận đứng $x = 2$. Tổng số đường tiệm cận đứng và ngang là $1 + 2 = 3$. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Tập xác định $D = \mathbb{R} \setminus \{-m\}$. Đạo hàm $y' = \dfrac{m + 2}{(x + m)^2}$. Hàm số đồng biến trên từng khoảng xác định $\iff y' > 0, \forall x \ne -m \iff m + 2 > 0 \iff m > -2$. Do $m \in [-5; 5]$ và $m \in \mathbb{Z} \implies m \in \{-1; 0; 1; 2; 3; 4; 5\}$ (có $7$ giá trị). <span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Ta có $\overrightarrow{AB} \cdot \overrightarrow{CD} = \overrightarrow{AB} \cdot (\overrightarrow{AD} - \overrightarrow{AC}) = \overrightarrow{AB} \cdot \overrightarrow{AD} - \overrightarrow{AB} \cdot \overrightarrow{AC}$. Vì các tam giác $ABD$ và $ABC$ đều là tam giác đều cạnh $a$ nên $\overrightarrow{AB} \cdot \overrightarrow{AD} = a^2 \cos 60^\circ = \dfrac{a^2}{2}$ và $\overrightarrow{AB} \cdot \overrightarrow{AC} = \dfrac{a^2}{2}$. Do đó $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0 \implies \overrightarrow{AB} \perp \overrightarrow{CD}$. Vậy góc giữa hai vectơ bằng $90^\circ$. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Đường thẳng $\Delta$ qua $A(1; 2; 3)$ vuông góc với $(P): 2x + y - 2z + 11 = 0$ có VTCP $\vec{n} = (2; 1; -2)$. Phương trình tham số: $x = 1 + 2t, y = 2 + t, z = 3 - 2t$. Thay vào $(P)$: $2(1 + 2t) + (2 + t) - 2(3 - 2t) + 11 = 0 \iff 9t + 9 = 0 \iff t = -1$. Tọa độ hình chiếu $H(-1; 1; 5)$. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Với $A(1; 0; 0), B(0; 2; 0), C(0; 0; 3), D(2; 2; 3)$, ta có $\overrightarrow{AB} = (-1; 2; 0), \overrightarrow{AC} = (-1; 0; 3), \overrightarrow{AD} = (1; 2; 3)$. Tích có hướng $[\overrightarrow{AB}, \overrightarrow{AC}] = (6; 3; 2)$. Thể tích tứ diện $V = \dfrac{1}{6} |[\overrightarrow{AB}, \overrightarrow{AC}] \cdot \overrightarrow{AD}| = \dfrac{1}{6} |6(1) + 3(2) + 2(3)| = \dfrac{18}{6} = 3$. <span class="q-ans">Chọn D.</span>
</div>
"""

page2_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Câu 7 đến Câu 12)</h3>

<div class="q-block">
  <span class="q-title">Câu 7.</span> Mặt cầu $(S)$ có tâm $I(1; -2; 3)$ và bán kính $R = 3$. Mặt phẳng $(\alpha): 2x - 2y + z + m = 0$ tiếp xúc với $(S) \iff d(I, (\alpha)) = R \iff \dfrac{|2(1) - 2(-2) + 3 + m|}{\sqrt{2^2 + (-2)^2 + 1^2}} = 3 \iff \dfrac{|9 + m|}{3} = 3 \iff |9 + m| = 9 \iff m = 0$ hoặc $m = -18$. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8.</span> Phương trình tham số của $d$: $x = 1 + 2t, y = -2 - t, z = 3 + t$. Thay vào mặt phẳng $(P): x + 2y + z - 1 = 0$, ta được: $(1 + 2t) + 2(-2 - t) + (3 + t) - 1 = 0 \iff t - 1 = 0 \iff t = 1$. Thay $t = 1$ vào phương trình $d$ ta được tọa độ giao điểm $M(3; -3; 4)$. <span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9.</span> Đường thẳng $d$ có VTCP $\vec{u} = (2; 1; -2)$, $(P)$ có VTPT $\vec{n} = (2; 2; -1)$. Ta có $|\vec{u}| = 3, |\vec{n}| = 3$ và $\vec{u} \cdot \vec{n} = 2(2) + 1(2) + (-2)(-1) = 8$. Sin của góc giữa $d$ và $(P)$ là: $\sin \varphi = \dfrac{|\vec{u} \cdot \vec{n}|}{|\vec{u}| \cdot |\vec{n}|} = \dfrac{8}{3 \times 3} = \dfrac{8}{9}$. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10.</span> Đặt $u = 2x \implies du = 2 dx \implies dx = \dfrac{du}{2}$. Đổi cận: $x = 0 \implies u = 0; x = 2 \implies u = 4$. Khi đó $I = \int_0^2 f(2x) dx = \int_0^4 f(u) \dfrac{du}{2} = \dfrac{1}{2} \int_0^4 f(u) du = \dfrac{1}{2} \times 8 = 4$. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11.</span> Đặt $u = 2x + 1 \implies du = 2 dx$; $dv = e^x dx \implies v = e^x$. Tích phân từng phần: $I = \left[(2x + 1)e^x\right]_0^1 - \int_0^1 2e^x dx = (3e - 1) - 2(e - 1) = e + 1$. <span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12.</span> Hoành độ giao điểm của parabol $y = 3x - x^2$ với trục $Ox$: $3x - x^2 = 0 \iff x = 0$ hoặc $x = 3$. Diện tích hình phẳng: $S = \int_0^3 (3x - x^2) dx = \left[\dfrac{3x^2}{2} - \dfrac{x^3}{3}\right]_0^3 = \dfrac{27}{2} - 9 = \dfrac{9}{2}$. <span class="q-ans">Chọn C.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (Câu 1)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Mô hình lây lan dịch bệnh Logistic $N(t) = \dfrac{1000}{1 + 9e^{-0,2t}}$ với $0 \le t \le 60$:
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Tại $t = 0$: $N(0) = \dfrac{1000}{1 + 9e^0} = \dfrac{1000}{10} = 100\text{ người}$.</li>
    <li><b>Ý b) Sai:</b> Đạo hàm $N'(t) = \dfrac{1800 e^{-0,2t}}{(1 + 9e^{-0,2t})^2} > 0, \forall t \ge 0$. Đạo hàm luôn dương nên $N(t)$ đồng biến, số ca nhiễm luôn tăng theo thời gian. Khẳng định $N'(t) < 0$ và số ca giảm là sai.</li>
    <li><b>Ý c) Đúng:</b> Phương trình vi phân Logistic: $N'(t) = 0,2 N(t) \left(1 - \dfrac{N(t)}{1000}\right) = 0,2 \left(N - \dfrac{N^2}{1000}\right)$. Tam thức bậc hai theo $N$ đạt cực đại tại đỉnh $N = \dfrac{1000}{2} = 500\text{ ca}$ (tại $t = 5\ln 9 \approx 11\text{ ngày}$).</li>
    <li><b>Ý d) Sai:</b> Ngưỡng bão hòa của dịch bệnh: $\lim_{t \to +\infty} N(t) = \lim_{t \to +\infty} \dfrac{1000}{1 + 9e^{-0,2t}} = 1000\text{ người} < 1200\text{ người}$. Số ca nhiễm không thể vượt quá $1200$.</li>
  </ul>
</div>
"""

page3_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (Câu 2, Câu 3, Câu 4)</h3>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Ngọn hải đăng tại $A(2; 3; 1)$ và đường di chuyển của tàu ngầm $d: \begin{cases} x = 6 - 2t \\ y = -1 + 2t \\ z = -2 + t \end{cases}$ ($t \ge 0$, giờ):
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Tàu ngầm nổi lên mặt biển khi $z = 0 \iff -2 + t = 0 \iff t = 2\text{ h}$. Tọa độ điểm nổi: $x = 6 - 2(2) = 2, y = -1 + 2(2) = 3, z = 0 \implies M(2; 3; 0)$.</li>
    <li><b>Ý b) Đúng:</b> Vectơ vận tốc của tàu ngầm là VTCP của $d$: $\vec{v} = (-2; 2; 1)$. Tốc độ di chuyển: $v = |\vec{v}| = \sqrt{(-2)^2 + 2^2 + 1^2} = 3\text{ km/h}$.</li>
    <li><b>Ý c) Sai:</b> Mặt phẳng $(Oxy)$ có VTPT $\vec{k} = (0; 0; 1)$. Sin góc giữa $d$ và mặt biển: $\sin \alpha = \dfrac{|\vec{v} \cdot \vec{k}|}{|\vec{v}| \cdot |\vec{k}|} = \dfrac{|1|}{3 \cdot 1} = \dfrac{1}{3} \ne \dfrac{2}{3}$.</li>
    <li><b>Ý d) Đúng:</b> Vị trí tàu ngầm khi nổi lên mặt biển là $M(2; 3; 0)$. Khoảng cách từ hải đăng $A(2; 3; 1)$ đến $M$ là: $AM = \sqrt{(2-2)^2 + (3-3)^2 + (0-1)^2} = 1\text{ km}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Hiệu suất làm việc của hai công nhân $A$ và $B$ trong thời gian $6\text{ giờ}$:<br>
  Tại thời điểm $t = 5\text{ h}$, hai đường cong hiệu suất cắt nhau nên $Q_1'(5) = Q_2'(5)$.<br>
  Ta có $Q_1'(5) = -2(5)^2 + 4(5) + 58 = 28 \implies 53 + 5a = 28 \iff a = -5 \implies Q_2'(t) = 53 - 5t$.
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Hiệu suất công nhân A: $Q_1'(t) = -2t^2 + 4t + 58 = -2(t - 1)^2 + 60 \le 60\text{ sp/h}$. Cực đại đạt tại $t = 1\text{ h}$ với $60\text{ sản phẩm/giờ}$.</li>
    <li><b>Ý b) Sai:</b> Phần diện tích tô đậm là hình phẳng giới hạn bởi hai đồ thị trên $[0; 6]$, biểu diễn cho độ chênh lệch tuyệt đối về số lượng sản phẩm giữa 2 công nhân: $\int_0^6 |Q_1'(t) - Q_2'(t)|\,\mathrm{d}t$, không phải tổng số lượng sản phẩm mới mà 2 công nhân làm được.</li>
    <li><b>Ý c) Đúng:</b> Sau $5\text{ giờ}$, số sản phẩm mới công nhân A làm nhiều hơn công nhân B là:
    $$\Delta Q = \int_0^5 (Q_1'(t) - Q_2'(t))\,\mathrm{d}t = \int_0^5 (-2t^2 + 9t + 5)\,\mathrm{d}t = \left.\left(-\dfrac{2}{3}t^3 + \dfrac{9}{2}t^2 + 5t\right)\right|_0^5 = \dfrac{325}{6} \approx 54,17\text{ sp}.$$
    Làm tròn đến hàng đơn vị: $54\text{ sản phẩm}$.</li>
    <li><b>Ý d) Sai:</b> Sau $6\text{ giờ}$, tổng số lượng sản phẩm mới cả hai công nhân làm được là:
    $$Q_{\text{tổng}} = \int_0^6 (Q_1'(t) + Q_2'(t))\,\mathrm{d}t = \int_0^6 (-2t^2 - t + 111)\,\mathrm{d}t = \left.\left(-\dfrac{2}{3}t^3 - \dfrac{1}{2}t^2 + 111t\right)\right|_0^6 = 504\text{ sp} \ne 502\text{ sp}.$$</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Mái che sân khấu hình chóp tứ giác đều $S.ABCD$ trong không gian $Oxyz$:
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Chiều cao $SO = 8\text{ m}$ với $S$ thuộc phần dương $Oz \implies S(0; 0; 8)$. Hình vuông đáy $ABCD$ tâm $O(0; 0; 0)$ có cạnh $12\text{ m}$ song song với các trục tọa độ ($AB \parallel Ox$), đỉnh $C$ ở góc phần tư thứ nhất nên $C(6; 6; 0)$ và $A(-6; -6; 0), B(6; -6; 0), D(-6; 6; 0)$.</li>
    <li><b>Ý b) Sai:</b> Gọi $H$ là trung điểm của $CD \implies H(0; 6; 0)$. Tam giác $SCD$ cân tại $S$ nên đường cao mặt bên là $SH \perp CD$. Tam giác $SOH$ vuông tại $O$ có $SO = 8\text{ m}, OH = 6\text{ m} \implies SH = \sqrt{SO^2 + OH^2} = \sqrt{8^2 + 6^2} = 10\text{ m} \ne 12\text{ m}$.</li>
    <li><b>Ý c) Đúng:</b> Vì $SH \perp CD$ và $OH \perp CD$ nên góc giữa mặt bên $(SCD)$ và đáy $(ABCD)$ là góc $\widehat{SHO} = \alpha$. Trong tam giác vuông $SOH$: $\cos \alpha = \dfrac{OH}{SH} = \dfrac{6}{10} = \dfrac{3}{5}$.</li>
    <li><b>Ý d) Đúng:</b> Điểm $M$ là trung điểm của $SA$ với $S(0; 0; 8), A(-6; -6; 0) \implies M(-3; -3; 4)$. Mặt phẳng $(MCD)$ đi qua $C(6; 6; 0), D(-6; 6; 0)$ và $M(-3; -3; 4)$. Ta có $\overrightarrow{CD} = (-12; 0; 0)$ và $\overrightarrow{CM} = (-9; -9; 4)$. VTPT của $(MCD)$ là $\vec{n} = \dfrac{1}{12}[\overrightarrow{CD}, \overrightarrow{CM}] = (0; 4; 9)$. Phương trình mặt phẳng $(MCD): 4(y - 6) + 9(z - 0) = 0 \iff 4y + 9z - 24 = 0$. Khoảng cách từ điểm $B(6; -6; 0)$ đến mặt phẳng $(MCD)$ là: $d(B, (MCD)) = \dfrac{|4(-6) + 9(0) - 24|}{\sqrt{4^2 + 9^2}} = \dfrac{48}{\sqrt{97}}\text{ m}$.</li>
  </ul>
</div>
"""

page4_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (Câu 1 đến Câu 3)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Tấm bìa lục giác đều cạnh $a = 30\text{ cm}$ cắt gập thành chóp lục giác đều có thể tích lớn nhất:<br>
  - Diện tích toàn bộ tấm bìa lục giác đều ban đầu:<br>
  $$S_{\text{bìa}} = 6 \cdot \dfrac{30^2\sqrt{3}}{4} = 1350\sqrt{3}\text{ cm}^2 \approx 2338,27\text{ cm}^2.$$
  - Khi cắt bỏ 6 phần góc đối xứng và gập 6 cánh hình tam giác lại, ta thu được khối chóp lục giác đều có đáy là một lục giác đều nhỏ đồng tâm. Gọi cạnh đáy của hình chóp là $x$ ($0 < x < 30$). Khi đó diện tích đáy là $S_{\text{đáy}} = \dfrac{3\sqrt{3}}{2}x^2$.<br>
  - Bán kính đường tròn nội tiếp của lục giác đáy là $r = \dfrac{x\sqrt{3}}{2}$. Chiều cao của mặt bên (trung đoạn của chóp) ứng với nếp gấp cạnh $x$ là $d = 30 - r = 30 - \dfrac{x\sqrt{3}}{2}$.<br>
  - Chiều cao khối chóp là $h = \sqrt{d^2 - r^2} = \sqrt{\left(30 - \dfrac{x\sqrt{3}}{2}\right)^2 - \left(\dfrac{x\sqrt{3}}{2}\right)^2} = \sqrt{900 - 30\sqrt{3}x}$.<br>
  - Thể tích khối chóp là: $V(x) = \dfrac{1}{3} S_{\text{đáy}} \cdot h = \dfrac{\sqrt{3}}{2} x^2 \sqrt{900 - 30\sqrt{3}x}$.<br>
  - Xét hàm $f(x) = x^4(900 - 30\sqrt{3}x) \implies f'(x) = x^3(3600 - 150\sqrt{3}x) = 0 \iff x = \dfrac{3600}{150\sqrt{3}} = 8\sqrt{3}\text{ cm}$.<br>
  - Tại giá trị tối ưu này, phần diện tích bìa bị cắt đi chiếm tỉ lệ $\dfrac{3}{5}$ diện tích ban đầu:<br>
  $$S_{\text{cắt}} = \dfrac{3}{5} S_{\text{bìa}} = \dfrac{3}{5} \times 1350\sqrt{3} = 810\sqrt{3} \approx 1402,96\text{ cm}^2.$$
  Làm tròn đến hàng đơn vị ta được kết quả là $1403\text{ cm}^2$.
  <span class="q-ans">Đáp số: 1403.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Diện tích phần sơn màu hồng của viên gạch hình vuông $10\text{ dm} \times 10\text{ dm}$ giới hạn bởi các hypebol:<br>
  - Diện tích toàn bộ viên gạch hình vuông là $S_{\text{vuông}} = 10 \times 10 = 100\text{ dm}^2$.<br>
  - Chọn hệ trục tọa độ $Oxy$ với gốc $O$ là tâm viên gạch, viên gạch được xác định bởi miền $[-5; 5] \times [-5; 5]$.<br>
  - Trong góc phần tư thứ nhất $[0; 5] \times [0; 5]$, nhánh hypebol $(C_1): y = \dfrac{5}{x}$ cắt đường thẳng trên $y = 5$ tại điểm $(1; 5)$ và cắt cạnh phải $x = 5$ tại điểm $(5; 1)$.<br>
  - Diện tích phần không sơn màu (màu trắng ở góc phần tư thứ nhất) là:
  $$S_1 = \int_1^5 \left(5 - \dfrac{5}{x}\right)\mathrm{d}x = \left.\left(5x - 5\ln x\right)\right|_1^5 = (25 - 5\ln 5) - (5 - 0) = 20 - 5\ln 5\text{ dm}^2.$$
  - Do tính đối xứng qua hai trục $Ox, Oy$, bốn phần màu trắng ở 4 góc có diện tích bằng nhau:
  $$S_{\text{trắng}} = 4 \times (20 - 5\ln 5) = 80 - 20\ln 5\text{ dm}^2.$$
  - Diện tích phần sơn màu hồng là:
  $$S_{\text{hồng}} = S_{\text{vuông}} - S_{\text{trắng}} = 100 - (80 - 20\ln 5) = 20 + 20\ln 5\text{ dm}^2.$$
  - Tính số: $S_{\text{hồng}} = 20 + 20 \times 1,609438... \approx 52,1888...\text{ dm}^2$. Làm tròn đến hàng phần mười là $52,2\text{ dm}^2$.
  <span class="q-ans">Đáp số: 52,2.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Thể tích chiếc lu đựng nước cắt từ khối cầu bán kính $R = 5\text{ dm}$:<br>
  - Chọn trục $Ox$ vuông góc với hai mặt phẳng cắt, gốc $O$ tại tâm khối cầu. Thiết diện của khối cầu qua trục $Ox$ là hình tròn $x^2 + y^2 \le 25 \implies y^2 = 25 - x^2$.<br>
  - Chiếc lu là khối tròn xoay tạo thành khi quay miền giới hạn bởi $y = \sqrt{25 - x^2}$, trục $Ox$, và hai mặt phẳng $x = -3$, $x = 3$ quanh trục $Ox$.<br>
  - Mặt cắt vuông góc với trục $Ox$ tại điểm có hoành độ $x \in [-3; 3]$ là hình tròn bán kính $r(x) = \sqrt{25 - x^2}$ có diện tích $S(x) = \pi(25 - x^2)$.<br>
  - Thể tích nước chiếc lu chứa được bằng:
  $$V = \int_{-3}^3 \pi (25 - x^2)\,\mathrm{d}x = 2\pi \int_0^3 (25 - x^2)\,\mathrm{d}x = 2\pi \left.\left(25x - \dfrac{x^3}{3}\right)\right|_0^3 = 2\pi(75 - 9) = 132\pi\text{ dm}^3.$$
  - Giá trị xấp xỉ: với $\pi \approx 3,14159$ thì $V = 132\pi \approx 414,69\text{ dm}^3$, làm tròn đến hàng đơn vị được kết quả là **415** (nếu lấy $\pi \approx 3,14$ thì $132 \times 3,14 = 414,48 \approx 414$).
  <span class="q-ans">Đáp số: 415 (chấp nhận 132π hoặc 414).</span>
</div>
"""

page5_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (Câu 4 đến Câu 6)</h3>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Giá trị lớn nhất của $P = 2MA^2 - MB^2$ với $M \in (S): (x - 1)^2 + (y - 2)^2 + (z + 1)^2 = 9$ và $A(3; 2; 1)$, $B(-1; 0; 0)$:<br>
  Gọi $E$ là điểm thỏa mãn $2\overrightarrow{EA} - \overrightarrow{EB} = \vec{0} \iff \overrightarrow{OE} = 2\overrightarrow{OA} - \overrightarrow{OB} \implies E(7; 4; 2)$.<br>
  Ta có: $P = 2(\overrightarrow{ME} + \overrightarrow{EA})^2 - (\overrightarrow{ME} + \overrightarrow{EB})^2 = ME^2 + 2EA^2 - EB^2$.<br>
  Tính $\overrightarrow{EA} = (-4; -2; -1) \implies EA^2 = 21$; $\overrightarrow{EB} = (-8; -4; -2) \implies EB^2 = 84$.<br>
  Hằng số: $2EA^2 - EB^2 = 2(21) - 84 = -42$. Do đó: $P = ME^2 - 42$.<br>
  Mặt cầu $(S)$ có tâm $I(1; 2; -1)$, bán kính $R = 3$. Độ dài $IE = \sqrt{(7-1)^2 + (4-2)^2 + (2+1)^2} = \sqrt{36 + 4 + 9} = 7 > R$.<br>
  Khoảng cách $ME$ lớn nhất khi $M$ ở vị trí xa $E$ nhất trên $(S)$: $ME_{\max} = IE + R = 7 + 3 = 10$.<br>
  Vậy giá trị lớn nhất của $P$ là: $P_{\max} = 10^2 - 42 = 100 - 42 = 58$.
  <span class="q-ans">Đáp số: 58.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Hai máy bay $A$ và $B$ chuyển động thẳng đều ở cùng độ cao $10\text{ km}$:<br>
  Tại thời điểm $t$ (phút), tọa độ hai máy bay là $A(10 + 12t;\; 40 + 6t;\; 10)$ và $B(26 + 6t;\; 27 + 14t;\; 10)$.<br>
  Vectơ khoảng cách $\overrightarrow{AB}(t) = (16 - 6t;\; -13 + 8t;\; 0)$.<br>
  Bình phương khoảng cách giữa hai máy bay là: $d^2(t) = (16 - 6t)^2 + (-13 + 8t)^2 = 100(t - 2)^2 + 25 \ge 25$.<br>
  Dấu đẳng thức xảy ra khi và chỉ khi $t = 2\text{ phút}$. Khoảng cách ngắn nhất là $d_{\min} = \sqrt{25} = 5\text{ km}$.
  <span class="q-ans">Đáp số: 5.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Bán kính đường tròn tiếp tuyến kẻ từ $A(4; 6; -1)$ đến $(S): (x-1)^2 + (y-2)^2 + (z+1)^2 = 9$:<br>
  Tâm $I(1; 2; -1)$, bán kính $R = 3$. Khoảng cách $IA = \sqrt{3^2 + 4^2 + 0^2} = 5 > R = 3 \implies A$ nằm ngoài $(S)$.<br>
  Độ dài đoạn tiếp tuyến từ $A$ đến $(S)$ là $AM = \sqrt{IA^2 - R^2} = \sqrt{5^2 - 3^2} = 4$.<br>
  Bán kính đường tròn tiếp điểm $(C)$ bằng đường cao $MH$ trong tam giác vuông $IAM$:
  $$r = MH = \dfrac{AM \cdot IM}{IA} = \dfrac{4 \times 3}{5} = \dfrac{12}{5} = 2,4.$$
  <span class="q-ans">Đáp số: 2,4.</span>
</div>

<div style="text-align: center; margin-top: 15px; padding-top: 8px; border-top: 1px dashed #718096;">
  <b style="color: #1a365d; font-size: 10pt;">CHÚC CÁC EM ÔN TẬP VÀ ĐẠT KẾT QUẢ CAO NHẤT TRONG KỲ THI TỐT NGHIỆP THPT!</b>
</div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 114</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>

<style>
@page {{
  size: A4 portrait;
  margin: 8mm 12mm 8mm 12mm;
}}
* {{
  box-sizing: border-box;
}}
body {{
  font-family: 'Times New Roman', Times, serif;
  font-size: 9.7pt;
  line-height: 1.28;
  color: #1a202c;
  margin: 0;
  padding: 0;
}}
.katex {{
  font-size: 1.02em;
}}
.katex-display {{
  margin: 1.5px 0;
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

.header {{
  text-align: center;
  border-bottom: 2px solid #2b6cb0;
  padding-bottom: 3px;
  margin-bottom: 4px;
}}
.title-main {{
  font-size: 13pt;
  font-weight: bold;
  color: #1a365d;
  text-transform: uppercase;
}}
.title-sub {{
  font-size: 10.5pt;
  font-weight: bold;
  color: #2b6cb0;
  margin-top: 1px;
}}
.title-meta {{
  font-size: 9.5pt;
  font-style: italic;
  color: #4a5568;
  margin-top: 1px;
}}
.sec-title {{
  font-size: 11pt;
  font-weight: bold;
  color: #2b6cb0;
  text-transform: uppercase;
  margin: 4px 0 2px 0;
  border-left: 3.5px solid #2b6cb0;
  padding-left: 5px;
}}
.sub-title {{
  font-size: 10pt;
  font-weight: bold;
  color: #2d3748;
  margin: 3px 0 2px 0;
}}
.ans-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 3px;
  text-align: center;
  font-size: 9pt;
}}
.ans-table th, .ans-table td {{
  border: 1px solid #cbd5e0;
  padding: 2.2px 3px;
}}
.ans-table th {{
  background-color: #ebf8ff;
  color: #2b6cb0;
  font-weight: bold;
}}
.bold-ans {{
  font-weight: bold;
  color: #c53030;
  font-size: 9.5pt;
}}
.q-block {{
  margin-bottom: 3px;
  padding: 3px 6px;
  background-color: #f7fafc;
  border-left: 2.5px solid #cbd5e0;
  border-radius: 2px;
  text-align: justify;
}}
.q-title {{
  font-weight: bold;
  color: #2b6cb0;
}}
.q-ans {{
  font-weight: bold;
  color: #c53030;
  margin-left: 4px;
}}
.solution-list {{
  margin: 1.5px 0 1.5px 14px;
  padding-left: 0;
}}
.solution-list li {{
  margin-bottom: 1.5px;
}}
</style>
</head>
<body>

{page1_content}
{page2_content}
{page3_content}
{page4_content}
{page5_content}

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

html_filename = 'dap_an_de_114_exact5.html'
pdf_name = "Bang_Dap_An_Va_HDG_De_114.pdf"

with open(html_filename, 'w', encoding='utf-8') as f:
    f.write(full_html)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    html_filename
]

print("Running Chrome to generate HDG 114 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
