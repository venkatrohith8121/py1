# json string into py data type
import json
emp_json="""{
    "emp":101,
    "ename":"rahul",
    "avial":true,
    "loc":"undefined",
    "esal":null
}"""
print(type(emp_json))
print(emp_json)
emp_dict=json.loads(emp_json)
print(type(emp_dict))
print(emp_dict)