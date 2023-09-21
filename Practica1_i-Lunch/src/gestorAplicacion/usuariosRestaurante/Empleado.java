/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO 
 
 *Clase padre de las clases ADMINISTRADOR, REPARTIDOR, CHEF y MESERO. Aqui se definen los atributos cedula,
 *nombre, cargo, disponinilidad, salario, restaurante y ****pagado****. Ademas de sus respectivos metodos get y set.*/

package gestorAplicacion.usuariosRestaurante;

import gestorAplicacion.gestionRestaurante.*;
import java.io.Serializable;
import java.util.ArrayList;

public class Empleado implements Serializable, Usuario {

	// Atributos utilizados para la serialización
	private static final long serialVersionUID = 1L; // Se requiere del atributo serialVersionUID por usar la interface
														// Serializable.
	private static ArrayList<Empleado> empleados;
	static {
		empleados = new ArrayList<Empleado>();
	}

	// Atributos
	protected int cedula;
	protected String nombre;
	protected String cargo;
	protected boolean disponibilidad;
	protected int salario;
	protected Restaurante restaurante;

	/* Constructor de la clase empleado */
	public Empleado(int cedula, String nombre, String cargo, boolean disponibilidad, int salario,
			Restaurante restaurante) {
		this.cedula = cedula;
		this.nombre = nombre;
		this.cargo = cargo;
		this.disponibilidad = disponibilidad;
		this.salario = salario;
		this.restaurante = restaurante;
		empleados.add(this);
	}

	/* Sobrecarga del constructor para valores predeterminados */
	public Empleado() {
		this(0, "NN", "NA", false, 0, null);
	}

	/* Metodos GET y SET para los atributos */
	public int getCedula() {
		return this.cedula;
	}

	public void setCedula(int cedula) {
		this.cedula = cedula;
	}

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCargo() {
		return this.cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public int getSalario() {
		return this.salario;
	}

	public boolean getDisponibilidad() {
		return this.disponibilidad;
	}

	public void setDisponibilidad(boolean disponibilidad) {
		this.disponibilidad = disponibilidad;
	}

	public void setSalario(int salario) {
		this.salario = salario;
	}

	public Restaurante getRestaurante(Restaurante restaurante) {
		return this.restaurante;
	}

	public void setRestaurante(Restaurante restaurante) {
		this.restaurante = restaurante;
	}

	public static ArrayList<Empleado> getEmpleados() {
		return empleados;
	}

	public Restaurante getRestaurante() {
		return restaurante;
	}

	public static void setEmpleados(ArrayList<Empleado> empleados) {
		Empleado.empleados = empleados;
	}

	/*
	 * SET Y GET del atributo pagado
	 * 
	 * public boolean isPagado() { return pagado; }
	 * 
	 * public void setPagado(boolean estado) { pagado=estado;}
	 */

	/*
	 * Metodo para cambiar el estado de un pedido(atributo "estadoPedido") a su fase
	 * inicial "En preparacion". Recibe como parametro un pedido y tiene como
	 * finalidad modificar el atributo "estadoPedido", la primera vez y de manera
	 * unica.
	 */

	// Métodos
	public boolean procesarPedido(Pedido pedido) {
		if (restaurante.verificarPersonal(pedido) && restaurante.verificarProductos(pedido)) {
			return true;
		}
		return false;
	}

	/*
	 * Metodo para cambiar el estado de un pedido(atributo "estadoPedido") en sus
	 * distintas etapas, de manera secuencial. Una vez termine la etapa actual, se
	 * puede continuar con la siguiente fase. Recibe como parametro un pedido y
	 * tiene como finalidad modificar el atributo "estadoPedido".
	 */
	public boolean actualizarEstadoPedido(Pedido pedido, boolean aceptado) {
		if (!aceptado) {
			pedido.setEstado(estadoPedido.Rechazado.name());
			return false;
		}

		switch (pedido.getEstado()) {

		case "Recibido":
			pedido.setEstado(estadoPedido.Aceptado.name());
			break;
		case "Aceptado":
			pedido.setEstado(estadoPedido.EnPreparacion.name());
			break;
		case "EnPreparacion":
			pedido.setEstado(estadoPedido.Listo.name());
			break;
		case "Listo":
			pedido.setEstado(estadoPedido.Despachado.name());
			break;
		}

		return true;

	}

	// Implementación de la interfaz Usuario
	public String informacion() {
		if (this.getDisponibilidad()) {
			return "El Empleado " + this.nombre + " con C.C. " + this.cedula + " trabaja en el restaurante "
					+ this.restaurante.getNombre() + "\n" + "Tiene un salario de: $" + this.salario
					+ " y desempeña el cargo de " + this.cargo + ".\n" + "Está disponible actualmente.";
		} else {
			return "El Empleado " + this.nombre + " con C.C. " + this.cedula + " trabaja en el restaurante "
					+ this.restaurante.getNombre() + "\n" + "Tiene un salario de: $" + this.salario
					+ " y desempeña el cargo de " + this.cargo + ".\n" + "No está disponible actualmente.";
		}
	}

	public String toString() {
		return "Cedula: \"" + cedula + "\"\n" + "Nombre: \"" + nombre + "\"\n" + "Cargo: \"" + cargo + "\"\n"
				+ "Disponiblidad: " + disponibilidad + "\n" + "Salario: " + salario + "\n" + "Restaurante: "
				+ restaurante;
	}
}
