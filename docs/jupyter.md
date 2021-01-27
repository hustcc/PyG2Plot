# 在 Jupyter 中使用

Python 是一个非常方便的数据科学语言，具备有强大的数据处理能力，那么在数据处理之后，进行数据的可视化操作，是顺其自然的事情，所以 PyG2Plot 就是为了在 Python 的语言环境中，也可以享受到 [G2Plot](https://github.com/antvis/G2Plot) 的可视化能力。

> Jupyter Notebook 是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。—— [Jupyter Notebook 官方介绍](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

简而言之，Jupyter Notebook 是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

----

其实 PyG2Plot 在 Jupyter 中的使用，和原生的用法区别不大，只是最后调用的 render 函数区别而已。

```py
# py 环境
plot.render()

# jupyter 环境
plot.render_notebook()
```

首先我们打开 Jupyter 官网，开启试用 Jupyter，然后进行一个新建的模板文档。

![image](https://user-images.githubusercontent.com/7856674/105943290-eef28280-609b-11eb-9321-747d66ab81a6.png)

然后我们在一个区块中输入下面的一段代码：

> 下面的代码直接来源于 scatter.py 文件，仅仅修改了最后的 render_notebook 方法。

```py
!pip install pyg2plot

from pyg2plot import Plot

data = [
  { "x": 42, "y": 38, "size": 20, "genre": "female" },
  { "x": 6, "y": 18, "size": 1, "genre": "female" },
  { "x": 1, "y": 93, "size": 55, "genre": "female" },
  { "x": 57, "y": 2, "size": 90, "genre": "female" },
  { "x": 80, "y": 76, "size": 22, "genre": "female" },
  { "x": 11, "y": 74, "size": 96, "genre": "female" },
  { "x": 88, "y": 56, "size": 10, "genre": "female" },
  { "x": 30, "y": 47, "size": 49, "genre": "female" },
  { "x": 57, "y": 62, "size": 98, "genre": "female" },
  { "x": 4, "y": 16, "size": 16, "genre": "female" },
  { "x": 46, "y": 10, "size": 11, "genre": "female" },
  { "x": 22, "y": 87, "size": 89, "genre": "female" },
  { "x": 57, "y": 91, "size": 82, "genre": "female" },
  { "x": 45, "y": 15, "size": 98, "genre": "female" },
  { "x": 9, "y": 81, "size": 63, "genre": "male" },
  { "x": 98, "y": 5, "size": 89, "genre": "male" },
  { "x": 51, "y": 50, "size": 73, "genre": "male" },
  { "x": 41, "y": 22, "size": 14, "genre": "male" },
  { "x": 58, "y": 24, "size": 20, "genre": "male" },
  { "x": 78, "y": 37, "size": 34, "genre": "male" },
  { "x": 55, "y": 56, "size": 53, "genre": "male" },
  { "x": 18, "y": 45, "size": 70, "genre": "male" },
  { "x": 42, "y": 44, "size": 28, "genre": "male" },
  { "x": 3, "y": 52, "size": 59, "genre": "male" },
  { "x": 31, "y": 18, "size": 97, "genre": "male" },
  { "x": 79, "y": 91, "size": 63, "genre": "male" },
  { "x": 93, "y": 23, "size": 23, "genre": "male" },
  { "x": 44, "y": 83, "size": 22, "genre": "male" }
]

scatter = Plot("Scatter")

scatter.set_options({
  "height": 400,
  "appendPadding": 32,
  "data": data,
  "xField": "x",
  "yField": "y",
  "colorField": "genre",
  "color": [
    "r(0.4, 0.3, 0.7) 0:rgba(255,255,255,0.5) 1:#5B8FF9",
    "r(0.4, 0.4, 0.7) 0:rgba(255,255,255,0.5) 1:#61DDAA",
  ],
  "sizeField": "size",
  "size": [5, 20],
  "shape": "circle",
  "yAxis": {
    "nice": True,
    "line": {
      "style": {
        "stroke": "#eee",
      },
    },
  },
  "xAxis": {
    "grid": {
      "line": {
        "style": {
          "stroke": "#eee",
        },
      },
    },
    "line": {
      "style": {
        "stroke": "#eee",
      },
    },
  },
})

scatter.render_notebook()
```

然后点击运行，即可看到预览效果：

![image](https://user-images.githubusercontent.com/7856674/105945664-ab4e4780-60a0-11eb-88d9-602a86e39368.png)


> 大概就是这样的一个使用方式了，本质没有任何使用区别。更多其他的图表类型，可以参考 [绘制常用统计图表](./plot.md)。
