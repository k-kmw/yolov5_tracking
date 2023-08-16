from datetime import datetime
import requests
import json


def check_weather():

    now = datetime.now()

    # 조회 기간 시작 년/월/일/시

    year = now.year
    month = now.month
    day = now.day
    hour = now.hour

    if month < 10:
        s_month = '0' + str(month)
    else:
        s_month = str(month)

    if day < 10:
        s_day = '0' + str(day)
    else:
        s_day = str(day)

    if hour < 10:
        s_hour = '0' + str(hour) + '00'
    else:
        s_hour = str(hour) + '00'

    start_day = str(year) + s_month + s_day
    # print(start_day)
    # print(s_hour)

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': "8ThuMroeCYl5iU3Xg+nu49WbCy4thmH4Vgr20RnyhhBnKMhWnJK3jJLjYRVgGf6OsUUk5J7lANZsMO6ETDW7Hw==",
              'pageNo': '1',  # 페이지 번호
              'numOfRows': '8',  # 한 페이지 결과 수
              'dataType': 'JSON',  # 응답 자료 형식
              'base_date': '20230816',
              'base_time': '1100',
              'nx': '98',
              'ny': '77'
              }

    response = requests.get(url, params=params)
    # print(response.content)
    json_ob = json.loads(response.content)
    # print(json_ob)

    datas = json_ob['response']['body']['items']['item']

    data = {}
    for d in datas:
        if d['category'] == 'REH':
            data['humidity'] = d['obsrValue']
        elif d['category'] == 'T1H':
            data['temperature'] = d['obsrValue']
        elif len(data) == 2:
            break

    # print(data)

    return data
