import ply.lex as lex
import os
import sys
import re
import codecs

tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
          'ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT',
          'RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']

reservadas={
    'begin':'BEGIN',
    'end':'END',
    'if':'IF',
    'then':'THEN',
    'while':'WHILE',
    'do':'DO',
    'call':'CALL',
    'const':'CONST',
    'int':'INT',
    'procedure':'PROCEDURE',
    'out':'OUT',
    'in':'IN',
    'else':'ELSE'
}

tokens = tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t
def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
    print ("caracter ilegal'%s'" % t.value[0])
    t.lexer.skip(1)

def cuentalinea(fileName):
    cont=0
    archivo=open(fileName,"r")
    linea=archivo.readline()
    while linea != '':
        linea=archivo.readline()
        cont=cont+1
    return cont


fileName='prueba.mj'
fp=codecs.open(fileName, 'r')
file_text = fp.read()
analizador = lex.lex()
analizador.input(file_text)
while True:
    tok = analizador.token()
    if not tok:
        break
    else:
        print(tok)
fp.close()

acum=cuentalinea(fileName)
print(acum)




