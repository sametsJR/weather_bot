from config import open_weather_token #import api token
import requests# pip install requests in Terminal

#Создаем функцию, принимающую 2 параметра: город и токен
def get_weateher(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}"
        )
        data = r.json() #получаем данные в формате json и записываем их в переменную data
        print(data)

    except Exception as ex:
        print(ex)
        print("Проверьте название города!!!")#Вывод сообщения об ошибке

def main():
    city = input("Введите город: ")#Запрос ввода названия города
    get_weateher(city, open_weather_token)#Вызов функции

if __name__ == '__main__':#Точка входа в программу
    main()#Вызов функции