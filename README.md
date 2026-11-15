# Ngân Hàng Đề Thi Thử Kì Thi TNTHPT Quốc Gia – Môn Toán (Toán 12 / THPT)

> **© 2026 Trần Trung Quân ([@TrungQuanHCMUT](https://github.com/TrungQuanHCMUT)). All Rights Reserved / Mọi bản quyền được bảo lưu.**
>
> Kho lưu trữ này được công khai nhằm mục đích **xem trực tiếp và tham khảo**. Việc repo để chế độ **Public** không đồng nghĩa với mã nguồn mở hay từ bỏ bản quyền (repo **không cấp kèm giấy phép mã nguồn mở / No License**).
>
> **Quy định sử dụng:**
> - Học sinh và người đọc được phép xem trực tiếp đề thi, đáp án và hướng dẫn giải trên GitHub để tự ôn luyện.
> - Mọi tổ chức, cá nhân có nhu cầu **sao chép, trích xuất, chỉnh sửa, biên soạn lại, phân phối lại hoặc sử dụng vào mục đích giảng dạy / thương mại** vui lòng **liên hệ xin ý kiến và được sự chấp thuận của tác giả** trước khi sử dụng.
> - Liên hệ tác giả: **Trần Trung Quân** — Email: `quan130807@gmail.com` · GitHub: [@TrungQuanHCMUT](https://github.com/TrungQuanHCMUT).

---

## Cấu trúc thư mục

Mỗi đề thi được tổ chức thành **một thư mục độc lập** (bao gồm đề `.pdf`/`.md`, đáp án/HDG, script sinh đề `.py` và thư mục `assets/` chứa hình vẽ riêng của đề đó):

```text
├── De_200/ ... De_201/  # Form chuẩn mới nhất (ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA)
├── De_108/ ... De_115/  # Bộ đề Khảo sát chất lượng & Ôn luyện tổng hợp Toán 12
├── De_107/              # Chuyên đề Khảo sát Hàm số
├── De_105/ ... De_106/  # Đề thi thử Giữa kì 1 Toán 12
├── De_101/ ... De_104/  # Bộ đề Ôn thi Giữa kì 1 (Đề 01 – 04) & De_101_Mo_Dau/
└── Bai_Tap_Luyen_Them/  # Tài liệu Bài tập luyện thêm
```

---

## 1. Mục lục Đề thi & Đáp án / Hướng dẫn giải (HDG)

### 1.1. Đề Thi Thử Kì Thi TNTHPT Quốc Gia (Form chuẩn mới nhất)

Bao phủ toàn bộ chương trình Toán THPT theo cấu trúc kì thi TNTHPT 2025–2026 gồm 3 phần (12 câu TNKQ, 4 câu Đúng/Sai, 6 câu Trả lời ngắn) trình bày chuẩn 4 trang A4.

| Mã đề | Thư mục | Nội dung | Đề thi | Bảng đáp án | Đáp án & HDG chi tiết | Script tạo đề |
|:---:|:---|:---|:---:|:---:|:---:|:---|
| **201** | [De_201/](De_201/) | Đề thi thử Kì thi TNTHPT Quốc gia *(Form chuẩn mới 11.5pt)* | [PDF](De_201/De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_201.pdf) · [MD](De_201/De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_201.md) | [MD](De_201/Bang_Dap_An_De_201.md) | [PDF](De_201/Bang_Dap_An_Va_HDG_De_201.pdf) · [MD](De_201/Bang_Dap_An_Va_HDG_De_201.md) | [generate_de201.py](De_201/generate_de201.py) · [generate_de201_diagrams.py](De_201/generate_de201_diagrams.py) · [generate_dap_an_201.py](De_201/generate_dap_an_201.py) |
| **200** | [De_200/](De_200/) | Đề thi thử Kì thi TNTHPT Quốc gia *(Form chuẩn mới)* | [PDF](De_200/De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_200.pdf) · [MD](De_200/De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_200.md) | [MD](De_200/Bang_Dap_An_De_200.md) | [PDF](De_200/Bang_Dap_An_Va_HDG_De_200.pdf) · [MD](De_200/Bang_Dap_An_Va_HDG_De_200.md) | [generate_de200.py](De_200/generate_de200.py) · [generate_de200_diagrams.py](De_200/generate_de200_diagrams.py) · [generate_dap_an_200.py](De_200/generate_dap_an_200.py) |

### 1.2. Bộ Đề Khảo Sát Chất Lượng & Ôn Luyện Tổng Hợp (Mã đề 106 – 115)

| Mã đề | Thư mục | Nội dung | Đề thi | Bảng đáp án | Đáp án & HDG chi tiết | Script tạo đề |
|:---:|:---|:---|:---:|:---:|:---:|:---|
| **115** | [De_115/](De_115/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_115/De_Thi_Khao_Sat_Toan_12_Ma_115.pdf) · [MD](De_115/De_Thi_Khao_Sat_Toan_12_Ma_115.md) | [MD](De_115/Bang_Dap_An_De_115.md) | [PDF](De_115/Bang_Dap_An_Va_HDG_De_115.pdf) · [MD](De_115/Bang_Dap_An_Va_HDG_De_115.md) | [generate_de115.py](De_115/generate_de115.py) · [generate_dap_an_115.py](De_115/generate_dap_an_115.py) |
| **114** | [De_114/](De_114/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_114/De_Thi_Khao_Sat_Toan_12_Ma_114.pdf) · [MD](De_114/De_Thi_Khao_Sat_Toan_12_Ma_114.md) | [MD](De_114/Bang_Dap_An_De_114.md) | [PDF](De_114/Bang_Dap_An_Va_HDG_De_114.pdf) · [MD](De_114/Bang_Dap_An_Va_HDG_De_114.md) | [generate_de114.py](De_114/generate_de114.py) · [generate_dap_an_114.py](De_114/generate_dap_an_114.py) |
| **113** | [De_113/](De_113/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_113/De_Thi_Khao_Sat_Toan_12_Ma_113.pdf) · [MD](De_113/De_Thi_Khao_Sat_Toan_12_Ma_113.md) | [MD](De_113/Bang_Dap_An_De_113.md) | [PDF](De_113/Bang_Dap_An_Va_HDG_De_113.pdf) · [MD](De_113/Bang_Dap_An_Va_HDG_De_113.md) | [generate_de113.py](De_113/generate_de113.py) · [generate_dap_an_113.py](De_113/generate_dap_an_113.py) |
| **112** | [De_112/](De_112/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_112/De_Thi_Khao_Sat_Toan_12_Ma_112.pdf) · [MD](De_112/De_Thi_Khao_Sat_Toan_12_Ma_112.md) | [MD](De_112/Bang_Dap_An_De_112.md) | [PDF](De_112/Bang_Dap_An_Va_HDG_De_112.pdf) · [MD](De_112/Bang_Dap_An_Va_HDG_De_112.md) | [generate_de112.py](De_112/generate_de112.py) · [generate_dap_an_112.py](De_112/generate_dap_an_112.py) |
| **111** | [De_111/](De_111/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_111/De_Thi_Khao_Sat_Toan_12_Ma_111.pdf) · [MD](De_111/De_Thi_Khao_Sat_Toan_12_Ma_111.md) | [MD](De_111/Bang_Dap_An_De_111.md) | [PDF](De_111/Bang_Dap_An_Va_HDG_De_111.pdf) · [MD](De_111/Bang_Dap_An_Va_HDG_De_111.md) | [generate_de111.py](De_111/generate_de111.py) · [generate_dap_an_111.py](De_111/generate_dap_an_111.py) |
| **110** | [De_110/](De_110/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_110/De_Thi_Khao_Sat_Toan_12_Ma_110.pdf) · [MD](De_110/De_Thi_Khao_Sat_Toan_12_Ma_110.md) | [MD](De_110/Bang_Dap_An_De_110.md) | [PDF](De_110/Bang_Dap_An_Va_HDG_De_110.pdf) · [MD](De_110/Bang_Dap_An_Va_HDG_De_110.md) | [generate_de110.py](De_110/generate_de110.py) · [generate_dap_an_110.py](De_110/generate_dap_an_110.py) |
| **109** | [De_109/](De_109/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_109/De_Thi_Khao_Sat_Toan_12_Ma_109.pdf) · [MD](De_109/De_Thi_Khao_Sat_Toan_12_Ma_109.md) | [MD](De_109/Bang_Dap_An_De_109.md) | [PDF](De_109/Bang_Dap_An_Va_HDG_De_109.pdf) · [MD](De_109/Bang_Dap_An_Va_HDG_De_109.md) | [generate_de109.py](De_109/generate_de109.py) · [generate_dap_an_109.py](De_109/generate_dap_an_109.py) |
| **108** | [De_108/](De_108/) | Đề ôn luyện tổng hợp Toán 12 | [PDF](De_108/De_Thi_Khao_Sat_Toan_12_Ma_108.pdf) · [MD](De_108/De_Thi_Khao_Sat_Toan_12_Ma_108.md) | [MD](De_108/Bang_Dap_An_De_108.md) | [PDF](De_108/Bang_Dap_An_Va_HDG_De_108.pdf) · [MD](De_108/Bang_Dap_An_Va_HDG_De_108.md) | [generate_de108.py](De_108/generate_de108.py) · [generate_dap_an_108.py](De_108/generate_dap_an_108.py) |
| **107** | [De_107/](De_107/) | Chuyên đề Khảo sát Hàm số (3 trang) | [PDF](De_107/De_Chuyen_De_Khao_Sat_Ham_So_Ma_107.pdf) · [MD](De_107/De_Chuyen_De_Khao_Sat_Ham_So_Ma_107.md) | — | [PDF](De_107/Bang_Dap_An_Va_HDG_De_107.pdf) · [MD](De_107/Bang_Dap_An_Va_HDG_De_107.md) | [generate_de107.py](De_107/generate_de107.py) · [generate_dap_an_107.py](De_107/generate_dap_an_107.py) |
| **106** | [De_106/](De_106/) | Đề thi thử Giữa kì 1 – Toán 12 | [PDF](De_106/De_Thi_Khao_Sat_Toan_12_Ma_106.pdf) · [MD](De_106/De_Thi_Khao_Sat_Toan_12_Ma_106.md) | — | [MD](De_106/Bang_Dap_An_Va_HDG_Ma_106.md) | [generate_de106.py](De_106/generate_de106.py) |

### 1.3. Bộ Đề Ôn Thi & Thi Thử Giữa Kì 1 Toán 12 (Mã đề 101 – 105)

| Mã đề | Thư mục | Nội dung | Đề thi | Đáp án & HDG | Script tạo đề |
|:---:|:---|:---|:---:|:---:|:---|
| **105** | [De_105/](De_105/) | Đề thi thử Giữa kì 1 – Toán 12 | [PDF](De_105/De_Thi_Thu_Giua_Ki_1_Toan_12.pdf) · [MD](De_105/De_Thi_Thu_Giua_Ki_1_Toan_12.md) | [PDF](De_105/Bang_Dap_An_Va_HDG_De_Thi_Thu_GK1_Toan_12.pdf) · [MD](De_105/Bang_Dap_An_Va_HDG_De_Thi_Thu_GK1_Toan_12.md) | [generate_de_thi_thu_gk1.py](De_105/generate_de_thi_thu_gk1.py) · [generate_dap_an_pdf.py](De_105/generate_dap_an_pdf.py) |
| **104** | [De_104/](De_104/) | Đề ôn thi Giữa kì 1 – Đề số 04 | [PDF](De_104/De_On_Thi_Giua_Ki_1_Toan_12_De_04.pdf) · [MD](De_104/De_Thi_Khao_Sat_Toan_12_De_04.md) | — | [generate_de4.py](De_104/generate_de4.py) |
| **103** | [De_103/](De_103/) | Đề ôn thi Giữa kì 1 – Đề số 03 | [PDF](De_103/De_On_Thi_Giua_Ki_1_Toan_12_De_03.pdf) · [MD](De_103/De_Thi_Khao_Sat_Toan_12_De_03.md) | [MD](De_103/Giai_Chi_Tiet_De_On_Thi_Giua_Ki_1_De_03.md) | [generate_de3.py](De_103/generate_de3.py) · [generate_de3_khao_sat.py](De_103/generate_de3_khao_sat.py) |
| **102** | [De_102/](De_102/) | Đề ôn thi Giữa kì 1 – Đề số 02 | [PDF](De_102/De_On_Thi_Giua_Ki_1_Toan_12_De_02.pdf) · [MD](De_102/De_Thi_Khao_Sat_Toan_12_De_02.md) | [MD](De_102/Giai_Chi_Tiet_De_On_Thi_Giua_Ki_1_De_02.md) | [generate_de2.py](De_102/generate_de2.py) · [generate_de2_khao_sat.py](De_102/generate_de2_khao_sat.py) |
| **101** | [De_101/](De_101/) | Đề ôn thi Giữa kì 1 – Đề số 01 | [PDF](De_101/De_On_Thi_Giua_Ki_1_Toan_12_De_01.pdf) · [MD](De_101/De_Thi_Khao_Sat_Toan_12_De_01.md) | — | [generate_de1.py](De_101/generate_de1.py) |
| **101*** | [De_101_Mo_Dau/](De_101_Mo_Dau/) | Đề ôn thi Giữa kì 1 *(bản khởi đầu)* | [PDF](De_101_Mo_Dau/De_On_Thi_Giua_Ki_1_Toan_12.pdf) · [MD](De_101_Mo_Dau/De_Thi_Khao_Sat_Toan_12.md) | — | [generate_pdf.py](De_101_Mo_Dau/generate_pdf.py) · [generate_perfect_exam.py](De_101_Mo_Dau/generate_perfect_exam.py) |

### 1.4. Tài Liệu Bài Tập Luyện Thêm

| Thư mục | Tên tài liệu | Tài liệu | Script biên dịch |
|:---|:---|:---:|:---|
| [Bai_Tap_Luyen_Them/](Bai_Tap_Luyen_Them/) | Bài tập luyện thêm (10 câu) | [PDF](Bai_Tap_Luyen_Them/Bai_Tap_Luyen_Them_10_Cau.pdf) · [MD](Bai_Tap_Luyen_Them/Bai_Tap_Luyen_Them_10_Cau.md) | [generate_luyenthem_pdf.py](Bai_Tap_Luyen_Them/generate_luyenthem_pdf.py) |
| [Bai_Tap_Luyen_Them/](Bai_Tap_Luyen_Them/) | Bài tập luyện thêm Chuyên đề Khảo sát Hàm số (Nâng cao) | [PDF](Bai_Tap_Luyen_Them/Bai_Tap_Luyen_Them_Ham_So.pdf) · [MD](Bai_Tap_Luyen_Them/Bai_Tap_Luyen_Them_Ham_So.md) | [compile_bai_tap_them.py](Bai_Tap_Luyen_Them/compile_bai_tap_them.py) |

---

## 2. Hướng dẫn sử dụng Form chuẩn (Từ Mã đề 201 trở đi)

Bộ script khuôn mẫu cập nhật nằm trong thư mục **[`De_201/`](De_201/)** (kế thừa và chuẩn hóa từ [`De_200/`](De_200/)):

1. **`generate_de201_diagrams.py`** — Sinh các hình vẽ minh họa thật sự cần thiết cho Phần III bằng `matplotlib` vào `assets/` với phong cách tối giản (không chèn chú thích chữ hay số trục tọa độ dư thừa).
2. **`generate_de201.py`** — Sinh đề thi PDF chuẩn **4 trang A4** bằng HTML + KaTeX + Google Chrome headless (`De_Thi_Thu_TNTHPT_Quoc_Gia_Toan_Ma_201.pdf`), sử dụng **cỡ chữ `11.5pt` (`line-height: 1.40`) và ngắt trang tự nhiên liên tục** với quy cách chuẩn:
   - Tên kì thi trên đầu đề: **ĐỀ THI THỬ KÌ THI TNTHPT QUỐC GIA** *(không đặt dòng "ĐỀ ÔN TẬP CHÍNH THỨC" phía trên dòng "(Đề thi gồm có 04 trang)")*.
   - Khung **Mã đề** đặt ở **cột bên trái** (đánh số từ **200** trở đi).
   - **Phần I (12 câu):** Mức độ Nhận biết – Thông hiểu nhẹ nhàng (không tham số $m$, không bài đếm khó; nếu có xác suất có điều kiện thì cho công thức trực tiếp); Câu 3 là câu đạo hàm; có câu dãy số (Câu 12).
   - **Phần II (4 câu Đúng/Sai):** Không chèn đồ thị/hình vẽ; Câu 1 là dạng bài khảo sát hàm số thuần túy.
   - **Phần III (6 câu Trả lời ngắn):** Chỉ chèn hình vẽ tối giản cho các câu thật sự cần minh họa trực quan; Câu 6 kết hợp xác suất cổ điển (tổ hợp) và xác suất có điều kiện / Bayes.
3. **`generate_dap_an_201.py`** — Sinh file PDF **Bảng Đáp Án & Hướng Dẫn Giải Chi Tiết** (`Bang_Dap_An_Va_HDG_De_201.pdf`).

### Cách chạy lại (từ bên trong thư mục đề)

```bash
cd De_201
python3 generate_de201_diagrams.py
python3 generate_de201.py
python3 generate_dap_an_201.py
```

*(Lưu ý: Khi tạo đề mới `De_202/`, ... chỉ cần nhân bản thư mục `De_201/`, đổi tên file và mã đề tương ứng mà vẫn giữ nguyên CSS `@page`, cỡ chữ `11.5pt`, ngắt trang tự nhiên, bảng header và chuẩn KaTeX.)*
