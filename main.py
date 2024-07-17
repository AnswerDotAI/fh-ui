from fasthtml.common import *
from fh_ui import card
from fh_ui.card import Card
from html import escape
import uvicorn

# Since this is just a CSS POC, for now we don't include jQuery or the js for each CSS framework
stylesheets = {
    'pico': 'https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css',
    'semanticui': 'https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css',
}

hdrs = [
    HighlightJS(langs=['python',]),
    Meta(name='description', content='fh-ui: FastHTML UI'),
    Link(href=stylesheets['semanticui'], rel='stylesheet', id='dynamic-stylesheet'),
    Script(src='https://unpkg.com/htmx.org@2.0.1/dist/htmx.js'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt('/change_stylesheet')
def post(style: str):
    return Link(href=stylesheets[style], rel='stylesheet', id='dynamic-stylesheet')

card1 = Div(
    Div(
        Img(src='https://via.placeholder.com/150', cls='ui image'),
        cls='image'
    ),
    Div(
        Div(
            'Uma the Kid',
            cls='header'
        ),
        Div(
            'Uma is a girl who swims like a mermaid',
            cls='description'
        ),
        cls='content',
    ),
    cls='ui card',
)

card2 = Card(
        title='Hannah the Kid',
        description='Hannah is a girl who dances and sings',
        image='https://via.placeholder.com/150',
        button_links=[('Read More', '#')],
    ),

@rt("/")
def get():
    return (
        Title("fh-ui: FastHTML UI"), 
        Div(
            H1("fh-ui: FastHTML UI", cls='ui header'),
            P("A set of FastHTML components that build upon CSS UI components"),

            A('GitHub fh-ui', href='https://github.com/AnswerDotAI/fh-ui', cls='ui button'),
            Button('PyPI fh-ui', href='pypi.org/project/fh-ui', cls='ui disabled button'),

            H2('Renderer', cls='ui header'),

            Select(
                Option('Pico CSS', value='pico'),
                Option('Semantic UI / Fomantic UI', value='semanticui'),
                cls='ui dropdown',
                hx_post='/change_stylesheet',
                hx_trigger='change',
                hx_target='#dynamic-stylesheet',
                hx_swap='outerHTML',
                name='style',
            ),
            
            H2('Cards', cls='ui header'),
            P('The first card is rendered manually. The second card is rendered using the Card class.'),

            # 2 cards, each paired with the FastHTML code used to render it
            Div(

                Section(
                    H3('This first card is rendered manually', cls='ui header'),
                    card1,
                    Div(
                        # Show the Python code that generated the card as a string
                        Pre(Code("""Div(
    Div(
        Img(src='https://via.placeholder.com/150', cls='ui image'),
        cls='image'
    ),
    Div(
        Div(
            'Uma the Kid',
            cls='header'
        ),
        Div(
            'Uma is a girl who swims like a mermaid',
            cls='description'
        ),
        cls='content',
    ),
    cls='ui card',
)""", cls='language-python')),
                        Pre(Code(to_xml(card1), cls='language-html')),
                    ),
                ),

                Section(
                    H3('This second card is rendered using the Card class', cls='ui header'),
                    card2,

                    Div(
                        Pre(Code("""Card(
    title='Hannah the Kid',
    description='Hannah is a girl who dances and sings',
    image='https://via.placeholder.com/150',
    button_links=[('Read More', '#')],
)""", cls='language-python')),
                        Pre(Code(to_xml(card2), cls='language-html')),
                    ),
                ),
            ),
            cls='ui container'
        )
    )

if __name__ == '__main__':
    # TODO: replace with something like run_uv(fname='__main__') 
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=5001)))