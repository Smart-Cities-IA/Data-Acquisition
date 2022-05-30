import glob

import pandas as pd


def get_twitter_files_path():
    files_path = glob.glob("clean-data/*")
    twitter_files_path = []
    for file in files_path:
        if "twitter" in file:
            twitter_files_path.append(file)
    return twitter_files_path


def merge_dataframes_from_path(paths):
    dataframes = []
    for path in paths:
        dataframes.append(pd.read_csv(path, sep=";"))
    return pd.concat(dataframes, ignore_index=False, sort=False)
