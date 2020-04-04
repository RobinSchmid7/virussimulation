"""
A system dynamics example script
@Robin Schmid
"""

import pysd

model = pysd.read_vensim('PySD-Cookbook/source/models/Teacup/Teacup.mdl')

stocks = model.run()

stocks.plot()