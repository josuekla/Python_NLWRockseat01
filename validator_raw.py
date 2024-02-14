from cerberus import Validator

body = {
    "date": {
        "elemento1": 123,
        "elemento2": "OláWold!",
        "elemento3": "123"
    }
}

body_validator = Validator({
    "date": {
        "type": "dict",
        "schema": {
            "elemento1": {"type": "float", "required": True, "empty": False},
            "elemento2": {"type": "string", "required": True, "empty": True},
            "elemento3": {"type": "string", "required": False, "empty": False}
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("Body OK")
