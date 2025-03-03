# İnternet hızına bakıyor
import speedtest

print("Speedtest nesnesi oluşturuluyor...")
st = speedtest.Speedtest(secure=True)

print("Sunucular listeleniyor ve en iyi sunucu seçiliyor...")
st.get_best_server()

print("İndirme hızı ölçülüyor...")
download_speed = st.download()

print("Yükleme hızı ölçülüyor...")
upload_speed = st.upload()

print("Ping değeri ölçülüyor...")
ping = st.results.ping 

# Sonuçları megabite çevirmek için bitlere bölüyoruz
download_speed_mbps = download_speed / 10**6
upload_speed_mbps = upload_speed / 10**6

print(f"İndirme hızı: {download_speed_mbps:.2f} Mbps")
print(f"Yükleme hızı: {upload_speed_mbps:.2f} Mbps")
print(f"Ping: {ping} ms")
