import requests
import csv
import pprint
import io

#data_index_number(1つ目の要素=0なので注意)
amedas_point = 513 #アメダス拠点番号(羽田、csvの行数)
amedas_point_name = 2 #地点名称(3つ目のフィールド)
#時刻情報index
time_year = 4
time_month = 5
time_day = 6
time_hour = 7
time_minute = 8

#雨量情報index
rain_1h_now = 25
rain_3h_now =29
rain_6h_now = 33
rain_12h_now = 37
rain_24h_now = 41
rain_48h_now = 45
rain_72h_now = 49


url = "https://www.data.jma.go.jp/obd/stats/data/mdrr/pre_rct/alltable/preall00_rct.csv"

res = requests.get(url)

res.encoding = res.apparent_encoding

# with open("preall00_rct.csv")as f:
#     csvdata = csv.reader(f)
#     csvlist = list(csvdata)

csvstr = io.StringIO()
csvstr.write(res.text)
csvstr.seek(0)

csvdata = csv.reader(csvstr)
csvlist = list(csvdata)

#日付生成(str型注意)
date = csvlist[amedas_point][time_year]+"/"+csvlist[amedas_point][time_month]+"/"+csvlist[amedas_point][time_day]+" "+csvlist[amedas_point][time_hour]+":"+csvlist[amedas_point][time_minute]

#型変換しつつ要素取得
rain1h= float(csvlist[amedas_point][rain_1h_now])
rain3h= float(csvlist[amedas_point][rain_3h_now])
rain6h= float(csvlist[amedas_point][rain_6h_now])
rain12h= float(csvlist[amedas_point][rain_12h_now])
rain24h= float(csvlist[amedas_point][rain_24h_now])
rain48h= float(csvlist[amedas_point][rain_48h_now])
rain72h= float(csvlist[amedas_point][rain_72h_now])

#取得した要素と型を確認
print(date)
print(type(date))
print(rain1h)
print(type(rain1h))
print(rain3h)
print(type(rain3h))
print(rain6h)
print(type(rain6h))
print(rain12h)
print(type(rain12h))
print(rain24h)
print(type(rain24h))
print(rain48h)
print(type(rain48h))
print(rain72h)
print(type(rain72h))
