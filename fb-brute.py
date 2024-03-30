import requests
import time
from bs4 import BeautifulSoup

def login_facebook(email, password):
    session = requests.Session()
    
    try:
        # Initial request to get cookies and required parameters
        response = session.get('https://www.facebook.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        inputs = soup.find_all('input', {'type': ['hidden', 'submit']})
        data = {input.get('name', ''): input.get('value', '') for input in inputs}

        # Update data with login credentials
        data['email'] = email
        data['pass'] = password

        # Send login request
        response = session.post('https://www.facebook.com/login.php?login_attempt=1', data=data)

        # Check login response
        if 'c_user' in response.cookies:
            print("Login successful.")
        else:
            print("Login failed. Check your email and password.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        session.close()

if __name__ == "__main__":
    email = input("Enter Facebook email: ")
    password = input("Enter Facebook password: ")
    
    login_facebook(email, password)
