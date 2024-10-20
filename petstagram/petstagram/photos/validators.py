# from django.core.exceptions import ValidationError
# from django.utils.deconstruct import deconstructible
#
#
# @deconstructible
# class FileSizeValidator:
#     def __init__(self, file_size_md: int, message=None):
#         self.file_size_md = file_size_md
#         self.message = message
#
#     @property
#     def message(self):
#         return self.__message
#
#     @message.setter
#     def message(self, value):
#         if value is None:
#             self.__message = f'File size must be {self.file_size_md}MB'
#         else:
#             self.__message = value
#
#     def __call__(self, value):
#         if value.size > self.file_size_md * 1024 * 1024:
#             raise ValidationError(self.message)
