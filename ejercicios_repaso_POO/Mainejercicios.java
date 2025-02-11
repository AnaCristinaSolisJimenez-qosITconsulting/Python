package ejercicios_repaso_POO;

public class Mainejercicios {
public static void main(String[] args) {
    Persona persona1=new Persona("pepe", 38);
    System.out.println(persona1);
    Estudiante estudiante1=new Estudiante("Luis", 19, "Arquitectura");
    System.out.println(estudiante1);
    
    Profesor profe=new Profesor("jochefluis", 30, "cocina");
    profe.trabajar();

    Direccion direccion=new Direccion("san luis", "trebujena", "12341234");
    System.out.println(direccion);

    Persona[] array = new Persona[3];
    array[0]= persona1;
    array[1]=estudiante1;
    array[2]=profe;
    System.out.println("MOSTRAR INFORMACION");
    System.out.println("=========================");

    for (Persona persona : array) {
        persona.mostrarinformacion();
        if (persona instanceof Trabajador) { // mira si el objeto es de tipo Trabajador
                Trabajador trabajador = (Trabajador) persona; // hace casting del objeto a tipo Trabajador
                trabajador.trabajar(); // Llama al método trabajar()
            }
        System.out.println("=========================");
    }
    
}
}
