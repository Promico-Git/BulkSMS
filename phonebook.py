from replit import db
import os

my_secret = os.environ['RECIPIENT_NUMBER'] # Protecting the recipient number



# This is the phonebook database
# Set up a dictionary to hold the contacts of who you wish to message
#db["Promise"] = {"First Name" : "Promise", "Last Name" : "Ndiagwalu", "Phone Number" : "+16xxxxxxxx9", "city" : "Toronto"}
#db["Chibuikem"] = {"First Name" : "Chibuikem", "Last Name" : "Ndiagwalu", "Phone Number" : "+2348xxxxxxxx9", "city" : "Abuja"}
db["Josephine"] = {"First Name" : "Josephine", "Last Name" : "Uchemefune", "Phone Number" : my_secret, "city" : "Vancouver"}

  

