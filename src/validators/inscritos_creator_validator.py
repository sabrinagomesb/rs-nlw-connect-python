from cerberus import Validator

def inscritos_creator_validator(request: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": { "type": "string", "required": True, "empty": False },
                "email": { "type": "string", "required": True, "empty": False, "regex": r"^[\w\.-]+@[\w\.-]+\.\w+$" },
                "link": { "type": "string", "required": False, "empty": False },
                "evento_id": { "type": "integer", "required": True, "empty": False, "min": 1 }


            }
        }
    })

    response = body_validator.validate(request.json)

    if response is False:
        print(body_validator.errors)


