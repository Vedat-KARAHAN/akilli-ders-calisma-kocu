from dotenv import load_dotenv
import os
import google.generativeai as gemini

load_dotenv()
api_key = os.getenv("anahtar")  

gemini.configure(api_key=api_key)


def tavsiyeVerme(ogrenci_adi, dersler, calisma_zamani, zor_konular):
    surum = gemini.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
Benim adım {ogrenci_adi}. Şu dersleri çalışıyorum: {dersler}.
Günde  {calisma_zamani} saat çalışıyorum.
şu konularda zorlanıyorum: {zor_konular}.

Lütfen bana sade, uygulanabilir bir çalışma planı, motivasyon önerileri ve bu konuları geliştirmem için küçük ipuçları ver.
Eğitim koçu gibi konuş.
"""
    
    try:
        cevap = surum.generate_content(prompt)
        return cevap.text

    except Exception as e:
        return f"Hata oluştu: {e}"



adınız = input("Adınız:")
dersler = input("Çalıştığınız dersler (virgülle ayır):")
calisma_zamani = input("Günde kaç saat çalışıyorsunuz?:")
zor_konular = input("Zorlandığınız konular:")



print("\n📚 Akıllı Çalışma Koçu'nun Tavsiyesi:\n")

print(tavsiyeVerme(adınız, dersler, calisma_zamani, zor_konular))