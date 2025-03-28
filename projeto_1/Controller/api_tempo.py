import requests

# Coloque sua chave de API aqui
API_KEY = '1cb57c905ec8cf04afd776c6c4eec3e6'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Função para obter clima
def obter_clima(cidade):
    # Construir URL com a cidade e chave de API
    url = f'{BASE_URL}?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
    
    # Fazer a requisição
    resposta = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()  # Converter a resposta em formato JSON
        
        # Extrair dados do clima
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        cidade_nome = dados['name']
        
        # Mostrar os dados
        print(f'Clima em {cidade_nome}:')
        print(f'Temperatura: {temperatura}°C')
        print(f'Condição: {descricao}')
        print(f'Umidade: {umidade}%')
    else:
        print('Cidade não encontrada ou erro na requisição')

# Exemplo de uso
cidade = input('Digite o nome da cidade: ')
obter_clima(cidade)