import os

def getSecrets():
    secrets = {
        'MONGO_HOST':"mongodb+srv://jcoffee0604:coffee4life@cluster0.g3g4baj.mongodb.net/COFFEE?retryWrites=true&w=majority",
        'MONGO_DB_NAME':"COFFEE",
        'GOOGLE_CLIENT_ID': "",
        'GOOGLE_CLIENT_SECRET':"",
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
        'MY_EMAIL_ADDRESS':""
        }
    return secrets