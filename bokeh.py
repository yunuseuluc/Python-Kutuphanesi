#Web tarayıcı üzerinden verileri görselleştirme
from bokeh.plotting import figure, show

p = figure(title="Bokeh Örneği")
p.line ([1, 2, 3], [4, 5, 6])
show(p)

#https://docs.bokeh.org