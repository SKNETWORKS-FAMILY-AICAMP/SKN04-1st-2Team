import requests
import json
def electric_car_crawling():
    electric_car_count = []
    response = requests.get("https://chargeinfo.ksga.org/ws/statistics/ev/list",
                            headers={
                                'user-agent': 'Mozilla 5.0',
                                'Referer': 'https://chargeinfo.ksga.org/front/statistics/evCar',
                            })
    result = json.loads(response.text)
    for year_dict in result.get('result'):
        electric_car_count.append(list(year_dict.values()))

    electric_car_last_count = []    
    electric_car_last_count.append(electric_car_count[0])
    for i in electric_car_count: 
        if i[0][-2:]=='12':
            electric_car_last_count.append(i)
    return electric_car_last_count
        