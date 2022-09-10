from flask import Flask, render_template, request

import sqlite3
from datetime import datetime, timezone
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
def raw_temp_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] raw_temp_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, rawTemperature FROM """+name)

    times = []
    rawTemps = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        rawTemps.append(row[1])
     
    c.close()
    conn.close()
    

    raw_temp_plot = figure(title='Raw Temperature:', tools='xpan,xwheel_zoom,reset', active_drag = None,  plot_width=1430, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    raw_temp_plot.line(times, rawTemps, name='rawTemp', color='lightsteelblue', line_width=1)
    raw_temp_plot.circle(times, rawTemps, name='rawTemp', fill_color='white', size=8)
    
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


    
@app.route('/pressure_plot/<name>')
def pressure_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] pressure_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, pressure FROM """+name)

    times = []
    pressures = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        pressures.append(row[1])
     
    c.close()
    conn.close()


    pressure_plot = figure(title='Pressure:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=1430, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    pressure_plot.line(times, pressures, name='Pressure', color='dodgerblue', line_width=1)
    pressure_plot.circle(times, pressures, name='Pressure', fill_color='white', size=8)
    
    pressure_plot.xaxis.axis_label = 'Time'
    pressure_plot.yaxis.axis_label = 'Pressure [Pa]'

    pressure_plot.ygrid.minor_grid_line_color = 'dodgerblue'
    pressure_plot.ygrid.minor_grid_line_alpha = 0.05

    pressure_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Pressure', '@y')],
                   formatters={'x': 'datetime'}))

    pressure_script, pressure_div = components(pressure_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] pressure_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=pressure_script, plot_div=pressure_div, cdn_js=cdn_js) 

    

        
    
if __name__ == '__main__':
    app.run(debug = False) 