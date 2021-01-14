# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

use jinja template to render HTML file.
'''
import os
from jinja2 import Environment, FileSystemLoader
from typing import Optional


GLOBAL_ENV = Environment(
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "templates"
        )
    ),
)


class Engine:

    def __init__(self, env: Optional[Environment] = None):
        self.env = env or GLOBAL_ENV

    '''
    render plot to html string with template
    '''
    def render(self, plot: any, template_name: str, **kwargs):
        # get template content
        tpl = self.env.get_template(template_name)
        # render with jinja2
        return tpl.render(plot=plot, **kwargs)
