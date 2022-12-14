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

# global variable
bokeh_plot_width = 1800




app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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
    

    raw_temp_plot = figure(title='Raw Temperature:', tools='xpan,xwheel_zoom,reset', active_drag = None,  plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
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


    pressure_plot = figure(title='Pressure:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    pressure_plot.line(times, pressures, name='Pressure', color='dodgerblue', line_width=1)
    pressure_plot.circle(times, pressures, name='Pressure', fill_color='white', size=8)
    
    pressure_plot.xaxis.axis_label = 'Time'
    pressure_plot.yaxis.axis_label = 'Pressure [Pa]'

    pressure_plot.ygrid.minor_grid_line_color = 'navy'
    pressure_plot.ygrid.minor_grid_line_alpha = 0.05

    pressure_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Pressure', '@y')],
                   formatters={'x': 'datetime'}))

    pressure_script, pressure_div = components(pressure_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] pressure_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=pressure_script, plot_div=pressure_div, cdn_js=cdn_js) 



@app.route('/rawHumidity_plot/<name>')
def rawHumidity_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] rawHumidity_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, rawHumidity FROM """+name)

    times = []
    rawHumiditys = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        rawHumiditys.append(row[1])
     
    c.close()
    conn.close()


    rawHumidity_plot = figure(title='Raw Humidity:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    rawHumidity_plot.line(times, rawHumiditys, name='Raw Humidity', color='rosybrown', line_width=1)
    rawHumidity_plot.circle(times, rawHumiditys, name='Raw Humidity', fill_color='white', size=8)
    
    rawHumidity_plot.xaxis.axis_label = 'Time'
    rawHumidity_plot.yaxis.axis_label = 'Raw Humidity [%]'

    rawHumidity_plot.ygrid.minor_grid_line_color = 'navy'
    rawHumidity_plot.ygrid.minor_grid_line_alpha = 0.05

    rawHumidity_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Raw Humidity', '@y')],
                   formatters={'x': 'datetime'}))

    rawHumidity_script, rawHumidity_div = components(rawHumidity_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] rawHumidity_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=rawHumidity_script, plot_div=rawHumidity_div, cdn_js=cdn_js) 



@app.route('/gasResistance_plot/<name>')
def gasResistance_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] gasResistance_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, gasResistance FROM """+name)

    times = []
    gasResistances = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        gasResistances.append(row[1])
     
    c.close()
    conn.close()


    gasResistance_plot = figure(title='Gas Resistance:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    gasResistance_plot.line(times, gasResistances, name='Gas Resistance', color='maroon', line_width=1)
    gasResistance_plot.circle(times, gasResistances, name='Gas Resistance', fill_color='white', size=8)
    
    gasResistance_plot.xaxis.axis_label = 'Time'
    gasResistance_plot.yaxis.axis_label = 'Gas Resistance [Ohm]'

    gasResistance_plot.ygrid.minor_grid_line_color = 'navy'
    gasResistance_plot.ygrid.minor_grid_line_alpha = 0.05

    gasResistance_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Gas Resistance', '@y')],
                   formatters={'x': 'datetime'}))

    gasResistance_script, gasResistance_div = components(gasResistance_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] gasResistance_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=gasResistance_script, plot_div=gasResistance_div, cdn_js=cdn_js) 
    
    
    
@app.route('/iaq_plot/<name>')
def iaq_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] iaq_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, iaq FROM """+name)

    times = []
    iaqs = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        iaqs.append(row[1])
     
    c.close()
    conn.close()


    iaq_plot = figure(title='IAQ:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    iaq_plot.line(times, iaqs, name='IAQ', color='olive', line_width=1)
    iaq_plot.circle(times, iaqs, name='IAQ', fill_color='white', size=8)
    
    iaq_plot.xaxis.axis_label = 'Time'
    iaq_plot.yaxis.axis_label = 'IAQ [?]'

    iaq_plot.ygrid.minor_grid_line_color = 'navy'
    iaq_plot.ygrid.minor_grid_line_alpha = 0.05

    iaq_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('IAQ', '@y')],
                   formatters={'x': 'datetime'}))

    iaq_script, iaq_div = components(iaq_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] iaq_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=iaq_script, plot_div=iaq_div, cdn_js=cdn_js) 
    
    
    
@app.route('/iaqAccuracy_plot/<name>')
def iaqAccuracy_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] iaqAccuracy_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, iaqAccuracy FROM """+name)

    times = []
    iaqAccuracys = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        iaqAccuracys.append(row[1])
     
    c.close()
    conn.close()


    iaqAccuracy_plot = figure(title='IAQ Accuracy:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    iaqAccuracy_plot.line(times, iaqAccuracys, name='IAQ Accuracy', color='tomato', line_width=1)
    iaqAccuracy_plot.circle(times, iaqAccuracys, name='IAQ Accuracy', fill_color='white', size=8)
    
    iaqAccuracy_plot.xaxis.axis_label = 'Time'
    iaqAccuracy_plot.yaxis.axis_label = 'IAQ Accuracy'

    iaqAccuracy_plot.ygrid.minor_grid_line_color = 'navy'
    iaqAccuracy_plot.ygrid.minor_grid_line_alpha = 0.05

    iaqAccuracy_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('IAQ Accuracy', '@y')],
                   formatters={'x': 'datetime'}))

    iaqAccuracy_script, iaqAccuracy_div = components(iaqAccuracy_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] iaqAccuracy_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=iaqAccuracy_script, plot_div=iaqAccuracy_div, cdn_js=cdn_js)     



@app.route('/temperature_plot/<name>')
def temperature_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] temperature_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, temperature FROM """+name)

    times = []
    temperatures = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        temperatures.append(row[1])
     
    c.close()
    conn.close()


    temperature_plot = figure(title='Temperature:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    temperature_plot.line(times, temperatures, name='Temperature', color='green', line_width=1)
    temperature_plot.circle(times, temperatures, name='Temperature', fill_color='white', size=8)
    
    temperature_plot.xaxis.axis_label = 'Time'
    temperature_plot.yaxis.axis_label = 'Temperature [C]'

    temperature_plot.ygrid.minor_grid_line_color = 'navy'
    temperature_plot.ygrid.minor_grid_line_alpha = 0.05

    temperature_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Temperature', '@y')],
                   formatters={'x': 'datetime'}))

    temperature_script, temperature_div = components(temperature_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] temperature_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=temperature_script, plot_div=temperature_div, cdn_js=cdn_js)  



@app.route('/humidity_plot/<name>')
def humidity_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] humidity_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, humidity FROM """+name)

    times = []
    humiditys = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        humiditys.append(row[1])
     
    c.close()
    conn.close()


    humidity_plot = figure(title='Humidity:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    humidity_plot.line(times, humiditys, name='Humidity', color='fuchsia', line_width=1)
    humidity_plot.circle(times, humiditys, name='Humidity', fill_color='white', size=8)
    
    humidity_plot.xaxis.axis_label = 'Time'
    humidity_plot.yaxis.axis_label = 'Humidity [%]'

    humidity_plot.ygrid.minor_grid_line_color = 'navy'
    humidity_plot.ygrid.minor_grid_line_alpha = 0.05

    humidity_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Humidity', '@y')],
                   formatters={'x': 'datetime'}))

    humidity_script, humidity_div = components(humidity_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] humidity_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=humidity_script, plot_div=humidity_div, cdn_js=cdn_js) 



@app.route('/dewPoint_plot/<name>')
def dewPoint_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] dewPoint_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, dewPoint FROM """+name)

    times = []
    dewPoints = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        dewPoints.append(row[1])
     
    c.close()
    conn.close()


    dewPoint_plot = figure(title='Dew Point:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    dewPoint_plot.line(times, dewPoints, name='Dew Point', color='fuchsia', line_width=1)
    dewPoint_plot.circle(times, dewPoints, name='Dew Point', fill_color='white', size=8)
    
    dewPoint_plot.xaxis.axis_label = 'Time'
    dewPoint_plot.yaxis.axis_label = 'Dew Point [C]'

    dewPoint_plot.ygrid.minor_grid_line_color = 'navy'
    dewPoint_plot.ygrid.minor_grid_line_alpha = 0.05

    dewPoint_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Dew Point', '@y')],
                   formatters={'x': 'datetime'}))

    dewPoint_script, dewPoint_div = components(dewPoint_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] dewPoint_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=dewPoint_script, plot_div=dewPoint_div, cdn_js=cdn_js) 


@app.route('/staticIaq_plot/<name>')
def staticIaq_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] staticIaq_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, staticIaq FROM """+name)

    times = []
    staticIaqs = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        staticIaqs.append(row[1])
     
    c.close()
    conn.close()


    staticIaq_plot = figure(title='Static IAQ:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    staticIaq_plot.line(times, staticIaqs, name='Static IAQ', color='fuchsia', line_width=1)
    staticIaq_plot.circle(times, staticIaqs, name='Static IAQ', fill_color='white', size=8)
    
    staticIaq_plot.xaxis.axis_label = 'Time'
    staticIaq_plot.yaxis.axis_label = 'Static IAQ [?]'

    staticIaq_plot.ygrid.minor_grid_line_color = 'navy'
    staticIaq_plot.ygrid.minor_grid_line_alpha = 0.05

    staticIaq_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Static IAQ', '@y')],
                   formatters={'x': 'datetime'}))

    staticIaq_script, staticIaq_div = components(staticIaq_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] staticIaq_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=staticIaq_script, plot_div=staticIaq_div, cdn_js=cdn_js) 


@app.route('/co2Equivalent_plot/<name>')
def co2Equivalent_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] staticIaq_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, co2Equivalent FROM """+name)

    times = []
    co2Equivalents = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        co2Equivalents.append(row[1])
     
    c.close()
    conn.close()


    co2Equivalent_plot = figure(title='CO2 Equivalent:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    co2Equivalent_plot.line(times, co2Equivalents, name='CO2 Equivalent', color='darksalmon', line_width=1)
    co2Equivalent_plot.circle(times, co2Equivalents, name='CO2 Equivalent', fill_color='white', size=8)
    
    co2Equivalent_plot.xaxis.axis_label = 'Time'
    co2Equivalent_plot.yaxis.axis_label = 'CO2 Equivalent [?]'

    co2Equivalent_plot.ygrid.minor_grid_line_color = 'navy'
    co2Equivalent_plot.ygrid.minor_grid_line_alpha = 0.05

    co2Equivalent_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('CO2 Equivalent', '@y')],
                   formatters={'x': 'datetime'}))

    co2Equivalent_script, co2Equivalent_div = components(co2Equivalent_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] co2Equivalent_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=co2Equivalent_script, plot_div=co2Equivalent_div, cdn_js=cdn_js) 



@app.route('/breathVocEquivalent_plot/<name>')
def breathVocEquivalent_plot(name):

    #collect data from DB
    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] staticIaq_plot for "+name+" started!")

    conn = sqlite3.connect("db/sensor_data.db")
    c = conn.cursor()

    c.execute("""SELECT timeNow, breathVocEquivalent FROM """+name)

    times = []
    breathVocEquivalents = []

    i = 0
    for row in c.fetchall():

        times.append(datetime.fromtimestamp(int(row[0])))
        breathVocEquivalents.append(row[1])
     
    c.close()
    conn.close()


    breathVocEquivalent_plot = figure(title='Breath VOC Equivalent:', tools='xpan,xwheel_zoom,reset', active_drag = None, plot_width=bokeh_plot_width, plot_height=600, toolbar_location='above', x_axis_type="datetime")
    breathVocEquivalent_plot.line(times, breathVocEquivalents, name='Breath VOC Equivalent', color='darkred', line_width=1)
    breathVocEquivalent_plot.circle(times, breathVocEquivalents, name='Breath VOC Equivalent', fill_color='white', size=8)
    
    breathVocEquivalent_plot.xaxis.axis_label = 'Time'
    breathVocEquivalent_plot.yaxis.axis_label = 'Breath VOC Equivalent [?]'

    breathVocEquivalent_plot.ygrid.minor_grid_line_color = 'navy'
    breathVocEquivalent_plot.ygrid.minor_grid_line_alpha = 0.05

    breathVocEquivalent_plot.add_tools(HoverTool(tooltips=[('Name', '$name'), ('Time', '@x{%Y-%m-%d %H:%M}'), ('Breath VOC Equivalent', '@y')],
                   formatters={'x': 'datetime'}))

    breathVocEquivalent_script, breathVocEquivalent_div = components(breathVocEquivalent_plot)

    cdn_js=CDN.js_files

    print("["+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+" UTC] breathVocEquivalent_plot for "+name+" done!")
    return render_template('bokeh_plot.html', name=name, plot_script=breathVocEquivalent_script, plot_div=breathVocEquivalent_div, cdn_js=cdn_js) 


@app.route('/multiple_plots_view/<name>')
def multiple_plots(name):
        
    return render_template('multiple_plots_view.html', name=name)
        
    
    
if __name__ == '__main__':
    app.run(debug = False) 