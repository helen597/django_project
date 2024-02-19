from django.core.management import BaseCommand
import json

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('data.json', 'r') as f:
            categories = json.load(f)

        categories_to_create = []
        for category in categories:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)

        products_list = [
            {'name': 'Intel Core i5 11400F', 'description': 'Ядро: Rocket Lake, Частота: 2.6 ГГц и 4.4 в режиме Turbo, Сокет: LGA 1200, Число ядер: 6, потоков 12, Тепловыделение: 65 Вт, Техпроцесс: 14 нм, Встроенное графическое ядро: отсутствует', 'category': 1, 'price': 11990},
            {'name': 'Жесткий диск Seagate Barracuda ST1000DM014',
             'description': 'Объём: 1024 ГБ, Скорость вращения: 7200 об/мин, Буферная память: 64 МБ',
             'category': 2, 'price': 6190},
            {'name': 'SSD накопитель Kingston A400 SA400S37/480G',
             'description': 'Объем накопителя 480 ГБ, Скорости чтения до 500 МБ/с, записи до 450 МБ/с, Интерфейс SATA III, Тип памяти 3D',
             'category': 2, 'price': 3690},
            {'name': 'Оперативная память AMD Radeon R7 Performance Series R748G2606U2S-U DDR4 - 8ГБ',
             'description': 'Объем 8 ГБ, Частота 2666 МГц, Латентность CL16, Тайминги 16-18-18-35, Форм-фактор DIMM, 288-pin',
             'category': 3, 'price': 1490},
            {'name': 'Видеокарта GIGABYTE NVIDIA GeForce RTX 3060',
             'description': 'Память 12 ГБ GDDR6, 15000 МГц; 192 bit, Интерфейс PCI-E 4.0, Разъемы Display Port х 2, HDMI х 2',
             'category': 4, 'price': 41140},
            {'name': 'Видеокарта PowerColor AMD Radeon RX 550',
             'description': 'Память 4 ГБ GDDR5, 6000 МГц; 128 bit, Интерфейс PCI-E 3.0, Разъемы Display Port х 1, HDMI х 1, DVI х 1',
             'category': 4, 'price': 10780},
            {'name': 'Блок питания Aerocool VX PLUS 500W',
             'description': 'Разъемы MB 20+4 pin, CPU 4+4 pin, видеокарта 6+2 pin, SATA 3 шт, Molex 3 шт',
             'category': 5, 'price': 2770},
            {'name': 'Блок питания GMNG GG-PS850M',
             'description': 'Разъемы MB 20+4 pin, CPU 2x(4+4) pin, видеокарта 4х(6+2) + 16 pin, SATA 9 шт, Molex 3 шт',
             'category': 5, 'price': 9790}
        ]
