from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {'cargo1':"Auxiliares",'cargo2':"Profesores", 'cargo3':"Ayudantes"}
    return render(request, 'app_de_IN3501/index.html', contexto)


def welcome(request):
    return render(request, 'app_de_IN3501/bienvenida.html')


def tarea(request):
    return render(request, 'app_de_IN3501/tarea.html')

def inputs(request):
	return render(request, 'app_de_IN3501/inputs.html')

def formulario_dudas(request):
    return render(request, 'app_de_IN3501/formulario_dudas.html')

def confirmacion_dudas(request):
    dato_nombre = request.POST['nombre_name']
    return render(request, 'app_de_IN3501/confirmacion_dudas.html')