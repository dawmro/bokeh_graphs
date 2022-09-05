from flask import Flask, render_template, request

import sqlite3
from datetime import datetime
import time


# standard bokeh imports
from bokeh.io import show

# other bokeh imports
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.embed import components
from bokeh.resources import CDN

# other imports
import numpy as np
import pandas as pd

# line plot
from bokeh.models import HoverTool





app = Flask(__name__)



@app.route('/rawTemperature_plot/<name>')
def gpu_core_temp_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] raw_temp_plot for "+name+" started!")

    
    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, rawTemperature FROM """+name)

    times = []
    rawTemps = []

    i = 0
    for row in c.fetchall():

        #times.append(row[0])
        times.append(i)
        i=i+1
        
        rawTemps.append(row[1])

        
    c.close()
    conn.close()
    print(type(rawTemps[0]))
    

    

    raw_temp_plot = figure(title='Raw Temperature:', tools='xpan,xwheel_zoom,reset', active_drag = None,  plot_width=1430, plot_height=600, toolbar_location='above', x_axis_type="datetime")

    raw_temp_plot.line(times, rawTemps, name='rawTemp', color='lightsteelblue', line_width=1)
    

    raw_temp_plot.xaxis.axis_label = 'Time'
    raw_temp_plot.yaxis.axis_label = 'Temperature [C]'

    raw_temp_plot.ygrid.minor_grid_line_color = 'navy'
    raw_temp_plot.ygrid.minor_grid_line_alpha = 0.05

    raw_temp_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Temp', '@y')],
                   formatters={'x': 'datetime'}))

    raw_temp_script, raw_temp_div = components(raw_temp_plot)

    cdn_js=CDN.js_files


    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] raw_temp_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=raw_temp_script, plot_div=raw_temp_div, cdn_js=cdn_js) 

    
    
    
if __name__ == '__main__':
    app.run(debug = False) 