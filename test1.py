# import os
# BASE_PATH = r"D:/ASD Academy"
# folder_path = os.path.join(BASE_PATH, f"Folder_{1}")
# # os.makedirs(folder_path, exist_ok=True)
# import shutil
# # shutil.rmtree(folder_path)
# # shutil.copy("a.txt", "hello/a.txt") # copy file
# shutil.move("a.txt", "hello/a.txt") # move file
# import openpyxl
# from openpyxl import Workbook
# wb = Workbook()
# sheet = wb.active
# sheet["A1"] = "Name"
# sheet["B1"] = "Marks"
# data = [("Aman", 85), ("Riya", 90), ("Sam", 72)]
# for i, (name, marks) in enumerate(data, start=2):
#     sheet[f"A{i}"] = name
#     sheet[f"B{i}"] = marks
# wb.save("students.xlsx"

import selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# search = driver.find_element("name", "q")
# search.send_keys("Python")
# search.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

# import requests
# from bs4 import BeautifulSoup
# url = "https://codewithharry.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print("Title:", soup.title.string)

# import schedule
# import time
# def job():
#     print("Running task...")
# schedule.every(1).seconds.do(job)
# # schedule.every().day.at("08:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# import pyautogui
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# import socket
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# print("Hostname:", hostname)
# print("IP Address:", ip)

# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("example.com", 80))
# client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
# data = client.recv(1024)
# print(data.decode())

# import os
# ip = input("Enter IP: ")
# response = os.system(f"ping -n 1 {ip}")
# if response == 0:
#     print("Host is alive")
# else:
#     print("Host is unreachable")


# import socket
# target = "192.168.29.232"
# # ports = [21, 22, 23, 80, 443, 3306,5432]
# for port in range(1,100):
#     sock = socket.socket()
#     sock.settimeout(1)
#     result = sock.connect_ex((target, port))
#     if result == 0:
#         print(f"[OPEN] Port {port}")
#     else:
#         print(f"[CLOSED] Port {port}")
# sock.close()


# import socket
# sock = socket.socket()
# sock.settimeout(1)
# try:
#     sock.connect(("example.com", 80))
#     sock.send(b"HEAD / HTTP/1.1\r\nHost: example.com\r\n\r\n")
#     banner = sock.recv(1024)
#     print(banner.decode())
# except:
#     print("No banner received")
# sock.close()


# import socket

# # List of common ports for quick scanning
# common_ports = [21, 22, 23, 25, 53, 80, 110, 143,
#                 443, 445, 3306, 3389, 8080, 5900,5432]

# def scan_ports(target, ports):
#     open_ports = []
#     print(f"\n[*] Scanning {target} ...")
#     for port in ports:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)  # 1 second timeout
#         result = s.connect_ex((target, port))
#         try:
#             service = socket.getservbyport(port, "tcp")
#         except:
#             service="unknown"
#         print(f"[+] Port {port} ({service}) is checked")
#         if result == 0:
#             try:
#                 service = socket.getservbyport(port, "tcp")
#             except:
#                 service = "Unknown"
#             print(f"[+] Port {port} ({service}) is OPEN")
#             open_ports.append((port, service))
#         s.close()
#     return open_ports

# # Target IP (Change to the host you want to test)
# target_ip = "192.168.29.232"

# # Run the scan
# open_ports = scan_ports(target_ip, common_ports)

# print("\nScan complete.")
# if open_ports:
#     print("Open ports found:")
#     for port, service in open_ports:
#         print(f"- {port} ({service})")
# else:
#     print("No open ports found.")


# import dns.resolver
# domain = "google.com"
# subdomains = [
# "mail", "ftp", "test", "admin", "api", "dev", "blog"]
# for sub in subdomains:
#     full_domain = f"{sub}.{domain}"
#     try:
#         result = dns.resolver.resolve(full_domain, "A")
#         print(f"[FOUND] {full_domain}")
#     except:
#         


# import time
# logfile = "activity_log.txt"
# def log_event(text):
#     with open(logfile, "a", encoding="utf-8") as f:
#         f.write(f"{time.ctime()} - {text}\n")
#         time.sleep(2)
# log_event("Program started")

import time
import pyperclip
import pyautogui
import os
import threading
logfile = "activity_log.txt"
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
def log_event(text):
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {text}\n")
def check_clipboard():
    data = pyperclip.paste()
    log_event(f"Clipboard: {data}")
def save_screenshot():
    filename = f"{screenshot_folder}/screenshot_{int(time.time())}.png"
    pyautogui.screenshot(filename)
    log_event(f"Screenshot: {filename}")
def monitor():
    for i in range(3):
        check_clipboard()
        save_screenshot()
        time.sleep(10)
log_event("Monitoring started")
monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()
monitor_thread.join()
log_event("Monitoring finished")