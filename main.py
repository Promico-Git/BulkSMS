from weather import get_weather
from harryp import get_character
from nasa import get_spaceInfo
from twilio.rest import Client
import phonebook
import random
import os

import json
from flask import Flask, render_template

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Get NASA
space = get_spaceInfo()
list_people = ""
no_people = space["number"]
lists = space["people"]

for people in lists:
  list_people += people["name"] + ": " + people["craft"] + ". "

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/success')
def success():
  # initializing recipientDB that will hold the log for the html page
  recipientDB = ""

  # Get Contact from phonebook
  contact = phonebook.db.keys()
  for key in contact:
    first = phonebook.db[key]["First Name"]
    last = phonebook.db[key]["Last Name"]
    recipient = phonebook.db[key]["Phone Number"]
    city = phonebook.db[key]["city"]

    # Get Harry Potter character
    char = random.randint(0, 50)
    character = get_character()
    character_name = character[char]["name"]
    print(character_name)
    cast = character[char]["actor"]
    if cast == "":
      cast = "N/A"
      print(cast)
    else:
      print(cast)

    # Get character House
    housename = character[char]["house"]
    if housename == "":
      housename = "No"
      print(housename)
    else:
      print(housename)

    # Get character Image
    image = character[char]["image"]
    if image == "":
      image = "Sorry, no image to display for this character"
      print(image)
    else:
      print(image)

    # Get weather
    weather = get_weather(city)
    temp = round(weather["main"]["temp"] - 273.15, 2)
    feels_like = round(weather["main"]["feels_like"] - 273.15, 2)
    print(temp, feels_like)

    # Message to be sent to the recipient
    msg = f'Hello {first} {last}, the temperature in {city} is {temp} Celcius, and feels like {feels_like}. Your wizardary character from Harry Potter of the day is {character_name}, played by {cast}. They were assigned to {housename} house. Click link to see actors\' image: {image}. About space! Do you know there are {no_people} people in space right now. Their names and the spacecraft they are in are: {list_people}'

    #store message and recipient

    recipientDB += first
    recipientDB += ": "
    recipientDB += msg
    recipientDB += "\n\n"

    # Send Message
    message = client.messages \
                    .create(
                         body=msg,
                         from_=os.environ['TWILIO_NUMBER'],# Replace with your Twilio number.
                         to=recipient
                     )

    print(message.sid)

    # log message into a json file
    with open("message.json", "a") as file:
      json.dump(msg, file)
      file.write("\n")

  return render_template('success.html', recipientDB=recipientDB)


if __name__ == '__main__':
  app.run()
