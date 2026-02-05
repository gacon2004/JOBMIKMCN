@echo off
chcp 65001 > nul
echo ========================================
echo    SHOPEE AUTO PICK - GEMINI AI
echo    Build Script v1.0
echo ========================================
echo.

echo [1/4] Kiểm tra môi trường...
python --version
if errorlevel 1 (
    echo ❌ Không tìm thấy Python!
    pause
    exit /b 1
)

echo.
echo [2/4] Cài đặt PyInstaller (nếu chưa có)...
pip install pyinstaller --quiet --upgrade

echo.
echo [3/4] Dọn dẹp build cũ...
if exist "dist\ShopeeAutoPick_Gemini" rmdir /s /q "dist\ShopeeAutoPick_Gemini"
if exist "build\ShopeeAutoPick_Gemini" rmdir /s /q "build\ShopeeAutoPick_Gemini"

echo.
echo [4/4] Build app (có thể mất 2-5 phút)...
pyinstaller autoanh_gemini.spec --clean --noconfirm

if errorlevel 1 (
    echo.
    echo ❌ Build thất bại!
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Build thành công!
echo ========================================
echo.
echo 📂 Folder: dist\ShopeeAutoPick_Gemini\
echo 🚀 File: ShopeeAutoPick_Gemini.exe
echo.
echo ⚠️  Nhớ copy các file này vào folder exe:
echo    - settings.json
echo    - nsfw_mobilenet2.224x224.h5
echo    - link.xlsx (file Excel chứa links)
echo.
pause
