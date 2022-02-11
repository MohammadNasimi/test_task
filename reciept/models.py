from django.db import models


class Discount(models.Model):
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    max_price = models.IntegerField(null=True)
    value = models.PositiveIntegerField(null=False)


class Off_code(models.Model):
    off_code = models.IntegerField()


class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT)

    def profit_value(self):
        if self.discount.type == 'price':
            return min(self.price, abs(self.discount.value - self.price))
        else:  # percent
            raw_profit = int((self.discount.value / 100) * self.price)
            return int(min(raw_profit, int(self.discount.max_price))) if self.discount.max_price else raw_profit


class Receipt(models.Model):
    orders = models.ForeignKey(Order, on_delete=models.RESTRICT)
    price_all = models.PositiveIntegerField()
    discount_all = models.ForeignKey(Off_code, on_delete=models.RESTRICT)

    def price_end(self):
        return int((self.discount_all.off_code / 100) * self.price_all)
