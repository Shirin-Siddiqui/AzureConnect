from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=sentimentanaly3520726209;AccountKey=Y1DoWu5bf3/aGedhiTAypTE9MFqBSchIuhIdgTEheLRKVDJTJFCuBXL6uARDrmuu4xGC8Vhokcbu+ASth/HySQ==;EndpointSuffix=core.windows.net"
container_name = "azureml-blobstore-9fee8675-8543-42ba-ab91-89f1a76206d3"
blob_name = "UI/2023-03-20_104628_UTC/training.1600000.processed.noemoticon.csv"

# Local file path to save the downloaded CSV file
local_file_path = "/Users/shirinsiddiqui/sentiment/downloaded.csv"

# Create a BlobServiceClient object from the connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get a reference to the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob content as bytes
blob_content = blob_client.download_blob().readall()

# Decode the blob content into a string
csv_data = blob_content.decode("utf-8")

# Save the CSV data to a local file
with open(local_file_path, "w") as f:
    f.write(csv_data)
