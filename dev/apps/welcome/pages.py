from fasts.core.render import render_component
from fasts.core.router import route, router

from .views.components.incremental import index as incremental_index
from .views.components.welcome import index as welcome_index


@route("/", name="welcome", methods=["GET"])
def welcome_controller():
    return render_component(welcome_index())


@route("/incremental/", name="incremental", methods=["GET"])
def incremental_controller():
    return render_component(incremental_index())


__all__ = ["router"]
