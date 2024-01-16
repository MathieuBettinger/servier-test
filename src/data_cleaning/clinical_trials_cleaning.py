import pandas as pd



def load_clinical(file ="data_pipeline_project/data/" ):
    # Load and data anlysis 
    data = pd.read_csv(file +"clinical_trials.csv")
    print(data) 
    return data


def cleaning_clinical(data):
    #cleaning data clinical steps
    data_cleaned  = data_cleaned
    return data_cleaned