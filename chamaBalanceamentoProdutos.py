from datetime import datetime
from rebalanceamentoProdutos import CalculaRebalanceamento
from rebalanceamentoProdutosItens import ChamaCodigos
from balanceamentoIntraSessao import gera_sugestoes_email


# # Verifica se hoje é terça-feira (segunda = 0, terça = 1, ..., domingo = 6)
# if datetime.now().weekday() == 1:
#     print("Hoje é terça-feira. Executando o rebalanceamento...")
#     CalculaRebalanceamento()
#     ChamaCodigos()
#     gera_sugestoes_email()
# else:
#     print("Hoje não é terça-feira. Nenhuma ação será executada.")


# Verifica se hoje é terça-feira
hoje = datetime.now()
dia_da_semana = hoje.weekday()  # segunda = 0, terça = 1, ..., domingo = 6
semana_do_ano = hoje.isocalendar()[1]  # número da semana no ano

# Executa apenas em terças-feiras de semanas pares
if dia_da_semana == 1 and semana_do_ano % 2 == 0:
    print("Hoje é terça-feira de uma semana par. Executando o rebalanceamento...")
    CalculaRebalanceamento()
    ChamaCodigos()
    gera_sugestoes_email()
else:
    print("Hoje não é terça-feira de uma semana par. Nenhuma ação será executada.")