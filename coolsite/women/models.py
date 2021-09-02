from django.db import models

from django.db import connection

# Спец метод reverse для создания абсолютного пути URL
from django.urls import reverse


def create_category():
    return category.objects.create(name='Категория 3')


def update_women(cat_id):
    # women = Women.objects.get()
    women = Women.objects.all()
    return women.update(cat_id=cat_id)


def drop_category():
    """Метод напрямую удаляет таблицу women_category"""
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE women_category")
        # row = cursor.fetchall()
        row = cursor.fetchone()
    return row


def create_category():
    """Метод напрямую создает таблицу women_category"""
    with connection.cursor() as cursor:
        cursor.execute('CREATE TABLE "women_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);')
        cursor.execute('CREATE INDEX "women_category_name_893c5c38" ON "women_category" ("name");')
        row = cursor.fetchall()
    return row


def select_all_from_category():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "women_category";')
        # cursor.execute('CREATE INDEX "women_category_name_893c5c38" ON "women_category" ("name");')
        # row = cursor.fetchall()
        row = cursor.fetchone()
        row += cursor.fetchone()
    return row


def get_all_women_models_all():
    womens = Women.objects.all()
    print('Метод get_all_women_models_all')
    show_all_women(womens)


def get_all_women_models_raw():
    womens = Women.objects.raw('SELECT * FROM women_women')
    print('Метод get_all_women_models_raw')
    show_all_women(womens)


def show_all_women(womens):
    print('womens = ', womens)
    for women in womens:
        print('type(women) = ', type(women))
        print('women = ', women)
        print('women.cat = ', women.cat)
        print('women.title = ', women.title)
        print('women.content = ', women.content)
        print('women.time_create = ', women.time_create)
        print('women.is_published = ', women.is_published)


def get_all_category_models(table=None):
    table = 'women_category' if table is None else table
    models = category.objects.raw(f'SELECT * FROM {table}')
    print('models = ', models)
    for model in models:
        print('table = ', table)
        print('model = ', model)
        print('model.__dict__ = ', model.__dict__)


class category(models.Model):
    """Категории для женщин"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        """
        Этот метод используется по умолчанию для придания названия
        в отображение категории в админке.
        """
        return self.name

    class Meta:
        """Мета данные для отображения модели в админ панели"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Women(models.Model):
    """Модель для таблицы о женщинах"""
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    # cat = models.ForeignKey('category', on_delete=models.PROTECT)
    # title = models.CharField(max_length=255, verbose_name='sdfsdfsd')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    class Meta:
        """Мета данные для отображения модели в админ панели"""
        # Название для ед-числа
        verbose_name = 'Известные женщины'
        # Название для множ-числа
        verbose_name_plural = 'Известные женщины'
        # Как отсортированы записи
        ordering = ['time_create', 'title']
        # ordering = ['-time_create', '-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Модули Django используют этот методе если он определен в модели
        своего рода создание замены слага.
        """
        return reverse('post', kwargs={'post_id': self.pk})
