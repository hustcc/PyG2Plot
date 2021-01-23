
from pyg2plot import Plot

gauge = Plot("Gauge")

gauge.set_options({
  "appendPadding": 32,
  "percent": 0.75,
  "range": {
    "ticks": [0, 1 / 3, 2 / 3, 1],
    "color": ["#F4664A", "#FAAD14", "#30BF78"],
  },
  "indicator": {
    "pointer": {
      "style": {
        "stroke": "#D0D0D0",
      },
    },
    "pin": {
      "style": {
        "stroke": "#D0D0D0",
      },
    },
  },
  "statistic": {
    "content": {
      "style": {
        "fontSize": "36px",
        "lineHeight": "36px",
      },
    },
  },
})

gauge.render("gauge.html")
