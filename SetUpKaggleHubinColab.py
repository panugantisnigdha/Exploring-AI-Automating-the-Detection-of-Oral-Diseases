!pip install kagglehub --upgrade

import kagglehub

# Download latest version of the dataset
path = kagglehub.dataset_download("salmansajid05/oral-diseases")

print("Dataset downloaded to:", path)
