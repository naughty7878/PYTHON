import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'https://www.runoob.com'
}

json_str = json.dumps(data)
print(type(json_str))
print(json_str)
print("Python 原始数据", type(repr(data)))
print("Python 原始数据", repr(data))

json_data = json.loads(json_str)
print(type(json_data))
print(json_data['name'])
print(type(json_data['name']))

data2 = ['a', 'b', 'c', 12.34, True, False, (1, 2)]
json_str2 = json.dumps(data2)
print(type(json_str2))
print(json_str2)
json_data2 = json.loads(json_str2)
print(type(json_data2))
print(json_data2)
print(json_data2[3], type(json_data2[3]))
print(json_data2[4], type(json_data2[4]))
print(json_data2[5], type(json_data2[5]))
print(json_data2[6], type(json_data2[6]))

if []:
    print(1)
else:
    print(2)
