import requests


# This scripts is getting data from CoinDesk API

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def showUSD():
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["USD"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["USD"]["rate"]  # getting price in USD from response.
    print(time,code,rate)
    
def showBGP():
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["BGP"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["BGP"]["rate"]  # getting price in USD from response.
    print(time,code,rate)

def showEuro():
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["EUR"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["EUR"]["rate"]  # getting price in USD from response.
    print(time,code,rate)
while True:
    try:
        print("1. Show Bitcoin Price in USD.")
        print("2. Show Bitcoin Price in GBP.")
        print("3. Show Bitcoin Price in EUR.")
        userInput = int(input("Please Enter Your Choice: "))
        if userInput == 1:
            showUSD()
            break
        elif userInput == 2:
            showGBP()
            break
        elif userInput == 3:
            showEURO()
            break
        else:
            print("Something Went Wrong, Please Try Again...")
            continue
    except:
        print("Something Went Wrong, Quitting...")
        break
