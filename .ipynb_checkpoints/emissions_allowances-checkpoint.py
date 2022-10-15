{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import spacy\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly\n",
    "import plotly.graph_objs as go\n",
    "import dash\n",
    "from dash.dependencies import Input, Output\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html\n",
    "import pandas_datareader\n",
    "from pandas_datareader import data as web\n",
    "from datetime import datetime as dt\n",
    "import plotly.express as px\n",
    "import dash_daq as daq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "allowance = pd.read_csv('allowance.csv')\n",
    "emissions = pd.read_excel('emissions.xlsx')\n",
    "aviation_allowance = pd.read_csv('aviation_allowances.csv')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "aviation_allowance['ETS Information'] = aviation_allowance['ETS Information'].apply(lambda x: x.replace(\" \", \"\"))\n",
    "aviation_allowance['ETS Information'] = pd.to_numeric(aviation_allowance['ETS Information'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "countries = pd.unique(allowance['registry'])\n",
    "countries_list = [{'label': c, 'value': c} for c in countries]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "emissions_sectors = pd.unique(emissions['main activity sector name'])\n",
    "emissions_dict = {k: k[2:] for k in emissions_sectors}\n",
    "activity = pd.unique(allowance['activity'])\n",
    "activity_dict = {a: a for a in activity}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in emissions_dict.keys():\n",
    "    if emissions_dict[i][0] == '-':\n",
    "        emissions_dict[i] = emissions_dict[i][3:]\n",
    "    elif emissions_dict[i][0] == '\\\\':\n",
    "        emissions_dict[i] = emissions_dict[i][4:]\n",
    "    else:\n",
    "        1 + 10\n",
    "    emissions_dict[i] = emissions_dict[i].replace('Production of', '')\n",
    "    emissions_dict[i] = emissions_dict[i].replace('Manufacture of', '')\n",
    "    emissions_dict[i] = emissions_dict[i].replace('Production or processing of', '')\n",
    "    emissions_dict[i] = emissions_dict[i].strip()\n",
    "\n",
    "\n",
    "for i in activity_dict.keys():\n",
    "    \n",
    "    activity_dict[i] = activity_dict[i].replace('Production of', '')\n",
    "    activity_dict[i] = activity_dict[i].replace('Manufacture of', '')\n",
    "    activity_dict[i] = activity_dict[i].replace('Production or processing of', '')\n",
    "    activity_dict[i] = activity_dict[i].replace('Installations for the production of', '')\n",
    "    activity_dict[i] = activity_dict[i].strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "emissions_dict = dict((v,k) for k,v in emissions_dict.items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "activity_dict = dict((v,k) for k,v in activity_dict.items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ceramics\n",
      "gypsum or plasterboard\n",
      "pulp\n",
      "paper or cardboard\n",
      "coke\n",
      "pig iron or steel\n",
      "mineral wool\n",
      "cement clinker\n",
      "Combustion of fuels\n",
      "glass\n",
      "ferrous metals\n",
      "secondary aluminium\n",
      "Metal ore roasting or sintering\n",
      "nitric acid\n",
      "Refining of mineral oil\n",
      "non-ferrous metals\n",
      "ammonia\n",
      "bulk chemicals\n",
      "soda ash and sodium bicarbonate\n",
      "lime, or calcination of dolomite/magnesite\n",
      "hydrogen and synthesis gas\n",
      "carbon black\n",
      "primary aluminium\n",
      "Capture of greenhouse gases under Directive 2009/31/EC\n",
      "glyoxal and glyoxylic acid\n",
      "adipic acid\n"
     ]
    }
   ],
   "source": [
    "count = 0\n",
    "bool_dict = {}\n",
    "sectors = []\n",
    "for key,val in emissions_dict.items():\n",
    "    bool_dict[key] = False \n",
    "    boolean = False\n",
    "    for act in activity_dict.keys():\n",
    "        if key == act:\n",
    "            print(act)\n",
    "            count += 1\n",
    "            bool_dict[act] = True\n",
    "            sectors += [act]\n",
    "sectors_list = [{'label': s, 'value': s} for s in sectors]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Cement/Lime', 'Glass/Ceramics', 'Combustion', 'Pulp/Paper',\n",
       "       'Chemicals', 'Metal', 'Coke ovens', 'Refineries', 'Other',\n",
       "       'Hydrogen Production', 'Carbon Capture'], dtype=object)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.unique(allowance['activityCategory'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def extrapolate(country, sector, percent):\n",
    "    \n",
    "    #visualize 2010-2021\n",
    "    #use regression to predict 2021-2030\n",
    "    #regress emissions on allowances\n",
    "    #visualize the forecast\n",
    "    #assume geometric decay at rate rate < 1\n",
    "    \n",
    "    rate = 1 - percent/100\n",
    "    sector_allow = activity_dict[sector]\n",
    "    sector_emission = emissions_dict[sector]\n",
    "    \n",
    "    allow = allowance[(allowance['registry'] == country) & (allowance['activity'] == sector_allow)]\n",
    "    emission = emissions[(emissions['main activity sector name'] == sector_emission) & (emissions['country']== country)]\n",
    "    \n",
    "    allocated_total = []\n",
    "    emissions_total = []\n",
    "    \n",
    "    for year in range(2005, 2022):\n",
    "        s = sum(allow[allow['year'] == year]['allocatedFree'])\n",
    "        if s:\n",
    "            alloc = s\n",
    "            allocated_total += [alloc]\n",
    "            emissions_total += [sum(emission[emissions['year'] == year]['value'])]\n",
    "        else:\n",
    "            allocated_total += [s]\n",
    "            emissions_total += [sum(emission[emissions['year'] == year]['value'])]\n",
    "            \n",
    "\n",
    "    \n",
    "    try:\n",
    "        model = np.polyfit(allocated_total, emissions_total, 1)\n",
    "    except np.linalg.LinAlgError:\n",
    "        model = np.polyfit(allocated_total, emissions_total, 0)\n",
    "    predict = np.poly1d(model)\n",
    "    \n",
    "    future_allocation = []\n",
    "\n",
    "    for year in range(2021, 2030):\n",
    "        alloc = rate*alloc\n",
    "        future_allocation += [alloc]\n",
    "    \n",
    "    \n",
    "    forecasts = predict(future_allocation)\n",
    "    forecasts = np.where(forecasts<0, 0, forecasts)\n",
    "    \n",
    "    return allocated_total, future_allocation, emissions_total, list(forecasts) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " Warning: This is a development server. Do not use app.run_server\n",
      " in production, use a production WSGI server like gunicorn instead.\n",
      "\n",
      " * Serving Flask app \"Hello World\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)\n",
      "/Users/abhinav/opt/anaconda3/lib/python3.7/site-packages/dash/resources.py:68: UserWarning: You have set your config to `serve_locally=True` but A local version of https://codepen.io/chriddyp/pen/bWLwgP.css is not available.\n",
      "If you added this file with `app.scripts.append_script` or `app.css.append_css`, use `external_scripts` or `external_stylesheets` instead.\n",
      "See https://dash.plot.com/external-resources\n",
      "  ).format(s[\"external_url\"])\n",
      "127.0.0.1 - - [15/Oct/2022 14:23:09] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [15/Oct/2022 14:23:09] \"\u001b[37mGET /_dash-dependencies HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [15/Oct/2022 14:23:09] \"\u001b[37mGET /_dash-layout HTTP/1.1\u001b[0m\" 200 -\n",
      "/Users/abhinav/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:24: UserWarning: Boolean Series key will be reindexed to match DataFrame index.\n",
      "127.0.0.1 - - [15/Oct/2022 14:23:10] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "/Users/abhinav/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:24: UserWarning:\n",
      "\n",
      "Boolean Series key will be reindexed to match DataFrame index.\n",
      "\n",
      "127.0.0.1 - - [15/Oct/2022 14:23:33] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "app = dash.Dash('Hello World')\n",
    "\n",
    "app.layout = html.Div([\n",
    "    html.Div([\n",
    "        html.Div([\n",
    "            html.Label('Country'),\n",
    "            dcc.Dropdown(\n",
    "                id='country',\n",
    "                options= countries_list,\n",
    "                multi=False,\n",
    "                value='Germany'\n",
    "            ),\n",
    "        ]),\n",
    "        html.Div([\n",
    "            html.Label('Sector'),\n",
    "            dcc.Dropdown(\n",
    "                id='sector',\n",
    "                options=sectors_list,\n",
    "                multi=False,\n",
    "                value= 'bulk chemicals'\n",
    "            ),\n",
    "        ]),\n",
    "        html.Div([html.Label('Annual Freely Allocated Allowance Percent Reduction (from 2021)'),\n",
    "    daq.Knob(id='percent', max=30, value = 5),\n",
    "    html.Div(id='knob-output-1')\n",
    "]),\n",
    "    ]),\n",
    "    dcc.Graph(id='my-graph')\n",
    "])\n",
    "\n",
    "@app.callback(Output('my-graph', 'figure'), [Input('country', 'value'), Input('sector', 'value'), Input('percent', 'value')])\n",
    "def update_graph(selected_dropdown_value1, selected_dropdown_value2, value3): #1, selected_dropdown_value2):\n",
    "    \n",
    "    country, sector, percent = selected_dropdown_value1, selected_dropdown_value2, float(value3)\n",
    "    x1,x2,y1,y2 = extrapolate(country, sector, percent)\n",
    "    x = x1 + x2\n",
    "    y = y1 + y2\n",
    "    feature = ['Historical']*(len(x1)) + ['Projected']*(len(x2))\n",
    "    years = list(range(2005, 2031))\n",
    "    df = pd.DataFrame({'x': x, 'y': y, 'DataType': feature, 'year': years})\n",
    "\n",
    "    data = px.bar(\n",
    "        df, x='year', y='y', \n",
    "        color=\"DataType\",\n",
    "        color_discrete_sequence=px.colors.qualitative.Set1,\n",
    "        hover_data = ['year', 'x', 'y'],\n",
    "        title= country.upper() +': Annual Emissions<br><sup>Sector: ' + sector.upper() + '</sup>',\n",
    "        labels={\n",
    "                     \"x\": \"Total Allocated Allowances (tons of CO2)\",\n",
    "                     \"y\": \"Emissions (tons of CO2)\",\n",
    "                     \"DataType\": \" \"\n",
    "                 }\n",
    "    )\n",
    "\n",
    "    return data\n",
    "\n",
    "app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
