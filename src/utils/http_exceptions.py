from fastapi import HTTPException, status


class LinkerBaseHTTPException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = None
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class NotUniqueLinkHTTPException(LinkerBaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Ошибка создание ссылки. Повторите попытку"

class LinkNotFoundHTTPException(LinkerBaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ссылка не найдена"