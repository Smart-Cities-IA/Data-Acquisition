import pandas as pd

def clean_data(tw):
    tw["start_date"] = pd.to_datetime(tw["start_date"]) 
    tw["end_date"] = pd.to_datetime(tw["end_date"]) 
    tw['date'] = [d.date() for d in tw['start_date']]
    return tw