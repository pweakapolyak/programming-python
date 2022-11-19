

student_dict = {
    "John": "B",
    "Mary": "A+",
    "Nick": "F"
}

print(student_dict["Mary"])

for key in student_dict:
    print('key:', key, 'value:', student_dict[key])

for key, value in student_dict.items():
    print('key:', key, 'value:', value)


if "Dennis" in student_dict:
    print(student_dict["Dennis"])
else:
    student_dict["Dennis"] = (1,2,3)

print(student_dict["Dennis"])


del student_dict["Dennis"]

print("Dennis" in student_dict)