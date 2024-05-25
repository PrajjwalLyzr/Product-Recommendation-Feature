def save_api_key(key):
    with open("api_key.txt", "w") as file:
        file.write(key)