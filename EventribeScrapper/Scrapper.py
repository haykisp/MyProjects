import requests


#####################       Marilyn.csv
has_next_page = True
count = 0
page = 1
f = open('Marilyn.csv', 'w', encoding="utf-8")
while has_next_page:
    response = \
        requests.get("https://www.eventbrite.com/org/11118815675/showmore/?type=future&page=" + str(page)).json()[
            "data"]
    has_next_page = response["has_next_page"]
    for event in response["events"]:
        title = str(event['name']['text']).replace(",", " ")
        location = ' '.join(
            str(p).replace(",", " ") for p in event['venue']['address']['localized_multi_line_address_display'])
        date = event["start"]["local"][:10]
        url = event["url"]
        f.write(title + ',' + location + ',' + date + ',' + url + '\n')
        count += 1
    page += 1
f.close()
print("Events in Marilyn.csv  ->  " + str(count) + "   -->    https://www.eventbrite.com/o/event-promotions-by-new-york-events-list-11118815675")



#####################       Sania.csv
has_next_page = True
count = 0
page = 1
f = open('Sania.csv', 'w', encoding="utf-8")
while has_next_page:
    response = \
    requests.get("https://www.eventbrite.com/org/15032446657/showmore/?type=future&page=" + str(page)).json()["data"]
    has_next_page = response["has_next_page"]
    for event in response["events"]:
        title = str(event['name']['text']).replace(",", " ")
        location = ' '.join(
            str(p).replace(",", " ") for p in event['venue']['address']['localized_multi_line_address_display'])
        date = event["start"]["local"][:10]
        url = event["url"]
        f.write(title + ',' + location + ',' + date + ',' + url + '\n')
        count += 1
    page += 1
f.close()
print("Events in Sania.csv  ->  " + str(count) + "   -->    https://www.eventbrite.com/o/new-york-events-list-15032446657")



#####################       Sanic.csv
has_next_page = True
count = 0
page = 1
f = open('Sanic.csv', 'w', encoding="utf-8")
while has_next_page:
    response = \
    requests.get("https://www.eventbrite.com/org/17301181405/showmore/?type=future&page=" + str(page)).json()["data"]
    has_next_page = response["has_next_page"]
    for event in response["events"]:
        title = str(event['name']['text']).replace(",", " ")
        location = ' '.join(
            str(p).replace(",", " ") for p in event['venue']['address']['localized_multi_line_address_display'])
        date = event["start"]["local"][:10]
        url = event["url"]
        f.write(title + ',' + location + ',' + date + ',' + url + '\n')
        count += 1
    page += 1
f.close()
print("Events in Sanic.csv  ->  " + str(count) + "   -->    https://www.eventbrite.com/o/new-york-events-list-17301181405")


#####################       Sanid.csv
has_next_page = True
count = 0
page = 1
f = open('Sanid.csv', 'w', encoding="utf-8")
while has_next_page:
    response = \
    requests.get("https://www.eventbrite.com/org/18533809825/showmore/?type=future&page=" + str(page)).json()["data"]
    has_next_page = response["has_next_page"]
    for event in response["events"]:
        title = str(event['name']['text']).replace(",", " ")
        location = ' '.join(
            str(p).replace(",", " ") for p in event['venue']['address']['localized_multi_line_address_display'])
        date = event["start"]["local"][:10]
        url = event["url"]
        f.write(title + ',' + location + ',' + date + ',' + url + '\n')
        count += 1
    page += 1
f.close()
print("Events in Sanid.csv  ->  " + str(count) + "   -->    https://www.eventbrite.com/o/new-york-events-list-18533809825")