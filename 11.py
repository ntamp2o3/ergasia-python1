import requests
 
#curl -s --user 'api:key-d971ef34fe87ea5bc26c3bd290bc4438' htps://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages 
#-F from='kpatsak@gmail.com' -F to='tester@mailinator.com' -F subject='Hello Tester' -F text='Hope you enjoy spamming :p'

def send_simple_message(email, beer):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages",
        auth=("api", "key-d971ef34fe87ea5bc26c3bd290bc4438"),
        data={"from": "kpatsak@gmail.com",
              "to": ["{0}".format(email)],
              "subject": "Hello i have some good beer to purpose you",
              "text": "Hope you enjoy this beer that i found {0}".format(beer)})

# minima enimerosis
print ("Will Download Random Beer.... please wait...")


url = "https://api.punkapi.com/v2/beers/random"
r = requests.get(url)

beer = r.json()[0]["name"];

print ("I Get a Beer : " +  r.json()[0]["name"] + " TagLine : " + r.json()[0]["tagline"])

#zitaei to email tou xristi pou tha stilis to email
userEmail = input("Give a email to send the beer !!! ")


print ("I will send the beer to : " + userEmail + " please wait....")

#kalei tin function tou dino to email pou pires kai tin mpira pou pires kai lamvanei mia apantisi piso apo to HTTP POST Request
result = send_simple_message(userEmail,beer)

if (result.status_code == 200):
	print ("Email sent to : " + userEmail)
else: #opoiodipote allo status ektos tou 200 simenei apotixia kai gia auto bgazoume kai to text tou apotelesmatos ti sinevi
	print ("Error sending email : " + str(result.status_code) + result.text)





