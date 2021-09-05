import requests
import datetime as dt
import random

# data = {
#     "country_code" : "id",
#     "country_name" :"indonesia" ,
#     "cases_total" :0 ,
#     "cases_today" :0 ,
#     "death_cases" :0 ,
#     "recovery_cases" :0 
# }
# API_URL_COVID = "https://coronavirus-19-api.herokuapp.com/countries"
# response = requests.get(API_URL_COVID)
# result = response.json()
# now = dt.datetime.now()
# date = now.strftime("%d-%m-%Y")
# name = input("Country name: ")
def country_code(country):
    COUNTRY_CODE_URL = f"https://restcountries.eu/rest/v2/name/{country}"
    response_country = requests.get(COUNTRY_CODE_URL)
    result_country = response_country.json()
    data = [i for i in result_country]
    for i in data:
        code = i['alpha2Code'].lower()
    return code

# def make_news(code):
#     code = code
#     # code = 'id'
#     api = "faf719230ea74835a67d79e57b25835b"
#     news_api = "https://newsapi.org/v2/top-headlines"
#     news_params = {
#     "country": code,
#     "category": "health",
#     "apiKey": api,
#     "language":'id'
#     }
#     news_response = requests.get(news_api, params=news_params)
#     result = news_response.json()['articles']
#     # data = result
#     # print(data)
#     return result

# print(make_news('id'))
# title = data['title']
# url = data['url']
# description = data['description']
# print(url)
# print(description)
# print(country_code(name))






# for i in result:
#     if i['country'] == "Indonesia" :
#         print(date)
#         country = i['country']
#         total = i['cases']
#         today = i['todayCases']
#         recovered = i['recovered']
#         deaths = i['deaths']
#         print(f'Country name : {country}')
#         print(f"Total cases : {total}")
#         print(f"Today cases : {today}")
#         print(f"Recovery cases : {recovered}")
#         print(f"Death cases : {deaths}")
# print(result)