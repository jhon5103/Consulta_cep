import requests

def requisitar(c):
    url = requests.get(f'https://viacep.com.br/ws/{c}/json')
    url_formatado = url.json()
    return url_formatado


while True:
    try:
        cep = str(input('digite seu cep: '))
        cep.replace('-', '')
        break
    except ValueError:
        print('ERRO! Digite seu cep novamente.')

requisicao = requisitar(cep)

logradouro = requisicao['logradouro']
bairro = requisicao['bairro']
cidade  = requisicao['localidade']
UF = requisicao['uf']

print('-'*30)
print('   RESULTADO    ')
print('-'*30)
print(f'Endereço: {logradouro}')
print(f'Bairro: {bairro}')
print(f'Cidade: {cidade}')
print(f'Unidade Federativa: {UF}')
print('-'*30)


  