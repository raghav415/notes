from fastapi import FastAPI
from databse import engine
import models

app = FastAPI()

# only executes if db does not exist. Changes in model won't be applied in db.
models.Base.metadata.create_all(bind=engine)


