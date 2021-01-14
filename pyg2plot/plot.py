# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

> pyg2plot Plot class.
'''
from jinja2 import Environment
from pyg2plot.engine import Engine
from pyg2plot.helper.code import json_dump_to_js
from pyg2plot.helper.file import write_utf8_file
from typing import Optional


class Plot():
    '''
    instance with plot type string
    '''
    def __init__(self, plot_type: str, version: str = '2'):
        self.plot_type = plot_type
        self.version = version
        self.options = {}
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
    render plot to html string
    '''
    def render_html(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = ["https://unpkg.com/@antv/g2plot@2"]
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
