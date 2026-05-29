print ("Hello, das ist die Lektion 2!")
list = [1, 2, 3, 4, 5]
list.sort(reverse=True)
print(list) 

list2 = ["Andreas", "Monika", "Lea", "Saphira", "Salome", "Hanna"]
print(list2)
list2.sort(reverse=True)
print(list2) 
list2.sort(reverse=False)
print(list2) 
list2.append("Lukas")
print(list2)
list2.insert(0, "Lena")
print(list2)
list2.remove("Lena")
print(list2)
list2.pop(0)
print(list2)
list2.insert(3, "Marry")
print(list2)

import requests

request = requests.get("https://www.google.com")
print(request.status_code)

req = requests.get("https://checkip.global.api.aws/")
print(req.text)