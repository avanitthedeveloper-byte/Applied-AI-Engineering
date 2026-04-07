# 10. Working with JSON Module

import json
'''
json_str = '{"name": "Cipher Mind", "isPrgrammer": true}'

python_obj = json.loads(json_str)

print(type(json_str), json_str)

print(type(python_obj), python_obj)

py_obj = {
    "name": "Cipher Mind",
    "age": None,
    "is_Teacher": True
}

json_str = json.dumps(py_obj)

print(type(py_obj), py_obj)

print(type(json_str), json_str)
'''


with open("jdata.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)

data = {
    "name": "Cipher Mind",
    "isProgrammer": True,
    "address": {
    "city": "Pondicherry",
    "country": "India"
  },
  "sub": ["Python", "Machine Learning", "Artificial Intelligence"],
}
with open("jwdata.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)