from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from museos.models import Museo, Configuracion, Comentarios, Seleccion
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import RequestContext
from bs4 import BeautifulSoup
import urllib
import datetime
from django.contrib.auth import authenticate, login, logout

accesibilidad = False

# Create your views here.
@csrf_exempt
def pag_principal(request):
    global accesibilidad
    plantilla = get_template("Kinda_Cloudy/index.html")
    tamano = "13px"
    color_fondo = "#D3D3D3"
    try:
        usuario = User.objects.get(username=request.user)
        color_user = Configuracion.objects.get(usuario=usuario).color_fondo
        letra_user = Configuracion.objects.get(usuario=usuario).letra_size
        if(usuario.is_authenticated and not color_user == "Null"):
            color_fondo = color_user
            tamano = letra_user
    except (User.DoesNotExist, Configuracion.DoesNotExist):
        color_fondo = "#D3D3D3"
        tamano = "13px"
    todos_museos = Museo.objects.all()
    lista_usuarios = User.objects.all()
    pag_personales = ""
    pag_personales = "<ul>"
    for usuario in lista_usuarios:
        try:
            pag_usuario = Configuracion.objects.get(usuario=usuario)
            titulo = pag_usuario.titulo
            pag_personales += "<li>" + usuario.username
            pag_personales += " <a href='/" + usuario.username + "'>"
            pag_personales += titulo + "</a><br>"
        except Configuracion.DoesNotExist:
            pag_personales += "<a href='/" + usuario.username + "'>Pagina de "
            pag_personales += usuario.username + "</a><br>"
    num_museos = len(todos_museos)
    if(num_museos==0):
        if request.method == "GET":
            name = 'Cargar'
            value = "Cargar"
            form_boton = "Cargar"
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
        c = RequestContext(request, {'form_boton': form_boton,
                        'name': name,
                        'value':value,
                        'saludo': saludo,
                        'paginas_personales': pag_personales,
                        'color': color_fondo,
                        'tamano': tamano})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    else:
        value = "Accesibilidad"
        name = "Accesibilidad"
        if request.method == 'GET':
            listaMasComentados = Museo.objects.all().order_by('-num_coment')
            listaMasComentados = listaMasComentados.exclude(num_coment=0)
            if accesibilidad:
                listaMasComentados = listaMasComentados.filter(accesibilidad=1)
                boton = "Mostrar todos"
            else:
                boton = "Mostrar accesibles"
            listaMasComentados = listaMasComentados[:5]
        elif request.method == 'POST':
            value = request.body.decode('utf-8').split("=")[1]
            if value == "Accesibilidad":
                accesibilidad = not accesibilidad
            listaMasComentados = Museo.objects.all().order_by('-num_coment')
            listaMasComentados = listaMasComentados.exclude(num_coment=0)
            if accesibilidad:
                listaMasComentados = listaMasComentados.filter(accesibilidad=1)
                boton = "Mostrar todos"
            else:
                boton = "Mostrar accesibles"
            listaMasComentados = listaMasComentados[:5]
        else:
            plantilla = get_template("Kinda_Cloudy/error.html")
            error = "Método no permitido"
            c = RequestContext(request, {'error': error})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
        c = RequestContext(request, {'listaMasComentados':listaMasComentados,
                            'form_boton': boton,
                            'name': name,
                            'value':value,
                            'paginas_personales': pag_personales,
                            'color': color_fondo,
                            'tamano': tamano})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)


@csrf_exempt
def pag_museos(request):
    global accesibilidad
    plantilla = get_template("Kinda_Cloudy/pag_museos.html")
    tamano = "13px"
    color_fondo = "#D3D3D3"
    try:
        usuario = User.objects.get(username=request.user)
        color_user = Configuracion.objects.get(usuario=usuario).color_fondo
        letra_user = Configuracion.objects.get(usuario=usuario).letra_size
        if(usuario.is_authenticated and not color_user == "Null"):
            color_fondo = color_user
            tamano = letra_user
    except (User.DoesNotExist, Configuracion.DoesNotExist):
        color_fondo = "#D3D3D3"
        tamano = "13px"
    todos_museos = Museo.objects.all()
    if accesibilidad:
        todos_museos = todos_museos.filter(accesibilidad=1)
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
        c = RequestContext(request, {'menu': menu_desplegable,
                        'museos': todos_museos,
                        'color': color_fondo,
                        'tamano': tamano})
    elif request.method == "POST":
        distrito = request.body.decode('utf-8').split("=")[1].replace("+"," ")
        if distrito == "TODOS":
            c = RequestContext(request, {'menu': menu_desplegable,
                                        'museos': todos_museos,
                                        'color': color_fondo,
                                        'tamano': tamano})
        else:
            museos_filtrados = Museo.objects.all().filter(distrito=distrito)
            informacion = "Estás viendo los museos de " + distrito
            c = RequestContext(request, {'menu': menu_desplegable,
                                        'museos': museos_filtrados,
                                        'informacion': informacion,
                                        'color': color_fondo,
                                        'tamano': tamano})
    else:
        plantilla = get_template("Kinda_Cloudy/error.html")
        error = "Método no permitido"
        c = RequestContext(request, {'error': error})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)

@csrf_exempt
def pag_museo(request, resource):
    plantilla = get_template("Kinda_Cloudy/pag_museo.html")
    tamano = "13px"
    color_fondo = "#D3D3D3"
    try:
        usuario = User.objects.get(username=request.user)
        color_user = Configuracion.objects.get(usuario=usuario).color_fondo
        letra_user = Configuracion.objects.get(usuario=usuario).letra_size
        if(usuario.is_authenticated and not color_user == "Null"):
            color_fondo = color_user
            tamano = letra_user
    except (User.DoesNotExist, Configuracion.DoesNotExist):
        color_fondo = "#D3D3D3"
        tamano = "13px"
    todos_museos = Museo.objects.all()
    museo = todos_museos.get(id_entidad=resource)
    datos_museo = "<b><h2>" + museo.nombre + "</h2></b>"
    datos_museo += "<b>DESCRIPCION:</b><br>"
    datos_museo += museo.descripcion + "<br>"
    datos_museo += "<b>ACCESIBILIDAD:</b> "
    if museo.accesibilidad == 1:
        datos_museo += "Sí<br>"
    else:
        datos_museo += "No<br>"
    datos_museo += "<b>HORARIO</b>:<br>"
    datos_museo += museo.horario
    datos_museo += "<b><br>DIRECCION</b>:<br>"
    datos_museo += museo.clase_vial + " " + museo.nombre_via + " "
    datos_museo += museo.tipo_num + " " + museo.num + "<br>"
    datos_museo += museo.localidad + ", " + museo.provincia
    datos_museo += "<br>" + museo.codigo_postal
    datos_museo += "<br>" + museo.barrio + " " + museo.distrito
    datos_museo += "<br>" + museo.coordenada_x + ", "
    datos_museo += museo.coordenada_y
    datos_museo += "<br>" + museo.latitud + ", " + museo.longitud
    datos_museo += "<br><b>DATOS DE CONTACTO</b>:<br>"
    datos_museo += museo.telefono + ", fax:" +  museo.fax + " "
    datos_museo += "<br>email:" + museo.email
    boton_add = "<form method = 'POST'><button type='submit' "
    boton_add += "name='Add' value=1>Add"
    boton_add += "</button>"
    if request.method == "GET":
        comentarios = Comentarios.objects.all().filter(museo=museo)
    elif request.method == "POST":
        value = request.body.decode('utf-8').split("=")[0]
        if value == "Add":
            museo = Museo.objects.get(id_entidad=resource)
            usuario = User.objects.get(username=request.user)
            fecha = datetime.date.today()
            museo_seleccionado = Seleccion(museo=museo, usuario=usuario, fecha=fecha)
            museo_seleccionado.save()
            comentarios = Comentarios.objects.all().filter(museo=museo)
        elif value == "Comentario":
            museo = Museo.objects.get(id_entidad=resource)
            comentario = request.body.decode('utf-8').split("=")[1].replace("+", " ")
            nuevo_comentario = Comentarios(comentario=comentario, museo=museo)
            nuevo_comentario.save()
            museo.num_coment = museo.num_coment + 1
            museo.save()
            comentarios = Comentarios.objects.all().filter(museo=museo)
    else:
        plantilla = get_template("Kinda_Cloudy/error.html")
        error = "Método no permitido"
        c = RequestContext(request, {'error': error})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    c = RequestContext(request, {'datos_museo': datos_museo,
                                'boton': boton_add,
                                'comentarios': comentarios,
                                'color': color_fondo,
                                'tamano': tamano})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)

@csrf_exempt
def pag_user(request, resource):
    plantilla = get_template("Kinda_Cloudy/pag_usuario.html")
    tamano = "13px"
    color_fondo = "#D3D3D3"
    try:
        usuario = User.objects.get(username=request.user)
        color_user = Configuracion.objects.get(usuario=usuario).color_fondo
        letra_user = Configuracion.objects.get(usuario=usuario).letra_size
        if(usuario.is_authenticated and not color_user == "Null"):
            color_fondo = color_user
            tamano = letra_user
    except (User.DoesNotExist, Configuracion.DoesNotExist):
        color_fondo = "#D3D3D3"
        tamano = "13px"
    usuario = User.objects.get(username=resource)
    museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
    boton_mas = ""
    if(len(museos_seleccionados) <= 5):
        museos_seleccionados = museos_seleccionados[:5]
    else:
        museos_seleccionados = museos_seleccionados[:5]
        boton_mas = "<form method = 'POST'><button type='submit' "
        boton_mas += "name='Mas' value=0>Más"
        boton_mas += "</button>"
        boton_mas += "</form>"
    if request.method == 'GET':
        try:
            usuario = User.objects.get(username=resource)
            pag_user = Configuracion.objects.get(usuario=usuario)
            museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
            museos_seleccionados = museos_seleccionados[:5]
        except User.DoesNotExist:
            plantilla = get_template("Kinda_Cloudy/error.html")
            error = "El usuario no existe"
            c = RequestContext(request, {'error': error})
            respuesta = plantilla.render(c)
            return HttpResponse(respuesta)
        except Configuracion.DoesNotExist:
            pag_user = Configuracion(usuario=usuario)
            pag_user.titulo = "Pagina de " + resource
            pag_user.save()
            return HttpResponseRedirect('/' + resource)
    elif request.method == 'POST':
        name = request.body.decode('utf-8').split("=")[0]
        usuario = User.objects.get(username=resource)
        pag_user = Configuracion.objects.get(usuario=usuario)
        museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
        museos_seleccionados = museos_seleccionados[:5]
        if name == 'Title':
            title = request.body.decode('utf-8').split("=")[1].replace("+", " ")
            if title == "": #Si se envia el formulario vacío
                pag_user.titulo = "Pagina de " + resource
            else:
                pag_user.titulo = title
            pag_user.save()
        elif name == 'Letra':
            letra = request.body.decode('utf-8').split("=")[1]
            pag_user.letra_size = letra
            pag_user.save()
        elif name == 'Color':
            color_fondo = request.body.decode('utf-8').split("=")[1]
            pag_user.color_fondo = color_fondo
            pag_user.save()
        elif name == 'Mas':
            n = request.body.decode('utf-8').split("=")[1]
            n = int(n) + 5
            museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
            try:
                museo = museos_seleccionados[n+5]
                boton_mas = "<form method = 'POST'><button type='submit' "
                boton_mas += "name='Mas' value=" + str(n) + ">Más"
                boton_mas += "</button></form>"
            except:
                boton_mas = ""
            museos_seleccionados = museos_seleccionados[n:n+5]
    else:
        plantilla = get_template("Kinda_Cloudy/error.html")
        error = "Método no permitido"
        c = RequestContext(request, {'error': error})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    c = RequestContext(request, {'usuarioname':resource,
            'usuario': usuario,
            'titulo': pag_user.titulo,
            'boton_mas': boton_mas,
            'seleccionados':museos_seleccionados,
            'color': color_fondo,
            'tamano':tamano})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)


def about(request):
    plantilla = get_template("Kinda_Cloudy/about.html")
    tamano = "13px"
    color_fondo = "#D3D3D3"
    try:
        usuario = User.objects.get(username=request.user)
        color_user = Configuracion.objects.get(usuario=usuario).color_fondo
        letra_user = Configuracion.objects.get(usuario=usuario).letra_size
        if(usuario.is_authenticated and not color_user == "Null"):
            color_fondo = color_user
            tamano = letra_user
    except (User.DoesNotExist, Configuracion.DoesNotExist):
        color_fondo = "#D3D3D3"
        tamano = "13px"
    c = RequestContext(request,{'color': color_fondo, 'tamano': tamano});
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta)

def xml_usuario(request, resource):
    try:
        usuario = User.objects.get(username=resource)
    except User.DoesNotExist:
        plantilla = get_template("Kinda_Cloudy/error.html")
        error = "El usuario no existe"
        c = RequestContext(request,{'error': error})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    plantilla = get_template('xml/canal_usuario.xml')
    museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
    c = RequestContext(request, {'usuario': usuario,
                              'museos_seleccionados': museos_seleccionados})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta, content_type="text/xml")

def xml_main(request):
    global accesibilidad
    plantilla = get_template('xml/canal_main.xml')
    listaMasComentados = Museo.objects.all().order_by('-num_coment')
    listaMasComentados = listaMasComentados.exclude(num_coment=0)
    if accesibilidad:
        listaMasComentados = listaMasComentados.filter(accesibilidad=1)
    listaMasComentados = listaMasComentados[:5]
    pag_personales = Configuracion.objects.all()
    c = RequestContext(request, {'paginas_personales': pag_personales,
                              'museosMasComentados': listaMasComentados})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta, content_type="text/xml")

def json_usuario(request, resource):
    try:
        usuario = User.objects.get(username=resource)
    except User.DoesNotExist:
        plantilla = get_template("Kinda_Cloudy/error.html")
        error = "El usuario no existe"
        c = RequestContext(request,{'error': error})
        respuesta = plantilla.render(c)
        return HttpResponse(respuesta)
    plantilla = get_template('json/canal_usuario.json')
    museos_seleccionados = Seleccion.objects.filter(usuario=usuario)
    c = RequestContext(request, {'usuario': usuario,
                              'museos_seleccionados': museos_seleccionados})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta, content_type="text/json")

def json_main(request):
    global accesibilidad
    plantilla = get_template('json/canal_main.json')
    listaMasComentados = Museo.objects.all().order_by('-num_coment')
    listaMasComentados = listaMasComentados.exclude(num_coment=0)
    if accesibilidad:
        listaMasComentados = listaMasComentados.filter(accesibilidad=1)
    listaMasComentados = listaMasComentados[:5]
    pag_personales = Configuracion.objects.all()
    c = RequestContext(request, {'paginas_personales': pag_personales,
                              'museosMasComentados': listaMasComentados})
    respuesta = plantilla.render(c)
    return HttpResponse(respuesta, content_type="text/json")

@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        userName = request.POST['username']
        pw = request.POST['password']
        visitante = authenticate(username=userName, password=pw)
        if visitante is not None:
            if visitante.is_active:
                login(request, visitante)

    return HttpResponseRedirect('/')

@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect('/')
