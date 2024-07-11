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
import re
from datetime import datetime, date

def validar_nombre_o_apellido(dato: str) -> bool:
    """
    La función `validar_nombre_o_apellido` comprueba si una cadena dada contiene sólo letras y espacios,
    con una longitud máxima de 30 caracteres.
    
    :param dato: El parámetro `dato` es una cadena que representa un nombre o apellido que necesita ser
    validar
    :type dato: str
    :return: La función `validar_nombre_o_apellido` devuelve un valor booleano. Devuelve `True` si
    el dato introducido `dato` es un nombre o apellido válido (sólo contiene letras y espacios, y tiene entre 1 y
    30 caracteres), y `False` en caso contrario.

    """
    if len(dato) > 30:
        return False
    return bool(re.match("^[A-Za-z\s]{1,30}$", dato))

def validar_edad(edad: int) -> bool:
    """
    La función `validar_edad` comprueba si una edad dada está entre 18 y 90 años.
    
    param edad: El parámetro "edad" representa la edad de una persona. La función "validar_edad" comprueba si
    la edad está entre 18 y 90 (ambos inclusive) y devuelve un valor booleano en consecuencia
    :type edad: int
    :devolver: La función `validar_edad` devuelve un valor booleano, que indica si la entrada
    (edad) está entre 18 y 90 años (ambos inclusive). Si la edad está entre 18 y 90, la función devolverá
    devolverá `True`, en caso contrario devolverá `False`.
    """
    return 18 <= edad <= 90

def validar_obra_social(edad: int, obra_social: str) -> bool:
    """
    La función `validar_obra_social` comprueba si una edad y un seguro médico dados son válidos basándose en
    listas predefinidas de seguros válidos para diferentes grupos de edad.
    
    param edad: El parámetro `edad` de la función `validar_obra_social` representa la edad del
    paciente para el que se está validando la obra social. La función comprueba si el
    es válida en función de la edad del paciente
    :type edad: int
    :param obra_social: El parámetro `obra_social` en la función `validar_obra_social` representa el
    nombre de la compañía de seguros médicos o del proveedor al que está asociado un paciente. La función
    comprueba si el seguro médico proporcionado es válido en función de la edad del paciente
    :type obra_social: str
    :devolver: La función `validar_obra_social` devuelve un valor booleano (`Verdadero` o `Falso`) basado en la
    validación de los parámetros de edad y obra social.

    """
    obras_sociales_validas_menores_60 = ["Swiss Medical", "Apres", "Particular"]
    obras_sociales_validas_mayores_60 = ["PAMI"]

    if edad >= 60:
        if obra_social not in obras_sociales_validas_mayores_60 and obra_social not in obras_sociales_validas_menores_60:
            print("Error: La obra social seleccionada es inexistente.")
            return False
        elif obra_social not in obras_sociales_validas_mayores_60:
            print("Error: Para pacientes de 60 años o más, solo se acepta PAMI como obra social.")
            return False
    else:
        if obra_social not in obras_sociales_validas_menores_60 and obra_social not in obras_sociales_validas_mayores_60:
            print("Error: La obra social seleccionada es inexistente.")
            return False
        elif obra_social not in obras_sociales_validas_menores_60:
            print("Error: Para pacientes menores de 60 años, la obra social seleccionada no es válida.")
            return False
    return True

def validar_dni(dni: str) -> bool:
    """
    La función `validar_dni` en Python comprueba si una cadena dada es un DNI (Documento Nacional de
    Documento Nacional de Identidad) verificando si consta de 8 dígitos.
    
    :param dni: La función `validar_dni` está diseñada para validar un número de Documento Nacional de Identidad
    (DNI) español. La función toma como entrada una cadena `dni` y comprueba si está formada sólo por dígitos
    y tiene una longitud de 8 caracteres. Si se cumplen ambas condiciones, la función devuelve `
    :tipo dni: cadena
    :return: La función `validar_dni` devuelve un valor booleano, que es `True` si la entrada `dni`
    está compuesto sólo por dígitos y tiene una longitud de 8 caracteres, y `False` en caso contrario.
    """
    return dni.isdigit() and len(dni) == 8

def validar_fecha_registro(fecha_str: str) -> bool:
    """
    La función `validar_fecha_registro` comprueba si una cadena de fecha dada es válida y no está en el futuro.
    
    param fecha_str: El parámetro `fecha_str` es una cadena que representa una fecha en el formato
    "día-mes-año", como "25-12-2022". La función `validar_fecha_registro` intenta convertir
    esta cadena en un objeto `datetime` utilizando el formato especificado ("%d-%m-%Y")
    :type fecha_str: str
    :return: La función `validar_fecha_registro` devuelve una tupla que contiene un valor booleano y un objeto
    objeto datetime. El valor booleano indica si la cadena de fecha introducida es válida o no, y el objeto
    representa la fecha analizada si es válida. Si la cadena de fecha no tiene el formato
    o representa una fecha futura, la función devuelve `(False, None)`.
    """
    try:
        fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
        return True, fecha_str
    except ValueError:
        return False,fecha_str
    except ValueError:
        return False,fecha_str