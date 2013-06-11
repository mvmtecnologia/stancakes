
from google.appengine.ext import db

"""
@author: matheus cardoso
@author: soliva
 
Copyright (C) 2013 MVM Tecnologia, Inc.

""" 
class Contato(db.Model):
    '''
    classe responsavel em representar o
    contato feito pelo cliente
    '''
    nome = db.StringProperty()
    email = db.EmailProperty()
    mensagem = db.TextProperty()
    dataContato = db.DateProperty()

    def isValid(self):
        if self.nome and self.email and self.mensagem and self.dataContato:
            return True
        else: False