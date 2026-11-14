import os, subprocess, pypdf

page1_content = r"""
<div class="header">
  <div class="title-main">BẢNG ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT</div>
  <div class="title-sub">KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 – ĐỀ ÔN LUYỆN TỔNG HỢP</div>
  <div class="title-meta">Môn: TOÁN – LỚP 12 | <b>Mã đề thi: 115</b> | Biên soạn: Trần Trung Quân</div>
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
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td><b style="color: #276749;">Đúng</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
    <td><b style="color: #c53030;">Sai</b></td>
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
    <td class="bold-ans">6,6</td>
    <td style="text-align: left; padding-left: 10px;">Độ dài ngắn nhất của sợi dây quấn quanh cây thông nón ($AM \approx 6,6\text{ m}$)</td>
  </tr>
  <tr>
    <td><b>Câu 2</b></td>
    <td class="bold-ans">340</td>
    <td style="text-align: left; padding-left: 10px;">Thể tích tối đa của thùng rượu gỗ sồi hình tròn xoay parabol ($V = \frac{324800\pi}{3}\text{ cm}^3 \approx 340,1\text{ lít}$)</td>
  </tr>
  <tr>
    <td><b>Câu 3</b></td>
    <td class="bold-ans">6</td>
    <td style="text-align: left; padding-left: 10px;">Khoảng cách ngắn nhất giữa tuyến cáp treo và đường dây điện cao thế ($d(d_1, d_2) = 6\text{ m}$)</td>
  </tr>
  <tr>
    <td><b>Câu 4</b></td>
    <td class="bold-ans">39</td>
    <td style="text-align: left; padding-left: 10px;">Giá trị nhỏ nhất của biểu thức $T = MA^2 + MB^2 + MC^2$ với $M \in (P)$ bằng $39$</td>
  </tr>
  <tr>
    <td><b>Câu 5</b></td>
    <td class="bold-ans">3</td>
    <td style="text-align: left; padding-left: 10px;">Giá trị của biểu thức $T = a - b + c$ với $a = 4, b = 3, c = 2$ ($T = 3$)</td>
  </tr>
  <tr>
    <td><b>Câu 6</b></td>
    <td class="bold-ans">90</td>
    <td style="text-align: left; padding-left: 10px;">Góc giữa hai vectơ $\overrightarrow{AM}$ và $\overrightarrow{BN}$ trong hình chóp $S.ABCD$ đáy hình thoi ($\overrightarrow{AM} \perp \overrightarrow{BN} \implies 90^\circ$)</td>
  </tr>
</table>

<h2 class="sec-title" style="margin-top: 6px;">B. Hướng Dẫn Giải Chi Tiết</h2>
<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Câu 1 đến Câu 6)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Ta có $y = \dfrac{2x^2 - 3x + 5}{x - 1} = 2x - 1 + \dfrac{4}{x - 1}$. Do $\lim_{x \to \pm \infty} \left[ y - (2x - 1) \right] = 0$ nên tiệm cận xiên là $y = 2x - 1$. Hệ số $a = 2, b = -1 \implies a + b = 1$. <span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Chi phí trung bình $\bar{C}(x) = \dfrac{C(x)}{x} = x + 40 + \dfrac{1600}{x}$ ($x > 0$). Đạo hàm $\bar{C}'(x) = 1 - \dfrac{1600}{x^2} = 0 \iff x = 40$. Hàm số đạt giá trị nhỏ nhất tại $x = 40$ tấn. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Ta có $y = \dfrac{x^2 - 2x + 3}{x + 1} = x - 3 + \dfrac{6}{x + 1}$. Tiệm cận đứng $x = -1$, tiệm cận xiên $y = x - 3$. Giao điểm của hai đường tiệm cận là tâm đối xứng $I(-1; -4)$. <span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Hợp lực $|\overrightarrow{F_1} + \overrightarrow{F_2}|^2 = 10^2 + 10^2 + 2(10)(10)\cos 120^\circ = 100 \implies |\overrightarrow{F_1} + \overrightarrow{F_2}| = 10\text{ N}$. Để chất điểm cân bằng: $\overrightarrow{F_3} = -(\overrightarrow{F_1} + \overrightarrow{F_2}) \implies |\overrightarrow{F_3}| = 10\text{ N}$. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Vectơ $\overrightarrow{AB} = (-1; 2; 0), \overrightarrow{AC} = (-1; 0; 4) \implies [\overrightarrow{AB}, \overrightarrow{AC}] = (8; 4; 2)$. Diện tích tam giác: $S = \dfrac{1}{2}\sqrt{8^2 + 4^2 + 2^2} = \dfrac{\sqrt{84}}{2} = \sqrt{21}$. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Bán kính mặt cầu có tâm $I(2; -1; 3)$ tiếp xúc với trục $Oz$: $R = d(I, Oz) = \sqrt{x_I^2 + y_I^2} = \sqrt{2^2 + (-1)^2} = \sqrt{5} \implies R^2 = 5$. Phương trình mặt cầu là: $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 5$. <span class="q-ans">Chọn D.</span>
</div>
"""

page2_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Câu 7 đến Câu 12)</h3>

<div class="q-block">
  <span class="q-title">Câu 7.</span> Đường thẳng $d_1$ qua $M_1(1; -1; 2)$ có VTCP $\vec{u}_1 = (2; 1; -1)$; $d_2$ qua $M_2(-1; 2; -1)$ có VTCP $\vec{u}_2 = (1; 2; 1)$. Tích có hướng $[\vec{u}_1, \vec{u}_2] = (3; -3; 3) \ne \vec{0}$. Vectơ $\overrightarrow{M_1M_2} = (-2; 3; -3)$. Tích hỗn tạp $[\vec{u}_1, \vec{u}_2] \cdot \overrightarrow{M_1M_2} = 3(-2) - 3(3) + 3(-3) = -24 \ne 0$. Vậy hai đường thẳng chéo nhau. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 8.</span> Hình chiếu vuông góc của điểm $M(1; -2; 3)$ lên trục tọa độ $Oy$ là điểm giữ nguyên tung độ và triệt tiêu hoành độ, cao độ: $H(0; -2; 0)$. <span class="q-ans">Chọn C.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 9.</span> Đường thẳng $d$ qua $M(1; 2; -1)$ có VTCP $\vec{u} = (1; 2; 2) \implies |\vec{u}| = 3$. Vectơ $\overrightarrow{MA} = (2; 1; -2)$. Tích có hướng $[\overrightarrow{MA}, \vec{u}] = (6; -6; 3) \implies |[\overrightarrow{MA}, \vec{u}]| = \sqrt{36 + 36 + 9} = 9$. Khoảng cách $d(A, d) = \dfrac{9}{3} = 3$. <span class="q-ans">Chọn B.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 10.</span> Theo định nghĩa tích phân: $\int_0^3 f(x)\,\mathrm{d}x = F(3) - F(0) \implies F(3) = F(0) + \int_0^3 f(x)\,\mathrm{d}x = 2 + 7 = 9$. <span class="q-ans">Chọn A.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 11.</span> Vận tốc $v(t) = \int a(t)\,\mathrm{d}t = 3t^2 - 2t + C$. Do $v(0) = 4 \implies C = 4 \implies v(t) = 3t^2 - 2t + 4 > 0, \forall t$. Quãng đường vật đi được sau 3 giây: $s = \int_0^3 (3t^2 - 2t + 4)\,\mathrm{d}t = \left[ t^3 - t^2 + 4t \right]_0^3 = 27 - 9 + 12 = 30\text{ m}$. <span class="q-ans">Chọn D.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 12.</span> Thể tích khối tròn xoay quanh trục hoành: $V = \pi \int_0^1 x e^{2x}\,\mathrm{d}x$. Tích phân từng phần: $u = x, \mathrm{d}v = e^{2x}\mathrm{d}x \implies \int_0^1 x e^{2x}\mathrm{d}x = \left[\dfrac{1}{2}x e^{2x}\right]_0^1 - \int_0^1 \dfrac{1}{2}e^{2x}\mathrm{d}x = \dfrac{e^2}{2} - \dfrac{e^2 - 1}{4} = \dfrac{e^2 + 1}{4}$. Vậy $V = \dfrac{\pi(e^2 + 1)}{4}$. <span class="q-ans">Chọn C.</span>
</div>

<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (Câu 1)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Nồng độ oxy hòa tan trong nước: $C(t) = 4 + \dfrac{8t}{t^2 + 4}$ ($0 \le t \le 12\text{ h}$):
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Tại $t = 0$: $C(0) = 4 + 0 = 4\text{ mg/L}$.</li>
    <li><b>Ý b) Sai:</b> Đạo hàm $C'(t) = \dfrac{8(t^2 + 4) - 8t(2t)}{(t^2 + 4)^2} = \dfrac{8(4 - t^2)}{(t^2 + 4)^2}$. Trên $(0; 2)$, $C'(t) > 0$ (nồng độ tăng); trên $(2; 12)$, $C'(t) < 0$ (nồng độ giảm). Mệnh đề nói nồng độ luôn tăng là sai.</li>
    <li><b>Ý c) Đúng:</b> Phương trình $C'(t) = 0 \iff t = 2$ (do $t \ge 0$). Hàm số đạt cực đại tại $t = 2\text{ h}$ với nồng độ cực đại là $C(2) = 4 + \dfrac{16}{8} = 6\text{ mg/L}$.</li>
    <li><b>Ý d) Sai:</b> Tại thời điểm $t = 12\text{ h}$, nồng độ oxy là $C(12) = 4 + \dfrac{96}{148} \approx 4,65\text{ mg/L} < 4,8\text{ mg/L}$. Mệnh đề nói luôn duy trì trên $4,8\text{ mg/L}$ là sai.</li>
  </ul>
</div>
"""

page3_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN II. Câu trắc nghiệm Đúng / Sai (Câu 2, Câu 3, Câu 4)</h3>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Cần cẩu tháp chân đế tại $O(0; 0; 0)$, tay cần tại $M(12; 16; 30)$, di chuyển hàng từ $C(12; 16; 10)$ sang $D(0; 25; 10)$:
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Khoảng cách từ đầu cần $M(12; 16; 30)$ đến trục quay $Oz$ là: $d(M, Oz) = \sqrt{12^2 + 16^2} = 20\text{ m}$.</li>
    <li><b>Ý b) Đúng:</b> Quãng đường di chuyển kiện hàng: $CD = \sqrt{(0 - 12)^2 + (25 - 16)^2 + (10 - 10)^2} = \sqrt{144 + 81} = 15\text{ m}$. Thời gian di chuyển với vận tốc $1,5\text{ m/s}$ là: $t = \dfrac{15}{1,5} = 10\text{ s}$.</li>
    <li><b>Ý c) Sai:</b> Đoạn $CD$ và đèn $E(0; 0; 10)$ cùng nằm trong mặt phẳng $z = 10$. Đường thẳng $CD$ đi qua $D(0; 25)$ có VTCP $(-4; 3) \implies$ phương trình: $3x + 4y - 100 = 0$. Khoảng cách ngắn nhất từ đèn $E(0; 0)$ đến kiện hàng là: $d(E, CD) = \dfrac{|-100|}{\sqrt{3^2 + 4^2}} = 20\text{ m} \ne 15\text{ m}$.</li>
    <li><b>Ý d) Đúng:</b> Dây cáp $MD$ có vectơ $\overrightarrow{MD} = (-12; 9; -20)$. Sin góc giữa cáp và mặt đất $(Oxy)$ có VTPT $\vec{k} = (0; 0; 1)$ là: $\sin \varphi = \dfrac{|-20|}{\sqrt{(-12)^2 + 9^2 + (-20)^2}} = \dfrac{20}{\sqrt{625}} = \dfrac{20}{25} = \dfrac{4}{5}$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Lưu lượng nước về hồ $f(t) = 15 + 6t - \dfrac{3}{4}t^2$, lưu lượng xả $g(t) = 24$ (triệu $\text{m}^3/\text{ngày}$):
  <ul class="solution-list">
    <li><b>Ý a) Sai:</b> Tại $t = 0$, lưu lượng nước về hồ là $f(0) = 15\text{ triệu m}^3/\text{ngày} \ne 20\text{ triệu m}^3/\text{ngày}$.</li>
    <li><b>Ý b) Đúng:</b> Ta có $f'(t) = 6 - \dfrac{3}{2}t = 0 \iff t = 4\text{ ngày}$. Lưu lượng nước lớn nhất là $f(4) = 15 + 24 - 12 = 27\text{ triệu m}^3/\text{ngày}$.</li>
    <li><b>Ý c) Sai:</b> Tổng dung tích thay đổi: $\Delta V = \int_0^8 [f(t) - g(t)]\,\mathrm{d}t = \int_0^8 \left(-9 + 6t - \dfrac{3}{4}t^2\right)\,\mathrm{d}t = \left[-9t + 3t^2 - \dfrac{t^3}{4}\right]_0^8 = -8\text{ triệu m}^3$ (giảm 8 triệu $\text{m}^3$, không tăng 16).</li>
    <li><b>Ý d) Đúng:</b> Nước vào lớn hơn xả khi $f(t) \ge 24 \iff -9 + 6t - \dfrac{3}{4}t^2 \ge 0 \iff 2 \le t \le 6$. Lượng nước tích thêm: $\Delta V = \int_2^6 \left(-9 + 6t - \dfrac{3}{4}t^2\right)\,\mathrm{d}t = \left[-9t + 3t^2 - \dfrac{t^3}{4}\right]_2^6 = 0 - (-8) = 8\text{ triệu m}^3$.</li>
  </ul>
</div>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Trạm radar tại $H(2; 3; 1)$, tầm quét $R = 10\text{ km}$. Quỹ đạo drone: $x = -6 + 4t, y = -3 + 3t, z = 7$:
  <ul class="solution-list">
    <li><b>Ý a) Đúng:</b> Drone luôn có cao độ $z = 7\text{ km}$ không đổi nên bay ở độ cao ổn định $7\text{ km}$ so với mặt đất $(Oxy)$.</li>
    <li><b>Ý b) Sai:</b> Vận tốc của drone là độ lớn VTCP $\vec{v} = (4; 3; 0)$: $v = \sqrt{4^2 + 3^2 + 0^2} = 5\text{ km/phút} \ne 10\text{ km/phút}$.</li>
    <li><b>Ý c) Sai:</b> Khoảng cách từ $H$ đến drone $M(t)$: $HM^2 = (-8 + 4t)^2 + (-6 + 3t)^2 + 6^2 = 25(t - 2)^2 + 36 \ge 36$. Khoảng cách ngắn nhất là $\sqrt{36} = 6\text{ km}$ (đạt tại $t = 2\text{ phút}$), không phải $8\text{ km}$.</li>
    <li><b>Ý d) Đúng:</b> Drone trong vùng phủ sóng khi $HM \le 10 \iff 25(t - 2)^2 + 36 \le 100 \iff |t - 2| \le 1,6 \iff 0,4 \le t \le 3,6$. Thời gian quan sát là $\Delta t = 3,2\text{ phút}$. Quãng đường bay: $s = 5 \times 3,2 = 16\text{ km}$.</li>
  </ul>
</div>
"""

page4_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (Câu 1 đến Câu 3)</h3>

<div class="q-block">
  <span class="q-title">Câu 1.</span> Độ dài ngắn nhất của sợi dây quấn quanh cây thông hình nón:<br>
  - Độ dài đường sinh của hình nón: $l = \sqrt{h^2 + r^2} = \sqrt{4^2 + 2^2} = \sqrt{20} = 2\sqrt{5}\text{ m}$.<br>
  - Cắt mặt xung quanh của hình nón theo đường sinh $SA$ và trải phẳng ra mặt phẳng, ta được một hình quạt tròn tâm $S$ bán kính $R = l = 2\sqrt{5}\text{ m}$.<br>
  - Chu vi đáy hình nón chính là độ dài cung tròn của hình quạt: $C = 2\pi r = 2\pi(2) = 4\pi\text{ m}$.<br>
  - Góc ở đỉnh của hình quạt tròn là:
  $$\alpha = \dfrac{C}{R} = \dfrac{4\pi}{2\sqrt{5}} = \dfrac{2\pi}{\sqrt{5}}\text{ (rad)} \approx 2,8099\text{ rad} \approx 160^\circ 59'.$$
  - Sợi dây quấn đúng một vòng quanh mặt nón từ mép $SA$ đến trung điểm $M$ của mép $SA'$ (với $SM = \dfrac{l}{2} = \sqrt{5}\text{ m}$).<br>
  - Quãng đường ngắn nhất của sợi dây là độ dài đoạn thẳng $AM$ trên hình khai triển phẳng.<br>
  - Xét tam giác $SAM$, áp dụng định lý côsin:
  $$AM^2 = SA^2 + SM^2 - 2 \cdot SA \cdot SM \cdot \cos\alpha = (2\sqrt{5})^2 + (\sqrt{5})^2 - 2(2\sqrt{5})(\sqrt{5})\cos\left(\dfrac{2\pi}{\sqrt{5}}\right)$$
  $$AM^2 = 20 + 5 - 20\cos\left(\dfrac{2\pi}{\sqrt{5}}\right) = 25 - 20\cos\left(\dfrac{2\pi}{\sqrt{5}}\right).$$
  - Với $\cos\left(\dfrac{2\pi}{\sqrt{5}}\right) \approx -0,945519$:
  $$AM^2 \approx 25 - 20(-0,945519) = 43,91037 \implies AM \approx \sqrt{43,91037} \approx 6,626\text{ m}.$$
  - Làm tròn kết quả đến hàng phần mười được <b>6,6</b>.
  <span class="q-ans">Đáp số: 6,6.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 2.</span> Thùng rượu gỗ sồi hình tròn xoay sinh bởi cung parabol quanh trục đối xứng $Ox$:<br>
  - Đặt hệ trục $Oxy$ với trục $Ox$ là trục đối xứng nối tâm hai đáy, gốc $O$ là tâm phần bụng phình to nhất.<br>
  - Chiều cao $80\text{ cm} \implies x \in [-40; 40]$. Bán kính bụng $y(0) = 40\text{ cm}$, bán kính đáy $y(\pm 40) = 30\text{ cm}$.<br>
  - Cung parabol có đỉnh $(0; 40)$ nên có dạng $y = ax^2 + 40$. Thay điểm $(40; 30) \implies 30 = 1600a + 40 \iff a = -\dfrac{1}{160}$.<br>
  - Phương trình đường sinh: $y = 40 - \dfrac{x^2}{160}$ với $x \in [-40; 40]$.<br>
  - Thể tích thùng rượu tròn xoay:
  $$V = \pi \int_{-40}^{40} y^2\,\mathrm{d}x = 2\pi \int_0^{40} \left(1600 - \dfrac{x^2}{2} + \dfrac{x^4}{25600}\right)\,\mathrm{d}x = 2\pi \left[1600x - \dfrac{x^3}{6} + \dfrac{x^5}{128000}\right]_0^{40}$$
  $$= 2\pi \left(64000 - \dfrac{32000}{3} + 800\right) = \dfrac{324800\pi}{3}\text{ cm}^3.$$
  - Đổi sang lít ($1\text{ lít} = 1000\text{ cm}^3$): $V = \dfrac{324,8\pi}{3} \approx 340,1298\text{ lít}$. Làm tròn đến hàng đơn vị được <b>340</b>.
  <span class="q-ans">Đáp số: 340.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 3.</span> Khoảng cách giữa tuyến cáp treo $d_1: \dfrac{x-1}{2} = \dfrac{y-3}{2} = \dfrac{z-2}{1}$ và đường dây điện $d_2: \dfrac{x-11}{1} = \dfrac{y-5}{-2} = \dfrac{z-2}{2}$:<br>
  - Điểm $M_1(1; 3; 2) \in d_1$, VTCP $\vec{u}_1 = (2; 2; 1)$; điểm $M_2(11; 5; 2) \in d_2$, VTCP $\vec{u}_2 = (1; -2; 2)$.<br>
  - Vectơ $\overrightarrow{M_1M_2} = (10; 2; 0)$.<br>
  - Tích có hướng: $[\vec{u}_1, \vec{u}_2] = (2(2) - 1(-2); 1(1) - 2(2); 2(-2) - 2(1)) = (6; -3; -6) \implies |[\vec{u}_1, \vec{u}_2]| = \sqrt{36 + 9 + 36} = 9$.<br>
  - Tích hỗn tạp: $[\vec{u}_1, \vec{u}_2] \cdot \overrightarrow{M_1M_2} = 6(10) - 3(2) - 6(0) = 54$.<br>
  - Khoảng cách ngắn nhất giữa hai đường thẳng là:
  $$d(d_1, d_2) = \dfrac{|[\vec{u}_1, \vec{u}_2] \cdot \overrightarrow{M_1M_2}|}{|[\vec{u}_1, \vec{u}_2]|} = \dfrac{54}{9} = 6\text{ m}.$$
  <span class="q-ans">Đáp số: 6.</span>
</div>
"""

page5_content = r"""
<div style="page-break-before: always;"></div>
<h3 class="sub-title">PHẦN III. Câu trắc nghiệm trả lời ngắn (Câu 4 đến Câu 6)</h3>

<div class="q-block">
  <span class="q-title">Câu 4.</span> Giá trị nhỏ nhất của $T = MA^2 + MB^2 + MC^2$ với $M \in (P): x + 2y - 2z + 7 = 0$ và $A(1; 2; -1), B(3; 0; 1), C(2; 1; 3)$:<br>
  - Trọng tâm tam giác $ABC$: $G = \left(\dfrac{1+3+2}{3}; \dfrac{2+0+1}{3}; \dfrac{-1+1+3}{3}\right) = (2; 1; 1)$.<br>
  - Biến đổi tâm tỉ cự: $T = 3MG^2 + GA^2 + GB^2 + GC^2$.<br>
  - Độ dài từ $G$: $\overrightarrow{GA} = (-1; 1; -2) \implies GA^2 = 6$; $\overrightarrow{GB} = (1; -1; 0) \implies GB^2 = 2$; $\overrightarrow{GC} = (0; 0; 2) \implies GC^2 = 4$. Do đó $GA^2 + GB^2 + GC^2 = 12$.<br>
  - Khoảng cách từ $G(2; 1; 1)$ đến mặt phẳng $(P)$ là:
  $$d(G, (P)) = \dfrac{|2 + 2(1) - 2(1) + 7|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \dfrac{9}{3} = 3.$$
  - Do $M \in (P) \implies MG \ge d(G, (P)) = 3 \implies MG^2 \ge 9$.<br>
  - Giá trị nhỏ nhất của $T$ là: $T_{\min} = 3(9) + 12 = 39$.
  <span class="q-ans">Đáp số: 39.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 5.</span> Giá trị của biểu thức $T = a - b + c$:<br>
  - Thực hiện phép chia đa thức tử cho mẫu (hàm bậc hai chia cho bậc nhất):
  $$\dfrac{2x^2 + 3x + 2}{x + 1} = \dfrac{2x(x + 1) + (x + 1) + 1}{x + 1} = 2x + 1 + \dfrac{1}{x + 1}.$$
  - Tính tích phân:
  $$\int_{1}^{2} \dfrac{2x^2 + 3x + 2}{x + 1}\,\mathrm{d}x = \int_{1}^{2} \left(2x + 1 + \dfrac{1}{x + 1}\right)\mathrm{d}x = \left[ x^2 + x + \ln|x + 1| \right]_{1}^{2}$$
  $$= (2^2 + 2 + \ln 3) - (1^2 + 1 + \ln 2) = (6 + \ln 3) - (2 + \ln 2) = 4 + \ln\left(\dfrac{3}{2}\right).$$
  - Theo giả thiết, tích phân có dạng $a + \ln\left(\dfrac{b}{c}\right)$ với $a \in \mathbb{Z}$, $b, c \in \mathbb{Z}^+$ và phân số $\dfrac{b}{c}$ tối giản.<br>
  - Do đó ta có: $a = 4$, $b = 3$, $c = 2$ (thỏa mãn $\dfrac{3}{2}$ là phân số tối giản).<br>
  - Vậy giá trị biểu thức $T = a - b + c = 4 - 3 + 2 = 3$.
  <span class="q-ans">Đáp số: 3.</span>
</div>

<div class="q-block">
  <span class="q-title">Câu 6.</span> Góc giữa hai vectơ $\overrightarrow{AM}$ và $\overrightarrow{BN}$ trong hình chóp $S.ABCD$ đáy hình thoi (Vận dụng cao):<br>
  - Đáy $ABCD$ là hình thoi cạnh $a$, $\widehat{ABC} = 60^\circ \implies \triangle ABC$ và $\triangle ACD$ là hai tam giác đều cạnh $a$.<br>
  - Gọi $O = AC \cap BD \implies AC \perp BD$ tại $O$. Ta có $OA = OC = \dfrac{a}{2}$ và $OB = OD = \dfrac{a\sqrt{3}}{2}$.<br>
  - Trọng tâm $G$ của tam giác $ACD$ nằm trên $OD$ và thỏa mãn $OG = \dfrac{1}{3}OD = \dfrac{a\sqrt{3}}{6}$.<br>
  - Khoảng cách $GA = \sqrt{OA^2 + OG^2} = \sqrt{\dfrac{a^2}{4} + \dfrac{3a^2}{36}} = \dfrac{a\sqrt{3}}{3}$. Do $SG \perp (ABCD)$ và $SA = a$:
  $$SG = \sqrt{SA^2 - GA^2} = \sqrt{a^2 - \dfrac{a^2}{3}} = \dfrac{a\sqrt{6}}{3}.$$
  - Chọn hệ trục tọa độ $Oxyz$ với gốc tại tâm hình thoi $O(0; 0; 0)$: trục $Ox$ dọc theo tia $OC$, trục $Oy$ dọc theo tia $OD$, trục $Oz$ song song $SG$ hướng lên trên. Tọa độ các điểm:
  $$A\left(-\dfrac{a}{2}; 0; 0\right),\quad B\left(0; -\dfrac{a\sqrt{3}}{2}; 0\right),\quad C\left(\dfrac{a}{2}; 0; 0\right),\quad D\left(0; \dfrac{a\sqrt{3}}{2}; 0\right),\quad S\left(0; \dfrac{a\sqrt{3}}{6}; \dfrac{a\sqrt{6}}{3}\right).$$
  - Trung điểm $M$ của cạnh $SB$: $M = \dfrac{S + B}{2} = \left(0; -\dfrac{a\sqrt{3}}{6}; \dfrac{a\sqrt{6}}{6}\right)$.<br>
  - Điểm $N \in SC$ thỏa mãn $SN = \dfrac{1}{2}NC \iff \overrightarrow{SN} = \dfrac{1}{3}\overrightarrow{SC} \implies N = \dfrac{2}{3}S + \dfrac{1}{3}C$:
  $$N\left(\dfrac{a}{6}; \dfrac{a\sqrt{3}}{9}; \dfrac{2a\sqrt{6}}{9}\right).$$
  - Tọa độ các vectơ:
  $$\overrightarrow{AM} = M - A = \left(\dfrac{a}{2}; -\dfrac{a\sqrt{3}}{6}; \dfrac{a\sqrt{6}}{6}\right),\quad \overrightarrow{BN} = N - B = \left(\dfrac{a}{6}; \dfrac{11a\sqrt{3}}{18}; \dfrac{2a\sqrt{6}}{9}\right).$$
  - Tích vô hướng của hai vectơ:
  $$\overrightarrow{AM} \cdot \overrightarrow{BN} = \left(\dfrac{a}{2}\right)\left(\dfrac{a}{6}\right) + \left(-\dfrac{a\sqrt{3}}{6}\right)\left(\dfrac{11a\sqrt{3}}{18}\right) + \left(\dfrac{a\sqrt{6}}{6}\right)\left(\dfrac{2a\sqrt{6}}{9}\right)$$
  $$= \dfrac{a^2}{12} - \dfrac{33a^2}{108} + \dfrac{12a^2}{54} = \dfrac{a^2}{12} - \dfrac{11a^2}{36} + \dfrac{2a^2}{9} = \dfrac{3a^2 - 11a^2 + 8a^2}{36} = 0.$$
  - Do $\overrightarrow{AM} \cdot \overrightarrow{BN} = 0$ nên $\overrightarrow{AM} \perp \overrightarrow{BN}$.<br>
  - Vậy số đo góc giữa hai vectơ $\overrightarrow{AM}$ và $\overrightarrow{BN}$ bằng <b>$90^\circ$</b>.
  <span class="q-ans">Đáp số: 90.</span>
</div>

<div style="text-align: center; margin-top: 15px; padding-top: 8px; border-top: 1px dashed #718096;">
  <b style="color: #1a365d; font-size: 10pt;">CHÚC CÁC EM ÔN TẬP VÀ ĐẠT KẾT QUẢ CAO NHẤT TRONG KỲ THI TỐT NGHIỆP THPT!</b>
</div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết - Mã Đề 115</title>
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
  letter-spacing: 0.5px;
}}
.title-sub {{
  font-size: 10.2pt;
  font-weight: bold;
  color: #2b6cb0;
  text-transform: uppercase;
  margin-top: 1px;
}}
.title-meta {{
  font-size: 9.3pt;
  color: #4a5568;
  margin-top: 1px;
}}
.sec-title {{
  font-size: 11pt;
  font-weight: bold;
  color: #2b6cb0;
  border-left: 3.5px solid #2b6cb0;
  padding-left: 6px;
  margin: 5px 0 3px 0;
  text-transform: uppercase;
}}
.sub-title {{
  font-size: 9.9pt;
  font-weight: bold;
  color: #2d3748;
  margin: 4px 0 2px 0;
}}
.ans-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 4px;
  font-size: 9.3pt;
  text-align: center;
}}
.ans-table th {{
  background-color: #ebf8ff;
  color: #2b6cb0;
  border: 1px solid #cbd5e0;
  padding: 3px 2px;
  font-weight: bold;
}}
.ans-table td {{
  border: 1px solid #cbd5e0;
  padding: 3px 2px;
}}
.bold-ans {{
  font-weight: bold;
  color: #c53030;
  font-size: 9.8pt;
}}
.q-block {{
  margin-bottom: 4px;
  text-align: justify;
  line-height: 1.28;
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
  margin: 2px 0 2px 14px;
  padding: 0;
  list-style-type: none;
}}
.solution-list li {{
  margin-bottom: 2px;
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

with open('test_dap_an_115.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML written to test_dap_an_115.html")
cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--print-to-pdf=Bang_Dap_An_Va_HDG_De_115.pdf',
    '--no-pdf-header-footer',
    'test_dap_an_115.html'
]

print("Running Chrome to generate HDG 115 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader('Bang_Dap_An_Va_HDG_De_115.pdf')
print("Total pages:", len(reader.pages))
for i, p in enumerate(reader.pages):
    txt = p.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
