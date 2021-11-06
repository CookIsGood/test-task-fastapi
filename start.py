from fastapi import FastAPI, status
from db.base import database
from endpoints import users
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
import fastapi.middleware.cors as _cors

app = FastAPI(title="test-task-fastapi")
app.include_router(users.router, prefix="", tags=["users"])

app.add_middleware(
    _cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    new_list_errors = []
    for error in exc.errors():
        info_error = {
            'name': error['loc'][1],
            'error': error['msg']
        }
        new_list_errors.append(info_error)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(new_list_errors),
    )


if __name__ == "__main__":
    uvicorn.run("start:app", reload=True, port=8000, host="0.0.0.0")
