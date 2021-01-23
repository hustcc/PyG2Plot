from pyg2plot import Plot

data = [
  { "type": "分类一", "value": 27 },
  { "type": "分类二", "value": 25 },
  { "type": "分类三", "value": 18 },
  { "type": "分类四", "value": 15 },
  { "type": "分类五", "value": 10 },
  { "type": "其他", "value": 5 },
]

pie = Plot("Pie")

pie.set_options({
  "appendPadding": 32,
  "data": data,
  "angleField": "value",
  "colorField": "type",
  "radius": 0.8,
  "label": {
    "type": "outer",
  },
  "interactions": [{ "type": "element-active" }],
})

pie.render("pie.html")
