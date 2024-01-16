import pandas as pd
import json
import datetime as dt
import sys
from pathlib import Path
#from data_processing.preprocessing import process_data, load_clean_data
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from data_processing.preprocessing import process_data, load_clean_data



def build_pipeline(filename  = "output_json/"): # Filename to save output file
    # Step 1: Clean the data if necessarry
    drugs_df, clinical_trials_df, pubmed_df, pubmed_json_df= load_clean_data()
    # Step 2: Process the cleaned data and Generate final output
    graph = process_data(drugs_df,clinical_trials_df, pubmed_df,pubmed_json_df)

    # Step 3: Any additional steps (like data transformation, analysis, etc.)
    # ...

    # Step 4: This could be saving data to a database, a file, or passing it to another system
    # ...
    now = dt.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H")
    file_extension = ".json"
    # Create the file name with the timestamp
    file_path = f"{filename}_{timestamp}.{file_extension}"
    with open(file_path, 'w') as file:
        json.dump(graph, file , indent=4)
    print("data saved ........................... in the following folder ",filename )

    return graph
   

if __name__ == "__main__":
    build_pipeline()