import json
from jsonschema import validate,ValidationError

def validate_json_data():
    with open('data/Student_info.json') as data_file1,open("schemas/student_info_schemas.json") as schemas_file1:
        student_data=json.load(data_file1)
        student_schema=json.load(schemas_file1)
        try:
            validate(instance=student_data,schema=student_schema)
            print("Student info Json data is valid.")
        except ValidationError as e:
            print(f"Json validation error: {e.message}")
    with open('data/admission_info.json') as data_file2,open("schemas/admission_info_schemas.json") as schemas_file2:
        admission_data=json.load(data_file2)
        admission_schema=json.load(schemas_file2)
        try:
            validate(instance=admission_data,schema=admission_schema)
            print("Admission info Json data is valid.")
        except ValidationError as e:
            print(f"Json validation error: {e.message}")
    with open('data/payment_info.json') as data_file3,open("schemas/payment_info_schemas.json") as schemas_file3:
        payment_data=json.load(data_file3)
        payment_schema=json.load(schemas_file3)
        try:
            validate(instance=payment_data,schema=payment_schema)
            print("Payment info Json data is valid.")
        except ValidationError as e:
            print(f"Json validation error: {e.message}")


