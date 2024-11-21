from pathlib import Path

from fastapi import FastAPI

from src.config import settings
from src.service import some_context


def create_fastapi_app(env_file: Path) -> FastAPI:
    settings.load_config(env_file)

    some_context.initialize_context()

    main_app = FastAPI()

    @main_app.get("/")
    def app_root():
        return {"Hello": "World"}

    return main_app


app = create_fastapi_app(Path(__file__).parent / ".env")
