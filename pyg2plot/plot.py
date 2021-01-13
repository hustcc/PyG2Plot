# -*- coding: utf-8 -*-
'''
Created on 2021-01-14
@author: hustcc

> pyg2plot Plot class.
'''

from pyg2plot.engine import render


class Plot():
    '''
    instance with plot type string
    '''
    def __init__(self, type: str):
        self.type = type

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
        env: any = None,
        **kwargs
    ) -> str:
        template_name = ''
        return render(self, path, template_name, env, **kwargs)
