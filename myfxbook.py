import requests, json

session_code = ""

#CREDENTIALS
email = ""
password = ""

def getSentiment(pair_name):
    url = f"https://www.myfxbook.com/api/get-community-outlook.json?session={session_code}"

    response = requests.get(url)
    print(f"getSentiment status code ->  {response.status_code}")
    
    while response.status_code != 200:
        getSentiment(pair_name)

    for index in range(len(response.json()['symbols'])):
        if(response.json()['symbols'][index]['name'] == pair_name):
            break

    short_percentage = response.json()['symbols'][index]['shortPercentage']
    long_percentage = 100 - short_percentage
    print(f"SHORTS: {short_percentage}\nLONGS: {long_percentage}")

def main():
    url = f"https://www.myfxbook.com/api/login.json?email={email}&password={password}"
    
    response = requests.get(url)
    print(f"first status code ->  {response.status_code}")

    while response.status_code != 200:
        print(f"Error: {response.json()['message']}")
        main()

    #session_code = response.json()["session"]
    #print(session_code)

    pair = input("Inserisci il pair per trovare il market sentiment: ")
    getSentiment(pair.upper())

main()