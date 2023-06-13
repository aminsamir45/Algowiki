# Extract the document ID from the URL - middle id
import pandas as pd
import requests

document_id = "1c6HTfHQfp7MIg1LFo6_wFOzKLIHA1rzVpDxXIPosRQ0"

def sheet_to_df(sheet_id: int, name: str document_id = document_id) -> pd.DataFrame:
    """ Function that takes in a google sheet's id number and document id as input and returns
        the dataframe of the particular sheet as output """
        
    # CSV download link
    csv_url = f"https://docs.google.com/spreadsheets/d/{document_id}/export?format=csv&gid={sheet_id}"

    # Download the CSV file
    response = requests.get(csv_url)
    csv_data = response.content

    # Save the CSV data to a file
    csv_file = f"{name}_visualizations.csv"
    with open(csv_file, "wb") as file:
        file.write(csv_data)

    # Read the CSV file into a DataFrame using pandas
    df = pd.read_csv(csv_file)
    
    return df
