from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from museos.models import Museo, Configuracion
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from bs4 import BeautifulSoup
import urllib

# Create your views here.
@csrf_exempt
def pag_principal(request):
    plantilla = get_template("Kinda_Cloudy/index.html")
    todos_museos = Museo.objects.all()
    num_museos = len(todos_museos)
    if(num_museos==0):
        if request.method == "GET":
            form_boton = "<form method = 'POST'><button type='submit' "
            form_boton += "name='Cargar' value=1>Cargar"
            form_boton += "</button>"
        elif request.method == "POST":
            url_museos = "https://datos.madrid.es/portal/site/egob/"
            url_museos += "menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/"
            url_museos += "?vgnextoid=00149033f2201410VgnVCM100000171f"
            url_museos += "5a0aRCRD&format=xml&file=0&filename=201132-0"
            url_museos += "-museos&mgmtid=118f2fdbecc63410VgnVCM1000000"
            url_museos += "b205a0aRCRD&preview=full"
            url = urllib.request.urlopen(url_museos)
            soup = BeautifulSoup(url, "html.parser")
            datos_museo = soup.findAll('contenido')
            for elemento in datos_museo:
                atributos_museo = elemento.findAll('atributo')
                nuevo_museo = Museo()
                for atributo in atributos_museo:
                    if atributo.attrs["nombre"] == "ID-ENTIDAD":
                        nuevo_museo.id_entidad = atributo.text
                    elif atributo.attrs["nombre"] == "NOMBRE":
                        nuevo_museo.nombre = atributo.text
                    elif atributo.attrs["nombre"] == "DESCRIPCION_ENTIDAD":
                        nuevo_museo.descripcion_entidad = atributo.text
                    elif atributo.attrs["nombre"] == "HORARIO":
                        nuevo_museo.horario = atributo.text
                    elif atributo.attrs["nombre"] == "EQUIPAMIENTO":
                        nuevo_museo.equipamiento = atributo.text
                    elif atributo.attrs["nombre"] == "TRANSPORTE":
                        nuevo_museo.transporte = atributo.text
                    elif atributo.attrs["nombre"] == "DESCRIPCION":
                        nuevo_museo.descripcion = atributo.text
                    elif atributo.attrs["nombre"] == "ACCESIBILIDAD":
                        nuevo_museo.accesibilidad = atributo.text
                    elif atributo.attrs["nombre"] == "CONTENT-URL":
                        nuevo_museo.content_url = atributo.text
                    elif atributo.attrs["nombre"] == "NOMBRE-VIA":
                        nuevo_museo.nombre_via = atributo.text
                    elif atributo.attrs["nombre"] == "CLASE-VIAL":
                        nuevo_museo.clase_vial = atributo.text
                    elif atributo.attrs["nombre"] == "TIPO-NUM":
                        nuevo_museo.tipo_num = atributo.text
                    elif atributo.attrs["nombre"] == "NUM":
                        nuevo_museo.num = atributo.text
                    elif atributo.attrs["nombre"] == "PLANTA":
                        nuevo_museo.planta = atributo.text
                    elif atributo.attrs["nombre"] == "ORIENTACION":
                        nuevo_museo.orientacion = atributo.text
                    elif atributo.attrs["nombre"] == "LOCALIDAD":
                        nuevo_museo.localidad = atributo.text
                    elif atributo.attrs["nombre"] == "PROVINCIA":
                        nuevo_museo.provincia = atributo.text
                    elif atributo.attrs["nombre"] == "CODIGO-POSTAL":
                        nuevo_museo.codigo_postal = atributo.text
                    elif atributo.attrs["nombre"] == "BARRIO":
                        nuevo_museo.barrio = atributo.text
                    elif atributo.attrs["nombre"] == "DISTRITO":
                        nuevo_museo.distrito = atributo.text
                    elif atributo.attrs["nombre"] == "COORDENADA-X":
                        nuevo_museo.coordenada_x = atributo.text
                    elif atributo.attrs["nombre"] == "COORDENADA-Y":
                        nuevo_museo.coordenada_y = atributo.text
                    elif atributo.attrs["nombre"] == "LATITUD":
                        nuevo_museo.latitud = atributo.text
                    elif atributo.attrs["nombre"] == "LONGITUD":
                        nuevo_museo.longitud = atributo.text
                    elif atributo.attrs["nombre"] == "TELEFONO":
                        nuevo_museo.telefono = atributo.text
                    elif atributo.attrs["nombre"] == "FAX":
                        nuevo_museo.fax = atributo.text
                    elif atributo.attrs["nombre"] == "EMAIL":
                        nuevo_museo.email = atributo.text
                    else:
                        pass
                    nuevo_museo.save()
            return HttpResponseRedirect('/')
        saludo = "Presione el botón si desea cargar los datos:"
        c = Context({'boton': form_boton, 'saludo': saludo})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    else:
        respuesta = "Hola"
        return HttpResponse(respuesta)

@csrf_exempt
def pag_museos(request):
    plantilla = get_template("Kinda_Cloudy/pag_museos.html")
    todos_museos = Museo.objects.all()
    lista_distritos = todos_museos.order_by().values_list('distrito', flat=True).distinct()
    menu_desplegable = "<form method='POST'>"
    menu_desplegable += "Filtrar por distrito:<br/>"
    menu_desplegable += "<select name='Distrito'>"
    menu_desplegable += "<option value='TODOS'>TODOS</option>"
    for distrito in lista_distritos:
        menu_desplegable += "<option value='" + distrito + "'>"
        menu_desplegable += distrito + "</option>"
    menu_desplegable += "</select>"
    menu_desplegable += "<input type='submit' value='Enviar'>"
    menu_desplegable += "</form>"
    if request.method == "GET":
        museos = "<ul>"
        for museo in todos_museos:
            museos += "<li>"
            museos += "<b><a href='/museos/" + museo.id_entidad + "'>" + museo.nombre
            museos += "</a></b>"
            museos += "</li>"
        museos += "</ul>"
        funcionamiento = "Pulse sobre el nombre del museo"
        funcionamiento += " para ir a su página"
        c = Context({'menu': menu_desplegable, 'funcionamiento': funcionamiento, 'museos': museos})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    elif request.method == "POST":
        distrito = request.body.decode('utf-8').split("=")[1].replace("+"," ")
        if distrito == "TODOS":
            museos = "<ul>"
            for museo in todos_museos:
                museos += "<li>"
                museos += "<b><a href="">" + museo.nombre
                museos += "</a></b>"
                museos += "</li>"
            museos += "</ul>"
            funcionamiento = "Pulse sobre el nombre del museo"
            funcionamiento += " para ir a su página"
            c = Context({'menu': menu_desplegable, 'funcionamiento': funcionamiento, 'museos': museos})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
        else:
            museos_filtrados = Museo.objects.all().filter(distrito=distrito)
            museos = "<ul>"
            for museo in museos_filtrados:
                museos += "<li>"
                museos += "<b><a href="">" + museo.nombre
                museos += "</a></b>"
                museos += "</li>"
            museos += "</ul>"
            informacion = "Estás viendo los museos de " + distrito
            funcionamiento = "Pulse sobre el nombre del museo"
            funcionamiento += " para ir a su página"
            c = Context({'menu': menu_desplegable, 'funcionamiento': funcionamiento, 'museos': museos, 'informacion': informacion})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
    else:
        return HttpResponse("Hola")

@csrf_exempt
def pag_museo(request, resource):
    plantilla = get_template("Kinda_Cloudy/pag_museo.html")
    todos_museos = Museo.objects.all()
    if request.method == "GET":
        museo = todos_museos.get(id_entidad=resource)
        datos_museo = "<b><h2>" + museo.nombre + "</h2></b>"
        datos_museo += "<b>DESCRIPCION:</b><br>"
        datos_museo += museo.descripcion + "<br>"
        datos_museo += "<b>ACCESIBILIDAD:</b> "
        if museo.accesibilidad == 1:
            datos_museo += "Sí<br>"
        else:
            datos_museo += "No<br>"
        datos_museo += "<b>DIRECCION</b>:<br>"
        datos_museo += museo.clase_vial + " " + museo.nombre_via + " "
        datos_museo += museo.tipo_num + " " + museo.num + "<br>"
        datos_museo += museo.localidad + ", " + museo.provincia
        datos_museo += "<br>" + museo.codigo_postal
        datos_museo += "<br>" + museo.barrio + " " + museo.distrito
        datos_museo += "<br>" + museo.coordenada_x + ", "
        datos_museo += museo.coordenada_y
        datos_museo += "<br>" + museo.latitud + ", " + museo.longitud
    elif request.method == "POST":
        return HttpResponse("Hola")
    else:
        return HttpResponse("Hola")
    c = Context({'datos_museo': datos_museo})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)

@csrf_exempt
def pag_user(request, resource):
    plantilla = get_template("Kinda_Cloudy/pag_usuario.html")
    if request.method == 'GET':
        try:
            usuario = User.objects.get(username=resource)
            saludo = "Esta es la pagina del usuario"
            c = Context({'saludo': saludo})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
        except User.DoesNotExist:
            plantilla = get_template("Kinda_Cloudy/error.html")
            c = Context({'error': "El usuario no existe"})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
        pag_user = Configuracion.objects.get(usuario=usuario)
    else:
        return HttpResponse("Hola")

def about(request):
    plantilla = get_template("Kinda_Cloudy/about.html")
    c = Context();
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)
