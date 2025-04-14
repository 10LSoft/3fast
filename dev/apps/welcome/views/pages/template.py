import fasthtml.common as view
from ..styles.welcome import welcome_css


def welcome_template(content):
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
            view.Script(src="/static/scripts/htmx.min.js"),
        ),
        view.Body(
            content,
        ),
    )
