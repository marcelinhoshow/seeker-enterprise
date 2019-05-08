import pymongo

conexao = pymongo.MongoClient('mongodb+srv://botpython:bc123456!@storm-project-eu6jj.mongodb.net/SeekerEnterprise')
mydb = conexao['SeekerEnterprise']

def inserirDados(nomeEmpresa,telefoneEmpresa):
    buscaMongo = mydb.dadosEmpresas.find_one({
        'nomeEmpresa' : nomeEmpresa
    })

    if buscaMongo == None:
        mydb.dadosEmpresas.insert({
            'nomeEmpresa' : nomeEmpresa,
            'telefoneEmpresa' : telefoneEmpresa
        })
        print ('Inserido')
    else:
        print ('Existente')
        print (buscaMongo)

inserirDados('Jacto','1234')