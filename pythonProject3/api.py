import requests
api= requests.get("https://reqres.in/api/users?page=2")
print("get method:",api.json())
data1={'1': 1, '2': 4,'3': 9, '4': 16}
api2=(requests.put("https://reqres.in/api/users/2",data=data1))
print("api 2:",api2)
api3=requests.get("https://mail.google.com/mail/u/0/#inbox")
print("mail:",api3.json())