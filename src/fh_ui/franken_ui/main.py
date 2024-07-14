from fasthtml.common import *

from fh_ui.franken_ui import *

hdrs = [
    Meta(name='description', content='FastHTML Franken UI'),
    # Slate is 1 of 12 Franken UI CSS options.
    # TODO: allow easy swapping
    Link(href='https://unpkg.com/franken-wc@0.0.2/dist/css/slate.min.css', rel='stylesheet'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt("/")
def get():
    cards = (Card(
                title="Card Title",
                body=(
                    P("This is a card component."),
                    P("It has a title, body, and footer."),
                ),
                footer="Card Footer",
            ),
            Card(
                title="Card Title",
                body=(
                    P("This is a card component."),
                    P("It has no footer"),
                ),
            ),                     
            Card(
                body=(
                    P("This is a card component."),
                    P("It has no title"),
                ),
                footer="Card Footer",
            ),           
            Card(
                body=(
                    P("This is a card component."),
                    P("It has no title or footer"),
                ),
            ),
    )
    cards = [Div(card) for card in cards]


    return (
        Title("fh-franken-ui: FastHTML Franken UI"), 
        Div(
            H1("fh-franken-ui: FastHTML Franken UI", cls='uk-h1'),
            P("A set of FastHTML components that build upon Franken UI components"),
            A('GitHub fh-franken-ui', href='https://github.com/AnswerDotAI/fh-franken-ui', cls='uk-button uk-button-default'),
            Button('PyPI fh-franken-ui', href='pypi.org/project/fh-franken-ui', cls='uk-button uk-button-default', disabled=True),

            Div(*cards, cls="uk-child-width-1-2@m uk-grid-small", uk_grid=True),
                                                          
            cls='uk-container'
        )
    )

if __name__ == '__main__':
    run_uv()
