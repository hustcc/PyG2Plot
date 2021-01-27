# 技术原理

> PyG2Plot 原理其实非常简单，其中借鉴了 pyecharts 的实现，但是因为蚂蚁金服的 G2Plot 完全基于可视分析理论的配置式结构，所以封装上比 pyecharts 简洁非常非常多。

基本的原理，就是通过 Python 语法提供 API，然后在调用 render 的时候，生成最终的 G2Plot HTML 文本，而针对不同的环境，生成的 HTML 稍有区别。

1. 针对 HTML 生成，则直接使用正常的 html 模板，然后 script 引入 G2Plot 资源，生成 G2Plot 的 JavaScript 代码，渲染即可
2. 针对 Jupyter 环境，生成的的内容中比较特殊的时候，使用 requireJS 去加载 G2Plot 资源，后续的逻辑一致

这个原理可以理解是所有的语种封装 JavaScript 模块的统一做法。

```py
from pyg2plot import Plot

line = Plot("Line")

line.set_options({
  "data": [
    { "year": "1991", "value": 3 },
    { "year": "1992", "value": 4 },
    { "year": "1993", "value": 3.5 },
    { "year": "1994", "value": 5 },
    { "year": "1995", "value": 4.9 },
    { "year": "1996", "value": 6 },
    { "year": "1997", "value": 7 },
    { "year": "1998", "value": 9 },
    { "year": "1999", "value": 13 },
  ],
  "xField": "year",
  "yField": "value",
})

# 1. 渲染成 html 文件
line.render("plot.html")
# 2. 渲染成 html 字符串
line.render_html()
# 2. 渲染到 Jupyter 的预览区
line.render_notebook()
```

> 所以对于 PyG2Plot，核心文件是：

- `plot.py`： 提供了 PyG2Plot 的几乎全部 API
- `engine.py`：提供了渲染 HTML 的能力，其实是基于 jinja2 这个模板引擎实现的
- `templates`：提供了所有的 jinja2 模板文件，对于模板怎么用，jinja2 的文档是非常非常详细的
