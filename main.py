from enum   import Enum
from typing import Optional

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet  = 'resnet'
    lenet   = 'lenet'

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'bar'}, {'item_name': 'baz'}]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'deep learning FTW!'}
    
    if model_name == ModelName.lenet:
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have som residuals'}

@app.get('/items/{item_id')
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}
    


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/users/me")
# async def read_user_me():
#     return {'user_id': 'the current user'}

# @app.get('/users/{user_id}')
# async def read_user(user_id: str):
#     return {'user_id': user_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}