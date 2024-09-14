class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} hace un sonido."

class Perro(Animal):
    def __init__(self, name, breed):
        # Llama al constructor de la clase padre (Animal)
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Llama al método speak de la clase padre y lo extiende
        return super().speak() + " ¡Guau!"

# Crear un objeto de la clase Perro
mi_perro = Perro("Max", "Labrador")
print(mi_perro.speak())  # Output: Max hace un sonido. ¡Guau!
