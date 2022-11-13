
    
agenda=[]
dados = {}

resp='SIM'
while resp =='SIM':
    dados['nome'] = input('NOME DO CONTATO =')
    dados['tel'] = input('TELEFONE DO CONTATO =')
    agenda.append(dados.copy())
    resp = input('DESEJA INSERIR MAIS CONTATOS SIM/NAO')
    resp = resp.upper()
    
print(agenda)

for k,v in agenda.items():
    print(k,'=',v)


