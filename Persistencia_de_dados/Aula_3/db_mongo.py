import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
db= client["escola"]
estudantes = db["estudantes"]

estudantes.insert_one({"nome":"João","idade":20})

for estudantes in estudantes.find():
    print(estudantes)