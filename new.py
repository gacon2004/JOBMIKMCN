# -*- coding: utf-8 -*-
"""
SHOPEE AUTO PICK - GEMINI AI VERSION
Chọn ảnh tốt nhất từ Shopee cho video Veo3 bằng Gemini Vision API
"""
import os, time, glob, subprocess, threading, json, sys
from pathlib import Path
import hashlib
import platform
import uuid
import requests
import random  # ADDED
from bs4 import BeautifulSoup  # ADDED

# GUI / Image
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import pandas as pd
def build_ui(self):
    # Khởi tạo toàn bộ giao diện, bao gồm log_text
    header = tk.Frame(self, bg="#1a1a2e", height=80)
    header.pack(side=tk.TOP, fill=tk.X)

    title_frame = tk.Frame(header, bg="#1a1a2e")
    title_frame.pack(expand=True)

    tk.Label(
        title_frame,
        text="🤖 SHOPEE AUTO PICK",
        bg="#1a1a2e",
        fg="#00d4ff",
        font=("Segoe UI", 20, "bold")
    ).pack()

    tk.Label(
        title_frame,
        text="Powered by Gemini AI 2.5 Flash",
        bg="#1a1a2e",
        fg="#a0a0a0",
        font=("Segoe UI", 10, "italic")
    ).pack()

    mode_container = tk.Frame(self, bg="#f5f5f5")
    mode_container.pack(side=tk.TOP, fill=tk.X, padx=15, pady=15)

    mode_frame = tk.Frame(mode_container, bg="white", relief=tk.SOLID, borderwidth=1)
    mode_frame.pack(fill=tk.X, padx=5, pady=5)

    mode_header = tk.Frame(mode_frame, bg="#3498db", height=40)
    mode_header.pack(fill=tk.X)

    tk.Label(
        mode_header,
        text="⚙️ CHẾ ĐỘ CHỌN ẢNH",
        bg="#3498db",
        fg="white",
        font=("Segoe UI", 11, "bold")
    ).pack(side=tk.LEFT, padx=15, pady=8)

    mode_options = tk.Frame(mode_frame, bg="white")
    mode_options.pack(fill=tk.X, padx=20, pady=15)

    opt1_frame = tk.Frame(mode_options, bg="#e8f5e9", relief=tk.RAISED, borderwidth=2)
    opt1_frame.pack(side=tk.LEFT, padx=10, ipadx=15, ipady=10)

    self.radio_mode1 = tk.Radiobutton(
        opt1_frame,
        text="🤖 Gemini AI",
        variable=self.pick_mode,
        value=1,
        font=("Segoe UI", 11, "bold"),
        bg="#e8f5e9",
        fg="#2e7d32",
        selectcolor="#c8e6c9",
        activebackground="#e8f5e9",
        cursor="hand2"
    )
    self.radio_mode1.pack(anchor=tk.W)

    tk.Label(
        opt1_frame,
        text="✓ AI chọn ảnh tốt nhất\n✓ Lọc ảnh xấu tự động\n✓ Độ chính xác cao",
        bg="#e8f5e9",
        fg="#555",
        font=("Segoe UI", 9),
        justify=tk.LEFT
    ).pack(anchor=tk.W, padx=20)

    opt2_frame = tk.Frame(mode_options, bg="#fff3e0", relief=tk.RAISED, borderwidth=2)
    opt2_frame.pack(side=tk.LEFT, padx=10, ipadx=15, ipady=10)

    self.radio_mode2 = tk.Radiobutton(
        opt2_frame,
        text="⚡ Auto Nhanh",
        variable=self.pick_mode,
        value=2,
        font=("Segoe UI", 11, "bold"),
        bg="#fff3e0",
        fg="#e65100",
        selectcolor="#ffe0b2",
        activebackground="#fff3e0",
        cursor="hand2"
    )
    self.radio_mode2.pack(anchor=tk.W)

    tk.Label(
        opt2_frame,
        text="✓ Chọn ảnh đầu tiên\n✓ Xử lý siêu nhanh\n✓ Tiết kiệm API",
        bg="#fff3e0",
        fg="#555",
        font=("Segoe UI", 9),
        justify=tk.LEFT
    ).pack(anchor=tk.W, padx=20)

    ctrl_container = tk.Frame(self, bg="#f5f5f5")
    ctrl_container.pack(side=tk.TOP, fill=tk.X, padx=15, pady=(0, 15))

    ctrl = tk.Frame(ctrl_container, bg="white", relief=tk.SOLID, borderwidth=1)
    ctrl.pack(fill=tk.X, padx=5, pady=5)

    ctrl_inner = tk.Frame(ctrl, bg="white")
    ctrl_inner.pack(padx=15, pady=15)

    btn_frame = tk.Frame(ctrl_inner, bg="white")
    btn_frame.pack(side=tk.LEFT)

    self.btn_start = tk.Button(
        btn_frame,
        text="▶ BẮT ĐẦU",
        bg="#27ae60",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=14,
        height=2,
        relief=tk.FLAT,
        cursor="hand2",
        command=self.on_start
    )
    self.btn_start.pack(side=tk.LEFT, padx=5)
    self.btn_start.bind("<Enter>", lambda e: self.btn_start.config(bg="#229954"))
    self.btn_start.bind("<Leave>", lambda e: self.btn_start.config(bg="#27ae60"))

    self.btn_stop = tk.Button(
        btn_frame,
        text="⏹ DỪNG LẠI",
        bg="#e74c3c",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=14,
        height=2,
        relief=tk.FLAT,
        cursor="hand2",
        command=self.on_stop,
        state=tk.DISABLED
    )
    self.btn_stop.pack(side=tk.LEFT, padx=5)
    self.btn_stop.bind("<Enter>", lambda e: self.btn_stop.config(bg="#c0392b") if self.btn_stop['state'] == 'normal' else None)
    self.btn_stop.bind("<Leave>", lambda e: self.btn_stop.config(bg="#e74c3c") if self.btn_stop['state'] == 'normal' else None)

    info_frame = tk.Frame(ctrl_inner, bg="#ecf0f1", relief=tk.SOLID, borderwidth=1)
    info_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

    key_count = len(_API_KEYS_LIST) if _API_KEYS_LIST else 1

    tk.Label(
        info_frame,
        text=f"📁 File Excel",
        bg="#ecf0f1",
        fg="#7f8c8d",
        font=("Segoe UI", 9)
    ).pack(anchor=tk.W, padx=10, pady=(10, 0))

    tk.Label(
        info_frame,
        text=os.path.basename(self.settings['excel_file']),
        bg="#ecf0f1",
        fg="#2c3e50",
        font=("Segoe UI", 10, "bold")
    ).pack(anchor=tk.W, padx=10)

    edit_frame = tk.LabelFrame(info_frame, text="⚙️ Tuỳ chỉnh cấu hình", bg="#ecf0f1", fg="#34495e", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
    edit_frame.pack(anchor=tk.W, fill=tk.X, padx=10, pady=(15, 10))

    tk.Label(edit_frame, text="⏱️ Thời gian chờ mở link (giây):", bg="#ecf0f1", fg="#7f8c8d", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w")
    self.open_link_delay_var = tk.StringVar(value=str(self.settings.get('open_link_delay', 2)))
    open_link_delay_entry = tk.Entry(edit_frame, textvariable=self.open_link_delay_var, width=8, font=("Segoe UI", 10))
    open_link_delay_entry.grid(row=0, column=1, padx=(8,0), pady=3, sticky="w")

    tk.Label(edit_frame, text="🔑 Danh sách Gemini API Key:", bg="#ecf0f1", fg="#7f8c8d", font=("Segoe UI", 9)).grid(row=1, column=0, sticky="nw", pady=(10,0))
    self.api_keys_text = tk.Text(edit_frame, height=key_count if key_count < 8 else 8, width=38, font=("Consolas", 9), bg="#f8f8ff")
    self.api_keys_text.grid(row=1, column=1, padx=(8,0), pady=(10,0), sticky="w")
    for k in _API_KEYS_LIST:
        self.api_keys_text.insert(tk.END, k + "\n")
    tk.Label(edit_frame, text="(Nhập mỗi key trên 1 dòng)", bg="#ecf0f1", fg="#b2bec3", font=("Segoe UI", 8, "italic")).grid(row=2, column=1, sticky="w", padx=(8,0))

    save_btn = tk.Button(edit_frame, text="💾 Lưu cấu hình", bg="#27ae60", fg="white", font=("Segoe UI", 11, "bold"), command=self.save_settings, cursor="hand2")
    save_btn.grid(row=3, column=1, sticky="e", pady=(15,0))

    # Khởi tạo khung nhật ký và preview ảnh ngay từ đầu
    content = tk.Frame(self, bg="#f5f5f5")
    content.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

    left_container = tk.Frame(content, bg="white", relief=tk.SOLID, borderwidth=1)
    left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 7))

    log_header = tk.Frame(left_container, bg="#34495e", height=35)
    log_header.pack(fill=tk.X)

    tk.Label(
        log_header,
        text="📋 NHẬT KÝ XỬ LÝ",
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).pack(side=tk.LEFT, padx=15, pady=7)

    log_content = tk.Frame(left_container, bg="white")
    log_content.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

    self.log_text = tk.Text(
        log_content,
        wrap=tk.WORD,
        font=("Consolas", 9),
        bg="#fafafa",
        fg="#2c3e50",
        relief=tk.FLAT,
        padx=10,
        pady=10
    )
    self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scroll = tk.Scrollbar(log_content, command=self.log_text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    self.log_text.config(yscrollcommand=scroll.set)

    right_container = tk.Frame(content, bg="white", relief=tk.SOLID, borderwidth=1, width=420, height=520)
    right_container.pack(side=tk.RIGHT, fill=tk.Y, padx=(7, 5), pady=10)
    right_container.pack_propagate(False)

    preview_header = tk.Frame(right_container, bg="#34495e", height=40)
    preview_header.pack(fill=tk.X)

    tk.Label(
        preview_header,
        text="🖼️ XEM TRƯỚC ẢNH",
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 12, "bold")
    ).pack(side=tk.LEFT, padx=15, pady=8)

    preview_content = tk.Frame(right_container, bg="#f5f5f5")
    preview_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    self.preview_label = tk.Label(
        preview_content,
        bg="#ecf0f1",
        text="Chưa có ảnh",
        fg="#95a5a6",
        font=("Segoe UI", 14, "bold"),
        relief=tk.SOLID,
        borderwidth=2,
        anchor="center"
    )
    self.preview_label.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
if isinstance(api_keys, str):
    _API_KEYS_LIST = [api_keys]
elif isinstance(api_keys, list):
    _API_KEYS_LIST = api_keys
else:
    _API_KEYS_LIST = []

_CURRENT_API_KEY_INDEX = 0
print(f"📝 Đã load {len(_API_KEYS_LIST)} API key(s)")

def is_quota_error(error_msg):
    quota_keywords = [
        "quota",
        "rate limit",
        "429",
        "RESOURCE_EXHAUSTED",
        "quota exceeded",
        "limit exceeded"
    ]
    error_lower = str(error_msg).lower()
    return any(kw.lower() in error_lower for kw in quota_keywords)

def pick_best_image_with_gemini(file_list, gemini_api_keys=None):
    """
    🤖 GEMINI AI - Chọn ảnh tốt nhất cho Veo3
    """
    global _NSFWO_G, _API_KEYS_LIST, _CURRENT_API_KEY_INDEX
    
    print(f"\n🤖 GEMINI AI - Đang phân tích {len(file_list)} ảnh...")
    
    # BƯỚC 1: NSFW Check + Quality Filter
    safe_files = []
    for p in file_list:
        if is_sensitive_image(p, _NSFWO_G):
            print(f"🚫 Ảnh nhạy cảm (bỏ qua): {os.path.basename(p)}")
            continue
        
        try:
            img = _safe_read_image(p)
            if img is None:
                continue
            h, w = img.shape[:2]
            
            if min(h, w) < 600:
                print(f"🚫 Độ phân giải thấp ({w}x{h}): {os.path.basename(p)}")
                continue
            
            aspect = w / h
            if aspect < 0.5 or aspect > 2.5:
                print(f"🚫 Tỷ lệ khung hình lệch ({aspect:.2f}): {os.path.basename(p)}")
                continue
            
            safe_files.append(p)
        except:
            continue
    
    if not safe_files:
        print("❌ Không có ảnh hợp lệ sau khi lọc")
        return None, -1
    
    print(f"✅ Còn {len(safe_files)} ảnh hợp lệ, gửi cho Gemini...")
    
    # BƯỚC 2: GỬI CHO GEMINI (với retry khi hết quota)
    max_retries = len(_API_KEYS_LIST) if _API_KEYS_LIST else 1
    
    prompt = f"""Bạn là chuyên gia chọn ảnh cho video quảng cáo Veo3. Tôi có {len(safe_files)} ảnh sản phẩm từ Shopee.

NHIỆM VỤ:
1. Phân tích tất cả ảnh để hiểu sản phẩm đang bán là gì
2. Chọn 1 ảnh TỐT NHẤT để làm video quảng cáo Veo3

TIÊU CHÍ CHỌN:
✅ ẢNH TỐT (ƯU TIÊN CHỌN):

- Ưu tiên Ảnh sản phẩm rõ ràng, chuyên nghiệp
- Ưu tiên nền 1 màu , sạch sẽ
- Sản phẩm ở giữa, góc chụp đẹp
- Ưu tiên chọn ảnh 1 sản phẩm
- có thể có người cầm hoặc đang sử dụng sản phẩm 
- Hạn chế chứa chữ quảng cáo, logo, hay watermark.
- VD: chai mỹ phẩm trên nền trắng, túi da, pin dự phòng

❌ ẢNH CẤM (Không chọn):
- không đồ nhái thương hiệu (logo fake, tên thương hiệu giả mạo)
- không đồ cấm như bia rượu, vật sắc nhọn
- Giấy tờ bảo hành, chứng nhận
- Hướng dẫn sử dụng
- Bảng thành phần với nhiều icon tròn/vuông
- Chính sách cam kết 
- Ảnh mờ, screenshot
- không sản phẩm tình dục : bao cao su, sextoy, các sản phẩm hỗ trợ 18+
- Không mô hình búp bê sexy
- Khiêu dâm/Phản cảm: Đồ lót, nội y, bikini, trang phục bó sát lộ rõ đường nét, hở ngực, lộ khe mông, tập trung vào bộ phận nhạy cảm (kể cả bị che/làm mờ).
- Vũ khí, vật sắc nhọn, Dao , máu me, vết thương, tai nạn.
- Hàng cấm: Bia, rượu, thuốc lá, ma túy, chất cấm.
- không chọn hình ảnh hở đùi nhiều, hở bụng, ngực, lưng.
- Không chọn hình ảnh có trẻ em.

⚠️ ĐẶC BIỆT:
- Nếu phát hiện đồ lót/nội y → Trả về {{"best_image_index": -1, "reason": "REJECT_SENSITIVE"}}
- Nếu KHÔNG có ảnh nào đạt chuẩn → {{"best_image_index": -1, "reason": "No good product photo"}}

TRẢ LỜI (JSON format):
{{
  "product_type": "Tên sản phẩm (VD: Sữa rửa mặt, Túi da, Pin dự phòng...)",
  "best_image_index": 0,
  "reason": "Lý do chọn ảnh này (1 câu ngắn)"
}}

CHÚ Ý: Index đếm từ 0. Ảnh đầu tiên là index 0, ảnh thứ 2 là index 1, etc.
"""
    
    # Load tất cả ảnh (copy vào memory để tránh file lock)
    images = []
    for p in safe_files:
        try:
            with PILImage.open(p) as img:
                img_copy = img.copy()
                images.append(img_copy)
        except:
            continue
    
    if not images:
        print("❌ Không thể load ảnh")
        return None, -1
    
    # Retry loop với nhiều API keys
    for retry in range(max_retries):
        try:
            current_key = _API_KEYS_LIST[_CURRENT_API_KEY_INDEX] if _API_KEYS_LIST else gemini_api_keys
            
            model = load_gemini_model(current_key)
            if model is None:
                print("❌ Gemini không khả dụng")
                if retry < max_retries - 1:
                    get_next_api_key()
                    continue
                return None, -1
            
            print(f"📤 Đang gửi {len(images)} ảnh cho Gemini AI...")
            
            response = model.generate_content([prompt] + images)
            result_text = response.text.strip()
            
            print(f"\n🤖 Gemini phản hồi:\n{result_text}\n")
            
            import re
            json_match = re.search(r'\{[^}]+\}', result_text, re.DOTALL)
            if not json_match:
                index_match = re.search(r'"best_image_index"\s*:\s*(\d+)', result_text)
                if index_match:
                    best_idx = int(index_match.group(1))
                else:
                    print("❌ Không parse được JSON")
                    return None, -1
            else:
                result_json = json.loads(json_match.group(0))
                best_idx = result_json.get('best_image_index', -1)
                product_type = result_json.get('product_type', 'Unknown')
                reason = result_json.get('reason', '')

                print(f"📦 Sản phẩm: {product_type}")
                print(f"💡 Lý do: {reason}")

                if "REJECT_SENSITIVE" in reason or "No good" in reason or best_idx == -1:
                    print(f"🚫 Gemini từ chối: {reason}")
                    return None, -1

            if best_idx < 0 or best_idx >= len(safe_files):
                print(f"❌ Index không hợp lệ: {best_idx}")
                return None, -1

            best_path = safe_files[best_idx]

            original_idx = file_list.index(best_path) + 1

            print(f"✅ Gemini chọn: {os.path.basename(best_path)} (#{original_idx})")

            return best_path, original_idx
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Gemini error: {error_msg}")
            
            if is_quota_error(error_msg):
                print(f"⚠️ API Key #{_CURRENT_API_KEY_INDEX + 1} hết quota!")
                
                if retry < max_retries - 1:
                    next_key = get_next_api_key()
                    print(f"🔄 Đổi sang API Key #{_CURRENT_API_KEY_INDEX + 1}...")
                    time.sleep(1)
                    continue
                else:
                    print(f"❌ Tất cả {len(_API_KEYS_LIST)} API keys đều hết quota!")
                    return None, -1
            else:
                import traceback
                traceback.print_exc()
                return None, -1
    
    print("❌ Không thể kết nối Gemini sau nhiều lần thử")
    return None, -1

# ========= BACKEND LOGIC (MỚI) =========

SHOPEE_CDN_HOST = "https://down-vn.img.susercontent.com/"
HEADERS_SPOOFED = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://shopee.vn/', 
}

def extract_image_urls_from_shopee(html_content):
    """Trích xuất URL ảnh (image hashes) từ mã HTML của Shopee."""
    soup = BeautifulSoup(html_content, 'html.parser')
    image_hashes = []
    
    # Tìm thẻ img hoặc div/picture trong gallery
    image_tags = soup.select('.shopee-product-gallery__picture, .shopee-photo-item img')
    
    for tag in image_tags:
        hash_part = None
        
        # Thử lấy từ thuộc tính src/data-src
        src = tag.get('src') or tag.get('data-src')
        if src and SHOPEE_CDN_HOST in src:
            hash_part = src.split('/')[-1]
        
        # Thử lấy từ style (background-image)
        if not hash_part:
            style = tag.get('style')
            if style and 'background-image' in style:
                match = re.search(r'url\("(.+?)"\)', style)
                if match and SHOPEE_CDN_HOST in match.group(1):
                     hash_part = match.group(1).split('/')[-1]
                     
        if hash_part and len(hash_part) > 10 and hash_part not in image_hashes:
            image_hashes.append(hash_part)
            
    # Xây dựng lại URL đầy đủ từ hash
    return [f"{SHOPEE_CDN_HOST}{hash_part}" for hash_part in image_hashes]

def direct_download_images(image_urls, download_dir):
    """Tải ảnh tuần tự với độ trễ ngẫu nhiên (An toàn)."""
    downloaded_files = []
    
    for i, url in enumerate(image_urls):
        
        # *** ĐỘ TRỄ NGẪU NHIÊN BẮT BUỘC ***
        delay = random.uniform(4, 10) # Chờ từ 4 đến 10 giây
        print(f"⏳ Đang chờ {delay:.2f} giây trước khi tải ảnh {i+1}/{len(image_urls)}...")
        time.sleep(delay)
        
        try:
            response = requests.get(url, headers=HEADERS_SPOOFED, timeout=30)
            
            if response.status_code == 200 and response.content:
                file_path = os.path.join(download_dir, f"{i+1}.jpg")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                
                downloaded_files.append(file_path)
                print(f"✅ Đã tải thành công ảnh #{i+1}")
            else:
                print(f"❌ Lỗi tải ảnh #{i+1}: Status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Lỗi kết nối khi tải ảnh #{i+1}: {e}")
            
    return downloaded_files

# ========= CHROME AUTOMATION (XÓA BỎ HOÀN TOÀN) =========
# Các hàm liên quan đến subprocess.Popen và pyautogui đã bị xóa khỏi luồng chạy chính

# ========= RUNNER THREAD (Luồng chạy mới) =========
class RunnerThread(threading.Thread):
    def __init__(self, ui):
        super().__init__(daemon=True)
        self.ui = ui
        self._stop_event = threading.Event()
    
    def stop(self):
        self._stop_event.set()
    
    def run(self):
        s = self.ui.settings
        
        ensure_dirs(s["download_dir"], s["img_done_dir"])
        excel_ensure(s["result_xlsx"])
        
        try:
            links = read_links(s["excel_file"])
        except Exception as e:
            self.ui.log(f"❌ Không đọc được Excel: {e}")
            self.ui.after(0, self.ui.on_thread_done)
            return
        
        self.ui.log(f"Tổng {len(links)} link.")
        
        for idx_link, link in enumerate(links, start=1):
            if self._stop_event.is_set():
                break
            
            clear_download_dir(s["download_dir"])
            self.ui.log(f"\n[{idx_link}] Đang xử lý link: {link}")
            
            stt = excel_next_stt(s["result_xlsx"])
            
            # --- START NEW WORKFLOW (BACKEND) ---
            
            # 1. Fetch HTML
            self.ui.log("… Tải HTML (Backend)...")
            try:
                # Sử dụng open_link_delay làm timeout cho requests
                response = requests.get(link, headers=HEADERS_SPOOFED, timeout=float(s.get("open_link_delay", 15))) 
                
                # Kiểm tra lỗi chặn (CAPTCHA/Verify)
                if response.status_code != 200 or "/verify/traffic/error" in response.url:
                    self.ui.log(f"  ❌ Lỗi: Bị Shopee chặn hoặc link không hợp lệ (Status: {response.status_code})")
                    excel_append_row(s["result_xlsx"], [stt, link, "BLOCKED"])
                    continue
                    
                html_content = response.text
                
            except requests.exceptions.RequestException as e:
                self.ui.log(f"  ❌ Lỗi kết nối: {e}")
                excel_append_row(s["result_xlsx"], [stt, link, "ERROR_NET"])
                continue
            
            # 2. Trích xuất link ảnh từ HTML
            self.ui.log("… Trích xuất link ảnh...")
            image_urls = extract_image_urls_from_shopee(html_content)
            
            if not image_urls:
                self.ui.log("  ❌ Không tìm thấy URL ảnh trong HTML.")
                excel_append_row(s["result_xlsx"], [stt, link, 0])
                continue
                
            self.ui.log(f"  ✅ Tìm thấy {len(image_urls)} URL ảnh.")
            
            # 3. Tải ảnh an toàn (CHẬM, TUẦN TỰ)
            files = direct_download_images(image_urls, s["download_dir"])
            
            # --- END NEW WORKFLOW (BACKEND) ---
            
            if not files:
                self.ui.log("  ❌ Không có ảnh nào được tải thành công.")
                excel_append_row(s["result_xlsx"], [stt, link, 0])
                continue
            
            # Tiếp tục logic Gemini/AutoFirst như cũ
            files = sorted(files, key=stable_key)
            
            pick_mode = self.ui.pick_mode.get()
            
            if pick_mode == 2:
                # OPTION 2: Tự động chọn ảnh đầu tiên
                self.ui.log("⚡ Auto chọn ảnh đầu tiên...")
                best_path = files[0]
                best_idx = 1
                
                try:
                    im = Image.open(best_path).convert("RGB")
                    self.ui.show_preview_image(im)
                except Exception as e:
                    self.ui.log(f"  ⚠️ Lỗi preview: {e}")
                
                self.ui.log(f"  ✅ Chọn ảnh #{best_idx}")
                excel_append_row(s["result_xlsx"], [stt, link, best_idx])
            else:
                # OPTION 1: Gemini AI
                self.ui.log("🤖 Gemini đang chọn ảnh tốt nhất...")
                
                best_path, best_idx = pick_best_image_with_gemini(files)
                
                if not best_path:
                    self.ui.log("  ❌ Gemini không chọn được ảnh.")
                    excel_append_row(s["result_xlsx"], [stt, link, 0])
                else:
                    try:
                        im = Image.open(best_path).convert("RGB")
                        self.ui.show_preview_image(im)
                    except Exception as e:
                        self.ui.log(f"  ⚠️ Lỗi preview: {e}")
                    
                    self.ui.log(f"  ✅ Chọn ảnh #{best_idx}")
                    excel_append_row(s["result_xlsx"], [stt, link, best_idx])
            
        self.ui.log("\n✅ Hoàn tất!")
        self.ui.after(0, self.ui.on_thread_done)

# ========= GUI (Giữ nguyên) =========
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        try:
            if sys.platform.startswith("win"):
                import ctypes
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        
        self.title("Shopee Auto Pick - Gemini AI")
        self.geometry("1200x750")
        self.minsize(1100, 650)
        self.configure(bg="#f5f5f5")
        
        self.settings = load_settings(strict=True)
        
        api_keys = self.settings.get("gemini_api_keys") or self.settings.get("gemini_api_key")
        init_api_keys(api_keys)
        
        ensure_nsfw_model(self.settings["nsfw_h5"])
        
        self.pick_mode = tk.IntVar(value=1)
        
        self.runner = None
        
        self.build_ui()
    
    def build_ui(self):
        header = tk.Frame(self, bg="#1a1a2e", height=80)
        header.pack(side=tk.TOP, fill=tk.X)
        
        title_frame = tk.Frame(header, bg="#1a1a2e")
        title_frame.pack(expand=True)
        
        tk.Label(
            title_frame,
            text="🤖 SHOPEE AUTO PICK",
            bg="#1a1a2e",
            fg="#00d4ff",
            font=("Segoe UI", 20, "bold")
        ).pack()
        
        tk.Label(
            title_frame,
            text="Powered by Gemini AI 2.5 Flash",
            bg="#1a1a2e",
            fg="#a0a0a0",
            font=("Segoe UI", 10, "italic")
        ).pack()
        
        mode_container = tk.Frame(self, bg="#f5f5f5")
        mode_container.pack(side=tk.TOP, fill=tk.X, padx=15, pady=15)
        
        mode_frame = tk.Frame(mode_container, bg="white", relief=tk.SOLID, borderwidth=1)
        mode_frame.pack(fill=tk.X, padx=5, pady=5)
        
        mode_header = tk.Frame(mode_frame, bg="#3498db", height=40)
        mode_header.pack(fill=tk.X)
        
        tk.Label(
            mode_header,
            text="⚙️ CHẾ ĐỘ CHỌN ẢNH",
            bg="#3498db",
            fg="white",
            font=("Segoe UI", 11, "bold")
        ).pack(side=tk.LEFT, padx=15, pady=8)
        
        mode_options = tk.Frame(mode_frame, bg="white")
        mode_options.pack(fill=tk.X, padx=20, pady=15)
        
        opt1_frame = tk.Frame(mode_options, bg="#e8f5e9", relief=tk.RAISED, borderwidth=2)
        opt1_frame.pack(side=tk.LEFT, padx=10, ipadx=15, ipady=10)
        
        self.radio_mode1 = tk.Radiobutton(
            opt1_frame,
            text="🤖 Gemini AI",
            variable=self.pick_mode,
            value=1,
            font=("Segoe UI", 11, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            selectcolor="#c8e6c9",
            activebackground="#e8f5e9",
            cursor="hand2"
        )
        self.radio_mode1.pack(anchor=tk.W)
        
        tk.Label(
            opt1_frame,
            text="✓ AI chọn ảnh tốt nhất\n✓ Lọc ảnh xấu tự động\n✓ Độ chính xác cao",
            bg="#e8f5e9",
            fg="#555",
            font=("Segoe UI", 9),
            justify=tk.LEFT
        ).pack(anchor=tk.W, padx=20)
        
        opt2_frame = tk.Frame(mode_options, bg="#fff3e0", relief=tk.RAISED, borderwidth=2)
        opt2_frame.pack(side=tk.LEFT, padx=10, ipadx=15, ipady=10)
        
        self.radio_mode2 = tk.Radiobutton(
            opt2_frame,
            text="⚡ Auto Nhanh",
            variable=self.pick_mode,
            value=2,
            font=("Segoe UI", 11, "bold"),
            bg="#fff3e0",
            fg="#e65100",
            selectcolor="#ffe0b2",
            activebackground="#fff3e0",
            cursor="hand2"
        )
        self.radio_mode2.pack(anchor=tk.W)
        
        tk.Label(
            opt2_frame,
            text="✓ Chọn ảnh đầu tiên\n✓ Xử lý siêu nhanh\n✓ Tiết kiệm API",
            bg="#fff3e0",
            fg="#555",
            font=("Segoe UI", 9),
            justify=tk.LEFT
        ).pack(anchor=tk.W, padx=20)
        
        ctrl_container = tk.Frame(self, bg="#f5f5f5")
        ctrl_container.pack(side=tk.TOP, fill=tk.X, padx=15, pady=(0, 15))
        
        ctrl = tk.Frame(ctrl_container, bg="white", relief=tk.SOLID, borderwidth=1)
        ctrl.pack(fill=tk.X, padx=5, pady=5)
        
        ctrl_inner = tk.Frame(ctrl, bg="white")
        ctrl_inner.pack(padx=15, pady=15)
        
        btn_frame = tk.Frame(ctrl_inner, bg="white")
        btn_frame.pack(side=tk.LEFT)
        
        self.btn_start = tk.Button(
            btn_frame,
            text="▶ BẮT ĐẦU",
            bg="#27ae60",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=14,
            height=2,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.on_start
        )
        self.btn_start.pack(side=tk.LEFT, padx=5)
        self.btn_start.bind("<Enter>", lambda e: self.btn_start.config(bg="#229954"))
        self.btn_start.bind("<Leave>", lambda e: self.btn_start.config(bg="#27ae60"))
        
        self.btn_stop = tk.Button(
            btn_frame,
            text="⏹ DỪNG LẠI",
            bg="#e74c3c",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=14,
            height=2,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.on_stop,
            state=tk.DISABLED
        )
        self.btn_stop.pack(side=tk.LEFT, padx=5)
        self.btn_stop.bind("<Enter>", lambda e: self.btn_stop.config(bg="#c0392b") if self.btn_stop['state'] == 'normal' else None)
        self.btn_stop.bind("<Leave>", lambda e: self.btn_stop.config(bg="#e74c3c") if self.btn_stop['state'] == 'normal' else None)
        
        info_frame = tk.Frame(ctrl_inner, bg="#ecf0f1", relief=tk.SOLID, borderwidth=1)
        info_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

        key_count = len(_API_KEYS_LIST) if _API_KEYS_LIST else 1

        tk.Label(
            info_frame,
            text=f"📁 File Excel",
            bg="#ecf0f1",
            fg="#7f8c8d",
            font=("Segoe UI", 9)
        ).pack(anchor=tk.W, padx=10, pady=(10, 0))

        tk.Label(
            info_frame,
            text=os.path.basename(self.settings['excel_file']),
            bg="#ecf0f1",
            fg="#2c3e50",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor=tk.W, padx=10)

        edit_frame = tk.LabelFrame(info_frame, text="⚙️ Tuỳ chỉnh cấu hình", bg="#ecf0f1", fg="#34495e", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
        edit_frame.pack(anchor=tk.W, fill=tk.X, padx=10, pady=(15, 10))

        tk.Label(edit_frame, text="⏱️ Thời gian chờ mở link (giây):", bg="#ecf0f1", fg="#7f8c8d", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w")
        self.open_link_delay_var = tk.StringVar(value=str(self.settings.get('open_link_delay', 2)))
        open_link_delay_entry = tk.Entry(edit_frame, textvariable=self.open_link_delay_var, width=8, font=("Segoe UI", 10))
        open_link_delay_entry.grid(row=0, column=1, padx=(8,0), pady=3, sticky="w")

        tk.Label(edit_frame, text="🔑 Danh sách Gemini API Key:", bg="#ecf0f1", fg="#7f8c8d", font=("Segoe UI", 9)).grid(row=1, column=0, sticky="nw", pady=(10,0))
        self.api_keys_text = tk.Text(edit_frame, height=key_count if key_count < 8 else 8, width=38, font=("Consolas", 9), bg="#f8f8ff")
        self.api_keys_text.grid(row=1, column=1, padx=(8,0), pady=(10,0), sticky="w")
        for k in _API_KEYS_LIST:
            self.api_keys_text.insert(tk.END, k + "\n")
        tk.Label(edit_frame, text="(Nhập mỗi key trên 1 dòng)", bg="#ecf0f1", fg="#b2bec3", font=("Segoe UI", 8, "italic")).grid(row=2, column=1, sticky="w", padx=(8,0))

        save_btn = tk.Button(edit_frame, text="💾 Lưu cấu hình", bg="#27ae60", fg="white", font=("Segoe UI", 11, "bold"), command=self.save_settings, cursor="hand2")
        save_btn.grid(row=3, column=1, sticky="e", pady=(15,0))
    def save_settings(self):
        new_delay = self.open_link_delay_var.get()
        try:
            new_delay_float = float(new_delay)
            self.settings['open_link_delay'] = new_delay_float
        except Exception:
            messagebox.showerror("Lỗi", "Thời gian chờ phải là số!")
            return

        keys_raw = self.api_keys_text.get("1.0", tk.END).strip()
        keys_list = [k.strip() for k in keys_raw.splitlines() if k.strip()]
        self.settings['gemini_api_keys'] = keys_list

        try:
            with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Thành công", "Đã lưu thay đổi vào settings.json!")
            init_api_keys(keys_list)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không lưu được settings.json: {e}")
        
        content = tk.Frame(self, bg="#f5f5f5")
        content.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        left_container = tk.Frame(content, bg="white", relief=tk.SOLID, borderwidth=1)
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 7))
        
        log_header = tk.Frame(left_container, bg="#34495e", height=35)
        log_header.pack(fill=tk.X)
        
        tk.Label(
            log_header,
            text="📋 NHẬT KÝ XỬ LÝ",
            bg="#34495e",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side=tk.LEFT, padx=15, pady=7)
        
        log_content = tk.Frame(left_container, bg="white")
        log_content.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        self.log_text = tk.Text(
            log_content,
            wrap=tk.WORD,
            font=("Consolas", 9),
            bg="#fafafa",
            fg="#2c3e50",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scroll = tk.Scrollbar(log_content, command=self.log_text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scroll.set)
        
        right_container = tk.Frame(content, bg="white", relief=tk.SOLID, borderwidth=1, width=420, height=520)
        right_container.pack(side=tk.RIGHT, fill=tk.Y, padx=(7, 5), pady=10)
        right_container.pack_propagate(False)

        preview_header = tk.Frame(right_container, bg="#34495e", height=40)
        preview_header.pack(fill=tk.X)

        tk.Label(
            preview_header,
            text="🖼️ XEM TRƯỚC ẢNH",
            bg="#34495e",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(side=tk.LEFT, padx=15, pady=8)

        preview_content = tk.Frame(right_container, bg="#f5f5f5")
        preview_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.preview_label = tk.Label(
            preview_content,
            bg="#ecf0f1",
            text="Chưa có ảnh",
            fg="#95a5a6",
            font=("Segoe UI", 14, "bold"),
            relief=tk.SOLID,
            borderwidth=2,
            anchor="center"
        )
        self.preview_label.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
    
    def log(self, msg):
        def _do():
            self.log_text.insert(tk.END, msg + "\n")
            self.log_text.see(tk.END)
            
        if threading.current_thread() != threading.main_thread():
            self.after(0, _do)
        else:
            _do()
    
    def show_preview_image(self, pil_img):
        def _do():
            w, h = pil_img.size
            max_w, max_h = 280, 500
            scale = min(max_w / w, max_h / h, 1.0)
            new_w = int(w * scale)
            new_h = int(h * scale)
            resized = pil_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized)
            self.preview_label.config(image=photo, text="")
            self.preview_label.image = photo
        
        if threading.current_thread() != threading.main_thread():
            self.after(0, _do)
        else:
            _do()
    
    def on_start(self):
        if self.runner and self.runner.is_alive():
            messagebox.showwarning("Cảnh báo", "Đang chạy rồi!")
            return
        
        self.log_text.delete("1.0", tk.END)
        
        mode_name = "🤖 Gemini AI" if self.pick_mode.get() == 1 else "⚡ Auto chọn ảnh đầu tiên"
        self.log(f"🚀 Bắt đầu...\n")
        self.log(f"⚙️ Chế độ: {mode_name}\n")
        
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.radio_mode1.config(state=tk.DISABLED)
        self.radio_mode2.config(state=tk.DISABLED)
        
        self.runner = RunnerThread(self)
        self.runner.start()
    
    def on_stop(self):
        if self.runner:
            self.runner.stop()
        self.log("\n⏹ Đã dừng.")
        self.on_thread_done()
    
    def on_thread_done(self):
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.radio_mode1.config(state=tk.NORMAL)
        self.radio_mode2.config(state=tk.NORMAL)

# ========= ADMIN TOOLS (Giữ nguyên) =========
def show_machine_id():
    machine_id = _get_machine_id()
    
    print("\n" + "="*70)
    print("🖥️ MACHINE ID CỦA MÁY NÀY")
    print("="*70)
    print(f"\nMachine ID: {machine_id}")
    print("\n📋 Hướng dẫn:")
    print("1. Copy Machine ID này")
    print("2. Gửi cho admin để đăng ký license")
    print("3. Đợi admin thêm vào database")
    print("4. Chạy lại tool")
    print("\n⚠️ Mỗi máy có Machine ID khác nhau!")
    print("="*70 + "\n")
    
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
        "Machine ID",
        f"🖥️ MACHINE ID CỦA MÁY NÀY\n\n"
        f"{machine_id}\n\n"
        f"📋 Hướng dẫn:\n"
        f"1. Copy Machine ID này\n"
        f"2. Gửi cho admin để đăng ký\n"
        f"3. Chạy lại tool sau khi được kích hoạt"
    )
    root.destroy()

# ========= MAIN (Giữ nguyên) =========
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--show-id":
        show_machine_id()
        sys.exit(0)
    
    if not check_license_from_google_sheet():
        print("\n❌ Tool bị chặn do chưa có license!")
        print(f"Machine ID: {_get_machine_id()}")
        print("Gửi Machine ID này cho admin để được kích hoạt.")
        sys.exit(1)
    
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khởi động:\n{e}")
        import traceback
        traceback.print_exc()