package ejercicios_repaso_POO.ej9;

class Estudiante extends Persona {
    private String carrera;

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
    public void mostrarInformacion() {
        super.mostrarInformacion();
        System.out.println("Carrera: " + carrera);
    }
}
