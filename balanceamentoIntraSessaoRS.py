import pandas as pd
import mysql.connector
import cx_Oracle
from datetime import datetime
from datetime import timedelta
import locale
import psycopg2

import sys

sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG


# Conecta ao Oracle
def conecta_oracle(sql):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email(mensagemEmail, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa

def sql_secao_completa(secao):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_balanceamento():
    pass # Logica de negocio removida por seguranca corporativa

def gera_sugestoes_email():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
  gera_sugestoes_email()