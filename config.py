import pyrebase

config = {
    "apiKey": "AIzaSyDJyRtJAWXAEVeZpkemzHgSopT69c78vP0",
    "authDomain": "safe-9b5da.firebaseapp.com",
    "databaseURL": "https://safe-9b5da.firebaseio.com", 
    "projectId": "safe-9b5da",
    "storageBucket": "safe-9b5da.appspot.com",
    "messagingSenderId": "260761786014",
    "appId": "1:260761786014:web:46f404b20062a99c3dcd8f",
    "measurementId": "G-LHLSNMS9L5"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()