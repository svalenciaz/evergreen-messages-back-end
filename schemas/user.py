def userEntity(user) -> dict:
    return{
        "_id": str(user['_id']),
        "name": user['name'],
        "gender": user["gender"],
        "email": user["email"],
        "number": user["number"],
        "birth_date": str(user['birth_date']),
        "sender": user['sender'],
        "receiver": user["receiver"]
    }

def userEntities(users) -> list:
    return [userEntity(user) for user in users]