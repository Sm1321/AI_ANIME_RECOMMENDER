import pandas as pd


class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv


    def load_and_process(self):
        df = pd.read_csv(self.original,encoding  = 'utf-8',error_bad_lines = False).dropna()
        requried_cols = {'Name','Genres','sypnopsis'}
        missing = requried_cols - set(df.columns)
        if missing:
            raise ValueError("Missing Column in CSV File")
        df['combined_info'] = (
            "Title: " + df['Name'] + " Overview"
        )
        
        

