from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

#View poara criação de tags

class TagCreatorView:
    '''
     responsability for interacting with HTTP
     metodos em class precisam ter o self
    '''

    def validate_and_create(self, http_request:HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        #self para falar que está no contexto da class TagCreatorView
        body = http_request.body
        product_code = body["product_code"]

        #logica de regra de negocio
        formatted_response=tag_creator_controller.create(product_code)

        #retorno http
        return HttpResponse(status_code=200, body=formatted_response)
