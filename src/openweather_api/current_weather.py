import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_response(city: str) -> str | None:
    WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_TOKEN")
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = round(requisicao_dic['main']['temp'] - 273.15,1)
    temperatura_min = round(requisicao_dic['main']['temp_min'] - 273.15,1)
    temperatura_max = round(requisicao_dic['main']['temp_max'] - 273.15,1)
    temperatura_sens = round(requisicao_dic['main']['feels_like'] - 273.15,1)
    humidade = requisicao_dic['main']['humidity']
    vento = requisicao_dic['wind']['speed']

    # print(descricao, f"{temperatura}ºC")
    return [city, descricao, f"{temperatura}ºC", f"{temperatura_sens}ºC", f"{temperatura_min}ºC", f"{temperatura_max}ºC", f"{humidade}%", f"{vento}m/s"]