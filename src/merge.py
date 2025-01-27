import os
import pandas as pd

def merge(date):
    """
    This function return a dataframe that contains merge data.
    But please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC
    Parameters: 
        date : str, The last date of each month.  form date = "11-30-2021"
    """
    base_CDC = "data/CDC/"
    base_JHU = "data/JHU/"
    df = pd.read_csv(base_CDC + "vaccinations-" + date + ".csv",
                     converters={'FIPS': str})
    deaths = pd.read_csv(
        base_JHU + "deaths-03-01-2021-to-"+date+".csv", converters={'FIPS': str})

    # Add the deaths data to the dataframe
    return df.merge(deaths, on='FIPS')

def write_merge_data_to_csv(date):
    """This function write a csv to directory data/Merge. 
    Parameters: 
        date: str, The last date of each month.  form date = "11-30-2021"
    """
    base_Merge = "data/Merge/"
    
    # Create the directory if it doesn't exist
    os.makedirs(base_Merge, exist_ok=True)
    
    df = merge(date)
    # print(df)
    df.to_csv(base_Merge+"vaccinations-and-deaths-" + date + '.csv', index=False)

def create_merge_data():
    """This function write 9 csvs to directory data/Merge. 
    Please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC
    """
    dates = [
        "03-31-2021",
        "04-30-2021",
        "05-31-2021",
        "06-30-2021",
        "07-31-2021",
        "08-31-2021",
        "09-30-2021",
        "10-31-2021",
        "11-30-2021"
    ]
    for date in dates:
        write_merge_data_to_csv(date)

if __name__ == "__main__":
    create_merge_data()
