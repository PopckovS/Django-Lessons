from django.contrib.auth.models import User
from django.db import models

from coolsite.settings import MEDIA_ROOT
from store.image_transform import create_small_img


class Book(models.Model):
    BIG_IMG_PATH = "photos/store/big/"
    SMALL_IMG_PATH = "photos/store/small/"

    owner = models.ForeignKey(User, default=True, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    big_photo = models.ImageField(upload_to=BIG_IMG_PATH, verbose_name='Большое Фото')
    small_photo = models.ImageField(upload_to=SMALL_IMG_PATH, default=' ', verbose_name='Маленькое Фото')

    def __str__(self):
        return f'Id {self.id}:  {self.name}'

    def get_big_photo_path(self):
        return self.big_photo.path

    def get_small_photo_path(self):
        return self.big_photo.path

    def save(self, *args, **kwargs):
        """Сохраняем модель, генерируем минифицированнцю версию изображения"""
        super().save(*args, **kwargs)
        # create_small_img(self, 500)
        # super().save()

    def get_path_to_small_photo(self):
        """Путь к директории минифицированной версии картинки"""
        return "{0}/{1}".format(MEDIA_ROOT, self.SMALL_IMG_PATH)




# # TODO НИГДЕ НЕ ИСПОЛЬЗУЕТСЯ ! ПРОСТО ДЛЯ ПРИМЕРА
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to="photos/store/new/")
#
#     def __str__(self):
#         return f'Profile {self.user.username}'
#
#     def show_path(self):
#         return self.image.path
#
#     def save_old(self):
#         super().save()
#         img = Image.open(self.image.path)
#
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#








# import PIL
# from PIL import Image
# from imagekit.models.fields import ImageSpecField
# from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
#
#
# class Jobseeker(models.Model):
#     def get_file_path(self, filename):
#         extension = filename.split('.')[-1]
#         filename = "%s.%s" % (uuid.uuid4(), extension)
#         return os.path.join("images", filename)
#
#         photo = models.ImageField(verbose_name=u'Poster',upload_to=get_file_path,max_length=256, blank=True, null=True)
#         photo_small =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(50, 50)], image_field='photo', format='JPEG', options={'quality': 90})
#         photo_medium =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(300, 200)], image_field='photo', format='JPEG', options={'quality': 90})
#         photo_big = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(640, 480)], image_field='photo', format='JPEG', options={'quality': 90})
#

