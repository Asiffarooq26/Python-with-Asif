# class Employee:
#     company = "Google"

#     # @classmethod #Decorator
#     # def change_company(cls, new):
#     #     cls.company = new

#     @staticmethod
#     def change_company():
#         print("Hello World")

# # Employee.change_company("Microsoft")
# # print(Employee.company)
# obj=Employee()
# obj.change_company()
# print(obj.company)
import requests
#Get,Post,Put,Delete

# response=requests.get("https://jsonplaceholder.typicode.com/posts/20")
# print(response.text)
# if response.status_code==200:
#     data=response.json() #Json to Dictionary Format
#     print(data["title"])
#     print(data["body"])
#     print(data["userId"])
# else:
#     print("API Failed")

# new_post = {
# "title": "Hello API",
# "body": "This is sample data.",
# "userId": 1
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post) #Payload
# if response.status_code == 201:
#     print("New Post Created:")
#     print(response.json())
#     data=response.json()
#     print(data["body"])
# else:
#     print("Failed")

# updated = {
# "title": "Updated Title",
# "body": "Updated content"
# }
# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated)
# if response.ok:
#     print("Updated Data:", response.json())

# response = requests.delete("https://jsonplaceholder.typicode.com/posts/5")
# if response.status_code==200:
#     print("Deleted Successfuly")
#     print(response.json())

# city = "Delhi"
# url = f"https://api.weatherapi.com/v1/current.json?key=demo&q={city}"
# response = requests.get(url)
# if response.ok:
#     data = response.json()
#     print("Temperature:", data["current"]["temp_c"], "°C")
# else:
#     print("Error fetching data")

# site = input("Enter website URL: ")
# response = requests.get(site)
# print("Status Code:", response.status_code)
import json
person = {
"name": "Rahul",
"age": 22,
"city": "Delhi"
}
# print(type(person))
# person_json=json.dumps(person,indent=4)
# print(type(person_json))
with open("person.json", "w") as f:
    json.dump(person, f, indent=2)
print("JSON saved")

with open("person.json","r") as f:
    data=json.load(f)

print(data["name"])
print(data["city"])
print(data["age"])
