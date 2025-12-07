from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='UV Python Template')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5173',
        'http://127.0.0.1:5173',
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'mode': 'web-only'}


@app.get('/items/{item_id}')
def read_item(item_id: int) -> dict[str, int]:
    return {'item_id': item_id}
