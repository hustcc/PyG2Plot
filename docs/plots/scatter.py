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

scatter.render("scatter.html")
