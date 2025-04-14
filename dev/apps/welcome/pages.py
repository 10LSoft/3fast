from fastapi import APIRouter
from fasts.core.render import render_component
from .views.components.welcome import index as welcome_index
from .views.components.incremental import app as rt, index as incremental_index

app = APIRouter()


@app.get("/", name='welcome')
def welcome_controller():
    component = welcome_index()
    return render_component(component)


@app.get('/incremental/', name='incremental')
def incremental_controller():
    component = incremental_index()
    return render_component(component)


app.include_router(rt, prefix='/incremental')
__all__ = ["app"]
