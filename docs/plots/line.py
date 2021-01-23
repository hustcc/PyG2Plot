from pyg2plot import Plot

data = [
  { "year": '1991', "value": 3 },
  { "year": '1992', "value": 4 },
  { "year": '1993', "value": 3.5 },
  { "year": '1994', "value": 5 },
  { "year": '1995', "value": 4.9 },
  { "year": '1996', "value": 6 },
  { "year": '1997', "value": 7 },
  { "year": '1998', "value": 9 },
  { "year": '1999', "value": 13 },
]

line = Plot("Line")

line.set_options({
  "appendPadding": 32,
  "data": data,
  "xField": "year",
  "yField": "value",
  "label": {},
  "smooth": True,
  "lineStyle": {
    "lineWidth": 3,
  },
  "point": {
    "size": 5,
    "shape": 'diamond',
    "style": {
      "fill": "white",
      "stroke": "#5B8FF9",
      "lineWidth": 2,
    }
  }
})

line.render("line.html")
