from config import open_weather_token #import api token
from pprint import pprint #модуль для аккуратного отображения данных
import datetime #модуль для преобразования времени unix timestamp в стандартное
import requests# pip install requests in Terminal

#Создаем функцию, принимающую 2 параметра: город и токен
def get_weateher(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json() #получаем данные в формате json и записываем их в переменную data
    #pprint(data)

        #забираем данные, которые хотим получить в выводе
        city = data["name"] #название города
        country = data["sys"]["country"] #страна
        cur_temp = data["main"]["temp"] #температура
        humidity = data["main"]["humidity"] #влажность
        pressure = data["main"]["pressure"]  #давление
        wind = data["wind"]["speed"]  #скорость ветра
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"Погода в городе: {city}, {country}\nТемпература: {cur_temp} *C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм. рт. ст.\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}"
        )

    except Exception as ex:
        print(ex)
        print("Проверьте название города") #Вывод сообщения об ошибке

def main():
    city = input("Введите город: ")#Запрос ввода названия города
    get_weateher(city, open_weather_token)#Вызов функции

if __name__ == '__main__':#Точка входа в программу
    main()#Вызов функции