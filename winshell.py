#windowstaki bazı işlemleri görevleri otomatikleştirme
import winshell

winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
print("Çöp Kutusu Basarıyla Silindi.")