from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .userprofile.user_info import user_info_router
from .userprofile.language_operations import language_operations_router


with open("./app_config.yml", 'r') as f:
    tags_metadata = yaml.safe_load(f)['tags']

app = FastAPI(
    title="Github Stats",
    version="1.0.0",
    description="This API is integrated with github rest api to fetch user info and generate statistics",
    openapi_tags=tags_metadata,
    docs_url="/swagger",
    redoc_url="/"
)

app.include_router(user_info_router)
app.include_router(language_operations_router)

origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Fast API demo"])
def read_root():
    return "This API is built using FAST API , which performs some operations using Github API"
