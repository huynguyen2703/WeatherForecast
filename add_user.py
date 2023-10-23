# The "add_user.py" script is designed to streamline the process of collecting and posting user data to a Google Sheet.
# It provides a user-friendly command-line interface for inputting user information and offers the flexibility to
# update or add new entries to the target Google Sheet using the Sheety API.
# It also handles multiple HTTP errors if something goes wrong, this program is designed and implemented
# for role Data analyst especially.

import requests
from constants import SHEETY_ENDPOINT, HEADER

# Variable to control the loop
turn_on = True

while turn_on:
    # Prompt the user for username and contact method
    name = input('Enter username for new user: ')
    contact = input('Enter contact method for new user: ')

    # Set the endpoint and header for the Sheety API
    sheety_endpoint = SHEETY_ENDPOINT
    header = {'Authorization': HEADER}

    # Create a dictionary with user data
    sheety_params = {
        "sheet1": {
            'user': name,
            'contacts': contact
        }
    }
    try:
        # Send a POST request to add user data to the Google Sheet
        request = requests.post(url=sheety_endpoint, json=sheety_params, headers=header)
        request.raise_for_status()

        # Check the response status code
        if request.status_code == 200:
            print("Data successfully posted to Google Sheet.\n")
        else:
            print(f"Unexpected status code: {request.status_code}")
            break

    except requests.exceptions.HTTPError as http_error:
        # Handle HTTP errors (e.g., 4xx and 5xx)
        print(f"HTTP error occurred: {http_error}")
        break
    except requests.exceptions.ConnectionError as connection_error:
        # Handle network connection issues
        print(f"Connection error occurred: {connection_error}")
        break
    except requests.exceptions.Timeout as timeout_error:
        # Handle request timeout
        print(f"Request timeout error occurred: {timeout_error}")
        break
    except requests.exceptions.RequestException as request_exception:
        # Handle other request exceptions
        print(f"Request exception occurred: {request_exception}")
        break
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        break
    else:
        # Ask the user if they want to continue
        check_system = input('Do you want to continue? : ')
        if check_system.lower() == 'yes' or check_system.lower() == 'y':
            continue
        elif check_system.lower() == 'no' or check_system.lower() == 'n':
            turn_on = False
