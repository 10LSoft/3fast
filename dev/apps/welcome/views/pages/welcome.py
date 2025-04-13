from datetime import datetime

import fasthtml.common as view

from ..styles.welcome import welcome_css


def index():
    paragraphs = [
        """
        O 3Fast é um framework web usando Python cujo objetivo é oferecer aos
        desenvolvedores uma plataforma onde eles possam criar aplicações web de
        forma rápida, fácil e intuitiva usando apenas a linguagem Python.
        """,
        """
        O 3Fast tem esse nome pela sua composição principal. Aqui temos
        simultameamente FastAPI, FastHTML e FastCSS. Esta última é uma lib
        escrita especificamente para o framework.
        """,
        """
        Esperamos que este projeto possa lhe ajudar a desenvolver aplicações
        web com prazer e sem precisar se preocupar com detalhes técnicos e
        stacks específicas. A ideia aqui é usar apenas Python.
        """
    ]

    return view.Html(
        view.Head(
            view.Title("3Fast"),
            view.Meta(charset="utf-8"),
            view.Meta(
                name="viewport",
                content="width=device-width, initial-scale=1"
            ),
            view.Style(welcome_css()),
            view.Link(rel="stylesheet", href="/static/styles/animate.min.css"),
        ),
        view.Body(
            view.Div(
                view.H1("Bem vindo ao 3Fast"),
                *[view.P(p) for p in paragraphs],
                view.Img(
                    src='/static/images/logo.svg',
                    cls='move__flipInY',
                ),
                view.Div(
                    view.P(
                        "3Fast - Full Python web Framework "
                        f"- {datetime.now().year}"
                    ),
                    id="footer"
                ),
                id="welcome"
            ),
        ),
    )
