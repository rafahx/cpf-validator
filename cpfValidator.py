def main():

    lista_cpf = ['123.456.850-10', '035.321.190-89', '04291233027', '642.124080/15', '642.951.080-10']

    for cpf in lista_cpf:
        if validateCpf(cpf):
            print('CPF: %s\t é válido' %(cpf))
        else:
            print('CPF: %s\t é inválido' %(cpf))

def validateCpf(cpf):
    cpf = cpfToNumber(cpf)

    if len(cpf) != 11:
        return False

    if not isFirstDigitValidatorValid(cpf):
        return False

    if not isSecondDigitValidatorValid(cpf):
        return False

    return True
    
# Retorna apenas os números do cpf
def cpfToNumber(cpf):
    cpfNumerico = ""
    for nro in cpf:
        if nro.isnumeric():
            cpfNumerico = cpfNumerico + nro
    return cpfNumerico

# Retorna se primeiro dígito verificador é válido
def isFirstDigitValidatorValid(cpf):
    i = 10
    soma = 0
    for digito in range(9):
        soma = (int(cpf[digito]) * i) + soma
        i = i - 1
    digito_verificador = 11 - (soma % 11)
    if digito_verificador >= 10:
        digito_verificador = 0

    if digito_verificador != int(cpf[9]):
        return False
    return True

# Retorna se segundo dígito verificador é válido
def isSecondDigitValidatorValid(cpf):
    i = 11
    soma = 0
    for digito in range(10):
        soma = (int(cpf[digito]) * i) + soma
        i = i - 1
    digito_verificador = 11 - (soma % 11)
    if digito_verificador >= 10:
        digito_verificador = 0

    if digito_verificador != int(cpf[10]):
        return False
    return True

main()