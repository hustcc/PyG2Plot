# PyG2Plot

> 🎨 Python3 binding for `@AntV/G2Plot` Plotting Library. Inspired by pyecharts.

[![Latest Stable Version](https://img.shields.io/pypi/v/pyg2plot.svg)](https://pypi.python.org/pypi/pyg2plot)
[![build Status](https://github.com/hustcc/pyg2plot/workflows/build/badge.svg?branch=main)](https://github.com/hustcc/pyg2plot/actions?query=workflow%3Abuild)

## Installation

```bash
$ pip install pyg2plot
```


## Usage

```py
from pyg2plot import __version__, Plot

line = Plot("line")

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

line.render()
```

![image](https://user-images.githubusercontent.com/7856674/104399307-5c29f200-558b-11eb-9908-0911030c79f8.png)


## API

Now, only has one API of `pyg2plot`.

 - **Plot**

1. *Plot(type: str)*: get an instance of `Plot` class.

2. *plot.set_options(options: object)*: set the options of [G2Plot](https://g2plot.antv.vision/) into instance.

3. *plot.render(path, env, **kwargs)*: render out a html by set the path, jinja2 env and kwargs.

> More apis is on the way.

## License

MIT@[hustcc](https://github.com/hustcc).