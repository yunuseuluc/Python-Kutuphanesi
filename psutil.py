#İşlemtim sisteminin performansı ve kaynak kullanımı izlenimi
import psutil
for proc in psutil.process_iter(['pid','name']):
    print(proc.info)

memory = psutil.virtual_memory()
print(f"Toplam bellek: {memory.total} bytes")
print(f"Kullanım bellek:{memory.used} bytes")    