"""Primera clase de Django, permitirá responder a una petición de un cliente."""
from django.http import HttpResponse 
from django.shortcuts import render #Nos permite responder a la petición del cliente
"""Definimos una función"""
#def index(request): #De forma obligatoria deben de tener un parametro request
   # return HttpResponse('Hola desde el archivo views.py!') #Se responde al cliente con HttpResponse
def index(request):
    return render(request,'index.html',{
        'message':"Listado de productos",
        'title':"Productos",
        'products':[
            {'title':'Playera','price':5,'stock':True},
            {'title':'Camisa','price':7,'stock':True},
            {'title':'Mochila','price':20,'stock':False},
            {'title':'Laptop','price':500,'stock':False} #La lista almacenará diccionarios, los cuales almacenarán un producto
        ] 
        #DIccionario hace referencia a contexto
    })