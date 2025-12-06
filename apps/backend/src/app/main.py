from fastapi import FastAPI

app = FastAPI(title='UV Python Template')


@app.get('/')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'mode': 'web-only'}
