# 🔑 HƯỚNG DẪN LICENSE - GOOGLE SHEETS

## 📌 Cách hoạt động

Tool kiểm tra **Machine ID** với database trên **Google Sheets**:
- Khi khởi động, tool lấy Machine ID của máy
- Đọc danh sách key từ Google Sheets
- Nếu Machine ID có trong danh sách → ✅ Cho phép chạy
- Nếu không có → ❌ Chặn và yêu cầu đăng ký

---

## 👨‍💼 DÀNH CHO ADMIN

### 1. Setup Google Sheets

**Link Sheet:** https://docs.google.com/spreadsheets/d/17Q_J2X1q3-y1oJdZq8K2E19ATsv6L8156js-uSyw0EQ/edit

**Cấu trúc:**
```
| key              |
|------------------|
| abc123def456     |
| xyz789ghi012     |
| ...              |
```

- Cột đầu tiên tên là `key`
- Mỗi dòng là 1 Machine ID hợp lệ

### 2. Quy trình bán hàng

**Khi khách hàng liên hệ mua:**

1. **Khách gửi Machine ID cho bạn**
   - Yêu cầu khách chạy tool lần đầu
   - Tool sẽ báo lỗi và hiện Machine ID
   - Khách copy Machine ID gửi cho bạn

2. **Bạn thêm vào Google Sheets**
   - Mở Google Sheets
   - Thêm Machine ID vào cột `key`
   - Save (tự động sync)

3. **Khách chạy lại tool**
   - Tool kiểm tra lại Google Sheets
   - Machine ID đã có trong danh sách
   - ✅ Cho phép chạy!

### 3. Quản lý khách hàng

**Thêm cột thông tin (optional):**
```
| key              | email               | ngày mua   | ghi chú     |
|------------------|---------------------|------------|-------------|
| abc123def456     | customer@gmail.com  | 2025-11-11 | Khách VIP   |
| xyz789ghi012     | user@email.com      | 2025-11-10 | Gói 1 năm   |
```

**Lưu ý:** Tool chỉ đọc cột đầu tiên (`key`), các cột khác dùng để bạn quản lý.

### 4. Thu hồi license

**Muốn chặn 1 khách:**
- Xóa dòng có Machine ID của khách khỏi Google Sheets
- Lần sau khách chạy tool → Bị chặn ngay

---

## 👤 DÀNH CHO KHÁCH HÀNG

### Cách kích hoạt

**Bước 1: Chạy tool lần đầu**
```
Double click autoanh_gemini.exe
```

Nếu chưa đăng ký, sẽ báo lỗi:
```
❌ TOOL CHƯA ĐƯỢC KÍCH HOẠT!

Machine ID của máy này:
abc123def456

Vui lòng:
1. Copy Machine ID này
2. Gửi cho admin để đăng ký
3. Admin sẽ thêm vào database
4. Chạy lại tool
```

**Bước 2: Gửi Machine ID cho admin**

Copy Machine ID (VD: `abc123def456`) và gửi cho admin.

**Bước 3: Đợi admin kích hoạt**

Admin sẽ thêm Machine ID vào database (1-2 phút).

**Bước 4: Chạy lại tool**

Tool sẽ kiểm tra lại và cho phép chạy:
```
✅ Tool đã được kích hoạt!

Machine ID: abc123def456

Đã xác thực với database.
```

### Lưu ý

- ⚠️ Cần **kết nối internet** để kiểm tra license
- ⚠️ Mỗi máy có Machine ID khác nhau
- ⚠️ Muốn dùng nhiều máy → Mua nhiều license

---

## 🛡️ BẢO MẬT

### Ưu điểm:

✅ **Tập trung:** Quản lý tất cả license ở 1 chỗ
✅ **Realtime:** Thêm/xóa key có hiệu lực ngay
✅ **Không hack được:** Database online, không thể fake
✅ **Dễ quản lý:** Giao diện Google Sheets quen thuộc
✅ **Theo dõi:** Biết chính xác ai đang dùng

### Cách chống chia sẻ:

1. **Machine ID unique:** Mỗi máy có ID duy nhất
2. **Database online:** Không thể hack offline
3. **Kiểm tra mỗi lần chạy:** Phải online để verify
4. **Thu hồi dễ dàng:** Xóa khỏi Sheet = chặn ngay

---

## 🔧 SETUP CHO ADMIN

### Cấu hình Google Sheets:

1. **Mở link:** https://docs.google.com/spreadsheets/d/17Q_J2X1q3-y1oJdZq8K2E19ATsv6L8156js-uSyw0EQ/edit

2. **Set quyền:**
   - File → Share → Anyone with the link can **view**
   - ⚠️ KHÔNG cho phép edit public!

3. **Thêm Machine ID:**
   - Cột A: `key`
   - Các dòng: Machine ID của khách hàng

### Nếu muốn đổi Sheet:

Sửa URL trong code:
```python
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"
```

Thay `YOUR_SHEET_ID` bằng ID Sheet của bạn.

---

## ❓ XỬ LÝ LỖI

### Lỗi: "TOOL CHƯA ĐƯỢC KÍCH HOẠT"

➡️ Machine ID chưa có trong database. Gửi Machine ID cho admin.

### Lỗi: "Không thể kiểm tra license (lỗi mạng)"

➡️ Không có internet hoặc Google Sheets bị chặn. Kiểm tra kết nối mạng.

### Lỗi: "Google Sheet trống"

➡️ Admin chưa setup Sheet hoặc Sheet sai format. Liên hệ admin.

---

## 💰 MÔ HÌNH KINH DOANH

### Lợi ích cho Admin:

✅ **Quản lý tập trung:** Tất cả license ở 1 nơi
✅ **Không cần build lại:** 1 file EXE cho tất cả
✅ **Linh hoạt:** Thêm/xóa/gia hạn license bất cứ lúc nào
✅ **Tracking:** Biết chính xác số khách đang active

### Gói bán hàng gợi ý:

**Gói cơ bản:** 1 máy - XXX VNĐ
**Gói doanh nghiệp:** 5 máy - XXX VNĐ (giảm 20%)
**Gói gia hạn:** Gia hạn thêm 1 năm - XXX VNĐ

---

## 📞 Liên hệ hỗ trợ

**Admin:** [Thêm thông tin liên hệ]
- Email:
- Zalo/Phone:
- Telegram:

---

## ✨ TÓM TẮT

**BẠN (Admin):**
1. Setup Google Sheets với cột `key`
2. Build tool 1 lần duy nhất
3. Khách gửi Machine ID → Bạn thêm vào Sheet
4. Khách chạy lại → OK!

**KHÁCH HÀNG:**
1. Chạy tool → Lấy Machine ID
2. Gửi cho admin
3. Đợi admin thêm vào database
4. Chạy lại → Xong!

**➡️ ĐƠN GIẢN, BẢO MẬT, Dễ QUẢN LÝ!** 🎉
