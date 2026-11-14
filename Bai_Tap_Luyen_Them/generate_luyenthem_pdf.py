import subprocess

html_template = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Bài tập luyện thêm</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {
  size: A4;
  margin: 14mm 15mm 15mm 15mm;
  @bottom-right {
    content: "Trang " counter(page);
    font-family: 'Times New Roman', serif;
    font-size: 9.5pt;
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
  font-size: 18pt;
  text-transform: uppercase;
  color: #1a365d;
  margin-top: 0;
  margin-bottom: 6px;
}
.divider {
  border-top: 1.5px solid #2b4c7e;
  margin: 10px 0 16px 0;
}
.question {
  margin-bottom: 16px;
  text-align: justify;
  page-break-inside: avoid;
}
.q-title {
  font-weight: bold;
  color: #b91c1c;
}
.img-wrap {
  text-align: center;
  margin: 10px 0;
}
.img-wrap img {
  max-width: 95%;
  height: auto;
}
.flex-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.flex-col {
  flex: 1;
}
</style>
</head>
<body>

<h1 class="main-title">BÀI TẬP LUYỆN THÊM</h1>
<div class="divider"></div>

<!-- Cau 1 -->
<div class="question">
  <span class="q-title">Câu 1.</span> Cho hàm số bậc ba $f(x) = ax^3 + bx^2 + cx + d$ có bảng biến thiên như sau:
  <div class="img-wrap"><img src="assets/luyenthem_bbt_cau1.png" style="max-height: 210px;"></div>
  Xét tính đúng sai của các mệnh đề sau:<br>
  a) Hàm số đã cho nghịch biến trên khoảng $(-1; 3)$.<br>
  b) $a + b + c + d = -10$.<br>
  c) Giá trị lớn nhất của hàm số đã cho trên đoạn $[0; 6]$ bằng $6$.<br>
  d) Có đúng hai số nguyên $x$ thỏa mãn $x < 3$ và $f(x) > 0$.
</div>

<!-- Cau 2 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col">
      <span class="q-title">Câu 2.</span> Trong một công viên có một hồ nước và một chòi nghỉ hình tròn nằm giữa hồ. Chọn hệ trục tọa độ $Oxy$ (đơn vị trên mỗi trục là mét) sao cho bờ hồ là phần parabol $(P): y = \frac{x^2}{8}$ với $-8 \le x \le 8$, mặt nước nằm phía trên $(P)$, chòi nghỉ có tâm $I(0; 6)$ và bán kính $1,5\text{ m}$. Người ta muốn bắc một cây cầu thẳng từ một điểm $M$ trên bờ hồ đến chòi nghỉ sao cho cầu ngắn nhất. Xét tính đúng sai của các mệnh đề sau:<br>
      a) Điểm có tọa độ $(8; 8)$ nằm trên bờ hồ.<br>
      b) Nếu $M$ có hoành độ $x$ thì $IM^2 = x^2 + \left(\frac{x^2}{8} - 6\right)^2$.<br>
      c) Khoảng cách từ $I$ đến bờ hồ (khoảng cách ngắn nhất từ $I$ đến một điểm của $(P)$) bằng $4\sqrt{2}\text{ m}$.<br>
      d) Có đúng một vị trí của $M$ trên bờ hồ để cây cầu ngắn nhất.
    </div>
    <div style="width: 300px; text-align: center; flex-shrink: 0;">
      <img src="assets/luyenthem_parabol_cau2.png" style="width: 100%; height: auto;">
    </div>
  </div>
</div>

<!-- Cau 3 -->
<div class="question">
  <span class="q-title">Câu 3.</span> Một nhà máy sản xuất X hoạt động tại khu vực gần một dòng suối lớn. Trong quá trình sản xuất, nhà máy thải ra một lượng chất ô nhiễm đáng kể vào môi trường, gây ảnh hưởng nghiêm trọng đến chất lượng nước và sức khoẻ cộng đồng. Để cải thiện tình hình và tuân thủ các quy định về bảo vệ môi trường, nhà máy đã quyết định đầu tư vào một hệ thống xử lý nước thải hiện đại. Chi phí để loại bỏ $x\%$ chất ô nhiễm từ nguồn nước thải được mô hình hoá bởi hàm số:
  $$C(x) = \dfrac{2x+1}{1-0,01x}\text{ (triệu đồng)},\quad 0 \le x < 100$$
  Các mệnh đề sau đây đúng hay sai?<br>
  a) Chi phí để loại bỏ $20\%$ chất ô nhiễm là $51,52$ triệu đồng.<br>
  b) Nhà máy không thể loại bỏ $100\%$ chất ô nhiễm.<br>
  c) Để chi phí không quá $200$ triệu đồng thì nhà máy chỉ có thể xử lý tối đa $49,75\%$ chất ô nhiễm.<br>
  d) Nếu nhà máy giảm từ $20\%$ chất ô nhiễm trở lên thì doanh thu sẽ tăng lên (nhờ vào việc nâng cao uy tín và hình ảnh thương hiệu) được biểu diễn bởi hàm số $R(x) = 12x - 240$ (triệu đồng). Khi đó lợi nhuận cho việc loại bỏ chất ô nhiễm có thể đạt hơn $177$ triệu đồng.
</div>

<!-- Cau 4 -->
<div class="question">
  <span class="q-title">Câu 4.</span> Một nhà máy chế biến cà phê bán trong nước và xuất khẩu ra nước ngoài cho biết, nếu giá vốn sản xuất mỗi kg cà phê là $x\text{ USD}$ thì sản lượng nhà máy sản xuất được là $R(x) = x - 150\text{ (kg)}$ và lượng tiêu thụ trong nước là $Q(x) = 2700 - x\text{ (kg)}$. Phần cà phê còn dư được xuất khẩu với giá cố định là $1900\text{ USD}$ mỗi kg. Biết rằng với mỗi kg cà phê xuất khẩu thì nhà máy phải chịu mức thuế là $m\text{ USD}$. Lợi nhuận từ xuất khẩu và thuế thu được từ nhà nước luôn giữ tỷ lệ bằng $4 : 1$. Hãy tìm giá trị của $m$ để lợi nhuận từ xuất khẩu đạt giá trị lớn nhất.
</div>

<!-- Cau 5 -->
<div class="question">
  <span class="q-title">Câu 5.</span> Một công ty khai thác tuyến tàu cao tốc chở khách du lịch từ đất liền ra đảo với khoảng cách $80\text{ km}$. Giả sử tàu di chuyển với vận tốc $v$ không đổi trên suốt tuyến đường. Chi phí vận hành cho mỗi giờ hoạt động của tàu bao gồm:
  <ul>
    <li>Chi phí nhiên liệu: $125v^3$ (đồng), với $v\text{ (km/h)}$ là vận tốc của tàu ($v > 0$).</li>
    <li>Chi phí cố định (lương thủy thủ đoàn, khấu hao, bến bãi, ...): $12\,000\,000$ đồng.</li>
  </ul>
  Để đảm bảo lịch trình và trải nghiệm của hành khách, thời gian di chuyển mỗi chuyến không được vượt quá 2 giờ. Đồng thời, vì lý do an toàn hàng hải, tàu không được chạy quá $60\text{ km/h}$. Tàu có sức chứa tối đa 200 hành khách và giả sử rằng số lượng khách trên mỗi chuyến đi luôn đạt mức tối đa. Ban giám đốc thiết lập mục tiêu lợi nhuận thu được từ mỗi chuyến đi bằng $25\%$ tổng chi phí vận hành của chuyến đó. Để đạt được mức lợi nhuận này trong điều kiện tàu được vận hành với tổng chi phí thấp nhất, giá vé mỗi hành khách phải trả là bao nhiêu nghìn đồng?
</div>

<!-- Cau 6 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col">
      <span class="q-title">Câu 6.</span> Trong một công viên có một hồ nước và một đường đi lát gạch hoa. Thiết lập hệ trục $Oxy$ như hình vẽ dưới, kiến trúc sư thấy rằng bờ hồ có thể coi như một nhánh của đồ thị hàm số $y = \dfrac{2x+1}{x-1}$ và đường đi khi đó ứng với đường thẳng $(d): y = -x + 4$. Để đảm bảo ánh sáng, kiến trúc sư muốn đặt 2 cột đèn trên bờ hồ và 2 cột đèn trên đường đi sao cho 4 cột đèn này tạo thành một hình vuông. Tính khoảng cách giữa hai cột đèn trên bờ hồ *(làm tròn đến hàng phần trăm)*.
    </div>
    <div style="width: 285px; text-align: center; flex-shrink: 0;">
      <img src="assets/luyenthem_cau6_hinhvuong.png" style="width: 100%; height: auto;">
    </div>
  </div>
</div>

<!-- Cau 7 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col">
      <span class="q-title">Câu 7.</span> Một khu vực trồng hoa được xây dựng trong khu du lịch sinh thái. Trong mô hình minh họa (như hình vẽ), nó được giới hạn bởi các trục tọa độ và đồ thị $(C)$ của một hàm số bậc ba. Biết rằng đồ thị $(C)$ đi qua các điểm $A(0; 8), B(2; 5,4), K(5; 6,75)$ và $H(8; 0)$. Trong khu du lịch sinh thái có một con đường chạy dọc theo đường thẳng $d: y = -\dfrac{13}{9}x + \dfrac{169}{9}$. Tìm hoành độ của điểm $M$ thuộc $(C)$ sao cho khoảng cách từ $M$ đến $d$ là nhỏ nhất *(làm tròn kết quả đến hàng phần trăm)*.
    </div>
    <div style="width: 300px; text-align: center; flex-shrink: 0;">
      <img src="assets/luyenthem_cau7_vuonhoa.png" style="width: 100%; height: auto;">
    </div>
  </div>
</div>

<!-- Cau 8 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col">
      <span class="q-title">Câu 8.</span> Một camera được đặt trên mặt đất, cách bệ phóng tên lửa $3000\text{ m}$. Tên lửa được phóng thẳng đứng lên trên với tốc độ $200\text{ m/s}$. Để giữ tên lửa luôn ở trung tâm khung hình, camera phải liên tục quay ngẩng lên. Hỏi góc ngẩng của camera đang thay đổi với tốc độ bao nhiêu (tính bằng $\text{rad/s}$) tại thời điểm tên lửa đạt độ cao $4000\text{ m}$?
    </div>
    <div style="width: 195px; text-align: center; flex-shrink: 0;">
      <img src="assets/luyenthem_cau8_camera.png" style="width: 100%; height: auto;">
    </div>
  </div>
</div>

<!-- Cau 9 -->
<div class="question">
  <div class="flex-row">
    <div class="flex-col">
      <span class="q-title">Câu 9.</span> Hai con đường thẳng vuông góc cắt nhau tại $O$. Cùng một thời điểm, xe $A$ xuất phát từ $O$, chạy trên đường thứ nhất với tốc độ $40\text{ km/h}$; xe $B$ đang cách $O$ một khoảng $30\text{ km}$ trên đường thứ hai, chạy về phía $O$ với tốc độ $30\text{ km/h}$. Hai xe chuyển động thẳng đều. Tại thời điểm lần thứ hai khoảng cách giữa hai xe bằng $25\text{ km}$, khoảng cách ấy đang tăng hay giảm, với tốc độ bao nhiêu?
    </div>
    <div style="width: 235px; text-align: center; flex-shrink: 0;">
      <img src="assets/luyenthem_cau9_haixe.png" style="width: 100%; height: auto;">
    </div>
  </div>
</div>

<!-- Cau 10 -->
<div class="question">
  <span class="q-title">Câu 10.</span> Hai thùng hàng $A$ và $B$ đặt trên mặt sàn nhà kho được nối với nhau bằng một sợi dây dài $15\text{ m}$. Sợi dây vắt qua một ròng rọc cố định tại điểm $P$ trên trần nhà. Khoảng cách từ ròng rọc $P$ thẳng đứng xuống điểm $Q$ trên mặt sàn là $PQ = 4\text{ m}$. Bỏ qua ma sát; trong suốt quá trình di chuyển, sợi dây luôn căng và hai thùng hàng chỉ trượt trên mặt sàn. Tại thời điểm thùng $A$ cách $Q$ một khoảng $3\text{ m}$ và đang bị kéo trượt ra xa $Q$ với tốc độ $0,5\text{ m/s}$, thùng $B$ đang tiến lại gần $Q$ với tốc độ bao nhiêu? *(Làm tròn kết quả đến hàng phần trăm.)*
  <div class="img-wrap"><img src="assets/luyenthem_cau10_rongroc.png" style="max-height: 135px;"></div>
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

with open("bai_tap_luyen_them_10_cau.html", "w", encoding="utf-8") as f:
    f.write(html_template)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=6000",
    "--print-to-pdf=Bai_Tap_Luyen_Them_10_Cau.pdf",
    "bai_tap_luyen_them_10_cau.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Exit code:", res.returncode)
