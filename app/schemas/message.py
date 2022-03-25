def messageEntity(message) -> dict:
    return{
        "_id": str(message['_id']),
        "sender": message['sender'],
        "receivers": message['receivers'],
        "subject": message["subject"],
        "content": message["content"],
        "status": message["status"]
    }

def messageEntities(messages) -> list:
    return [messageEntity(message) for message in messages]