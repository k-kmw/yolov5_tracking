from urllib.parse import urlencode, unquote, quote_plus
import requests
import json


def check_weather():
    url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
    params = {'serviceKey': "8ThuMroeCYl5iU3Xg+nu49WbCy4thmH4Vgr20RnyhhBnKMhWnJK3jJLjYRVgGf6OsUUk5J7lANZsMO6ETDW7Hw==",
              'pageNo': '1',  # 페이지 번호
              'numOfRows': '1',  # 한 페이지 결과 수
              'dataType': 'JSON',  # 응답 자료 형식
              'dataCd': 'ASOS',  # 자료 분류 코드
              'dateCd': 'HR',  # 날짜 분류 코드
              'startDt': '20230726',  # 조회 기간 시작일
              'startHh': '01',  # 조회 기간 시작시
              'endDt': '20230726',  # 조회 기간 종료일
              'endHh': '02',  # 조회 기간 종료시
              'stnIds': '108'  # 종관기상관측 지점 번호
              }

    response = requests.get(url, params=params)
    json_ob = json.loads(response.content)
    # print(json_ob)

    temperature = json_ob['response']['body']['items']['item']
    humidity = json_ob['response']['body']['items']['item']

    datas = {}
    for t in temperature:
        datas['temperature'] = t['ta']
        break
    for h in humidity:
        datas['humidity'] = h['hm']
        break
    # print(datas)

    return datas
