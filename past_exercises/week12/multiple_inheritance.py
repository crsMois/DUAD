
# USOS DE LA HERENCIA MULTIPLE
# Reutlizacion de codigo: Hay clases que ya tienen codigo que uno requiere y gracias a la herencia podemos reutilizar el codigo de diferente clases que talvez no tengan todos los elementos en comun
# Programacion modular: Se puede crear clases que tengan funciones muy especificas y se puede crear una que reuna o gestione esas funciones de la forma que el programador requira haciendo el uso del codigo mas flexible sin necesidad de duplicar
# Permiter crear mas clases abstractas que obliguen al programador a seguir un orden especifico y por ende programar de una forma mas ordenada



class DataCollection:
    def collect_data(self):
        print("Collecting data for the report.")

class ReportGeneration:
    def generate_report(self):
        print("Generating the report based on collected data.")

class ReportApp(DataCollection, ReportGeneration):
    def create_report(self):
        self.collect_data()
        self.generate_report()

app = ReportApp()
app.create_report()
