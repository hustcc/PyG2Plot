# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

use jinja template to render HTML file.
'''
import os
from jinja2 import Environment, FileSystemLoader
from pyg2plot.helper.file import write_utf8_file
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
    write plot into path with template
    '''
    def render_to_file(self, plot: any,  path: str, template_name: str, **kwargs):
        # get template content
        tpl = self.env.get_template(template_name)
        # render with jinja2
        html = tpl.render(plot=plot, **kwargs)
        # write output into file
        write_utf8_file(path, html)
