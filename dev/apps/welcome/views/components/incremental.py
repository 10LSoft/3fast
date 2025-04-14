import fasthtml.common as view
from fastapi import APIRouter

from fasts.core.render import render_component

from ..pages.template import welcome_template

app = APIRouter()

value = 0


def increment_component():
    return view.Div(view.H2(f'Contador: {value}'))


@app.get('/add/', name='incremental_add')
def incremental_add():
    """
    Incrementa o valor passado na URL e retorna o novo valor.
    """
    global value
    value += 1

    component = increment_component()

    return render_component(component)


def index():
    content = view.Div(
        view.Img(src='/static/images/logo.svg', cls='move__zoomIn'),
        view.H1('Contador de cliques'),
        view.P(
            'Clique no botão para incrementar o contador ou ',
            view.A('clique aqui para voltar', href='/'),
        ),
        view.Div(
            increment_component(),
            id='incremental'
        ),
        view.Button(
            'Incrementar',
            id='incremental_button',
            hx_get='/incremental/add/',
            hx_target='#incremental',
            hx_trigger='click',
            hx_swap='innerHTML',
        ),
        id='welcome'
    )

    return welcome_template(content)
