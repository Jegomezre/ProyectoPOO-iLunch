from tkinter import *
import pathlib
import os

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.usuariosRestaurante.administrador import Administrador


from guiMain.ventanaUsuario import VentanaUsuario

class VentanaInicio(Tk):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana

        self.title('i-Lunch - Inicio')
        self.option_add("*tearOff",  False)
        self.geometry("1400x720")
        self.resizable(False,False)

        # Creacion del menu

        self._barraMenu = Menu(self)
        inicio = Menu(self._barraMenu)
        inicio.add_command(label = "Descripcion", command = lambda: self.desplegarDescripcion())
        inicio.add_command(label = "Salir", command = lambda: self.destroy())
        self._barraMenu.add_cascade(label = "Inicio", menu = inicio)
        self.config(menu = self._barraMenu)

        # Bienvenida al sistema

        self._p1 = P1(self)

        # Hoja de vida e imagen de los desarrolladores

        self._p2 = P2(self) 

        # Colocar los elementos en pantalla

        self._p1.grid(row = 0, column = 0, padx=(10,10))
        self._p2.grid(row = 0, column = 1, padx=(10,10))

    # Desplegar la descripcion y aumentar un poco el tamano de la ventana

    def desplegarDescripcion(self):
        self._p1._descripcion.pack(pady=(10,0))
        self.geometry("1420x840")

# Frame P1 con la bienvenida al sistema

class P1(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        # Guardar la referncia a la ventana para cerrarla luego

        self._ventana = ventana

        # Definir los Frames en los que se pondran los elementos

        self._p3 = Frame(self)
        self._p4_1 = Frame(self)
        self._p4_2 = Frame(self)

        # Mesaje de bienvenida en P3

        restaurante = Restaurante.getRestaurantes()[0]
        administrador = Administrador.getAdministradores()[0]

        textoSaludo = f"Bienvenido de nuevo a i-Lunch.\n" \
                      f"Administrador: {administrador.getNombre()}.\n" \
                      f"Restaurante: {restaurante.getNombre()}."
        self._saludo = Label(self._p3, text = textoSaludo, font = ("Verdana", 16), fg = "#245efd")
        self._saludo.pack()

        # Mostrar descripcion en P3 si se le da click al boton en el menu

        textoDescripcion = f"i-Lunch es una aplicacion de gestion de restaurantes. El administrador del restaurante que contrate la aplicacion\n" \
                           f"tendra acceso a un software en el cual podra llevar el control de todos los aspectos de su restaurante como:\n" \
                           f"• La informacion basica del restaurante.\n" \
                           f"• Su oferta de productos.\n" \
                           f"• Sus empleados.\n" \
                           f"• Los pedidos realizados al restaurante.\n" \
                           f"• El balance de cuenta y la nomina de los empleados.\n" \
                           f"• Su clientela."
        self._descripcion = Label(self._p3, text = textoDescripcion, width = 100, justify = "left", font=("Verdana", 8))

        # Cargar la imagenes relacionadas con la app en que se usaran en P4

        self._imagenActual = 0 # Imagen actual
        self._imagenes = []

        for i in range(5):
            archivo = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), f"src\\recursos\imagenApp{i+1}.png")
            imagen = PhotoImage(file = archivo)
            self._imagenes.append(imagen)

        # Imprimir la primera imagen relacionada a la aplicacion en P4

        self._imagen = Label(self._p4_1, image = self._imagenes[0], height = 480, width = 640)
        self._imagen.bind('<Enter>', self.cambiarImagen) # Cambiar de imagen de P4 al pasar el mouse por encima
        self._imagen.pack()

        # Boton de acceso a la aplicacion abajo en P4

        self._boton = Button(self._p4_2, text = "Acceder a la aplicacion", font = ("Verdana", 16), fg = "white", bg = "#245efd", command = lambda: self.accederApp(restaurante, administrador))
        self._boton.pack()

        # Colocar todos los elementos en pantalla

        self._p3.grid(row = 0, column = 0, pady=(10,10))
        self._p4_1.grid(row = 1, column = 0, pady=(10,10))
        self._p4_2.grid(row = 2, column = 0, pady=(10,10))
    
    # Cambiar de imagen de P4 al pasar el mouse por encima

    def cambiarImagen(self, args): # Recibe un parametro porque Bind de Tkinter lo manda asi
        if self._imagenActual == 4:
            self._imagenActual = 0
        else:
            self._imagenActual += 1

        self._imagen.configure(image = self._imagenes[self._imagenActual])
        self._imagen.image = self._imagenes[self._imagenActual]

    # Acceder a la aplicacion al darle click al boton de P4

    def accederApp(self, restaurante, administrador):
        self._ventana.destroy()
        ventanaUsuario = VentanaUsuario(restaurante, administrador)

# Frame P2 con la hoja de vida de los desarrolladores

class P2(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)

        self._p5 = Frame(self)
        self._p6 = Frame(self)

        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]
        self._labels = []

        self.cargarHVTexto(0)

        for i in range(0, 4):
            label = Label(self._p6, width = 320, height = 240)
            (r, c) = P2._posicion_imagen[i]
            label.grid(row=r, column=c)
            self._labels.append(label)
            # Se cargan las primeras imagenes
            self.cargarHVImagen(0, i)
    
        self._p5.grid()
        self._p6.grid()

    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self._next_hv < 3:
            self._next_hv = self._next_hv + 1
        else:
            self._next_hv = 0

        self._photos = [None, None, None, None]
        self.cargarHVTexto(self._next_hv)
        for i in range(0, 4):
            self.cargarHVImagen(self._next_hv, i)

    # Carga el component imagen que sirve para mostrar las fotos
    def cargarHVImagen(self, hv_num, numero):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\recursos\HV{0}{1}.png'.format(hv_num, numero))
        photo = PhotoImage(file = path)
        self._labels[numero].configure(image = photo)
        self._labels[numero].image = photo

    # Carga el texto para la hoja de vida respecto al numero asignado

    def cargarHVTexto(self, numero):
        self._text = Text(self._p5, height = 10, font = ("Verdana",10), width = 80)
        self._text.grid(row = 1, column = 0)
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\recursos\HV{0}4.txt'.format(numero))

        with open(path, "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())
