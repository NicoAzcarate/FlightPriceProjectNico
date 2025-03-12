import os

# Define the Kaggle dataset
dataset = "dilwong/flightprices"

# Check if kaggle is installed
try:
    import kaggle
except ImportError:
    os.system("pip install kaggle")

# Download dataset
os.system(f"kaggle datasets download -d {dataset} -p ./flight_data")

# Unzip the dataset
os.system("unzip ./flight_data/flightprices.zip -d ./flight_data")