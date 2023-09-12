import requests
from constants import SHEETY_ENDPOINT, HEADER

turn_on = True

while turn_on:
    name = input('Enter username for new user: ')
    contact = input('Enter contact method for new user: ')

    sheety_endpoint = SHEETY_ENDPOINT
    header = {'Authorization': HEADER}
    sheety_params = {
        "sheet1": {
            'user': name,
            'contacts': contact
        }
    }
    try:
        request = requests.post(url=sheety_endpoint, json=sheety_params, headers=header)
        request.raise_for_status()
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
        check_system = input('Do you want to continue? : ')
        if check_system.lower() == 'yes' or check_system.lower() == 'y':
            continue
        elif check_system.lower() == 'no' or check_system.lower() == 'n':
            turn_on = False
