from bokeh.plotting import figure
from bokeh.io import output_file, show

x=[3,7.5,10]
y=[3,6,9]

output_file("Line.html")
 
f=figure()

f.line(x,y)
#f.triangle(x,y)

show(f)