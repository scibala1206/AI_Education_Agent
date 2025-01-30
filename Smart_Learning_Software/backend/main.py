from fastapi import FastAPI
from app.routes import user_routes  # Import user routes
from config.db import database  # Import database instance

app = FastAPI()

# Include user routes
app.include_router(user_routes.router, prefix="/api", tags=["Users"])

@app.on_event("startup")
async def startup():
    """Connect to the database when the app starts."""
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    """Disconnect from the database when the app shuts down."""
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI User Management API"}

# Run the app with: uvicorn main:app --reload
