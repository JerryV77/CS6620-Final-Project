import pandas as pd
import os

def readit(filename):
    """This is a function that reads in a csv from a URL and returns a dataframe. It 
    removes any entries for which the FIPS code is entry.
    Parameters:
        filename: str
    Returns:
        pandas dataframe
    """
    # Read CSV while keeping FIPS as a string
    base = "https://raw.githubusercontent.com/"
    base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
    base += "csse_covid_19_daily_reports/"
    df = pd.read_csv(base + filename + ".csv", converters={'FIPS': str})
    return df[df['FIPS'] != ""]

def get_death_number_JHU(start, end):
    """This is a function that returns a dataframe that contains FIPS and the death number from start to end (two dates passed as strings), and create a CSV file in data.
    Parameters: 
        start: str , write it in form "03-01-2021",
        end: str,
    """
    data = {}

    df_deaths = readit(end)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] = row["Deaths"]

    df_deaths = readit(start)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] -= row["Deaths"]

    # Remove negative values
    data = {k: v for k, v in data.items() if v >= 0}

    # Output directory
    output_dir = "data/JHU"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write dictionary to a CSV file
    filename = os.path.join(output_dir, "deaths-" + \
               start[:2] + '-' + start[3:5] + "-" + start[6:10] + "-to-" + \
               end[:2] + '-' + end[3:5] + "-" + end[6:] + ".csv")

    with open(filename, 'w') as file:
        file.write("FIPS,Deaths\n")  # header
        for key, value in data.items():
            file.write(",".join([key, str(value)]) + "\n")
    df = pd.read_csv(filename)
    return df

def get_confirm_number_JHU(start, end):
    """This is a function that returns the confirmed number from start_date to end_date
    Parameters: 
        start_date:str , write it in form "05-01-2021",
        end_date: str,
    """
    data = {}

    df_confirmed = readit(end)
    for i, row in df_confirmed.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] = row["Confirmed"]

    df_confirmed = readit(start)
    for i, row in df_confirmed.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] -= row["Confirmed"]

    # Remove negative values
    data = {k: v for k, v in data.items() if v >= 0}

    # Output directory
    output_dir = "data/JHU"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write dictionary to a CSV file
    filename = os.path.join(output_dir, "confirmed-" + \
               start[:2] + '-' + start[3:5] + "-" + start[6:10] + "-to-" + \
               end[:2] + '-' + end[3:5] + "-" + end[6:] + ".csv")

    with open(filename, 'w') as file:
        file.write("FIPS,Confirmed\n")  # header
        for key, value in data.items():
            file.write(",".join([key, str(value)]) + "\n")
    df = pd.read_csv(filename)
    return df

def create_death_number_JHU():
    """This function writes death number into 9 (month) csv files, each file document death number from 03-01 to the end of this month
    Please create a JHU file in ../data First, Or this function will give error. 
    If you don't want to waste time inputting arguments to create a csv file for every month, please run this function.
    """
    start = "03-01-2021"
    ends = [
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
    for end in ends:
        get_death_number_JHU(start, end)

if __name__ == "__main__":
    create_death_number_JHU()
