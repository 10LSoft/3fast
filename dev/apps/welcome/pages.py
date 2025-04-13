from fastapi import APIRouter
from fasts.core.render import render_component
from .views.pages.welcome import index

app = APIRouter()


@app.get("/", name='welcome')
def welcome_controller():
    component = index()
    return render_component(component)


__all__ = ["app"]
