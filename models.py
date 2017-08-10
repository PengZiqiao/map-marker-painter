import requests
import json

KEY = 'bb0db1700b2084cf0e94c0525afb5b05'
BASE_URL = 'http://restapi.amap.com/v3/'
CITY = '南京'


def geocode(add):
    url = f'{BASE_URL}geocode/geo?address={add}&city={CITY}&key={KEY}'
    result = json.loads(requests.get(url).content)
    if result['status'] == '1' and result['geocodes']:
        # 如果获取成果，且结果不为空
        geo = result['geocodes'][0]
        result = dict()
        # 区属
        result['dist'] = geo['district']
        # 地址
        result['add'] = geo['formatted_address']
        # 经纬度
        result['lng'], result['lat'] = geo['location'].split(',')
        result['loc'] = geo['location']
        return result
    else:
        # 获取失败则返回情况说明
        return result


def write_pos(df):
    for index, row in df.iterrows():
        print(f">>> 正在查询{row['name']}坐标")
        pos = geocode(row['name'])
        print(pos)
        if 'info' not in pos:
            df.at[index,'lng']=pos['lng']
            df.at[index,'lat']=pos['lat']
    return df
