import pandas as pd
import os

def vaccines(desired_date):
    input_filename = "./data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
    df = pd.read_csv(input_filename, compression="gzip", converters={'FIPS' : str})
    print("START:", df.shape)
    
    # Filter by date
    desired_date = desired_date.replace("-", "/")
    df = df[df["Date"] == desired_date]

    # Extract columns of interest
    columns = ["FIPS", "Recip_County", "Recip_State", "Series_Complete_18PlusPop_Pct", "Census2019_18PlusPop"]
    df = df[columns]

    # Clean the dataset
    print("BEFORE:", df.shape)
    df = df.dropna()
    print("AFTER:", df.shape)

    # Output directory
    output_dir = "./data/CDC"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_filename = os.path.join(output_dir, "vaccinations-" + desired_date[:2] + '-' + \
                    desired_date[3:5] + "-" + desired_date[6:11] + ".csv")

    # Write filtered dataframe to a file
    df.to_csv(output_filename, index=False)
    return df

def create_vaccines():
    """This function generates vaccination data for nine different dates.
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
        vaccines(date)

if __name__ == "__main__":
    create_vaccines()
