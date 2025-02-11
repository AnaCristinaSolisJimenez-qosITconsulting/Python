package ejercicios_repaso_POO.ej9;

public class Main {
    public static void main(String[] args) {
        // Crear profesores
        Profesor profesor1 = new Profesor("Juan Pérez", 45, "Matemáticas");
        Profesor profesor2 = new Profesor("Ana García", 38, "Física");

        // Crear estudiantes
        Estudiante estudiante1 = new Estudiante("Luis Rodríguez", 20, "Ingeniería");
        Estudiante estudiante2 = new Estudiante("María Sánchez", 22, "Medicina");
        Estudiante estudiante3 = new Estudiante("Pedro López", 19, "Derecho");

        // Crear cursos
        Curso curso1 = new Curso("Cálculo I", profesor1);
        Curso curso2 = new Curso("Física General", profesor2);

        // Matricular estudiantes en cursos
        curso1.matricularEstudiante(estudiante1);
        curso1.matricularEstudiante(estudiante2);
        curso2.matricularEstudiante(estudiante3);

        // Mostrar información de los cursos
        curso1.mostrarInformacion();
        curso2.mostrarInformacion();
    }
}
