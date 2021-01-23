# PyG2Plot

> 🎨 PyG2Plot 是 [`@AntV/G2Plot`](https://github.com/antvis/G2Plot) 在 Python3 上的封装。 G2Plot 是一套简单、易用、并具备一定扩展能力和组合能力的统计图表库，基于图形语法理论搭建而成。

[![Latest Stable Version](https://img.shields.io/pypi/v/pyg2plot.svg)](https://pypi.python.org/pypi/pyg2plot)
[![build Status](https://github.com/hustcc/pyg2plot/workflows/build/badge.svg?branch=main)](https://github.com/hustcc/pyg2plot/actions?query=workflow%3Abuild)

<div align="center">
  <img src="https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*sXqrRrEwFRQAAAAAAAAAAABkARQnAQ" width="800">
</div>

**相关文档**： [英文介绍](./README_EN.md)  ·  [绘制常用统计图表](./docs/plot.md)  ·  [在 Jupyter 中使用](./docs/jupyter.md)  ·  [技术原理](./docs/how.md)

## 安装

```bash
$ pip install pyg2plot
```


## 使用

#### **渲染成 HTML**

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
```

![image](https://user-images.githubusercontent.com/7856674/104466432-31be5000-55f0-11eb-8333-68279d50861e.png)

#### **在 Jupyter 中使用**

```py
from pyg2plot import Plot

line = Plot("Line")

line.set_options({
  "height": 400, # set a default height in jupyter preview
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

line.render_notebook()
```


## API

目前 `pyg2plot` 只提供简单的一个 API。

 - **Plot**

1. *Plot(plot_type: str)*: 获取 `Plot` 对应的类实例。

2. *plot.set_options(options: object)*: 给图表实例设置一个 [G2Plot](https://g2plot.antv.vision/) 图形的配置，文档可以直接参考 G2Plot 官网，未进行任何二次数据结构包装。

3. *plot.render(path, env, **kwargs)*: 渲染出一个 HTML 文件，同时可以传入文件的路径，以及 jinja2 env 和 kwargs 参数。

4. *plot.render_notebook(env, **kwargs)*: 将图形渲染到 jupyter 的预览。

5. *plot.render_html(env, **kwargs)*: 渲染出 HTML 字符串，同时可以传入 jinja2 env 和 kwargs 参数。

6. *plot.dump_js_options(env, **kwargs)*: 输出 Javascript 的 option 配置结构，同时可以传入 jinja2 env 和 kwargs 参数，可以用于 Server 中的 HTTP 结构返回数据结构。

> 更多区分 Plot 级别的语法糖 API 还在筹备中。


## 协议

MIT@[hustcc](https://github.com/hustcc).