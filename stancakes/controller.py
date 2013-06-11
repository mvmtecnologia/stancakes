from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Contato
from webapp2 import RequestHandler
import datetime



class HomeHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de home do sistema.
    '''

    def get(self):
        self.response.out.write(template.render('pages/home.html', {}))



class ServicoHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de servico do sistema.
    '''

    def get(self):
        self.response.out.write(template.render('pages/servico.html', {}))



class PortifolioHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de Portifolio do sistema.
    '''

    def get(self):
        self.response.out.write(template.render('pages/portifolio.html', {}))



class AdministradorHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de Administrador do sistema.
    '''

    def get(self):
        self.response.out.write(template.render('pages/entrada-admin.html', {}))

    def post(self):
        self.response.out.write(template.render('pages/painel-aplicacao.html', {}))
        
        


class ContatoHandler(RequestHandler):
    '''
    Classe que representa o formulario de contato do sitema.
    '''
    
    def get(self):
        self.response.out.write(template.render('pages/contato.html', {}))

    def post(self):
        if self.request.get('email'):
            self.email = self.request.get('email');
                
        contato = Contato(nome=self.request.get('name'),
                              email=self.email,
                              mensagem=self.request.get('comment'),
                              dataContato=datetime.datetime.now().date())
        if contato.isValid():
            contato.put() 
        return  self.redirect('/')
    

application = webapp.WSGIApplication([('/', HomeHandler),
                                      ('/servico', ServicoHandler),
                                      ('/portifolio', PortifolioHandler),
                                      ('/contato', ContatoHandler),
                                      ('/stancakesadmin', AdministradorHandler),
                                       ('/login', AdministradorHandler)], 
                                     debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
