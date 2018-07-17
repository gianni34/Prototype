import _json
from django.http import JsonResponse, HttpResponse
from rest_framework import status, viewsets
from rest_framework.utils import json

from rest_framework.decorators import api_view, detail_route
from HomeAutomation.serializers import *
from HomeAutomation.models import *
from HomeAutomation.business import *


class ZonesViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ParametersViewSet(viewsets.ModelViewSet):
    queryset = Parameters.objects.all()
    serializer_class = ParametersSerializer


class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer


class StateVariableViewSet(viewsets.ModelViewSet):
    queryset = StateVariable.objects.all()
    serializer_class = StateVariableSerializer


@api_view(['PUT'])
def set_temperature(request):

    print("------- algo consume el servicio -----------")
    print(request.data)
    intermediary = request.data['intermediary']
    print(intermediary)
    value = request.data['value']
    print(value)

    try:
        i = Intermediary.objects.filter(name=intermediary).first()
        z = Zone.objects.filter(intermediary=i.id).first()
        z.set_temperature(value)
    except ValueError:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'ERROR': 'No se encontró la zona correspondiente.'})

    #return Response(status=status.HTTP_200_OK)
    return JsonResponse({'EXITO': 'Estado modificado con Exito'})


""""
@api_view(['PUT'])
def change_password(request):

    user = request.data['user']
    old_password = request.data['oPass']
    new_password = request.data['nPass']

    usu = User.objects.filter(name=user).first()
    ret = usu.change_password(old_password, new_password)

    if ret == 'OK':
        return JsonResponse({'EXITO': 'OK'})
    else:
        return JsonResponse({'ERROR': ret})
"""


@api_view(['PUT'])
def check_answer(request):

    user = request.data['user']
    answer = request.data['answer']

    u = User.objects.filter(name=user).first()
    if u.check_answer(answer):
        return HttpResponse('Respuesta correcta.', status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Respuesta incorrecta incorrectos.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def login(request):
    user = request.data['user']
    password = request.data['pass']

    obj = User.objects.filter(name=user).first()
<<<<<<< HEAD
    if obj and obj.password == password:
        response_data = {'result': True, 'message': 'Inició correctamente.', 'data': obj.id}
    return JsonResponse(response_data)
    #return HttpResponse(json.dumps(response_data), content_type="application/json")


@api_view(['POST'])
def new_user(request):
    user = request.data['user']
    admin = request.data['admin']
    if len(User.objects.filter(name=user["name"])) > 0:
        return JsonResponse({'result': False, 'message': 'El nombre de usuario ingresado ya existe.'})
    usu = User.objects.filter(id=admin).first()

    if User.is_admin(usu):
        new = User()
        new.name = user["name"]
        new.isAdmin = user["isAdmin"]
        new.password = user["password"]
        new.save()
        return JsonResponse({'result': True})
    else:
        return JsonResponse({'result': False, 'message': 'Debe ser administrador para dar de alta un usuario.'})
=======
    if obj.login(password):
        return HttpResponse('Inició correctamente.', status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Usuario y/o contraseña incorrectos.", status=status.HTTP_400_BAD_REQUEST)
>>>>>>> ecb13989d45dc8494718bb6b87880023406bad85


@api_view(['PUT'])
def user_question(request):
    user = request.data['user']
<<<<<<< HEAD
    response_data = {'result': False, 'question': ''}
    obj = User.objects.filter(name=user).first()
    if obj and obj.question:
        response_data = {'result': True, 'question': obj.question}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
=======
    obj = User.objects.filter(name=user).first();
    question = obj.get_question()
    return HttpResponse(question, content_type="application/json")
>>>>>>> ecb13989d45dc8494718bb6b87880023406bad85
