import pandas as pd
import json
import datetime as dt
import sys
from pathlib import Path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
#from data_cleaning.clinical_trials_cleaning import cleaning_clinical
#from data_cleaning.pubmed_csv_cleaning import cleaning_pubmed
#from data_cleaning.pubmed_json_cleaning import cleaning_pubmed_json


def load_clean_data(file = "src/data/"): 
    # Read every csv 
    drugs_df = pd.read_csv(file +'drugs.csv')
    clinical_trials_df = pd.read_csv(file +'clinical_trials.csv')
    pubmed_df = pd.read_csv(file +'pubmed.csv')

    # Manually parse the pubmed.json file
    with open(file + "pubmed.json", 'r') as files:
        pubmed_json_data = json.load(files)

    # Convert the parsed data to a DataFrame and display the first few rows
    pubmed_json_df = pd.DataFrame(pubmed_json_data)

    #cleaning if necessary
    ##clinical_trials_df = cleaning_clinical(clinical_trials_df)
    ##pubmed_df = cleaning_pubmed(pubmed_df)
    ##pubmed_json_df= cleaning_pubmed_json(pubmed_json_df)

    return drugs_df, clinical_trials_df, pubmed_df,pubmed_json_df


def process_data(drugs_df, clinical_trials_df, pubmed_df,pubmed_json_df):
    # Initialize a dictionary to hold the graph data
    graph = {}

    # In lower case to normalise data between title text and drug name
    drugs_df['drug'] = drugs_df['drug'].str.lower()
    
    # Process pubmed Data
    for index, row in pubmed_df.iterrows():
        for drug in drugs_df['drug']:
            if drug in row['title'].lower():
                if drug not in graph:
                    graph[drug] = {'PubMed': [], 'ClinicalTrials': []}
                graph[drug]['PubMed'].append({'title': row['title'], 'date': row['date'], 'journal': row['journal']})

    # Process Pubmed json  Data
    for index, row in pubmed_json_df.iterrows():
        for drug in drugs_df['drug']:
            if drug in row['title'].lower():
                if drug not in graph:
                    graph[drug] = {'PubMed': [], 'ClinicalTrials': []}
                graph[drug]['PubMed'].append({'title': row['title'], 'date': row['date'], 'journal': row['journal']})

    # Process Clinical Trials Data
    for index, row in clinical_trials_df.iterrows():
        for drug in drugs_df['drug']:
            if drug in row['scientific_title'].lower():
                if drug not in graph:
                    graph[drug] = {'PubMed': [], 'ClinicalTrials': []}
                graph[drug]['ClinicalTrials'].append({'title': row['scientific_title'], 'date': row['date'], 'journal': row['journal']})

    return graph


# if __name__ == "__main__":
#     drugs_df, clinical_trials_df, pubmed_df,pubmed_json_df = load_clean_data()
#     graph = process_data(drugs_df, clinical_trials_df, pubmed_df,pubmed_json_df)
#     print(graph)
    