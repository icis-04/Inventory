from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routers import items, photos, labels

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Parts Ledger API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten this before going to production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(photos.router)
app.include_router(labels.router)

# Serves the existing frontend/index.html (your parts-ledger.html, renamed)
# at http://localhost:8000/ once you swap its window.storage calls for fetch() calls.
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
