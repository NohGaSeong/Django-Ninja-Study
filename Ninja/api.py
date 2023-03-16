from ninja import NinjaAPI, Schema

api = NinjaAPI()

class HelloSchema(Schema):
    name:str = "world"

@api.post("/hello")
def hello(request, data:HelloSchema):
    return f"hello {data.name}"

@api.get("/hello")
def hello(request, name = "world"):
    return f"Hello {name}"

@api.get("/math/{a}and{b}")
def math(request, a:int, b:int):
    return {"add" : a+ b, "multiply": a*b}