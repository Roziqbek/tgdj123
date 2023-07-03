import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'

def create_feedback(user_id,tel,location,food,many,check1,food2,many2,check2,food3,many3,check3,food4,many4,check4,food5,many5):
  url = f"{BASE_URL}/feedback/"
  if user_id and tel:
    post = requests.post(url=url,data={
      'user_id':user_id,
      'tel':tel,
      'location':location,
      'food':food,
      'many':many,
      'check1':check1,
      'food2':food2,
      'many2':many2,
      'check2':check2,
      'food3':food3,
      'many3':many3,
      'check3':check3,
      'food4':food4,
      'many4':many4,
      'check4':check4,
      'food5':food5,
      'many5':many5,
    })
    return "Adminga jo'natildi"
  else:
    return 'Amal oxirigacha ishlamadi qaytadan qurinib kuring'