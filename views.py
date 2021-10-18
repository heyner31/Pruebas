# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types,Ingredientes,Recetas

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def index(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'index.html', {'title': "Bumblebee" })

def cotizador(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'cotizador.html', {'title': "Bumblebee" })  


    
    if request.method == 'POST':
        try: 
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["dog_name"]
                Dogs.objects.filter(id=dogid).update(name=json_object["dog_name"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["dog_type"]
                Dogs.objects.filter(id=dogid).update(type_id=json_object["dog_type"])
                contador = contador +1
            except KeyError:
                responseData={}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['data'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['data'] = 'Dog update'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)
        
# ///___________________________________________________________________________________________________________________///

def recetas(request):
    
    if request.method == 'GET':
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Recetas.objects.all().values())
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)

def RecetaAdd(request):
    
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
            b = Recetas(nombre_re=json_object['nombre_re'], procedimiento_re=json_object['procedimiento_re'],calorias_re=json_object['calorias_re'],img_re=json_object['img_re'])
            b.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Receta inserted'

            return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def RecetaDelete(request):
    
    if request.method == 'DELETE':
        try:
            json_object = json.loads(request.body)
            try: 
                one_entry = Recetas.objects.get(id_re=json_object["id"])
            except:
                responseData ={}
                responseData['success'] = 'false'
                responseData['message'] = 'The id_re its not valid'
                return JsonResponse(responseData, status=400)
            Recetas.objects.filter(id_re=json_object["id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Receta delete'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def RecetaDeleteID(request, idre):
    
    if request.method == 'DELETE':
        try:
            try: 
                one_entry = Recetas.objects.get(id_re=idre)
            except:
                responseData ={}
                responseData['success'] = 'false'
                responseData['message'] = 'The id_re its not valid'
                return JsonResponse(responseData, status=400)
            Recetas.objects.filter(id_re=idre).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Receta delete'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def recetaGetId(request, idre):
    
    if request.method == 'GET':
        try: 
            one_entry = Recetas.objects.get(id_re=idre)
        except:
            responseData ={}

            responseData['success'] = 'false'
            responseData['message'] = 'The id_re its not valid'
            return JsonResponse(responseData, status=400)
           
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['id'] = one_entry.id_re
        responseData['data']['nombre'] = one_entry.nombre_re
        responseData['data']['procedimiento'] = one_entry.procedimiento_re
        responseData['data']['calorias'] = one_entry.calorias_re
        responseData['data']['img'] = one_entry.img_re
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=400)

def RecetaUpdate(request, recetaid):
    
    if request.method == 'POST':
        try: 
            one_entry = Recetas.objects.get(id_re=recetaid)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The id_re its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["nombre_re"]
                Recetas.objects.filter(id_re=recetaid).update(nombre_re=json_object["nombre_re"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["procedimiento_re"]
                Recetas.objects.filter(id_re=recetaid).update(procedimiento_re=json_object["procedimiento_re"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["calorias_re"]
                Recetas.objects.filter(id_re=recetaid).update(calorias_re=json_object["calorias_re"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["img_re"]
                Recetas.objects.filter(id_re=recetaid).update(img_re=json_object["img_re"])
                contador = contador +1
            except KeyError:
                responseData={}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['data'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['data'] = 'Receta update'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

# ///___________________________________________________________________________________________________________________///

def ingredientes(request):
    
    if request.method == 'GET':
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Ingredientes.objects.all().values())
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)

def ingredientesAdd(request):
    
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
            b = Ingredientes(nombre_in=json_object['nombre_in'],img_in=json_object['img_in'],tipo=json_object['tipo'])
            b.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Ingrediente inserted'

            return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def ingredientesDelete(request):
    
    if request.method == 'DELETE':
        try:
            json_object = json.loads(request.body)
            try: 
                one_entry = Ingredientes.objects.get(id_in=json_object["id"])
            except:
                responseData ={}
                responseData['success'] = 'false'
                responseData['message'] = 'The id_in its not valid'
                return JsonResponse(responseData, status=400)
            Ingredientes.objects.filter(id_in=json_object["id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Ingrediente delete'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def ingredientesDeleteID(request, idIn):
    
    if request.method == 'DELETE':
        try:
            try: 
                one_entry = Ingredientes.objects.get(id_in=idIn)
            except:
                responseData ={}
                responseData['success'] = 'false'
                responseData['message'] = 'The id_in its not valid'
                return JsonResponse(responseData, status=400)
            Ingredientes.objects.filter(id_in=idIn).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Ingrediente delete'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData ={}
            responseData['success'] = 'false'
            responseData['mesage'] = 'Invalid Json'
            return JsonResponse(responseData, status=404)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def ingredientesGetId(request, idin):
    
    if request.method == 'GET':
        try: 
            one_entry = Ingredientes.objects.get(id_in=idin)
        except:
            responseData ={}

            responseData['success'] = 'false'
            responseData['message'] = 'The id_in its not valid'
            return JsonResponse(responseData, status=400)
           
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['id'] = one_entry.id_in
        responseData['data']['nombre'] = one_entry.nombre_in
        responseData['data']['tipo'] = one_entry.tipo
        responseData['data']['img'] = one_entry.img_in
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=400)

def ingredientesUpdate(request, in_id):
    
    if request.method == 'POST':
        try: 
            one_entry = Ingredientes.objects.get(id_in=in_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The id_in its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["nombre_in"]
                Ingredientes.objects.filter(id_in=in_id).update(nombre_in=json_object["nombre_in"])
                contador = contador +1
            except KeyError:
                responseData={}
            
            try:
                value = json_object["tipo"]
                Ingredientes.objects.filter(id_in=in_id).update(tipo=json_object["tipo"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["img_in"]
                Ingredientes.objects.filter(id_in=in_id).update(img_in=json_object["img_in"])
                contador = contador +1
            except KeyError:
                responseData={}


            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['data'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['data'] = 'Ingredientes update'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)


