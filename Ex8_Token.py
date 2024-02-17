import requests
import time
import json

r1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(r1.text)

token = {
    "token":f"{obj["token"]}"
}

r2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)

print(f"Задача еще не готова, подождем {obj["seconds"]} секунд.. ", r2.text, )
time.sleep(obj["seconds"])


r3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print("Задача выполнена, результат: ", r3.text)
