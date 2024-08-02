from app import app

# Necessary for deploying to Azure
import os
import json

# Fetch the service account key from environment variables
service_account_info = os.getenv("GCP_SERVICE_ACCOUNT_KEY")
if service_account_info is None:
    raise Exception("GCP_SERVICE_ACCOUNT_KEY not found")

# Convert the string back to a dictionary
credentials_dict = json.loads(service_account_info)

# Write the credentials to a file
with open('google.json', 'w') as f:
    json.dump(credentials_dict, f)

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google.json'



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
