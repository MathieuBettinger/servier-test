import pandas as pd


def load_pubmed(file ="data_pipeline_project/data/" ):
    # Load and data anlysis 
    data = pd.read_csv(file +"pubmed.csv")
    print(data) 
    return data

# Step to use if cleaning is necessary

def cleaning_pubmed(data):
    #cleaning data clinical steps
    data_cleaned  = data_cleaned
    return data_cleaned