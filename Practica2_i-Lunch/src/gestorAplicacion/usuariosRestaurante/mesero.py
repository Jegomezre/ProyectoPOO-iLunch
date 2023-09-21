from gestorAplicacion.usuariosRestaurante.empleado import Empleado

from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Mesero(Empleado):

    # Atributos estaticos

    _meseros = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None):
        super().__init__(cedula, nombre, "Mesero", disponibilidad, salario, restaurante)

        self._pedidosAtendidos = []
        self._historialPropinas = []

        Empleado._empleados.append(self)
        Mesero._meseros.append(self)
    
    # Getters y Setters

    def getPedidosAtendidos(self):
        return self._pedidosAtendidos

    def setPedidosAtendidos(self, pedidosAtendidos):
        self._pedidosAtendidos = pedidosAtendidos

    def getHistorialPropinas(self):
        return self._historialPropinas

    def setHistorialPropinas(self, historialPropinas):
        self._historialPropinas = historialPropinas

    @classmethod
    def getMeseros(cls):
        return cls._meseros

    @classmethod
    def setMeseros(cls, meseros):
        cls._meseros = meseros

    # Metodos

    def recibirPropina(self, propina):
        self._historialPropinas.append(propina)

    def agregarPedidoHistorial(self, pedido, propina):
        self._pedidosAtendidos.append(pedido)
        self.recibirPropina(propina)

    # Simulacion de llevar el pedido a un cliente
    def llevarPedido(self, pedido, propina):
        self.agregarPedidoHistorial(pedido, propina)
        
        # Solo se puede hacer si el pedido es de tipo consumir en el local y ya esta listo. Cambiar el estado del pedido
        if pedido.getEstado() == EstadoPedido.LISTO.value and pedido.getTipo() == TipoPedido.TIENDA.value:
            pedido.setEstado(EstadoPedido.DESPACHADO.value)

    # Calcular propinas totales del mesero
    def totalPropinas(self):
        total = 0

        for propina in self._historialPropinas:
            total += propina

        return total

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Mesero {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}.\n" \
               f"Tiene un salario de: ${self._salario}.\n"
        
        if self._disponibilidad:
            return info + "Esta disponible actualmente."
        else:
            return info + "No esta disponible actualmente."