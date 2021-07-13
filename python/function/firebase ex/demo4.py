from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://python-rosy-default-rtdb.firebaseio.com/,None")
result = fire.put("employee","101",{"name":"rosy","salary":1850000.00})
print(result)