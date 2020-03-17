from django.db import models


class UserMessage(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    subject = models.CharField(max_length=50, verbose_name='Tema')
    message = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Brief'
        verbose_name_plural = 'Briefe'


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rubrik'
        verbose_name_plural = 'Rubrike'
        ordering = ['name']


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ware')
    content = models.TextField(null=True, blank=True, verbose_name='Beschreibung')
    price = models.FloatField(null=True, blank=True, verbose_name='Preis')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Veröffentlicht')
    image = models.ImageField(upload_to='images', default='images/default.jpg', verbose_name='Photo')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubrike')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anschlag'
        verbose_name_plural = 'Anschlagen'
        ordering = ['-published']




