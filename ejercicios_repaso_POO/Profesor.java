package ejercicios_repaso_POO;

public class Profesor extends Persona implements Trabajador {
String especialidad;

public Profesor() {
}

public Profesor(String nombre, int edad, String especialidad) {
    super(nombre, edad);
    this.especialidad = especialidad;
}

public String getEspecialidad() {
    return especialidad;
}

public void setEspecialidad(String especialidad) {
    this.especialidad = especialidad;
}

@Override
public String toString() {
    return nombre+" esta enseñando "+especialidad;
}
 @Override
    public void trabajar() {
        System.out.println(this.getNombre()+ " esta enseñando "+this.getEspecialidad());
    }
    
}
