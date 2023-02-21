import json

# salvar dados do jogo em um arquivo JSON
def save_game(data):
    with open('save.json', 'w') as f:
        json.dump(data, f)

# carregar dados do jogo a partir de um arquivo JSON
def load_game():
    try:
        with open('./save.json', 'r') as f:
            dados = json.load(f)
            if(dados == ''):
                save_game(getData(1, []))
        return dados
    except:
        print('Erro! o Json de save não foi encontrado!')
        exit()

def getData(lv, items):
    return {"lv": f"{lv}", "items": f"{items}"}

def getLevel(lv):
    lvConfig = json.load(open('./Model/levels.json'))
    return lvConfig[str(lv)]
