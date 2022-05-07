# Data-Acquisition

Data Acquisition for our Smart Cities project of an energy consumption dataset and Twitter tweets data.

## Download and place data
Since data should not be stored in git repositories, the energy consumption data (csv) should be placed in the energy-consumption/data folder. It can be downloaded at the following url:
https://www.kaggle.com/datasets/kaggle/world-development-indicators?resource=download&select=Indicators.csv 
The archive should be decompressed and the file Indicators.csv should be placed under the energy-consumption/data folder.

## Set up the virtual environment
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