# 🔑 CÁCH LẤY MACHINE ID

## 📌 3 Cách lấy Machine ID:

---

## ✅ CÁCH 1: Chạy tool lần đầu (Dễ nhất)

**Bước 1:** Double click file `autoanh_gemini.exe`

**Bước 2:** Nếu chưa đăng ký, tool sẽ tự động hiện popup:

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

**Bước 3:** Copy Machine ID từ popup → Gửi cho admin

---

## ✅ CÁCH 2: Dùng lệnh (Nhanh nhất)

**Nếu dùng Python:**
```bash
python autoanh_gemini.py --show-id
```

**Nếu dùng EXE:**
```bash
autoanh_gemini.exe --show-id
```

Tool sẽ hiển thị:
```
🖥️ MACHINE ID CỦA MÁY NÀY
======================================================================
Machine ID: abc123def456

📋 Hướng dẫn:
1. Copy Machine ID này
2. Gửi cho admin để đăng ký license
3. Đợi admin thêm vào database
4. Chạy lại tool

⚠️ Mỗi máy có Machine ID khác nhau!
======================================================================
```

---

## ✅ CÁCH 3: Từ terminal/cmd

**Mở PowerShell hoặc CMD:**

**Nếu dùng Python:**
```powershell
cd D:\KHONGGIANLAMVIEC\nhandienvatthe
python autoanh_gemini.py --show-id
```

**Nếu dùng EXE:**
```powershell
cd D:\Path\To\Tool
autoanh_gemini.exe --show-id
```

---

## 📋 SAU KHI CÓ MACHINE ID:

### Khách hàng:
1. ✅ Copy Machine ID (VD: `abc123def456`)
2. ✅ Gửi cho admin qua Zalo/Email/Telegram
3. ✅ Đợi admin xác nhận đã thêm vào database
4. ✅ Chạy lại tool → Thành công!

### Admin:
1. ✅ Nhận Machine ID từ khách
2. ✅ Mở Google Sheets: https://docs.google.com/spreadsheets/d/17Q_J2X1q3-y1oJdZq8K2E19ATsv6L8156js-uSyw0EQ/edit
3. ✅ Thêm Machine ID vào cột `key`
4. ✅ Save → Thông báo khách chạy lại

---

## ❓ FAQ

**Q: Machine ID là gì?**
A: Là mã định danh duy nhất của máy tính, dựa trên hostname, architecture và MAC address.

**Q: Machine ID có thể thay đổi không?**
A: Chỉ thay đổi khi đổi tên máy hoặc thay network card. Rất hiếm khi thay đổi.

**Q: Mỗi máy có Machine ID khác nhau?**
A: Có, mỗi máy có Machine ID riêng biệt.

**Q: Muốn dùng nhiều máy?**
A: Cần gửi Machine ID của từng máy cho admin để đăng ký riêng.

---

## 💡 VÍ DỤ

**Machine ID thường có dạng:**
- `abc123def456` (16 ký tự hex)
- `f3a9b2c8d1e4f5a6`
- `1a2b3c4d5e6f7g8h`

**Copy chính xác toàn bộ chuỗi và gửi cho admin!**

---

## 📞 Liên hệ hỗ trợ

Nếu gặp khó khăn, liên hệ admin:
- Email: [Thêm email]
- Zalo/Phone: [Thêm số]
- Telegram: [Thêm username]
