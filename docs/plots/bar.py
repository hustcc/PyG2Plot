from pyg2plot import Plot

data = [
  { "year": "1951 年", "value": 38 },
  { "year": "1952 年", "value": 52 },
  { "year": "1956 年", "value": 61 },
  { "year": "1957 年", "value": 145 },
  { "year": "1958 年", "value": 48 },
]

bar = Plot("Bar")

bar.set_options({
  "appendPadding": 32,
  "data": data,
  "xField": "value",
  "yField": "year",
  "seriesField": "year",
  "legend": False
})

bar.render("bar.html")
