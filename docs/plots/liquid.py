from pyg2plot import Plot

liquid = Plot("Liquid")

liquid.set_options({
  "appendPadding": 32,
  "percent": 0.25,
  "outline": {
    "border": 4,
    "distance": 4,
  },
  "wave": {
    "length": 128,
  },
})

liquid.render("liquid.html")
