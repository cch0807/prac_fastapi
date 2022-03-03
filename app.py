import uvicorn, uuid
from fastapi import FastAPI
from fastapi.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.route('/health')
async def health_check():
  return 'OK'

@app.get('/{name}')
async def generate_id_for_name(name:str):
  return JSONResponse({
    'id': str(uuid.uuid4()),
    'name': name
  })

if __name__ == '__main__':
  uvicorn.run(app,host='0.0.0.0',port=8000)