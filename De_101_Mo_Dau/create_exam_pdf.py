import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class ExamPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(15, 12, 15)
        self.set_auto_page_break(auto=True, margin=15)
        
        # Load fonts
        self.add_font('TimesVN', '', '/System/Library/Fonts/Supplemental/Times New Roman.ttf')
        self.add_font('TimesVN', 'B', '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf')
        self.add_font('TimesVN', 'I', '/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf')
        self.add_font('ArialUni', '', '/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
        self.set_fallback_fonts(['ArialUni'])

    def header(self):
        if self.page_no() == 1:
            self.set_y(12)
            
            # Left side
            self.set_font('TimesVN', 'B', 11.5)
            self.set_xy(15, 12)
            self.cell(75, 5.5, 'ĐỀ ÔN THI GIỮA KÌ 1', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_font('TimesVN', 'I', 11)
            self.set_x(15)
            self.cell(75, 5, 'Biên soạn: Trần Trung Quân', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Right side
            self.set_font('TimesVN', 'B', 11)
            self.set_xy(90, 12)
            self.cell(105, 5, 'KỲ KHẢO SÁT CHẤT LƯỢNG LỚP 12 NĂM HỌC 2025 - 2026', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_font('TimesVN', 'B', 11)
            self.set_x(90)
            self.cell(105, 5, 'Môn: TOÁN - Lớp 12', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_font('TimesVN', 'I', 10)
            self.set_x(90)
            self.cell(105, 4.5, 'Thời gian làm bài: 90 phút, không kể thời gian giao đề', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Left box
            self.rect(26, 24.5, 53, 11)
            self.set_xy(26, 25)
            self.set_font('TimesVN', 'B', 9.5)
            self.cell(53, 5, 'ĐỀ ÔN TẬP CHÍNH THỨC', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_x(26)
            self.set_font('TimesVN', '', 9)
            self.cell(53, 4.5, '(Đề thi có 03 trang)', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Right box (Mã đề)
            self.rect(142, 28, 42, 7.5)
            self.set_xy(142, 28)
            self.set_font('TimesVN', 'B', 11.5)
            self.cell(42, 7.5, 'Mã đề: 101', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Line 1
            self.set_draw_color(0, 0, 0)
            self.set_line_width(0.4)
            self.line(15, 38.5, 195, 38.5)
            
            # Student info
            self.set_xy(15, 40)
            self.set_font('TimesVN', '', 10.5)
            self.cell(115, 6, 'Họ và tên học sinh:...........................................................................', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.cell(65, 6, 'Lớp:............................................', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Line 2
            self.set_line_width(0.6)
            self.line(15, 47.5, 195, 47.5)
            self.set_y(49.5)

    def footer(self):
        self.set_y(-12)
        self.set_font('TimesVN', '', 10)
        page_str = f"Trang {self.page_no()}/{{nb}} – Mã đề 101"
        self.cell(0, 8, page_str, align='R')

    def print_section_header(self, title):
        self.ln(2)
        self.set_font('TimesVN', 'B', 10.5)
        self.multi_cell(0, 5.5, title)
        self.ln(1)

    def print_question_stem(self, q_num, text):
        self.set_font('TimesVN', 'B', 10.5)
        q_label = f"Câu {q_num}: "
        label_w = self.get_string_width(q_label)
        
        if self.get_y() > 260:
            self.add_page()
            
        self.cell(label_w, 5.5, q_label, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('TimesVN', '', 10.5)
        self.multi_cell(0, 5.5, text)

    def print_options_4col(self, a, b, c, d):
        self.set_font('TimesVN', '', 10)
        col_w = 45
        if self.get_y() > 265:
            self.add_page()
        y = self.get_y()
        self.set_xy(15, y)
        self.cell(col_w, 5, f"A. {a}", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(col_w, 5, f"B. {b}", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(col_w, 5, f"C. {c}", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(col_w, 5, f"D. {d}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.5)

    def print_options_2col(self, a, b, c, d):
        self.set_font('TimesVN', '', 10)
        col_w = 90
        if self.get_y() > 260:
            self.add_page()
        y = self.get_y()
        self.set_xy(15, y)
        self.cell(col_w, 5, f"A. {a}", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(col_w, 5, f"B. {b}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(15)
        self.cell(col_w, 5, f"C. {c}", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(col_w, 5, f"D. {d}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.5)

    def print_sub_items(self, a, b, c, d):
        self.set_font('TimesVN', '', 10)
        for label, txt in [('a)', a), ('b)', b), ('c)', c), ('d)', d)]:
            if self.get_y() > 268:
                self.add_page()
            self.set_x(18)
            lbl_w = self.get_string_width(label + " ")
            self.set_font('TimesVN', 'B', 10)
            self.cell(lbl_w, 5, label + " ", new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('TimesVN', '', 10)
            self.multi_cell(0, 5, txt)
        self.ln(1.5)

pdf = ExamPDF()
pdf.alias_nb_pages()
pdf.add_page()

# ==================== PHẦN I ====================
pdf.print_section_header("PHẦN I. Học sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.")

# Câu 1
pdf.print_question_stem(1, "Cho hàm số y = f(x) có bảng biến thiên như sau:")
pdf.image('assets/bbt_cau1.png', x=38, y=pdf.get_y() + 1, w=134)
pdf.set_y(pdf.get_y() + 37)
pdf.set_font('TimesVN', '', 10.5)
pdf.multi_cell(0, 5.5, "Hàm số đã cho nghịch biến trên khoảng nào dưới đây?")
pdf.print_options_4col("(-1; 2).", "(-∞; -1).", "(2; +∞).", "(-1; 3).")

# Câu 2
pdf.print_question_stem(2, "Cho hàm số y = f(x) có đạo hàm f'(x) = x(x - 1)²(x + 2)³ với mọi x ∈ ℝ. Số điểm cực trị của hàm số đã cho là")
pdf.print_options_4col("1.", "2.", "3.", "4.")

# Câu 3
pdf.print_question_stem(3, "Đạo hàm của hàm số y = (2x - 1)/(x + 1) trên từng khoảng xác định là")
pdf.print_options_4col("y' = 3/(x + 1)².", "y' = 1/(x + 1)².", "y' = -3/(x + 1)².", "y' = 3/(x + 1).")

# Câu 4
pdf.print_question_stem(4, "Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số y = (x + 2)/(x² - 4) là")
pdf.print_options_4col("1.", "2.", "3.", "0.")

# Câu 5: Text on Left (130mm), Graph on Right (45mm)
start_y = pdf.get_y()
pdf.set_font('TimesVN', 'B', 10.5)
q5_label = "Câu 5: "
lw = pdf.get_string_width(q5_label)
pdf.set_xy(15, start_y)
pdf.cell(lw, 5.5, q5_label, new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.set_font('TimesVN', '', 10.5)
pdf.multi_cell(125, 5.5, "Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?")
pdf.set_y(pdf.get_y() + 2)

# Options for Q5 on left
pdf.set_font('TimesVN', '', 10)
y_opt = pdf.get_y()
pdf.set_xy(15, y_opt)
pdf.cell(62, 5.5, "A. y = -x³ + 3x.", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(63, 5.5, "B. y = x³ - 3x + 1.", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(15)
pdf.cell(62, 5.5, "C. y = x³ - 3x.", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.cell(63, 5.5, "D. y = x⁴ - 2x².", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Graph on the right
pdf.image('assets/dothi_cau5.png', x=148, y=start_y, w=42)

# Move Y below the taller of the two columns
pdf.set_y(max(pdf.get_y() + 2, start_y + 44))
pdf.ln(1)

# Câu 6
pdf.print_question_stem(6, "Cho dãy số (u_n) với số hạng tổng quát u_n = (2n - 1)/(n + 1). Giá trị của số hạng u₃ bằng")
pdf.print_options_4col("5/4.", "3/4.", "1.", "1/2.")

# Câu 7
pdf.print_question_stem(7, "Cho cấp số cộng (u_n) có số hạng đầu u₁ = 3 và công sai d = 4. Số hạng thứ 5 của cấp số cộng đó là")
pdf.print_options_4col("u₅ = 15.", "u₅ = 19.", "u₅ = 23.", "u₅ = 12.")

# Câu 8
pdf.print_question_stem(8, "Cho cấp số nhân (u_n) có số hạng đầu u₁ = 2 và công bội q = 3. Tổng của 4 số hạng đầu tiên của cấp số nhân đó bằng")
pdf.print_options_4col("S₄ = 80.", "S₄ = 40.", "S₄ = 26.", "S₄ = 54.")

# Câu 9
pdf.print_question_stem(9, "Cho hình lập phương ABCD.A'B'C'D'. Góc giữa hai đường thẳng AB và A'C' bằng")
pdf.print_options_4col("30°.", "45°.", "60°.", "90°.")

# Câu 10
pdf.print_question_stem(10, "Cho hình chóp S.ABC có đáy ABC là tam giác đều cạnh a. Cạnh bên SA vuông góc với mặt phẳng đáy (ABC) và SA = a. Góc giữa đường thẳng SB và mặt phẳng (ABC) bằng")
pdf.print_options_4col("30°.", "45°.", "60°.", "90°.")

# Câu 11
pdf.print_question_stem(11, "Cho hình chóp S.ABCD có đáy ABCD là hình chữ nhật với AB = a, AD = 2a. Cạnh bên SA vuông góc với mặt phẳng đáy (ABCD) và SA = 3a. Khoảng cách từ điểm S đến mặt phẳng (ABCD) bằng")
pdf.print_options_4col("a.", "2a.", "3a.", "a√14.")

# Câu 12
pdf.print_question_stem(12, "Cho hình chóp S.ABC có đáy ABC là tam giác vuông tại B. Cạnh bên SA vuông góc với mặt phẳng đáy (ABC). Kẻ AH ⊥ SB tại H. Khoảng cách từ điểm A đến mặt phẳng (SBC) bằng độ dài đoạn thẳng nào dưới đây?")
pdf.print_options_4col("AB.", "SA.", "AH.", "SB.")


# ==================== PHẦN II ====================
pdf.print_section_header("PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

# Câu 1 - Phần II
pdf.print_question_stem(1, "Một hội trường nhà hát được thiết kế có 25 hàng ghế xếp theo hình bậc thang từ thấp lên cao. Hàng ghế đầu tiên có 20 ghế, mỗi hàng sau có nhiều hơn hàng liền trước nó 3 ghế. Ký hiệu u_n là số ghế ở hàng thứ n (1 ≤ n ≤ 25).")
pdf.print_sub_items(
    "Dãy số (u_n) lập thành một cấp số cộng với số hạng đầu u₁ = 20 và công sai d = 3.",
    "Hàng ghế thứ 15 của hội trường có 65 ghế.",
    "Tổng số ghế của toàn bộ 25 hàng ghế trong hội trường là 1400 ghế.",
    "Ban tổ chức phát hành vé xem ca nhạc với giá 200.000 đồng/vé cho 10 hàng ghế đầu và 120.000 đồng/vé cho 15 hàng ghế còn lại. Khi bán hết toàn bộ số vé, tổng số tiền thu được là 208.700.000 đồng."
)

# Câu 2 - Phần II
pdf.print_question_stem(2, "Cho hàm số y = f(x) = (x² - 3x + 6)/(x - 2) có đồ thị là (C).")
pdf.print_sub_items(
    "Đồ thị (C) có đường tiệm cận đứng là đường thẳng x = 2.",
    "Hàm số đã cho nghịch biến trên khoảng (0; 4).",
    "Điểm cực đại của đồ thị hàm số là M(0; -3) và điểm cực tiểu của đồ thị hàm số là N(4; 5).",
    "Đường tiệm cận xiên của (C) cùng với hai trục tọa độ tạo thành một tam giác có diện tích bằng 1."
)

# Câu 3 - Phần II
pdf.print_question_stem(3, "Một hộ gia đình dự định xây dựng một bể chứa nước sinh hoạt hình hộp chữ nhật không có nắp với thể tích V = 36 m³. Đáy bể là hình chữ nhật có chiều dài gấp đôi chiều rộng. Biết rằng chi phí vật liệu xây dựng đáy bể là 400.000 đồng/m², chi phí xây dựng bốn mặt bên (thành bể) là 300.000 đồng/m². Gọi x (m) là chiều rộng của đáy bể (x > 0), h (m) là chiều cao của bể và C(x) (đồng) là tổng chi phí xây dựng bể.")
pdf.print_sub_items(
    "Chiều cao của bể nước được biểu diễn theo x là h = 18/x² (m).",
    "Tổng diện tích của bốn mặt bên xung quanh bể là S_xq = 108/x (m²).",
    "Tổng chi phí xây dựng bể nước biểu diễn theo x là hàm số C(x) = 800.000x² + 32.400.000/x (đồng).",
    "Để chi phí xây dựng bể là nhỏ nhất thì gia đình cần xây dựng đáy bể có chiều rộng x = 3 m, và khi đó chi phí nhỏ nhất là 21.600.000 đồng."
)

# Câu 4 - Phần II
pdf.print_question_stem(4, "Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a. Cạnh bên SA vuông góc với mặt phẳng đáy (ABCD) và SA = a√3. Gọi O là giao điểm của AC và BD.")
pdf.print_sub_items(
    "Đoạn thẳng AC là hình chiếu vuông góc của đoạn thẳng SC lên mặt phẳng (ABCD).",
    "Góc giữa đường thẳng SC và mặt phẳng đáy (ABCD) bằng 60°.",
    "Khoảng cách từ điểm A đến mặt phẳng (SBD) bằng (a√21)/7.",
    "Khoảng cách giữa hai đường thẳng chéo nhau SC và BD bằng (a√21)/14."
)


# ==================== PHẦN III ====================
pdf.add_page()
pdf.print_section_header("PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.")

# Câu 1 - Phần III
pdf.print_question_stem(1, "Cho cấp số nhân (u_n) có tất cả các số hạng đều là số thực dương, thỏa mãn u₂ + u₄ = 20 và u₃ + u₅ = 40.\nTìm số hạng thứ 7 (u₇) của cấp số nhân đó.")
pdf.ln(2)

# Câu 2 - Phần III
pdf.print_question_stem(2, "Cho hình chóp S.ABC có đáy ABC là tam giác vuông cân tại B, AB = BC = 2a. Cạnh bên SA vuông góc với mặt phẳng đáy (ABC) và SA = 2a√2. Tính số đo góc giữa đường thẳng SC và mặt phẳng (SAB) (đơn vị: độ).")
pdf.ln(2)

# Câu 3 - Phần III
pdf.print_question_stem(3, "Cho hình chóp S.ABC có đáy ABC là tam giác vuông tại B, AB = 3 cm, BC = 4 cm. Cạnh bên SA vuông góc với mặt phẳng đáy (ABC) và SA = 4 cm. Tính khoảng cách từ điểm A đến mặt phẳng (SBC) (kết quả ghi dưới dạng số thập phân).")
pdf.ln(2)

# Câu 4 - Phần III
pdf.print_question_stem(4, "Tìm giá trị nhỏ nhất của hàm số f(x) = (x² + 3)/(x - 1) trên đoạn [2; 4].")
pdf.ln(2)

# Câu 5 - Phần III
pdf.print_question_stem(5, "Một chất điểm chuyển động thẳng theo phương trình s(t) = -t³ + 9t² + 21t, trong đó t là thời gian tính bằng giây (t ≥ 0) và s(t) là quãng đường đi được tính bằng mét. Trong khoảng thời gian từ lúc bắt đầu chuyển động (t = 0) đến khi chất điểm đạt vận tốc lớn nhất, vận tốc lớn nhất đó bằng bao nhiêu mét trên giây (m/s)?")
pdf.ln(2)

# Câu 6 - Phần III
pdf.print_question_stem(6, "Một xưởng may sản xuất một loại áo sơ mi. Khi định giá bán p nghìn đồng cho mỗi chiếc áo, số lượng áo bán được mỗi tuần được xác định bởi hàm cầu x = 800 - 2p (chiếc), với 100 ≤ p ≤ 350. Chi phí sản xuất mỗi chiếc áo là 150 nghìn đồng và chi phí quản lý cố định hàng tuần của xưởng là 10.000 nghìn đồng. Hỏi xưởng may cần định giá bán mỗi chiếc áo là bao nhiêu nghìn đồng để lợi nhuận thu được trong tuần là lớn nhất?")
pdf.ln(5)

# End of Exam
pdf.set_font('TimesVN', 'B', 10.5)
pdf.cell(0, 6, "----------------------- HẾT -----------------------", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('TimesVN', 'I', 9.5)
pdf.cell(0, 5, "Học sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

output_path = 'De_On_Thi_Giua_Ki_1_Toan_12.pdf'
pdf.output(output_path)
print(f"Exam PDF successfully generated at: {output_path} (Pages: {pdf.pages_count})")
