# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['fomanticcss', 'fomanticlink', 'FButton', 'FContainer', 'FGrid', 'FColumn', 'FForm', 'FInput', 'FDropdown']

# %% ../nbs/00_core.ipynb 3
from dataclasses import dataclass, asdict
from fastcore.utils import *
from fastcore.xml import *
from fastcore.xtras import *
from fastcore.meta import use_kwargs, delegates
from fasthtml.components import *

# %% ../nbs/00_core.ipynb 4
fomanticcss = "https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css"
fomanticlink = (Link(rel="stylesheet", href=fomanticcss),)

# %% ../nbs/00_core.ipynb 5
@delegates(Button, keep=True)
def FButton(*c, cls="ui button", **kwargs) -> FT:
    "A Fomantic UI Button, extending the existing Button component"
    return Button(*c, cls=cls, **kwargs)

# %% ../nbs/00_core.ipynb 8
@delegates(Div, keep=True)
def FContainer(*c, cls="ui container", **kwargs) -> FT:
    "A Fomantic UI Container"
    return Div(*c, cls=cls, **kwargs)

# %% ../nbs/00_core.ipynb 10
@delegates(Div, keep=True)
def FGrid(*c, cls="ui grid", **kwargs) -> FT:
    "A Fomantic UI Grid"
    return Div(*c, cls=cls, **kwargs)

# %% ../nbs/00_core.ipynb 13
@delegates(Div, keep=True)
def FColumn(*c, cls="column", **kwargs) -> FT:
    "A Fomantic UI Grid Column"
    if "width" in kwargs:
        # Convert number to word
        kwargs["width"] = num2word(kwargs["width"])
        cls = f"{kwargs.pop('width')} wide column"
    return Div(*c, cls=cls, **kwargs)

# %% ../nbs/00_core.ipynb 15
@delegates(Form, keep=True)
def FForm(*c, cls="ui form", **kwargs)->FT:
    "A Fomantic UI Form"
    return Form(*c, cls=cls, **kwargs)

# %% ../nbs/00_core.ipynb 17
@delegates(Div, keep=True)
def FInput(*c, cls="ui input", **kwargs)->FT:
    "A Semantic UI Input"
    return ft_hx('div', Input(*c, **kwargs), cls=cls)

# %% ../nbs/00_core.ipynb 20
@delegates(ft_hx, keep=True)
def FDropdown(placeholder, options, cls="ui dropdown", **kwargs)->FT:
    "A Semantic UI Dropdown"
    opts = [Option(text=o, value=o) for o in options]
    return ft_hx('select', *opts, cls=cls, placeholder=placeholder, **kwargs)
