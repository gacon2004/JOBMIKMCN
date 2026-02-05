# TEST MULTI API KEYS - GEMINI

## Test Case 1: Sử dụng 1 key (như cũ)

```json
{
  "gemini_api_keys": [
    "AIzaSyCswv0Cbyv-l0_inKs6QBGAQ7Z_T5-SyKw"
  ]
}
```

## Test Case 2: Sử dụng nhiều keys

```json
{
  "gemini_api_keys": [
    "AIzaSyCswv0Cbyv-l0_inKs6QBGAQ7Z_T5-SyKw",
    "AIzaSyD1234567890abcdefghijk_Key2_ABCD",
    "AIzaSyE9876543210zyxwvutsrqpo_Key3_EFGH"
  ]
}
```

## Test Case 3: Backward compatible (dùng key cũ)

```json
{
  "gemini_api_key": "AIzaSyCswv0Cbyv-l0_inKs6QBGAQ7Z_T5-SyKw"
}
```

> ✅ Vẫn hoạt động bình thường!

## Kịch bản test:

1. **Normal flow**: Key 1 hoạt động tốt → Xử lý hết links
2. **Quota exceeded**: Key 1 hết quota → Auto đổi Key 2 → Tiếp tục
3. **All keys exhausted**: Tất cả keys hết → Báo lỗi dừng lại
4. **Invalid key**: Key không hợp lệ → Skip sang key tiếp

## Expected logs:

```
📝 Đã load 3 API key(s)
🔍 Loading Gemini Vision model (Key #1)...
✅ Gemini 2.5 Flash loaded

[... sau một thời gian ...]

❌ Gemini error: 429 Resource has been exhausted
⚠️ API Key #1 hết quota!
🔄 Đổi sang API Key #2...
🔍 Loading Gemini Vision model (Key #2)...
✅ Gemini 2.5 Flash loaded
📤 Đang gửi 10 ảnh cho Gemini AI...
✅ Gemini chọn: product_03.jpg (#3)
```

## Các lỗi được xử lý:

- ✅ `RESOURCE_EXHAUSTED`
- ✅ `429 Too Many Requests`
- ✅ `quota exceeded`
- ✅ `rate limit`
- ✅ `limit exceeded`
