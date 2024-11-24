# EN ESTE MÓDULO SE CREAN LAS EXCEPCIONES PERSONALIZADAS QUE SE PIDEN (AUNQUE SEAN UN POCO LIMITADAS)

class OpcionNoValidaError(Exception):
    pass
class NombreError(Exception):
    pass
class DNIError(Exception):
    pass
class CiudadNoEncontrada(Exception):
    pass 