# dict obj in the json string type
import json
emp_dict={'emp': 101, 'ename': 'rahul', 'avial': True, 'loc': 'undefined', 'esal': None}
print(type(emp_dict))
print(emp_dict)
emp_json=json.dumps(emp_dict)
print(type(emp_json))
print(emp_json)