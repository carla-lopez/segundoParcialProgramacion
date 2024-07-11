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

from datetime import datetime

# La clase `Paciente` representa a un paciente con atributos como DNI, nombre, apellidos, número de DNI, edad,
# fecha de registro y seguro médico.
class Paciente:
    def __init__(self, id, nombre, apellido, dni, edad, fecha_registro, obra_social):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.fecha_registro = fecha_registro
        self.obra_social = obra_social
        
    def to_dict(self):
        """
        La función `to_dict` convierte los atributos de un objeto en un diccionario.
        :devuelve: Un diccionario que contiene los atributos 'id', 'nombre', 'apellido', 'dni', 'edad',
        'fecha_registro', y 'obra_social' con sus respectivos valores de la instancia del objeto.
        """
        return{
            'id':self.id,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'dni':self.dni,
            'edad':self.edad,
            'fecha_registro':self.fecha_registro,
            'obra_social':self.obra_social
        }

    def calcular_monto(self):
        """
        Esta función de Python calcula el importe final a pagar a partir de un precio base y descuentos
        en función de la edad y el seguro médico del paciente.
        :devuelve: el importe final a pagar tras aplicar el descuento en función de la edad y la
        afiliación a la obra social.
        """
        precio_base = 4000
        descuento = 0

        if self.obra_social == "Swiss Medical":
            descuento = 0.40
            if 18 <= self.edad <= 60:
                descuento += 0.10
        elif self.obra_social == "Apres":
            descuento = 0.25
            if 26 <= self.edad <= 59:
                descuento += 0.03
        elif self.obra_social == "PAMI":
            descuento = 0.60
            if self.edad >= 80:
                descuento += 0.03
        elif self.obra_social == "Particular":
            descuento = -0.05
            if 40 <= self.edad <= 60:
                descuento += -0.15
        else:
            print("No ingresaste una obra social válida")
            
        monto_final = precio_base * (1 - descuento)
        return monto_final
    
    def atender(self):
        """
        La función "atender" actualiza el estado de un objeto a "FINALIZADO" y establece la fecha y hora actuales
        y la hora como "fecha_atencion".
        """
        self.estado = "FINALIZADO"
        self.fecha_atencion = datetime.now()