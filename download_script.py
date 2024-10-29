#import token
from wiley_token import wiley_token
from doi import doi_list
import requests
from time import sleep

srs = [doi for doi in doi_list]

# Include token in header
headers = {
    "Wiley-TDM-Client-Token": wiley_token
}


# request for each doi
for doi in srs:
    # Construct URL
    url = f'https://api.wiley.com/onlinelibrary/tdm/v1/articles/{doi}'

    # Make a GET request to the Wiley TDM API
    response = requests.get(url, headers=headers)

    # Download PDF if status code indicates success
    if response.status_code == 200:

        # Name file after the DOI
        filename = f'{doi.replace("/", "_")}.pdf'

        # Write data to PDF file
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f'{filename} downloaded successfully')

    # Print status code if unsuccessful
    else:
        print(f"Failed to download PDF for {doi.replace('%2f', '/')}. Status code: {response.status_code}")

    # Wait 1 second to be nice on Wiley's servers
    sleep(1)
    