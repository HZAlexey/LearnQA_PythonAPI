import sys
import requests

r = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = r.history
second_response = r


# Подсчет количества редиректов от изначальной точки до итоговой
print("Количество редиректов: ",sys.getrefcount(first_response))

# Выыод итоговой URL
print("Итоговый URL: ",second_response.url)