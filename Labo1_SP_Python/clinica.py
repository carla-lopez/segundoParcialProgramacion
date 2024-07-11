# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from paciente import Paciente
from turno import Turno
from validaciones import *
import json
from tabulate import tabulate

class Clinica:
    def __init__(self, razon_social):
        self._razon_social = razon_social
        self._lista_pacientes = []
        self._lista_turnos = []
        self._especialidades = []
        self._obras_sociales_validas = {}
        self._recaudacion = 0.0
        self._hay_pacientes_sin_atencion = False
        
    def cargar_datos(self):
        """
        La función carga datos de un archivo JSON, asigna especialidades válidas y compañías de seguros médicos, crea instancias de pacientes y citas y las añade a las listas respectivas.
        válidos, crea instancias de pacientes y citas, y las añade a las listas respectivas.
        """
        # Leer el archivo JSON
        with open('configs.json', 'r') as file:
            data = json.load(file)

        # Asignar especialidades y obras sociales válidas desde el JSON
        if 'especialidades' in data and isinstance(data['especialidades'],list):
            self._especialidades = data['especialidades']
            
        self._obras_sociales_validas = data.get('obras_sociales',{})

        # Crear instancias de Paciente a partir de los datos y añadirlos a la lista de pacientes
        for idx, paciente_data in enumerate(data.get('pacientes',[]),start=1):
            paciente_data['id']= idx
            paciente = Paciente(**paciente_data)
            self._lista_pacientes.append(paciente)
            
        for turno_data in data.get('turnos',[]):
            turno = Turno(**turno_data)
            self._lista_turnos.append(turno)
            
            
        """
        Este código Python define propiedades para gestionar una lista de pacientes, una lista de citas, una
        lista de especialidades, una lista de compañías de seguros médicos válidas y un importe de ingresos.
        :devolver: El fragmento de código proporcionado define varias propiedades en una clase Python. Cuando se accede a estas
        propiedades, devuelven los valores almacenados en los atributos privados correspondientes de la clase.
        de la clase. Esto es lo que devuelve cada propiedad:
        """
    @property
    def lista_pacientes(self):
        return self._lista_pacientes
    
    @lista_pacientes.setter
    def lista_pacientes(self, pacientes):
        self._lista_pacientes = pacientes # objeto.lista_pacientes = valor
        
    @property
    def lista_turnos(self):
        return self._lista_turnos
    
    @lista_turnos.setter
    def lista_turnos(self, turnos):
        self._lista_turnos = turnos
        
    @property
    def especialidades(self):
        return self._especialidades
    
    @property
    def obras_sociales_validas(self):
        return self._obras_sociales_validas
    
    @property
    def recaudacion(self):
        return self._recaudacion
    
    @recaudacion.setter
    def recaudacion(self, monto):
        self._recaudacion = monto
    
    
    
    def alta_paciente(self,nombre,apellido,dni,edad,fecha_registro_str,obra_social):
        """
        La función `alta_paciente` en Python pide al usuario que introduzca información sobre el paciente, valida la entrada y crea un nuevo objeto `Paciente` para añadirlo a la lista de pacientes.
        y crea un nuevo objeto `Paciente` para añadirlo a una lista de pacientes.
        
        param nombre: El parámetro `nombre` del método `alta_paciente` se utiliza para almacenar el nombre del paciente.
        paciente. Se obtiene a partir de los datos introducidos por el usuario y se valida para garantizar que sólo contiene letras y espacios.
        y tiene una longitud máxima de 30 caracteres. Si la entrada no cumple estos criterios, se introduce un
        :param apellido: El parámetro `apellido` del método `alta_paciente` se refiere al apellido
        del paciente que se está registrando. Es un dato obligatorio para crear un nuevo registro de paciente en el
        sistema. El código pide al usuario que introduzca el apellido, lo valida utilizando el método
        validar_nombre_o_ap
        parámetro dni: El parámetro `dni` de la función `alta_paciente` se refiere al número nacional de
        nacional del paciente. Se trata de un identificador único asignado a las personas en muchos
        países con fines de identificación. En el contexto de esta función, se utiliza para garantizar que
        cada paciente esté identificado de forma única dentro del sistema
        :param edad: El parámetro "edad" en la función proporcionada representa la edad del paciente. En
        El usuario la introduce inicialmente como una cadena, que se convierte en un número entero tras la validación
        para asegurar que es un valor numérico dentro de un rango específico (entre 18 y 90 años).
        :param fecha_registro_str: El parámetro `fecha_registro_str` del método `alta_paciente
        se utiliza para almacenar la fecha de registro del paciente. Se pide al usuario que introduzca
        la fecha en el formato "DD-MM-AAAA". Esta entrada se valida con el método
        función `validar_fecha_registro
        param obra_social: El parámetro `obra_social` del método `alta_paciente` hace referencia al
        seguro médico o de la seguridad social al que pertenece el paciente. Se trata de un dato
        para los profesionales sanitarios, ya que puede influir en el acceso del paciente a determinados
        determinados servicios y tratamientos médicos. En el método
        :return: En el fragmento de código proporcionado, la función `alta_paciente` no devuelve explícitamente
        ningún valor. En su lugar, está creando un nuevo objeto `Paciente` con los datos de entrada proporcionados por el
        usuario y lo añade a la lista de pacientes (`self._lista_pacientes`).
        """
        nombre = input("Ingrese el nombre del paciente: ")
        
        if not validar_nombre_o_apellido(nombre):
            print(f"Error: El nombre '{nombre}' no es válido. Debe contener solo letras y espacios, y tener hasta 30 caracteres.")
            return None
        
        while True:
            apellido = input("Ingrese el apellido del paciente: ")
            if validar_nombre_o_apellido(apellido):
                break
            else:
                print(f"Error: el apellido '{apellido}' no es valido. Debe contener solo letras y espacios, y tener hasta 30 caracteres.")

        while True:
            dni = input("Ingrese el numero de documento del paciente: ")
            if validar_dni(dni):
                break
            else:
                print(f"Error: el DNI '{dni}' no es valido. Debe tener 8 digitos y ser solo numeros")

        while True:
            edad_str = input("Ingrese la edad del paciente: ")
            if edad_str.isdigit(): #Verifica si la entrada es numerica
                edad = int(edad_str)
                if validar_edad(edad):
                    break
                else:
                    print("Error: La edad debe estar entre 18 y 90 años")
            else:
                print("Error: La edad debe contener solo numeros.")
                
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print(f"Error: El DNI {dni} ya esta registrado para otro paciente.")
                return None

        while True:
            fecha_registro_str = input("Ingrese la fecha de registro del paciente (DD-MM-YYYY): ")
            valida,fecha_registro_str = validar_fecha_registro(fecha_registro_str)
            if valida:
                break
            else:
                print(f"Error: La fecha de registro '{fecha_registro_str}' no es valida.")

        while True:
            obra_social = input("Ingrese la obra social del paciente: ")
            if validar_obra_social(edad,obra_social):
                break
            else:
                print("Error: La obra social no es valida.")
        
        nuevo_paciente = Paciente(
            id = len(self._lista_pacientes) + 1,
            nombre = nombre, 
            apellido = apellido, 
            dni = dni, 
            edad = edad, 
            fecha_registro = fecha_registro_str, 
            obra_social = obra_social
            )
        self._lista_pacientes.append(nuevo_paciente)
    
    def alta_turno(self):
        """
        Esta función de Python permite programar una nueva cita para un paciente seleccionando una
        especialidad y calcular el importe del pago.
        :devolver: El método `alta_turno` no devuelve explícitamente ningún valor. Si el paciente con el
        proporcionado no se encuentra en la lista de pacientes, el método imprime un mensaje de error y devuelve
        `Ninguno`. En caso contrario, añade una nueva cita (Turno) a la lista de citas y guarda los datos, pero no devuelve ningún valor.
        datos, pero no devuelve ningún valor específico.
        """
        
        dni_paciente = input("Ingrese el DNI del paciente: ")
        paciente_existente = None
        
        for paciente in self.lista_pacientes:
            if paciente.dni == dni_paciente:
                paciente_existente = paciente
                break
            
        if not paciente_existente:
            print(f"Error: No se encontro ningun paciente con el DNI {dni_paciente}.")
            return None
        print("Especialidades disponibles: ")
        for i, especialidad in enumerate(self._especialidades):
            print(f"{i+1}.{especialidad}")

        while True:
            try:
                especialidad_index = int(input("Seleccione la especialidad deseada: "))
                if 1 <= especialidad_index <= len(self._especialidades):
                    especialidad_seleccionada = self._especialidades[especialidad_index - 1]
                    break
                else:
                    print(f"Por favor, ingrese un número entre 1 y {len(self._especialidades)}.")
            except ValueError:
                print("Error: Ingrese un número válido.")
                
            
        monto_a_pagar = Turno.calcular_monto(paciente)
        
        nuevo_id_turno = len(self._lista_turnos) + 1
        obra_social = paciente_existente.obra_social
        
        nuevo_turno = Turno(
            id= nuevo_id_turno,
            id_paciente=paciente_existente.id,
            especialidad=especialidad_seleccionada,
            estado="ACTIVO",
            monto=monto_a_pagar,
            obra_social=obra_social
        )
        
        self._lista_turnos.append(nuevo_turno)
        self.guardar_datos()
        print("Los datos fueron guardados existosamente")
    
    def mostrar_turnos(self):
        """
        Esta función recorre una lista de turnos e imprime sus detalles.
        """
        for turno in self._lista_turnos:
            obra_social_str = turno.obra_social 
            print(f"Turno({turno.id}, {turno.id_paciente}, {turno.especialidad}, {turno.monto}, {turno.estado}, {obra_social_str})")
                
       
    
    def ordenar_turnos(self,opcion):
        """
        Esta función de Python ordena una lista de citas por orden ascendente de seguro médico o por orden descendente de importe.
        seguro médico o en orden descendente de importe.
        
        param opcion: El parámetro `opcion` se utiliza para determinar el criterio de ordenación de la lista de
        vueltas. Se pide al usuario que seleccione una opción para ordenar los turnos bien por orden ascendente
        de la compañía de seguros médicos (`obra_social`) o por orden descendente del importe (`monto`)
        asociado a cada turno
        """
        opcion=input("Seleccione una opcion de ordenamiento: \na-Obra social ascendente. \nb-Monto descendente: \n")
        if opcion == 'a':
            self._lista_turnos.sort(key=lambda turno:turno.obra_social if turno.obra_social else "")
            print("Turnos ordenados por obra social ASC")
        elif opcion == 'b':
            self._lista_turnos.sort(key=lambda turno: (-turno.monto if turno.monto is not None else 0,turno.id))
            print("Turnos ordenados por monto DESC.")
        else:
            print("Opcion invalida para ordenar turnos")
            
        self.mostrar_turnos()
        
    def mostrar_pacientes_espera (self):
        """
        La función `mostrar_pacientes_espera` filtra los turnos activos y muestra los nombres e ID de los
        pacientes en lista de espera.
        """
        turnos_activos = list(filter(lambda turno: turno.estado == "ACTIVO",self.lista_turnos))
        id_pacientes_en_espera = set([turno.id_paciente for turno in turnos_activos])
        
        if not id_pacientes_en_espera:
            print("No hay pacientes en espera.")
        else:
            print("Pacientes en espera: ")
            for paciente in self.lista_pacientes:
                if paciente.id in id_pacientes_en_espera:
                    print(f"{paciente.nombre} {paciente.apellido} - DNI: {paciente.dni}")
                    
    def atender_pacientes(self):
        """
        La función "atender_pacientes" filtra las citas activas, empareja a los pacientes con sus
        citas, y actualiza el estado de las citas a "FINALIZADO" después de atenderlas.
        de atenderlas.
        :retorno: Si no hay turnos activos, se imprime el mensaje "No hay pacientes en espera." y
        la función retorna sin ningún valor de retorno explícito.
        """
        # Filtrar los turnos activos
        turnos_activos = [turno for turno in self.lista_turnos if turno.estado == "ACTIVO"][:2]

        if not turnos_activos:
            print("No hay pacientes en espera.")
            return
        
        pacientes_en_espera = []
        
        for turno in turnos_activos:
            paciente_encontrado = False
            for paciente in self.lista_pacientes:
                if paciente.id == turno.id_paciente:
                    pacientes_en_espera.append(paciente)
                    paciente_encontrado = True
                    break
            if not paciente_encontrado:
                print("No se encontro el paciente asociado al turno.")
        
        print("Pacientes en espera:")
        for paciente in pacientes_en_espera:
            print(f"{paciente.nombre} {paciente.apellido} - DNI: {paciente.dni}")
            
        for turno in turnos_activos:
            for paciente in pacientes_en_espera:
                if paciente.id == turno.id_paciente:
                    print(f"Atendiendo a {paciente.nombre} {paciente.apellido} {paciente.dni}")
                    
                    turno.estado = "FINALIZADO"
                    print(f"El estado del turno de {paciente.nombre} {paciente.apellido} {paciente.dni} ha sido cambiado a FINALIZADO")
                
        
            
    def cobrar_atenciones(self):
        """
        Esta función de Python es responsable de cobrar las tarifas por las citas completadas, actualizar el estado de las citas a "PAGADO" y llevar un registro de los ingresos totales generados.
        estado de las citas a "PAGADO", y llevar un registro de los ingresos totales generados.
        :devolver: Si no hay turnos finalizados para cobrar, la función imprimirá "No hay turnos
        finalizados para cobrar." y regresará sin realizar ninguna otra acción.
        """
        turnos_finalizados = [turno for turno in self.lista_turnos if turno.estado == "FINALIZADO"]
        
        if not turnos_finalizados:
            print("No hay turnos finalizados para cobrar. ")
            return
        
        total_recaudado = 0.0
        
        for turno in turnos_finalizados:
            paciente = next((paciente for paciente in self.lista_pacientes if paciente.id == turno.id_paciente), None)
            if paciente:
                monto_a_cobrar = paciente.calcular_monto()
               
                print(f"Cobrando atencion a {paciente.nombre} {paciente.apellido} por un monto de ${monto_a_cobrar:.2f}")
                total_recaudado += monto_a_cobrar
                
                turno.estado = "PAGADO"
                
        self.recaudacion += total_recaudado
        self.guardar_datos()
        print(f"Total recaudado: ${total_recaudado:.2f}")
        
        
    def cerrar_caja(self):
        pacientes_en_espera = any(turno.estado == "ACTIVO" or turno.estado== "FINALIZADO" for turno in self.lista_turnos)
        data = {
            'especialidades': self.especialidades,
            'obras_sociales': self.obras_sociales_validas,
            'pacientes': [paciente.to_dict() for paciente in self._lista_pacientes],# [vars(paciente) for paciente in self._lista_pacientes],
            'turnos': [turno.to_dict() for turno in self._lista_turnos] #[vars(turno) for turno in self._lista_turnos]
        }
        
        if pacientes_en_espera:
            print("Aun hay pacientes por atender.")
        else:
             # Mostrar especialidades
            print("\nEspecialidades:")
            print(tabulate([{"Especialidad": especialidad} for especialidad in self._especialidades],headers="keys"))

            # Mostrar obras sociales
            print("\nObras Sociales: ")
            print(tabulate([{"Obra Social": obra} for obra in self._obras_sociales_validas.keys()],headers="keys"))

            # Mostrar pacientes
            print("\nPacientes:")
            print(tabulate(data['pacientes'],headers="keys"))

            # Mostrar turnos
            print("\nTurnos:")
            print(tabulate(data['turnos'],headers="keys"))

            # Mostrar total recaudado
            print(f"Se cierra la caja. Total recaudado hoy: ${self.recaudacion:.2f}")
            self.guardar_datos()
            
        informe = self.informe_paciente_mas_joven_atendido()
        if informe:
            self.caja_cerrada.append({
                "fecha_cierre": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "informe_paciente_joven": informe
            })
            print("Caja cerrada y reporte guardado.")
    
    def informe_paciente_mas_joven_atendido(self):
        turnos_finalizados= [turno for turno in self.lista_turnos if turno.estado == "PAGADO"]
        
        if not turnos_finalizados:
            print("No hay pacientes atendidos para mostrar.")
            return
        
        paciente_mas_joven = None
        for turno in turnos_finalizados:
            paciente = next((p for p in self.lista_pacientes if p.id == turno.id_paciente), None)
            if paciente:
                if paciente_mas_joven is None or paciente.edad < paciente_mas_joven.edad:
                    paciente_mas_joven = paciente
                    
        if paciente_mas_joven:
            print("\nInforme - Paciente mas joven atendido: ")
            print(f"Nombre: {paciente_mas_joven.nombre} {paciente_mas_joven.apellido}")
            print(f"DNI: {paciente_mas_joven.dni}")
            print(f"Edad: {paciente_mas_joven.edad}")
            print(f"Fecha de registro: {paciente_mas_joven.fecha_registro}")
            print(f"Obra social: {paciente_mas_joven.obra_social}")
        else:
            print("No se encontro informacion del paciente mas joven atendido.")
            
    def guardar_datos(self):
        data = {
            'especialidades': self.especialidades,
            'obras_sociales': self.obras_sociales_validas,
            'pacientes': [paciente.to_dict() for paciente in self._lista_pacientes],# [vars(paciente) for paciente in self._lista_pacientes],
            'turnos': [turno.to_dict() for turno in self._lista_turnos] #[vars(turno) for turno in self._lista_turnos]
        }
        with open('configs.json', 'w') as file:
            json.dump(data, file, indent=4)
            
    print("Los datos han sido guardado")
    

        