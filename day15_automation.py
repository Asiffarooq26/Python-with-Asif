# import os
# base_path = "D:/Automation"
# for i in range(1, 6):
# folder = f"Folder_{i}"
# os.makedirs(os.path.join(base_path, folder), exist_ok=True)
# print("Folders created!")
# import os
# base_path="E:/ASD Academy"
# for i in range(1,6):
#     folder=f"Folder_{i}"
#     folder_path=os.path.join(base_path,folder)
#     print(folder_path)
#     # os.makedirs(os.path.join(base_path,folder),exist_ok=True)
#     os.makedirs((folder_path),exist_ok=True)
#     file_name = f"file_{i}.txt"
#     file_path=os.path.join(folder_path,file_name)
#     with open(file_path, "w") as f:
#         f.write(f"This is file number {i}")
#     # "E:/ASD Academy/folder_1"
# print("Folders created Succesfully")

# import os
BASE_PATH = r"E:/ASD Academy"
# for i in range(1, 6):
#     folder_path = os.path.join(BASE_PATH, f"Folder_{i}")
#     os.makedirs(folder_path, exist_ok=True)
#     file_path = os.path.join(folder_path, f"file_{i}.txt")
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write("الحمد لله ❤️ Python")
# print("Folders and files created successfully!")
import os
# prefix = "NEW_"
# print(os.listdir(BASE_PATH))
# for filename in os.listdir(BASE_PATH):
#     if filename.endswith(".txt"):
#         os.rename(filename, prefix + filename)

# import os

# BASE_PATH = r"E:/ASD Academy"
# PREFIX = "ASD_"

# for root, dirs, files in os.walk(BASE_PATH):
#     for filename in files:
#         if filename.endswith(".txt") and not filename.startswith(PREFIX):
#             print("Inside if condition")
#             old_path = os.path.join(root, filename)
#             new_path = os.path.join(root, PREFIX + filename)
#             os.rename(old_path, new_path)
#             print(filename)
#             # os.remove(filename)
# print("All files renamed successfully!")

# import os

# BASE_PATH = r"E:/ASD Academy"
# for root, dirs, files in os.walk(BASE_PATH):
#     for filename in files:
#         if filename.endswith(".txt"):
#             file_path = os.path.join(root, filename)
#             os.remove(file_path)
# print("All .txt files deleted successfully!")

#Day 2
# import shutil
# import os
# # os.makedirs("Demo Folder")
# # shutil.rmtree("Demo Folder")
# for i in range(1,6):
#     # shutil.copy(f"file_{i}.txt","hello")
#     shutil.move(f"file_{i}.txt","hello")

# from openpyxl import Workbook
# wb = Workbook()
# sheet = wb.active
# sheet["A1"] = "Name"
# sheet["B1"] = "Marks"
# sheet["C1"]="Class"
# data = [("Aman", 85,"10th"), ("Riya", 90,"11th"), ("Sam", 72,"12th")]
# for i, (name, marks,grade) in enumerate(data, start=2):
#     sheet[f"A{i}"] = name
#     sheet[f"B{i}"] = marks
#     sheet[f"C{i}"]= grade
# wb.save("students.xlsx")

# mylist=["Apple","Banana","Mango"]
# for i in enumerate(mylist,start=10):
#     print(i)
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# search = driver.find_element("name", "q")
# search.send_keys("Python automation")
# search.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

# import time
# import pyautogui
# for i in range(1,6):
#     img = pyautogui.screenshot()
#     img.save(f"screenshot{i}.png")
#     print("Taking Screenshots...")
#     time.sleep(2)