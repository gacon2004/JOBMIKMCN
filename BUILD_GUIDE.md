# 📦 HƯỚNG DẪN SỬ DỤNG APP - SHOPEE AUTO PICK GEMINI

## 🚀 Cách build app

### Bước 1: Mở PowerShell/CMD trong folder này
```bash
cd D:\KHONGGIANLAMVIEC\nhandienvatthe
```

### Bước 2: Chạy script build
```bash
build_app.bat
```

Hoặc chạy thủ công:
```bash
pyinstaller autoanh_gemini.spec --clean --noconfirm
```

### Bước 3: Đợi 2-5 phút
Build sẽ tạo folder: `dist\ShopeeAutoPick_Gemini\`

---

## 📁 Cấu trúc folder sau khi build

```
dist\ShopeeAutoPick_Gemini\
  ├── ShopeeAutoPick_Gemini.exe    ← File chạy chính
  ├── settings.json                 ← Config (bạn cần copy vào)
  ├── nsfw_mobilenet2.224x224.h5    ← Model NSFW (bạn cần copy vào)
  ├── link.xlsx                     ← File Excel links (bạn cần copy vào)
  ├── _internal\                    ← Các thư viện (PyInstaller tự tạo)
  └── ... (các file khác)
```

---

## ⚙️ Setup sau khi build

### 1. Copy các file cần thiết vào folder exe:
```
- settings.json
- nsfw_mobilenet2.224x224.h5
- link.xlsx
```

### 2. Chỉnh settings.json:
```json
{
  "excel_file": "link.xlsx",
  "download_dir": "fileanhtam",
  "img_done_dir": "imgdone",
  "result_xlsx": "imgdone\\result_links.xlsx",
  "chrome_exe": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "user_data_dir": "C:\\Users\\PC\\AppData\\Local\\Google\\Chrome\\User Data",
  "profile_dir_name": "Default",
  "open_link_delay": 3.2,
  "max_wait_dl": 120,
  "quiet_seconds": 5.0,
  "nsfw_h5": "nsfw_mobilenet2.224x224.h5",
  "gemini_api_keys": [
    "YOUR_API_KEY_1",
    "YOUR_API_KEY_2"
  ]
}
```

### 3. Tạo folder con:
```
mkdir fileanhtam
mkdir imgdone
```

---

## 🎯 Chạy app

### Cách 1: Double-click
- Mở folder `dist\ShopeeAutoPick_Gemini\`
- Double-click vào `ShopeeAutoPick_Gemini.exe`

### Cách 2: Command line
```bash
cd dist\ShopeeAutoPick_Gemini
ShopeeAutoPick_Gemini.exe
```

---

## 📦 Đóng gói để gửi người khác

### Nén folder thành ZIP:
```
dist\ShopeeAutoPick_Gemini\  →  ShopeeAutoPick_Gemini.zip
```

### Hoặc tạo installer (nâng cao):
Dùng **Inno Setup** hoặc **NSIS** để tạo file `setup.exe`

---

## ⚠️ Lưu ý quan trọng

### 1. Antivirus có thể chặn:
- PyInstaller thường bị Windows Defender/Antivirus báo false positive
- **Giải pháp**: Add exception cho file `.exe`

### 2. File exe khá lớn (~150-200 MB):
- Vì đóng gói cả Python + thư viện
- Bình thường!

### 3. Lần đầu chạy chậm:
- Windows cần giải nén thư viện
- Lần sau sẽ nhanh hơn

### 4. Không tự động update:
- Nếu sửa code → phải build lại
- Nếu đổi settings.json → không cần build lại

---

## 🐛 Troubleshooting

### Lỗi: "Failed to execute script"
→ Thiếu file `settings.json` hoặc `nsfw_mobilenet2.224x224.h5`

### Lỗi: "Google API key not found"
→ Chưa thêm API key vào `settings.json`

### Lỗi: "Cannot find Chrome"
→ Sai đường dẫn Chrome trong `settings.json`

### App không mở:
→ Chạy bằng CMD để xem lỗi:
```bash
cd dist\ShopeeAutoPick_Gemini
ShopeeAutoPick_Gemini.exe
```

---

## 📞 Hỗ trợ

Nếu gặp lỗi, check:
1. ✅ Đã copy đủ file vào folder exe?
2. ✅ `settings.json` đúng format?
3. ✅ Gemini API key còn quota?
4. ✅ Chrome đã cài đặt?

---

**Version**: 1.0  
**Last updated**: 2025-01-10
