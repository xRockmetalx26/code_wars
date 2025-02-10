import re

def validator(message: str) -> bool:
    if not message: return True

    is_valid =  message.isalnum() and message[0].isnumeric()
    if not is_valid: return False

    numbers = [int(x) for x in re.split(r'[a-zA-Z]+', message) if x]    
    words = [x for x in re.split(r'[0-9]+', message) if x]

    if len(numbers) != len(words):
        return False

    for i in range(len(numbers)):
        if numbers[i] != len(words[i]):
            return False

    return True

test = '3hey5hello2hi'

print(validator(test))
