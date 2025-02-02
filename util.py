def load_message(name):
    with open("texts/" + name + ".txt", 'r',encoding='utf-8') as file:
        return file.read()