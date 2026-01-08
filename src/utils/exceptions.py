class LinkerBaseException(Exception):
    detail = "Неожиданная ошибка"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)

class NotUniqueException(LinkerBaseException):
    detail = "Ошибка уникальности"

class NotUniqueLinkException(NotUniqueException):
    detail = "Уже существует такая ссылка"

class ObjNotFoundException(LinkerBaseException):
    detail = "Не найден объект"

class LinkNotFoundException(ObjNotFoundException):
    detail = "Ссылка не найдена"