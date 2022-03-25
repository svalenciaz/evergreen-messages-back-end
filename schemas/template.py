def templateEntity(template) -> dict:
    return{
        "_id": str(template['_id']),
        "name": template['name'],
        "subject": template["subject"],
        "content": template["content"],
    }

def templateEntities(templates) -> list:
    return [templateEntity(template) for template in templates]