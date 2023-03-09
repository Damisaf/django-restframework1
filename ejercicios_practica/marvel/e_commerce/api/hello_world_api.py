# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view,  permission_classes

# NOTE: Ejemplo de hello world con método GET
@api_view(['GET'])
def hello_world(request):
    template = '<h1>Hola mundo clase 4 Django APIs!</h1>' 
    return HttpResponse(template)

# NOTE: Ejemplo de hello world con método POST
@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_data(request):
    '''
    Esta función nos permite realizar una petición de tipo GET,
    \n Retorna el valor del parámetro "mi_nombre" enviada en la petición.
    '''
    template = f'<h1>{request.GET.get("mi_nombre")}</h1>'
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)

@api_view(['GET', 'POST'])
@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_par_o_impar(request):
    '''
    Esta función nos permite realizar una petición de tipo GET,
    \n Retorna el valor del parámetro "numero" enviada en la petición.
    '''
    elnumero=int(request.GET.get("numero"))
    if elnumero % 2 == 0:
        template = f'<h1> PAR </h1>'
    else:
        template = f'<h1> IMPAR </h1>'
    # Tambien podemos llamar al método dentro de request, haciendo:
    # request.POST.get('alguna_key')
    print(template)
    return HttpResponse(template)
