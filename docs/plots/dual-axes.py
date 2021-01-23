from pyg2plot import Plot

data1 = [
  { "time": "2019-03", "value": 350, "type": "uv" },
  { "time": "2019-04", "value": 900, "type": "uv" },
  { "time": "2019-05", "value": 300, "type": "uv" },
  { "time": "2019-06", "value": 450, "type": "uv" },
  { "time": "2019-07", "value": 470, "type": "uv" },
  { "time": "2019-03", "value": 220, "type": "bill" },
  { "time": "2019-04", "value": 300, "type": "bill" },
  { "time": "2019-05", "value": 250, "type": "bill" },
  { "time": "2019-06", "value": 220, "type": "bill" },
  { "time": "2019-07", "value": 362, "type": "bill" },
]

data2 = [
  { "time": "2019-03", "count": 800, "name": "a" },
  { "time": "2019-04", "count": 600, "name": "a" },
  { "time": "2019-05", "count": 400, "name": "a" },
  { "time": "2019-06", "count": 380, "name": "a" },
  { "time": "2019-07", "count": 220, "name": "a" },
  { "time": "2019-03", "count": 750, "name": "b" },
  { "time": "2019-04", "count": 650, "name": "b" },
  { "time": "2019-05", "count": 450, "name": "b" },
  { "time": "2019-06", "count": 400, "name": "b" },
  { "time": "2019-07", "count": 320, "name": "b" },
  { "time": "2019-03", "count": 900, "name": "c" },
  { "time": "2019-04", "count": 600, "name": "c" },
  { "time": "2019-05", "count": 450, "name": "c" },
  { "time": "2019-06", "count": 300, "name": "c" },
  { "time": "2019-07", "count": 200, "name": "c" },
]

dualAxes = Plot("DualAxes")

dualAxes.set_options({
  "appendPadding": 32,
  "data": [data1, data2],
  "xField": "time",
  "yField": ["value", "count"],
  "legend": {
    "position": "top",
  },
  "geometryOptions": [
    {
      "geometry": "line",
      "seriesField": "type",
      "lineStyle": {
        "lineWidth": 3,
        "lineDash": [5, 5],
      },
      "smooth": True,
    },
    {
      "geometry": "column",
      "seriesField": "name",
      "isStack": True,
    },
  ],
})

dualAxes.render("dual-axes.html")
