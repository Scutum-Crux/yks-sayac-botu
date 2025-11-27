import tweepy
from datetime import datetime
import os

# --- AYARLAR ---
# Hedef: 20 Haziran 2026, Saat 10:00
HEDEF_TARIH = datetime(2026, 6, 20, 10, 0) 
UYGULAMA_LINKI = "https://play.google.com/store/apps/details?id=senin.uygulama.adresi" # Linkini unutma

# API Anahtarları (GitHub Secrets'tan çeker)
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

def main():
    # 1. Kalan Zamanı Hesapla
    bugun = datetime.now()
    kalan = HEDEF_TARIH - bugun
    kalan_gun = kalan.days
    
    # Saati Hesapla
    kalan_saniye = kalan.seconds
    kalan_saat = kalan_saniye // 3600
    
    if kalan_gun < 0:
        print("Sınav tarihi geçti! Hedef tarihi güncellemeyi unutma.")
        return

    # 2. Akıllı Metin Oluşturma (0 Saat ise gösterme)
    if kalan_saat > 0:
        zaman_metni = f"{kalan_gun} GÜN {kalan_saat} SAAT"
    else:
        zaman_metni = f"{kalan_gun} GÜN"

    # Tweet Metni (Satır boşlukları ayarlı)
    tweet = f"📢 YKS 2026'ya Son {zaman_metni} Kaldı! ⏳\n\n" \
            f"#yks2026 #yks"

    # 3. Twitter'a Bağlan ve Gönder
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        response = client.create_tweet(text=tweet)
        print(f"✅ Başarılı! Tweet atıldı. ID: {response.data['id']}")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")

if __name__ == "__main__":
    main()
