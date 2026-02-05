import google.generativeai as genai
import json

# Đọc API key
with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)
    api_key = settings.get('gemini_api_key')

print(f"API Key: {api_key[:10]}..." if api_key else "No API key found")

# Configure
genai.configure(api_key=api_key)

# List models
print("\n📋 Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"  ✅ {m.name}")

# Test
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Hello!")
    print(f"\n✅ Test successful: {response.text}")
except Exception as e:
    print(f"\n❌ Error: {e}")
