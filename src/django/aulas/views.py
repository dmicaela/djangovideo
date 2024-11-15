#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def bye(request):
    return HttpResponse("Hasta luegooo!")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento

    mensaje = "En el año %d cumpliras %s años"%(futuro, cumplira)

    return HttpResponse(mensaje)

def primer_plantilla(request):
    plantilla = """
    <html>
        <body>
            <h2>
                Hola! {{nombre}} esta es mi primer plantilla
            </h2>
        </body>
    </html>
    """
    tpl = Template(plantilla)

    ctx = Context({
        'nombre': 'Juan Perez'
    })

    mensaje = tpl.render(ctx)

    return HttpResponse(mensaje)

def segunda_plantilla(request):
    tpl = get_template("segunda_plantilla.html")

    mensaje = tpl.render({
        'nombre': 'Mica',
        'fecha_actual': date.today()
    })

    return HttpResponse(mensaje)

def tercer_plantilla(request):

    return render(request, "tercer_plantilla.html", {
        'nombre': 'Cristina Fernandez de Kirchner',
        'fecha_actual': date.today()
    })