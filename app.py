from this import d
import uvicorn, uuid

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

# @app.route('/health')
# async def health_check():
#   return 'OK'

# @app.get('/{name}')
# async def generate_id_for_name(name:str):
#   return JSONResponse({
#     'id': str(uuid.uuid4()),
#     'name': name
#   })

#POST API
class Item(BaseModel):
  user_id: str
  password: str

@app.post('/register')
async def register_item(item:Item):
  dicted_item = dict(item)
  dicted_item['success'] = True

  return JSONResponse(dicted_item)

@app.put('/update')
async def update_item(item:Item):
  dicted_item = {k:v for k, v in dict(item).items()}
  dicted_item['success'] = True

  return JSONResponse(dicted_item)

@app.patch('/update')
async def update_item_sub(item: Item):
  dicted_item = {}
  for k, v in dict(item).items():
    if v:
      dicted_item[k] = v
  dicted_item['success'] = True

  return JSONResponse(dicted_item)

if __name__ == '__main__':
  uvicorn.run(app,host='0.0.0.0',port=8000)
