from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

#View poara criação de tags

class TagCreatorView:
    '''
     responsability for interacting with HTTP
     metodos em class precisam ter o self
    '''

    def validate_and_create(self, http_request:HttpRequest) -> HttpResponse:
        #self para falar que está no contexto da class TagCreatorView
        #body = http_request.body
        #product_code = body["product_code"]

        print(http_request)
        #logica de regra de negocio

        #retorno http
        return HttpResponse(status_code=200, body={"hello":"world"})
