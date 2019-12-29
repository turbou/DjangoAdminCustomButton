from django.db import models

APP_STATUS_CHOICES = (
    ('W', '承認待ち'),
    ('U', '更新承認済み'),
    ('B', '営業承認済み'),
)

class Oyoyo(models.Model):
    name = models.CharField('名前', max_length=30)
    app_status = models.CharField('承認ステータス', choices=APP_STATUS_CHOICES, max_length=1, default='W')
    filepath = models.CharField('ファイルパス', max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'およよ'
        verbose_name_plural = 'およよ一覧'

