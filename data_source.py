import pandas as pd
from enum import Enum

def get_data_frame():
    df = pd.read_csv('data/customerChurnData.csv')
    return df

class Dataset(Enum):
    ENROL = "enrol"
    PUPILS = "pupils"
    SPEND = "spend"

def get_bpp_5_data(dataset: Dataset, discard_rows = 3):
    # Map enum values to file paths
    file_map = {
        Dataset.ENROL: "data/bpp_topic_5_data/API_SE.PRM.ENRL.TC.ZS_DS2_en_csv_v2_131293.csv",
        Dataset.PUPILS: "data/API_SE.SEC.CUAT.UP.ZS_DS2_en_csv_v2_123269.csv",
        Dataset.SPEND: "data/API_SE.PRM.ENRL_DS2_en_csv_v2_6679.csv",
    }

    # Get the correct file path based on the enum
    file_path = file_map.get(dataset)
    print(file_path)

    if not file_path:
        raise ValueError(f"Invalid dataset type: {dataset}")

    # Read the corresponding CSV
    df = pd.read_csv(file_path, skiprows=discard_rows)
    return df

# Example usage
# data = get_bpp_5_data(Dataset.ENROL)
# print(data.head())