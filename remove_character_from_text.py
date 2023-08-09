def remove_character_from_text(text, character):
    result = []
    
    for char in text:
        if char.lower() != character.lower():
            result.append(char)
    
    return "".join(result)

input_text = "A beautiful day in the city park. The birds are chirping and the sun is shining."
character_to_remove = 'A'

print(remove_character_from_text(input_text, character_to_remove))
