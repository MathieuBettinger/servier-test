import pandas as pd
import json



def load_pubmed(file ="data_pipeline_project/data/" ):
    # Load and data anlysis 
    # Manually parse the pubmed.json file
    with open(file +"pubmed.json", 'r') as files:
        pubmed_json_data = json.load(files)

    # Convert the parsed data to a DataFrame and display the first few rows
    pubmed_json_df = pd.DataFrame(pubmed_json_data)
    print(pubmed_json_df) 
    return pubmed_json_df

# Step to use if cleaning is necessary

def cleaning_pubmed_json(pubmed_json_df):
    #cleaning data clinical steps
    data_cleaned = data_cleaned
    return data_cleaned