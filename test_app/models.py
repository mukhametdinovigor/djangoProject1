from django.db import models


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилий', max_length=100)
    address = models.CharField('Адрес', max_length=100)

'''
sdfgdsfg
sdfgsdfg
dfgdfg
sdfg
dfgsdfg
SDSD
sdgfsdfg
'''

class AnotherAuthor(models.Model):
    last_name = models.CharField('Фамилий', max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')


class Book(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

