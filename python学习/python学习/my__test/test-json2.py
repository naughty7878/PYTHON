import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'https://www.runoob.com'
}

json_str = json.dumps(data)
print(json_str)

json_data = json.loads(json_str)
print(type(json_data))
print(json_data)