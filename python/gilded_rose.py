from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AbstractItem(ABC):
    def __init__(self, item: Item):
        self.item = item

    max_quality = 50
    min_quality = 0

    @abstractmethod
    def update_quality(self):
        pass

    def update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def decrease_quality_by(self, amount):
        if self.item.quality - amount < AbstractItem.min_quality:
            self.item.quality = AbstractItem.min_quality
        else:
            self.item.quality = self.item.quality - amount

    def increase_quality_by(self, amount):
        if self.item.quality + amount > AbstractItem.max_quality:
            self.item.quality = AbstractItem.max_quality
        else:
            self.item.quality = self.item.quality + amount


class NormalItem(AbstractItem):

    degrade_amount = 1

    def update_quality(self):
        if self.item.quality > AbstractItem.min_quality:
            if self.item.sell_in >= 0:
                self.decrease_quality_by(self.degrade_amount)
            else:
                self.decrease_quality_by(2 * self.degrade_amount)


class ConjuredItem(NormalItem):
    def __init__(self, item: Item):
        super().__init__(item)
        self.degrade_amount = 2


class SulfurasItem(AbstractItem):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class AgedBrieItem(AbstractItem):

    def update_quality(self):
        if self.item.quality < AbstractItem.max_quality:
            if self.item.sell_in >= 0:
                self.increase_quality_by(1)
            else:
                self.increase_quality_by(2)


class BackstagePassesItem(AbstractItem):

    def update_quality(self):
        if self.item.sell_in >= 0:
            if self.item.sell_in >= 10:
                self.increase_quality_by(1)
            elif self.item.sell_in >= 5:
                self.increase_quality_by(2)
            elif self.item.sell_in > 0:
                self.increase_quality_by(3)
            else:
                self.item.quality = AbstractItem.min_quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
