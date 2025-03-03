import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import subprocess
import platform
import socket
import wmi
import re
import threading
import time

class ITDesk:
    def __init__(self, master):
        self.master = master
        master.title("IT Desk Uygulaması")
        master.geometry("600x800")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="IT Desk", font=('Arial', 18, 'bold')).pack(pady=10)

        buttons_frame = ttk.Frame(self.master)
        buttons_frame.pack(pady=20)

        ttk.Button(buttons_frame, text="Sistem Bilgisi", command=self.show_system_info).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Ağ Bilgisi", command=self.show_network_info).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Disk Kullanımı", command=self.show_disk_usage).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="CPU Kullanımı", command=self.show_cpu_usage).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Bellek Kullanımı", command=self.show_memory_usage).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Sistem Güncellemeleri", command=self.show_system_updates).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Çalışan Süreçler", command=self.show_running_processes).grid(row=3, column=0, columnspan=2, pady=5)

        ttk.Button(buttons_frame, text="Disk Tarama", command=self.scan_disk).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Windows Lisans Durumu", command=self.get_license_status).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="NetBIOS Durumu", command=self.check_netbios).grid(row=5, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="ARP Tablosu", command=self.show_arp_table).grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Route Tablosu", command=self.show_route_table).grid(row=6, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="WiFi Şifresi", command=self.show_wifi_password).grid(row=6, column=1, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Windows Sürüm Bilgisi", command=self.get_windows_version).grid(row=7, column=0, columnspan=2, pady=5)
        
        ttk.Button(buttons_frame, text="Pil/Güç Durumu", command=self.show_power_status).grid(row=8, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Donanım Bilgisi", command=self.show_hardware_info).grid(row=8, column=1, padx=5, pady=5)

        self.result_text = tk.Text(self.master, height=30, width=70)
        self.result_text.pack(padx=10, pady=10)

    def show_system_info(self):
        info = get_system_info()
        self.result_text.delete(1.0, tk.END)
        for key, value in info.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")

    def show_network_info(self):
        info = get_network_info()
        self.result_text.delete(1.0, tk.END)
        for key, value in info.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")

    def show_disk_usage(self):
        usage = check_disk_usage()
        self.result_text.delete(1.0, tk.END)
        for key, value in usage.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")

    def show_cpu_usage(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"CPU Kullanımı: {check_cpu_usage()}%")

    def show_memory_usage(self):
        usage = check_memory_usage()
        self.result_text.delete(1.0, tk.END)
        for key, value in usage.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")

    def show_system_updates(self):
        self.result_text.delete(1.0, tk.END)
        try:
            if platform.system() == "Linux":
                updates = subprocess.check_output(['apt', 'list', '--upgradable'], universal_newlines=True).split('\n')[1:]
                if updates:
                    for update in updates:
                        if update:
                            self.result_text.insert(tk.END, f"{update}\n")
                else:
                    self.result_text.insert(tk.END, "Güncelleme bulunamadı.")
            elif platform.system() == "Windows":
                updates = subprocess.check_output(['wmic', 'qfe', 'list', 'brief'], universal_newlines=True).split('\n')
                if len(updates) > 1:
                    self.result_text.insert(tk.END, "Windows Güncellemeleri:\n")
                    for update in updates[1:]:
                        self.result_text.insert(tk.END, f"{update}\n")
                else:
                    self.result_text.insert(tk.END, "Güncelleme bulunamadı.")
            else:
                self.result_text.insert(tk.END, "Bu işlem bu platformda desteklenmiyor.")
        except subprocess.CalledProcessError as e:
            self.result_text.insert(tk.END, f"Hata: {e}")

    def show_running_processes(self):
        self.result_text.delete(1.0, tk.END)
        for process in list_running_processes():
            self.result_text.insert(tk.END, f"{process}\n")

    def scan_disk(self):
        self.result_text.delete(1.0, tk.END)
        for disk in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(disk.mountpoint)
                self.result_text.insert(tk.END, f"Disk: {disk.device}\n")
                self.result_text.insert(tk.END, f"Mount Point: {disk.mountpoint}\n")
                self.result_text.insert(tk.END, f"File System: {disk.fstype}\n")
                self.result_text.insert(tk.END, f"Total Size: {usage.total / (2**30):.2f} GB\n")
                self.result_text.insert(tk.END, f"Used: {usage.used / (2**30):.2f} GB\n")
                self.result_text.insert(tk.END, f"Free: {usage.free / (2**30):.2f} GB\n")
                self.result_text.insert(tk.END, f"Percent Used: {usage.percent}%\n\n")
            except PermissionError:
                continue

    def get_license_status(self):
        if platform.system() == "Windows":
            try:
                c = wmi.WMI()
                license_info = c.Win32_OperatingSystem()[0]
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Windows Sürümü: {license_info.Caption}\n")
                self.result_text.insert(tk.END, f"Lisans Durumu: {license_info.SerialNumber}\n")
                self.result_text.insert(tk.END, "Not: Lisans durumu tam olarak belirlenemez.")
            except Exception as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def check_netbios(self):
        if platform.system() == "Windows":
            try:
                netbios_status = subprocess.check_output(['netstat', '-an'], text=True)
                netbios_lines = [line for line in netbios_status.split('\n') if '139' in line or '445' in line]
                self.result_text.delete(1.0, tk.END)
                for line in netbios_lines:
                    self.result_text.insert(tk.END, f"{line}\n")
                if not netbios_lines:
                    self.result_text.insert(tk.END, "NetBIOS bağlantı noktaları (139, 445) açık değil.")
            except subprocess.CalledProcessError as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def show_arp_table(self):
        if platform.system() == "Windows":
            try:
                arp_table = subprocess.check_output(['arp', '-a'], text=True)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, arp_table)
            except subprocess.CalledProcessError as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def show_route_table(self):
        if platform.system() == "Windows":
            try:
                route_table = subprocess.check_output(['route', 'print'], text=True)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, route_table)
            except subprocess.CalledProcessError as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def show_wifi_password(self):
        if platform.system() == "Windows":
            self.result_text.delete(1.0, tk.END)
            try:
                profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
                profiles = [i.split(":")[1][1:-1] for i in profiles if "All User Profile" in i]
                for profile in profiles:
                    try:
                        wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                        password = [line for line in wifi_info if "Key Content" in line][0].split(":")[1][1:-1]
                        self.result_text.insert(tk.END, f"{profile}: {password}\n")
                    except subprocess.CalledProcessError:
                        self.result_text.insert(tk.END, f"Şifre {profile} için alınamadı\n")
            except Exception as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def get_windows_version(self):
        if platform.system() == "Windows":
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Windows Sürümü: {platform.system()} {platform.release()} {platform.version()}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def show_power_status(self):
        if platform.system() == "Windows":
            battery = psutil.sensors_battery()
            if battery:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Pil Yüzdesi: {battery.percent}%\n")
                self.result_text.insert(tk.END, f"Şarj Durumu: {'Şarj oluyor' if battery.power_plugged else 'Şarj olmuyor'}\n")
                self.result_text.insert(tk.END, f"Kalan Pil Süresi: {time.strftime('%H:%M:%S', time.gmtime(battery.secsleft))} (tahmini)")
            else:
                self.result_text.insert(tk.END, "Pil bilgisi bulunamadı.")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

    def show_hardware_info(self):
        if platform.system() == "Windows":
            self.result_text.delete(1.0, tk.END)
            try:
                c = wmi.WMI()
                
                for cpu in c.Win32_Processor():
                    self.result_text.insert(tk.END, f"CPU: {cpu.Name}\n")
                
                for memory in c.Win32_PhysicalMemory():
                    self.result_text.insert(tk.END, f"RAM: {int(memory.Capacity) // (1024 ** 3)} GB {memory.Speed}MHz\n")
                
                for board in c.Win32_BaseBoard():
                    self.result_text.insert(tk.END, f"Anakart: {board.Product}\n")
                
                for gpu in c.Win32_VideoController():
                    self.result_text.insert(tk.END, f"Ekran Kartı: {gpu.Name}\n")
                
                for drive in c.Win32_DiskDrive():
                    self.result_text.insert(tk.END, f"Sabit Disk: {drive.Model}\n")
                
            except Exception as e:
                self.result_text.insert(tk.END, f"Hata: {e}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Bu işlem sadece Windows üzerinde çalışır.")

def get_system_info():
    return {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version()
    }

def get_network_info():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "IP bulunamadı"
    return {"Hostname": hostname, "IP Address": ip_address}

def check_disk_usage(disk='/'):
    usage = psutil.disk_usage(disk)
    return {
        "Total": f"{usage.total / (2**30):.2f} GB",
        "Used": f"{usage.used / (2**30):.2f} GB",
        "Free": f"{usage.free / (2**30):.2f} GB",
        "Percent Used": f"{usage.percent}%"
    }

def check_cpu_usage():
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "Total": f"{memory.total / (1024 * 1024):.2f} MB",
        "Available": f"{memory.available / (1024 * 1024):.2f} MB",
        "Used": f"{memory.used / (1024 * 1024):.2f} MB",
        "Percentage": f"{memory.percent}%"
    }

def list_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User: {proc.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes[:10]

if __name__ == "__main__":
    root = tk.Tk()
    app = ITDesk(root)
    root.mainloop()