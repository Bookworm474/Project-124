#import required modules
from flask import Flask, jsonify, request

#create application to run
app = Flask(__name__)

#create "contacts" array containing JSON lists
contacts = [
    {
        "id": 1,
        "name": "Raju",
        "contact": "9987644456",
        "done": False
    },
    {
        "id": 2,
        "name": "Rahul",
        "contact": "9876543222",
        "done": False
    }
]

#to execute on default route (to confirm it"s working)
@app.route("/")
def hello_world():
    return "Hello World!"

#to execute on "add-data" route
@app.route("/add-data", methods=["POST"])
#function to add a contact
def add_contact():
    #if data is not provided
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data."
        }, 400)
    
    #create JSON list to add, taking given data and calculating index number
    contact_to_add = {
        "id": contacts[-1]["id"] + 1,
        "name": request.json["name"],
        "contact": request.json.get("contact"),
        "done": False
    }
    #add to 'contacts' array
    contacts.append(contact_to_add)
    #return message of success
    return jsonify({
        "status": "success",
        "message": "Contact added successfully."
    })

#to execute on 'get-data' route
@app.route("/get-data")
#function to fetch data
def get_contacts():
    return jsonify({
        "data": contacts
    })

#run application and debug
if (__name__ == "__main__"):
    app.run(debug = True)