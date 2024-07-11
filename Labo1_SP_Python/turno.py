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

# Esta clase Python llamada Turno representa una cita médica con atributos como ID, paciente
# ID, especialidad, estado, importe y seguro médico.
class Turno:
    def __init__(self,id,id_paciente,monto,especialidad,estado = "ACTIVO",obra_social=None):
        self.id = id
        self.id_paciente = id_paciente
        self.especialidad = especialidad
        self.estado= estado
        self.monto = monto
        self.obra_social= obra_social
        
    def to_dict(self):
        """
        La función `to_dict` convierte los atributos de un objeto en un diccionario.
        :devolver: Se devuelve un diccionario con las siguientes claves y valores:
        - 'id': valor de self.id
        - 'id_paciente': valor de self.id_paciente
        - 'especialidad': valor de self.especialidad
        - estado': valor de self.estado
        - 'monto': valor de self.monto
        - 'obra_social': valor de self.obra_social
        """
        return{
            'id':self.id,
            'id_paciente':self.id_paciente,
            'especialidad':self.especialidad,
            'estado':self.estado,
            'monto':self.monto,
            'obra_social':self.obra_social
        }
    
    def calcular_monto(self):
        """
        La función calcula el importe final a pagar en función de la edad y el seguro médico del
        paciente, aplicando los diferentes descuentos correspondientes.
        
        param edad: El fragmento de código proporcionado define un método llamado `calcular_monto` que calcula
        el importe final a pagar en función de la edad y el seguro médico ("obra social") de una persona.
        El método recibe dos parámetros: `self` (suponiendo que forme parte de una clase) y `edad`, que
        devuelve: La función `calcular_monto` devuelve el importe final a pagar después de aplicar
        cualquier descuento aplicable basado en la edad de la persona y el proveedor de seguro médico.
        """
        precio_base = 4000
        monto_final = precio_base
        descuento = 0
        
        if self.obra_social == "Swiss Medical":
            descuento = 0.4
            if 18 <= self.edad <= 60:
                descuento += 0.1
        elif self.obra_social == "Apres":
            descuento = 0.25
            if 26 <= self.edad <= 59:
                descuento += 0.03
        elif self.obra_social == "PAMI":
            descuento = 0.6
            if self.edad >= 80:
                descuento += 0.03
        elif self.obra_social == "Particular":
            descuento = -0.05
            if 40 <= self.edad <= 60:
                descuento += 0.15
            
        monto_final *= (1 - descuento) #*= multiplica el valor actual de la variable por el valor a la derecha del operador
        return monto_final
    
    
    def __repr__(self) -> str:
        """
        La función `__repr__` devuelve una representación en forma de cadena de un objeto Turno con sus atributos.
        :devolver: El método `__repr__` devuelve una representación en forma de cadena del objeto de clase
        `Turno`. La cadena devuelta incluye los atributos `id`, `id_paciente`, `especialidad`,
        `monto`, `estado`, y `obra_social` del objeto. El atributo `obra_social` se convierte en
        y se incluye en la representación devuelta.
        """
        obra_social_str = self.obra_social 
        return f"Turno({self.id} , {self.id_paciente},{self.especialidad} , {self.monto} , {self.estado} , {obra_social_str})"