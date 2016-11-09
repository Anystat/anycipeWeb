from django.db import models


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=150)
    text = models.TextField('Рецепт')
    author = models.CharField('Автор', max_length=150, default='Admin')
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:

        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        # ordering = ['-create_date']

    def __str__(self):

        return '{} {}'.format(self.title, self.create_date)
