import requests, time

def readEmail():
    f = open("./credentials.txt")
    file_content = f.readlines()
    f.close()
    return file_content[0].strip()

def readPassword():
    f = open("./credentials.txt")
    file_content = f.readlines()
    f.close()
    return file_content[1].strip() 

def writeOnFile(shorts, longs, pair_name):
    f = open(f"C:/Users/edopi/OneDrive/Documenti/cAlgo/Sources/Robots/MarketSentiment/MarketSentiment/{pair_name}.txt", "w")
    f.write(f"{shorts}\n")
    f.write(f"{longs}\n")
    f.close()

def getSentiment(pair_name, session_code):
    url = f"https://www.myfxbook.com/api/get-community-outlook.json?session={session_code}"

    response = requests.get(url)
    print(f"getSentiment status code ->  {response.status_code}")
    
    while response.status_code != 200:
        getSentiment(pair_name, session_code)

    for index in range(len(response.json()['symbols'])):
        if(response.json()['symbols'][index]['name'] == pair_name):
            break

    short_percentage = response.json()['symbols'][index]['shortPercentage']
    long_percentage = 100 - short_percentage
    print(f"SHORTS: {short_percentage}/nLONGS: {long_percentage}")
    
    writeOnFile(short_percentage, long_percentage, pair_name) # writing datas on the file in order to be read by cAlgo BOT written in c#

def main():
    email = readEmail()
    password = readPassword()
    print(email, password)
    url = f"https://www.myfxbook.com/api/login.json?email={email}&password={password}"
    
    response = requests.get(url)
    print(f"first status code ->  {response.status_code}")

    print(response.json())

    while response.status_code != 200:
        print(f"Error: {response.json()['message']}")
        main()

    session_code = response.json()["session"]

    pair = input("Inserisci il pair per trovare il market sentiment: ")
    getSentiment(pair.upper(), session_code)

    time.sleep(3600) # every hour gives me the pair sentiment 

while True:
    main()
