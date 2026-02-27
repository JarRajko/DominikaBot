import google.generativeai as genai

try:
    with open("gemini_key.txt", "r") as f:
        api_key = f.read().strip()
    genai.configure(api_key=api_key)

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Dostupný model: {m.name}")
except Exception as e:
    print(f"Chyba: {e}")