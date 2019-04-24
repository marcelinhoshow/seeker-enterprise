import re

def buscarTelefones(texto):
    listaExpressoes = ['[0-9]{3} (9[0-9]{4})([0-9]{4})', '[0-9]{3}(9[0-9]{4})([0-9]{4})', '[0-9]{3} (9[0-9]{4})\-([0-9]{4})', '[0-9]{2} (9[0-9]{4})\-([0-9]{4})', '[0-9]{2} (9[0-9]{4})([0-9]{4})', '\([0-9]{2}\) (9[0-9]{4})([0-9]{4})', '[0-9]{2}(9[0-9]{4})([0-9]{4})', '\([0-9]{2}\)(9[0-9]{4})([0-9]{4})', '[(][\d]{2}[)][]?[\d]{4}-[\d]{4}', '\([1-9]{2}\) (9[0-9]{4})\-([0-9]{4})', '\([1-9]{2}\)(9[0-9]{4})\-([0-9]{4})', '[0-9]{5} (9[0-9]{4})([0-9]{4})', '[0-9]{5} (9[0-9]{4})\-([0-9]{4})', '[0-9]{3} ([0-9]{4})\-([0-9]{4})', '[0-9]{3} ([0-9]{4})([0-9]{4})', '([0-9]{2})([0-9]{4})\-([0-9]{4})', '([0-9]{2})([0-9]{4})([0-9]{4})', '([0-9]{3})([0-9]{4})([0-9]{4})', '([0-9]{2}) ([0-9]{4})([0-9]{4})', '([0-9]{2}) ([0-9]{4})\-([0-9]{4})', '([0-9]{3})([0-9]{4})\-([0-9]{4})', '([0-9]{5})(9[0-9]{4})([0-9]{4})', '([0-9]{5})(9[0-9]{4})\-([0-9]{4})', '([0-9]{3}) ([0-9]{2}) (9[0-9]{4})([0-9]{4})', '([0-9]{3}) ([0-9]{2}) (9[0-9]{4})\-([0-9]{4})', '\([0-9]{2}\)([0-9]{4})([0-9]{4})', '\([0-9]{2}\) ([0-9]{4})([0-9]{4})', '\([0-9]{2}\) ([0-9]{4})\-([0-9]{4})', '\([0-9]{3}\) (9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\) (9[0-9]{4})([0-9]{4})', '\([0-9]{3}\)(9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\)(9[0-9]{4})([0-9]{4})', '\([0-9]{3}\)([0-9]{4})\-([0-9]{4})', '\([0-9]{3}\) ([0-9]{4})\-([0-9]{4})', '\([0-9]{3}\)([0-9]{4})([0-9]{4})', '\([0-9]{3}\) ([0-9]{4})([0-9]{4})', '\([0-9]{3}\)([0-9]{2})(9[0-9]{4})([0-9]{4})', '\([0-9]{3}\)([0-9]{2})(9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\)([0-9]{2}) (9[0-9]{4})([0-9]{4})', '\([0-9]{3}\) ([0-9]{2}) (9[0-9]{4})([0-9]{4})', '\([0-9]{3}\) ([0-9]{2}) (9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\)([0-9]{2}) (9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\) ([0-9]{2})(9[0-9]{4})\-([0-9]{4})', '\([0-9]{3}\) ([0-9]{2})(9[0-9]{4})([0-9]{4})', '([0-9]{4}) ([0-9]{3}) ([0-9]{4})', '([0-9]{4})\-([0-9]{3})\-([0-9]{4})', '(\+[0-9]{2})([0-9]{2})(9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2})([0-9]{2})(9[0-9]{4})([0-9]{4})', '(\+[0-9]{2}) ([0-9]{2})(9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2}) ([0-9]{2})(9[0-9]{4})([0-9]{4})', '(\+[0-9]{2}) ([0-9]{2}) (9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2}) ([0-9]{2}) (9[0-9]{4})([0-9]{4})', '(\+[0-9]{2})([0-9]{2}) (9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2})([0-9]{2}) (9[0-9]{4})([0-9]{4})', '(\+[0-9]{2}) \([0-9]{2}\) (9[0-9]{4})([0-9]{4})', '(\+[0-9]{2}) \([0-9]{2}\) (9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2}) \([0-9]{2}\)(9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2}) \([0-9]{2}\)(9[0-9]{4})([0-9]{4})', '(\+ [0-9]{2}) \([0-9]{2}\)(9[0-9]{4})\-([0-9]{4})', '(\+ [0-9]{2}) \([0-9]{2}\)(9[0-9]{4})([0-9]{4})', '(\+ [0-9]{2}) \([0-9]{2}\) (9[0-9]{4})([0-9]{4})', '(\+ [0-9]{2}) \([0-9]{2}\) (9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2})\([0-9]{2}\)(9[0-9]{4})([0-9]{4})', '(\+[0-9]{2})\([0-9]{2}\)(9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2})\([0-9]{2}\) (9[0-9]{4})\-([0-9]{4})', '(\+[0-9]{2})\([0-9]{2}\) (9[0-9]{4})([0-9]{4})', '(\+ [0-9]{2})\([0-9]{2}\) (9[0-9]{4})\-([0-9]{4})', '(\+ [0-9]{2})\([0-9]{2}\) (9[0-9]{4})([0-9]{4})', '(\+ [0-9]{2})\([0-9]{2}\)(9[0-9]{4})\-([0-9]{4})', '(\+ [0-9]{2})\([0-9]{2}\)(9[0-9]{4})([0-9]{4})']
        
    for expressao in listaExpressoes:
        phones = re.findall(expressao, texto)
        if len(phones) != 0:
            return phones[0]
        else:
            pass

string = '(13)3452-1900'
telefone = buscarTelefones(string)
print (telefone)