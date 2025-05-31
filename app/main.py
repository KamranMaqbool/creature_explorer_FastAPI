from fastapi import FastAPI, Body, Header, Response

from web.explorer import router as explorer_router
from web.creatures import router as creature_router

app = FastAPI()



app.include_router(explorer_router)
app.include_router(creature_router)