from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import connect_to_db, close_db_connection
from routers import authentication, notes


def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    application.add_event_handler("startup", connect_to_db(application))
    application.add_event_handler("shutdown", close_db_connection(application))

    application.include_router(authentication.router)
    application.include_router(notes.router)

    return application


app = get_application()
