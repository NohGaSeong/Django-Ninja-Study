from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Employee

api = NinjaAPI()


class EmployeeIn(Schema):
    first_name : str
    last_name : str
    department_id : int = None
    birthdate : date = None

class EmployeeOut(Schema):
    id : int
    first_name : str
    last_name : str
    department_id : int = None
    birthdate : date = None
    
class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str

class HelloSchema(Schema):
    name:str = "world"


@api.post("/employees")
def create_employee(request, payload:EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id":employee.id}

@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employ_id:int):
    employee = get_object_or_404(Employee, id=employ_id)
    return employee

@api.get("/employees", response=List[EmployeeOut])
def list_employee(request):
    qs = Employee.objects.all()
    return qs

@api.put("/employees/{employee_id}")
def update_employee(request, employee_id:int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id = employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}

@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id:int):
    employee = get_object_or_404(Employee, id = employee_id)
    employee.delete()
    return {"success": True}


@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user

@api.post("/hello")
def hello(request, data:HelloSchema):
    return f"hello {data.name}"

@api.get("/hello")
def hello(request, name = "world"):
    return f"Hello {name}"

@api.get("/math/{a}and{b}")
def math(request, a:int, b:int):
    return {"add" : a+ b, "multiply": a*b}