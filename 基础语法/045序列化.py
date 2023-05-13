import json

name = ['a','v','b','f']

content = json.dumps(name)
print(content)
print(type(content))

tr = json.loads(content)
print(tr)
print(type(tr))
