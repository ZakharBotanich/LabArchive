import numpy
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
df = list(numpy.genfromtxt('8.csv', delimiter=','))
figures = []
lst = []
for i in range(29):
    lst.append([])
for j in range(1, 30):
    for i in range(len(df)):
        lst[j-1].append(df[i][j])
for i in range(29):
    for j in range(29):
        if i != j:         
            figure = plt.figure()
            figure.set_size_inches(0.27,0.24)
            axes = figure.subplots()
            axes.scatter(x = lst[i], y = lst[j])
            figures.append(figure)
            plt.close()
indent = 0
c = canvas.Canvas("Figures.pdf")
c.setTitle("Figures")
height = indent
k = 0
m = 0
x = 0
y = 29
for figure in figures:
    dpi = figure.get_dpi()
    figureSize = figure.get_size_inches()
    image = BytesIO()
    figure.savefig(image, format="png")
    image.seek(0)
    image = ImageReader(image)
    figureSize = figure.get_size_inches()*2.54
    c.drawImage(image, x*cm, y*cm, figureSize[0]*cm, figureSize[1]*cm)
    k += 1
    if k == 28:
        x = 0
        y -= 0.6
        k = 0
    x += figureSize[0]
c.save()
