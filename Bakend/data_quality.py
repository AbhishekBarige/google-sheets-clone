def trim(values):
    return [value.strip() for value in values]

def upper(values):
    return [value.upper() for value in values]

def lower(values):
    return [value.lower() for value in values]

def remove_duplicates(values):
    return list(set(values))

def find_and_replace(values, find_text, replace_text):
    return [value.replace(find_text, replace_text) for value in values]
