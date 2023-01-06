import requests, time, datetime
from datetime import date
from twilio.rest import Client

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

rome_timezone = datetime.timezone(datetime.timedelta(hours=1))

weekly_high_impact_news = []

def filter_high_impact(json):
    for i in range(len(json)):
        if json[i]["impact"] == "High" and (json[i]["country"] == "USD" or json[i]["country"] == "EUR" or json[i]["country"] == "GBP" or json[i]["country"] == "CAD"):
            weekly_high_impact_news.append({
                "title" : json[i]["title"],
                "currency" : json[i]["country"],
                "date" : json[i]["date"],
            })

    print(weekly_high_impact_news)

    account_sid = "ACab92ee3421e206cde9b74e854c56d11e"
    auth_token = "2b6c1441a392dd9816b053bad826a335"

    client = Client(account_sid, auth_token)

    today = date(date.today().year, date.today().month, date.today().day) #Getting today's date
    message_body = "*EVENTI DI OGGI:* \n\n"

    for i in range(len(weekly_high_impact_news)):
        aus = weekly_high_impact_news[i]["date"].split('T')
        if str(today) == str(aus[0]): #aus[0] is now the specific news' day (ex: 2023-01-05)
            init_hour = aus[1].split(':00-') #hour[0] is now the specific news' hour release (ex: 08:30)

            #Converting manually to rome's timezone (utc + 1)
            convert_to_rome_tz = str(init_hour[0]).split(':') #splitting hours from minutes (HOUR -> convert_to_rome_tz[0]; MINUTES -> convert_to_rome_tz[1])
            final_hour = str(int(convert_to_rome_tz[0]) + 6) #adding 6 hours in order to convert in UTC+2
            specific_hour_date = f"{final_hour}:{convert_to_rome_tz[1]}" #from '08:30' to '14:30'

            message_body += f"Ora: *{specific_hour_date}*\nCurrency: {weekly_high_impact_news[i]['currency']}\nEvento: {weekly_high_impact_news[i]['title']}\n\n"

    client.messages.create(
        to = "whatsapp:+393756689121",
        from_ = "whatsapp:+14155238886",
        body = message_body
    )
    print(message_body)
    time.sleep((3600 * 24))

def main():
    response = requests.get(URL)
    print(response.status_code)

    while response.status_code != 200:
        print("Error")
        main()

    json_calendar = response.json()
    filter_high_impact(json_calendar)

    time.sleep(604800) #for a WEEK


while True:
    main()