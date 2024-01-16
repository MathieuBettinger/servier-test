import pandas as pd



def load_drugs(file ="data_pipeline_project/data/" ):
    # Load and data anlysis 
    data = pd.read_csv(file +"drugs.csv")
    print(data) 
    return data


def cleaning_drugs(data):
    #cleaning data clinical steps
    data_cleaned  = data_cleaned
    return data_cleaned