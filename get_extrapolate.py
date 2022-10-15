import numpy as np
import pandas as pd
import spacy
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.express as px
import dash_daq as daq

allowance = pd.read_csv('allowance.csv')
emissions = pd.read_excel('emissions.xlsx')
aviation_allowance = pd.read_csv('aviation_allowances.csv')



aviation_allowance['ETS Information'] = aviation_allowance['ETS Information'].apply(lambda x: x.replace(" ", ""))
aviation_allowance['ETS Information'] = pd.to_numeric(aviation_allowance['ETS Information'])

countries = pd.unique(allowance['registry'])
countries_list = [{'label': c, 'value': c} for c in countries]

emissions_sectors = pd.unique(emissions['main activity sector name'])
emissions_dict = {k: k[2:] for k in emissions_sectors}
activity = pd.unique(allowance['activity'])
activity_dict = {a: a for a in activity}


for i in emissions_dict.keys():
    if emissions_dict[i][0] == '-':
        emissions_dict[i] = emissions_dict[i][3:]
    elif emissions_dict[i][0] == '\\':
        emissions_dict[i] = emissions_dict[i][4:]
    else:
        1 + 10
    emissions_dict[i] = emissions_dict[i].replace('Production of', '')
    emissions_dict[i] = emissions_dict[i].replace('Manufacture of', '')
    emissions_dict[i] = emissions_dict[i].replace('Production or processing of', '')
    emissions_dict[i] = emissions_dict[i].strip()


for i in activity_dict.keys():
    
    activity_dict[i] = activity_dict[i].replace('Production of', '')
    activity_dict[i] = activity_dict[i].replace('Manufacture of', '')
    activity_dict[i] = activity_dict[i].replace('Production or processing of', '')
    activity_dict[i] = activity_dict[i].replace('Installations for the production of', '')
    activity_dict[i] = activity_dict[i].strip()

emissions_dict = dict((v,k) for k,v in emissions_dict.items())

activity_dict = dict((v,k) for k,v in activity_dict.items())

count = 0
bool_dict = {}
sectors = []
for key,val in emissions_dict.items():
    bool_dict[key] = False 
    boolean = False
    for act in activity_dict.keys():
        if key == act:
            print(act)
            count += 1
            bool_dict[act] = True
            sectors += [act]
sectors_list = [{'label': s, 'value': s} for s in sectors]

pd.unique(allowance['activityCategory'])

def extrapolate(country, sector, percent):
    
    #visualize 2010-2021
    #use regression to predict 2021-2030
    #regress emissions on allowances
    #visualize the forecast
    #assume geometric decay at rate rate < 1
    
    rate = 1 - percent/100
    sector_allow = activity_dict[sector]
    sector_emission = emissions_dict[sector]
    
    allow = allowance[(allowance['registry'] == country) & (allowance['activity'] == sector_allow)]
    emission = emissions[(emissions['main activity sector name'] == sector_emission) & (emissions['country']== country)]
    
    allocated_total = []
    emissions_total = []
    
    for year in range(2005, 2022):
        s = sum(allow[allow['year'] == year]['allocatedTotal'])
        if s:
            alloc = s
            allocated_total += [alloc]
            emissions_total += [sum(emission[emissions['year'] == year]['value'])]
        else:
            allocated_total += [s]
            emissions_total += [sum(emission[emissions['year'] == year]['value'])]
            

    
    try:
        model = np.polyfit(allocated_total, emissions_total, 1)
    except np.linalg.LinAlgError:
        model = np.polyfit(allocated_total, emissions_total, 0)
    predict = np.poly1d(model)
    
    future_allocation = []

    for year in range(2021, 2030):
        alloc = rate*alloc
        future_allocation += [alloc]
    
    
    forecasts = predict(future_allocation)
    forecasts = np.where(forecasts<0, 0, forecasts)
    
    return allocated_total, future_allocation, emissions_total, list(forecasts) 