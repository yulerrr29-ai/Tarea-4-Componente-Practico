# archivo: cliente.py
# Estudiante: Verónica Ordoñez
# Tarea: Clase Cliente con validaciones

import re
from excepciones import DatoInvalidoError  # lo creará el Estudiante 4
from logger import logger  # lo creará el Estudiante 4

class Cliente:
    """Clase Cliente con encapsulación y validación de datos"""
    
    def __init__(self, nombre, email, telefono):
        self._nombre = None
        self._email = None
        self._telefono = None
        
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        
        logger.info(f"Cliente creado: {self._nombre}")
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        # Validación: no vacío y mínimo 3 caracteres
        if not valor or len(valor.strip()) < 3:
            raise DatoInvalidoError(f"Nombre inválido: mínimo 3 caracteres")
        self._nombre = valor.strip()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        # Validación: formato de email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor):
            raise DatoInvalidoError(f"Email inválido: {valor}")
        self._email = valor
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        # Validación: solo dígitos y mínimo 7
        if not valor.isdigit() or len(valor) < 7:
            raise DatoInvalidoError(f"Teléfono inválido: solo dígitos, mínimo 7")
        self._telefono = valor
    
    def mostrar_info(self):
        """Retorna información del cliente"""
        return f"Cliente: {self._nombre} | Email: {self._email} | Tel: {self._telefono}"
    