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
              'base_date': start_day,
              'base_time': s_hour,
              'nx': '98',
              'ny': '77'
              }

    response = requests.get(url, params=params)
    # print(response.content)
    json_ob = json.loads(response.content)
    # print(json_ob)

    datas = json_ob['response']['body']['items']['item']

    tm = 0
    hu = 0
    for d in datas:
        if d['category'] == 'REH':
            hu = d['obsrValue']
        elif d['category'] == 'T1H':
            tm = d['obsrValue']

    print(tm, ' ', hu)

    data = {'discomfort': calculate_discomfort(tm, hu)}

    return data


def calculate_discomfort(tm, hu):
    f_tm = float(tm)
    f_hu = float(hu)
    discomfort = f_tm - 0.55 * (1 - 0.01 * f_hu) * (f_tm - 14.5)

    # 21 도 이하는 쾌적, 21~24 : 반이하 불쾌, 24~27 반 이상이 불쾌, 29-32: 대부분 불쾌, 32: 조치 필요

    return discomfort
