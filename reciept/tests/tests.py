from django.test import TestCase

from reciept.models import *


# Create your tests here.
class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(value=20, type='percent', max_price='10000')
        self.discount2 = Discount.objects.create(value=5000, type='price', max_price='10000')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')
        self.off_code1 = Off_code.objects.create(off_code=5)
        self.orders1 = Order.objects.create(name="pitzza", price=10000, discount=self.discount1)
        self.orders2 = Order.objects.create(name="pitzza2", price=20000, discount=self.discount2)
        self.receipt1 = Receipt.objects.create(orders=self.orders1, price_all=self.orders1.profit_value(),
                                               discount_all=self.off_code1)
        self.receipt2 = Receipt.objects.create(orders=self.orders2, price_all=self.orders2.profit_value(),
                                               discount_all=self.off_code1)

    def test1_profit_price10000(self):
        self.assertEqual(self.orders1.profit_value(), 2000)
        self.assertEqual(self.receipt1.price_end(), 100)

    def test1_profit_price2000(self):
        self.assertEqual(self.orders2.profit_value(), 15000)
        self.assertEqual(self.receipt2.price_end(), 750)
