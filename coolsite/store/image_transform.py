from PIL import Image
import os


def create_small_img(Model, size=500):
    """
    Создание минифицированной версии изображения.

    Если изображение больше указанного size то пропорционально
    сжимаем картинку, если картинка не больше указанного предела,
    то обе ссылки будут вести на одно изображение.
    """

    img = Image.open(Model.image.path)

    if img.height > size or img.width > size:
        img.thumbnail((size, size))
        img.save(Model.get_path_to_small_photo() + os.path.basename(Model.image.path))
        Model.min_image = "{0}{1}".format(Model.SMALL_IMG_PATH, os.path.basename(Model.image.path))
    else:
        Model.min_image = Model.image
