import os

def folder_creation(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"A pasta {path} foi criada com sucesso!")
    else:
        print(f"A pasta {path} já existe.")
