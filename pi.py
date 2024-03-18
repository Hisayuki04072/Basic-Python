import re


text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
y=''
z=text.replace(",","").replace(".","").split()
x=list(map(len,z))
for i in range(len(x)):
    y=y+('{}'.format(x[i]))
print(y)
