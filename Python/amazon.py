import requests, time
from bs4 import BeautifulSoup
from twilio.rest import Client

# Define the product ID
#product_id = "B09CV6MB62" #PER LE LG FREE TONE FP9
#max_price = "100"

product_id = "B09BNVM9CP" #PER LE LG FREE TONE FP5
max_price = "49"

#product_id = "B07ZPCYF8F" #PER LE FNATIC REACT
#max_price = "38"

#product_id = "B0B88FZ5VM" #PER LE OPPO FREE ENCO 2i
#max_price = "50"

#product_id = "B07TLX61W7" #PER LE G PRO X
#max_price = "70"

#product_id = "B00SAYCXWG" #PER LE HYPERX CLOUD II
#max_price = "55"

price = ""
product_name = "" 
sale = ""
sleep_time = 1800

URL = f"https://www.amazon.it/dp/{product_id}"

def sendRequest():
    response = requests.get(URL)
    print(response.status_code)

    while response.status_code != 200:
        print("An error occurred while making the API request.")
        sendRequest()
    
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", class_="a-offscreen").text
    sale = soup.find("span", class_="savingsPercentage").text
        
    #Getting product's name
    tr = soup.find("tr", class_ = "po-brand")
    td = tr.find("td", class_ = "a-span9")
    first_name_part = td.find("span", class_ = "a-size-base").text
    tr = soup.find("tr", class_ = "po-model_name")
    td = tr.find("td", class_ = "a-span9")
    last_name_part = td.find("span", class_ = "a-size-base").text
    product_name = f"{first_name_part} {last_name_part}"

    print(product_name)
    print(sale)
    print(price)

    aus = price.split('€')
    if aus[0] <= max_price:
        #Twilio Account SID and Auth Token
        account_sid = "ACab92ee3421e206cde9b74e854c56d11e"
        auth_token = "2b6c1441a392dd9816b053bad826a335"

        #Create a Twilio client
        client = Client(account_sid, auth_token)

        #Send an SMS message
        client.messages.create(
            to = "whatsapp:+393756689121",
            from_ = "whatsapp:+14155238886",
            body = f"SCONTO! '{product_name}' costa €{aus[0]} con uno sconto del {sale}\nLink: {URL}"
        )
        sleep_time = 3600
    else: 
        sleep_time = 1800 # if the price is > than max_price, it checks each 30 mins; else it checks each 60 mins

    time.sleep(sleep_time)

while True:
    sendRequest()
