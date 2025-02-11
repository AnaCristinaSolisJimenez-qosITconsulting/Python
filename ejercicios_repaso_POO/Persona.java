package ejercicios_repaso_POO;

import java.util.Objects;

public class Persona implements Comparable<Persona>{
    
String nombre;
int edad;
Direccion direccion;

public Persona() {
}
public Persona(String nombre, int edad) {
    this.nombre = nombre;
    this.edad = edad;
}
public String getNombre() {
    return nombre;
}
public void setNombre(String nombre) {
    this.nombre = nombre;
}
public int getEdad() {
    return edad;
}
public void setEdad(int edad) {
    this.edad = edad;
}
@Override
public String toString() {
    return nombre+" tiene "+edad+ " años.";
}

@Override
    public boolean equals(Object obj) {//obj puede ser una instancia de cualquier clase.
    //equals viene de la clase Object y todas las clases, directa o indirectamente provienen de object
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            //obj.getClass() es un método que se puede llamar en cualquier objeto y se hereda de Object,
            //devuelve un objeto del tipo class que representa a la clase objeto.
            return false;
        }
        Persona other = (Persona) obj;
        return edad == other.edad && Objects.equals(nombre, other.nombre);
    }

 public void mostrarinformacion() {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad);
    }
     public Direccion getDireccion() {
        return direccion;
    }
     public void mostrardireccion() {
        System.out.println("direccion : " + direccion);
    }

    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }
      @Override
    public int comparar(Persona otraPersona) {
        if (this.edad == otraPersona.edad) {
            return 0; // Son iguales
        } else if (this.edad > otraPersona.edad) {
            return 1; // El objeto actual es mayor
        } else {
            return -1; // El objeto actual es menor
        }
    }
    
    
}
