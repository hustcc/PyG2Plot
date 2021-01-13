# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

> pyg2plot Plot class.
'''
from jinja2 import Environment
from pyg2plot.engine import Engine
from pyg2plot.helper.code import json_dump_to_js
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
    render the plot into html template file
    '''
    def render(
        self,
        path: str = "plot.html",
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        self.js_options = json_dump_to_js(self.options)
        self.dependencies = ["https://unpkg.com/@antv/g2plot@2"]

        return Engine(env=env).render_to_file(
            plot=self,
            path=path,
            template_name="plot.html",
            **kwargs
        )
