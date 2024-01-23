
# Create a Virtual ENV: cd d:\CODE\Proj_Data
# Install VENV: pip install pipenv
# pipenv install requests

# Upgrade pip Version : python.exe -m pip install --upgrade pip
# Install Library: python -m pip install matplotlib 
# python -m pip install numpy

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

def test():
 x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
 plt.plot(x, np.sin(x))       # Plot the sine of each x point
 plt.show()                   # Display the plot

def list():
    ls=[1,2,3,4,5,6]
    print(ls)
    print(type(ls))
    print(ls[:5])

def req():
  
    url = "https://reqres.in/api/users/5"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    data = data["data"]
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.T
    print(response.text)

if __name__== "__main__":
    req()
    # test()
