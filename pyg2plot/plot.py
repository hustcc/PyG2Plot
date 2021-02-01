# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

> pyg2plot Plot class.
'''
import uuid
from jinja2 import Environment
from pyg2plot.engine import Engine
from pyg2plot.helper.code import json_dump_to_js
from pyg2plot.helper.file import write_utf8_file
from pyg2plot.helper.html import HTML
from typing import Optional

G2PLOT_LIB = 'https://unpkg.com/@antv/g2plot@2'


class Plot():
    '''
    instance with plot type string
    '''
    def __init__(self, plot_type: str, version: str = '2'):
        self.plot_type = plot_type
        self.plot_id = uuid.uuid4().hex
        self.version = version
        self.options = {}

        # page settting
        self.page_title = "PyG2Plot"

    '''
    set the G2Plot options, documents [here](https://g2plot.antv.vision/)
    '''
    def set_options(self, options: object):
        self.options = options
        return self

    '''
    get the JavaScript options of G2Plot
    '''
    def dump_js_options(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        return json_dump_to_js(self.options)

    '''
    render plot into jupyter
    '''
    def render_notebook(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.html",
            **kwargs
        ))

    '''
    render plot into jupyter lab
    '''
    def render_jupyter_lab(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="jupyter-lab.html",
            **kwargs
        ))

    '''
    render plot to html string
    '''
    def render_html(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = [{
            "name": "G2Plot",
            "asset": G2PLOT_LIB,
        }]
        # get html string
        return Engine(env=env).render(
            plot=self,
            template_name="plot.html",
            **kwargs
        )

    '''
    render the plot into html file
    '''
    def render(
        self,
        path: str = "plot.html",
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        # get html string
        html = self.render_html(env, **kwargs)
        # write output into file
        write_utf8_file(path, html)
        return path
