from django.db import models

class Oyoyo(models.Model):
    name = models.CharField('名前', max_length=30)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'およよ'
        verbose_name_plural = 'およよ一覧'

