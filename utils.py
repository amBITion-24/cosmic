import pandas as pd


def load_citymate_data(filepath):
    citymate_df = pd.read_csv(filepath)
    return citymate_df
