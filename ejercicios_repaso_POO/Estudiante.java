package ejercicios_repaso_POO;

public class Estudiante extends Persona{
String carrera;

public Estudiante() {
}

public Estudiante(String nombre, int edad, String carrera) {
    super(nombre, edad);
    this.carrera = carrera;
}

public String getCarrera() {
    return carrera;
}

public void setCarrera(String carrera) {
    this.carrera = carrera;
}

@Override
public String toString() {
    return nombre+" es estudiante, tiene "+edad+" años "+"y estudia "+carrera;
}

@Override
    public void mostrarinformacion() {
        super.mostrarinformacion(); // Llama al método mostrarInformacion() de la clase Persona
        System.out.println("carrera: " + carrera);
    }


}
