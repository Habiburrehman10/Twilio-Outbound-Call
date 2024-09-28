from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
 
app = Flask(__name__)
 
# Your Twilio credentials
ACCOUNT_SID = ''  
AUTH_TOKEN = ''    
TWILIO_NUMBER = ''  
 
client = Client(ACCOUNT_SID, AUTH_TOKEN)
 
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Twilio Calling Service!"})
 
@app.route('/call', methods=['POST'])
def make_call():
    # Extract the target phone number from the POST request
    to_number = ''
    to_number = request.json.get('to_number')  # Number should be provided in JSON format 
    
    if not to_number:
        return jsonify({"error": "Phone number is missing!"}), 400
    response = VoiceResponse()
    response.say("Hello World")
 
    try:
        # Make the call via Twilio
        call = client.calls.create(
            to=to_number,
            from_=TWILIO_NUMBER,
            twiml=str(response)
        )
        return jsonify({"message": f"Call initiated to {to_number}. Call SID: {call.sid}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == "__main__":
    app.run(debug=True, port=5000)