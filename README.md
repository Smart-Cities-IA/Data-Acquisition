<img src="img/smart-grid.jpeg" />

## Energy Consumption Awareness 

The goal of this project is writing two data acquisition modules which read and process raw data and display interesting charts on a dashboard to perform analysis.

### Project structure 
The project is composed of three Python modules:
- app
- energy-consumption
- twitter

#### App
This module contains the code for cleaning the data from the export folder and for the development of the dashboard.
The Dashboard is done with the Python library Plotly Dash.
#### Energy-Consumption
This module is responsible for reading the csv raw data (Indicators.csv) downloaded Kaggle. 
We selected the right column we wanted to keep and we pivoted the table since all the kpi were contained in the same column which is not ideal for analysis. 
This module exports the processed csv to the export folder.

#### Twitter
This module is responsible for acquiring data from Twitter for certain keywords/hashtags. 
The data is fetched using Twitter API. 
Since there's limitation to the Twitter API, we get the tweets count per hour for the 7 last days for each keywords/hashtags.  
The end goal would be to automate this module to be run every week (since we get the data for the past 7 days). 
After few months~years, we would have a valuable dataset to run more interesting time-series analysis. 

### Set up the data for energy-consumption module
Since data should not be stored in git repositories, the energy consumption data (csv) should be placed in the energy-consumption/data folder. It can be downloaded at the following url:
https://www.kaggle.com/datasets/kaggle/world-development-indicators?resource=download&select=Indicators.csv  
The archive should be decompressed and the file Indicators.csv should be placed under the raw-data folder.

## Run the code

### Set up the virtual environment
In order to run the code, an virtual environment should be created and the library installed by running the following commands

**Create virtual environment** 
```
python3 -m venv env
```
**Activate the virtual environment**
```
activate env/bin/activate
```
**Install Python libraries**
```
pip install -r requirements.txt
```
**Run script**
```
python main.py
```
**Deactivate the virtual environment**
```
deactivate
```

#### Run Energy-Consumption Data Acqsuition
```
python src/energy-consumption/main.py
```
The result of the data acquisition and processing is exported to the exports folders

#### Run Twitter Data Acqsuition
```
python src/twitter/main.py
```
The result of the data acquisition and processing is exported to the exports folders

#### Run the Dashboard
```
python src/app/main.py
```
The dashboard will be run on http://127.0.0.1:8050/