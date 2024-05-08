class Tabela_Verdade:
# Função para referenciar os parâmetros à função principal;
    def __init__(self, variaveis, operaçoes):
        self.variaveis = variaveis
        self.operacoes = operaçoes


# Funções para retorno das operações lógicas;
    def and_logico(self, a, b):
        return a and b


    def or_logico(self, a, b):
        return a or b


    def not_logico(self, a):
        return not a


# Função para gerar a tabela verdade;
    def gerador_tabela(self):
        cabeçalho = self.variaveis.copy()
        cabeçalho.append(self.operacoes)
        print('\t'.join(cabeçalho))


        # Condições que analisam as operações lógicas;
        if self.operacoes in ['AND', 'OR']:
            for a in [0, 1]:
                for b in [0, 1]:
                    result = self.and_logico(a, b) if self.operacoes == 'AND' else self.or_logico(a, b)
                    print(f"{a}\t{b}\t{result}")
        elif self.operacoes == 'NOT':
            for a in [0, 1]:
                result = self.not_logico(a)
                print(f"{a}\t{result}")