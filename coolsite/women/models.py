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
    # Тут же можно и использовать функции БД в запросах
    # models = category.objects.raw(f'SELECT * FROM {table}')
    id = 1
    # models = category.objects.raw('SELECT * FROM  women_women WHERE id = %s', [id])
    # models = category.objects.raw('SELECT * FROM  women_women WHERE id = %(id)s', {'id': id})
    # models = category.objects.raw("SELECT * FROM %(table)s", {'table': table})
    for model in models:
        print('table = ', table)
        print('model = ', model)
        print('model.__dict__ = ', model.__dict__)
        # print('model.name = ', model.name)
        # print('model.pk = ', model.pk)
        print('=========================')


class category(models.Model):
    """Категории для женщин"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')

    def __str__(self):
        """
        Этот метод используется по умолчанию для придания названия
        в отображение категории в админке.
        """
        return self.name


class Women(models.Model):
    """Модель для таблицы о женщинах"""
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    # cat = models.ForeignKey('category', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     cat = self.cat  # self.value is a model field.
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Модули Django используют этот методе если он определен в модели
        своего рода создание замены слага.
        """
        return reverse('post', kwargs={'post_id': self.pk})
