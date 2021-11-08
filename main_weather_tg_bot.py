import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token) #создаем объект бота и передаем в него наш токен
dp = Dispatcher(bot) #создаем объект диспетчера и передаем в него наш бот. В aiogram хэндлерами управляет диспетчер

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):#функция ответа на команду start
    await message.reply("Введи название города на англиском языке и получишь текущий прогноз погоды")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json() #получаем данные в формате json и записываем их в переменную data

        #забираем данные, которые хотим получить в выводе
        city = data["name"] #название города
        country = data["sys"]["country"] #страна
        cur_temp = data["main"]["temp"] #температура
        humidity = data["main"]["humidity"] #влажность
        pressure = data["main"]["pressure"]  #давление
        wind = data["wind"]["speed"]  #скорость ветра
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"Погода в городе: {city}, {country}\nТемпература: {cur_temp} *C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм. рт. ст.\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}"
        )

    except:
        await message.reply("Проверьте название города") #Вывод сообщения об ошибке

if __name__ == '__main__':
    executor.start_polling(dp)#вызываем у экзекьютора метод start_polling и передаем в него объект класса диспетчер