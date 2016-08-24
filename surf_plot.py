#!/usr/bin/env python
# coding: utf-8

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
from datetime import date, timedelta, datetime
import json
from urllib2 import Request, urlopen, URLError
from pandas.io.json import json_normalize

# set color for the plot
cc = 'w'

# Prepare plot
fig = plt.figure(figsize=(10,1.8))

# Define location
# Go to magicseaweed.com and search for location
# then look up id in url of search result
api_location = '296' # La Jolla
# You need to get your api key at magicseaweed.com and store it in mswapi.txt
f = open('surf.widget/mswapi.txt','r')
mswapikey = f.readlines()
f.close()
api_key = mswapikey[0]
# web address with api
api_url = 'http://magicseaweed.com/api/'+api_key+'/forecast/?spot_id='+api_location+'&fields=swell.*,localTimestamp'

try:
    response = urlopen(api_url)
    tmp = response.read()
    data = json.loads(tmp)
    df2 = json_normalize(data)
    df2['localTimestamp'] = pd.to_datetime(df2['localTimestamp'],unit='s')
    df2 = df2.set_index('localTimestamp')
    # df2.head()

    # More settings with rc
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : 11,
            'sans-serif' : 'Helvetica Neue',
            'weight': 'light'}

    plt.rc('font', **font)
    xtick = {'color' : cc}
    plt.rc('xtick', **xtick)
    ytick = {'color' : cc}
    plt.rc('ytick', **ytick)
    axes = {'labelcolor' : cc}
    plt.rc('axes', **axes)

    # Add a subplot
    ax = fig.add_subplot(111)

    # Set title
    ttl = 'Surf @ La Jolla, CA'
    fig.suptitle(ttl, fontsize=12, fontweight='normal', color=cc, family='sans-serif')

    # Resample to six hours
    df2 = df2.resample('3H').mean()

    idx = df2.index.date
    plt.bar(df2.index, df2['swell.absMaxBreakingHeight'],0.08,color='0.95',edgecolor='0.95',alpha=0.5,align='center')
    plt.bar(df2.index, df2['swell.absMinBreakingHeight'],0.08,color=cc,    edgecolor=cc,alpha=0.5,align='center')

    # Plot current time
    t = datetime.now()
    s = df2['swell.absMaxBreakingHeight']
    d = s.asof(t)
    plt.plot(t,d,marker='o',color='r',linewidth='0',markersize=8,alpha=0.5)

    # time label settings
    ax.xaxis.set_minor_locator(dates.DayLocator(interval=1))
    ax.xaxis.set_minor_formatter(dates.DateFormatter('\n%d-%a'))
    ax.xaxis.set_major_locator(dates.HourLocator(byhour=range(0,24,12)))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))

    # Remove grid lines (dotted lines inside plot)
    ax.grid(False)
    ax.set_ylabel('ft')

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_position(('outward', 10))
    ax.spines['bottom'].set_smart_bounds(True)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['top'].set_color(None)

    ax.tick_params(axis='x', colors=cc)
    ax.tick_params(axis='y', colors=cc)

    ax.xaxis.label.set_color(cc)
    ax.yaxis.label.set_color(cc)

    # Remove plot frame
    ax.set_frame_on(False)
    plt.savefig('surf.widget/surf.png', bbox_inches='tight',transparent=True,dpi=fig.dpi)

except URLError as e:
    ttl = 'no internet connection'
    fig.suptitle(ttl, fontsize=12, fontweight='normal', color=cc, family='sans-serif')
    plt.savefig('surf.widget/surf.png', bbox_inches='tight',transparent=True,dpi=fig.dpi)