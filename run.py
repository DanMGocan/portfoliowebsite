from app import app

# Necessary for deploying to Azure
import os
import json

credentials_dict = json.loads(os.environ.get("GCP_SERVICE_ACCOUNT_KEY"))
with open('credentials/google.json', 'w') as f:
    json.dump(credentials_dict, f)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials/google.json'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
e