from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from museos.models import Museo
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
