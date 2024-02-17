import requests

# ========= Задание №1 =========


r1 = requests.get("https://playground.learnqa.ru/api/compare_query_type")

print("1) http-запрос без параметра method:")
print("Выводит: ",r1.text)
print("")

# ========= Задание № 2 =========

method = {
    "method": "HEAD"
}

r2 = requests.post("https://playground.learnqa.ru/api/compare_query_type", data=method)

print("2) http-запрос, в котором method не из списка:")
print("Выводит: ",r2.text)
print("")

# ========= Задание № 3 =========

method2 = {
    "method": "GET"
}
r3 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params=method2)

print("3) http-запрос с правильным значением method:")
print("Выводит: ",r3.text)
print("")

# ========= Задание № 4 =========

print("4) с помощью циклов вывести возможные сочетания method и типов запроса:")
print("")

m = ['GET', 'POST', 'PUT', 'DELETE']

i = 0

for i in m:
    method = {"method": f"{i}"}
    r_method = 'GET'
    response1 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params=method)
    if r_method != i and response1.text == '{"success":"!"}':
        print(f"c {r_method}-запросом передает значение параметра {i}: ", response1.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
    else:
        if r_method == i and response1.text == 'Wrong method provided':
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response1.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
        else:
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response1.text)
print('---------------------------')

for i in m:
    method = {"method": f"{i}"}
    r_method = 'POST'
    response2 = requests.post("https://playground.learnqa.ru/api/compare_query_type", params=method)
    if r_method != i and response2.text == '{"success":"!"}':
        print(f"c {r_method}-запросом передает значение параметра {i}: ", response2.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
    else:
        if r_method == i and response2.text == 'Wrong method provided':
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response2.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
        else:
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response2.text)
print('---------------------------')

for i in m:
    method = {"method": f"{i}"}
    r_method = 'PUT'
    response3 = requests.put("https://playground.learnqa.ru/api/compare_query_type", params=method)
    if r_method != i and response3.text == '{"success":"!"}':
        print(f"c {r_method}-запросом передает значение параметра {i}: ", response3.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
    else:
        if r_method == i and response3.text == 'Wrong method provided':
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response3.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
        else:
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response3.text)
print('---------------------------')

for i in m:
    method = {"method": f"{i}"}
    r_method = 'DELETE'
    response4 = requests.delete("https://playground.learnqa.ru/api/compare_query_type", params=method)
    if r_method != i and response4.text == '{"success":"!"}':
        print(f"c {r_method}-запросом передает значение параметра {i}: ", response4.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
    else:
        if r_method == i and response4.text == 'Wrong method provided':
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response4.text, "ВНИМАНИЕ: тип запроса не совпадает со значением параметра")
        else:
            print(f"c {r_method}-запросом передает значение параметра {i}: ", response4.text)