from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user_routes, transaction_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")

app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
