# Shapepy
A Python tool for programatically defining structures

# Installation
Install with pip-
`pip install shapepy`

# Usage
Define your shape files-
``` python
""" Some shape file"""
from shapepy import Cube, Cylinder, Cone

cube = Cube(length=10)
cylinder = Cylinder(radius=3, length=10)
cone = Cone(radius=5, length=5)

cone.faces.bottom.attach(cylinder.faces.top, align='center')
cylinder.faces.bottom.attach(cube.faces.top, align='center')

my_shape = cube.merge()
```

Render preview-
`shapepy render MyShape`
<img>

Export!