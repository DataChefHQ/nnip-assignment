# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):
    #  Normal Item
    def test_normal_udp_quality_with_q_gt_0(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=1, quality=20))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 19,
                          "For Normal Item, with positive sell_in, quality must decreases by one")

    def test_normal_upd_quality_with_q_eq_0(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=1, quality=0))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 0,
                          "For Normal Item, with positive sell_in, with zero quality, quality must not change")

    def test_normal_udp_quality_with_s_eq_0(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=0, quality=1))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 0,
                          "For Normal Item, with zero sell_in, quality must decreases by one")

    def test_normal_upd_quality_with_s_lt_0(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=-1, quality=4))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 2,
                          "For Normal Item, with negative sell_in, quality must decreases by two")

    def test_normal_upd_quality_with_s_lt_0_q_boarder(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=-1, quality=1))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 0,
                          "For Normal Item, with negative sell_in, with quality less that 2, "
                          "quality must decreases to zero")

    def test_normal_upd_quality_with_s_lt_0_q_0(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=-1, quality=0))
        normal_item.update_quality()
        self.assertEquals(normal_item.item.quality, 0,
                          "For Normal Item, with negative sell_in, with quality equal to zero, "
                          "quality must not change")

    def test_normal_upd_sell_in(self):
        normal_item = NormalItem(Item(name="+5 Dexterity Vest", sell_in=10, quality=20))
        normal_item.update_sell_in()
        self.assertEquals(normal_item.item.sell_in, 9, "For Normal Item, update sell_in must decrease sell_in by one")

    # Sulfuras Item
    def test_sulfuras_udp_quality_with_s_gt_0(self):
        sulfuras_item = SulfurasItem(Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80))
        sulfuras_item.update_sell_in()
        sulfuras_item.update_quality()
        self.assertEquals(sulfuras_item.item.sell_in, 1, "For Sulfuras Item, sell_in must not change")
        self.assertEquals(sulfuras_item.item.quality, 80, "For Sulfuras Item, quality must be equal to 80")

    def test_sulfuras_udp_quality_with_s_eq_0(self):
        sulfuras_item = SulfurasItem(Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80))
        sulfuras_item.update_sell_in()
        sulfuras_item.update_quality()
        self.assertEquals(sulfuras_item.item.sell_in, 0, "For Sulfuras Item, sell_in must not change")
        self.assertEquals(sulfuras_item.item.quality, 80, "For Sulfuras Item, quality must be equal to 80")

    def test_sulfuras_udp_quality_with_s_lt_0(self):
        sulfuras_item = SulfurasItem(Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80))
        sulfuras_item.update_sell_in()
        sulfuras_item.update_quality()
        self.assertEquals(sulfuras_item.item.sell_in, -1, "For Sulfuras Item, sell_in must not change")
        self.assertEquals(sulfuras_item.item.quality, 80, "For Sulfuras Item, quality must be equal to 80")

    #  Conjured Item
    def test_conjured_udp_quality_with_q_gt_0(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=1, quality=20))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 18,
                          "For Conjured Item, with positive sell_in, quality must decreases by two")

    def test_conjured_upd_quality_with_q_eq_0(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=1, quality=0))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 0,
                          "For Conjured Item, with positive sell_in, with zero quality, quality must not change")

    def test_conjured_udp_quality_with_s_eq_0(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=0, quality=2))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 0,
                          "For Conjured Item, with zero sell_in, quality must decreases by two")

    def test_conjured_upd_quality_with_s_lt_0(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=-1, quality=6))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 2,
                          "For Conjured Item, with negative sell_in, quality must decreases by four")

    def test_conjured_upd_quality_with_s_lt_0_q_boarder(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=-1, quality=1))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 0,
                          "For Conjured Item, with negative sell_in, with quality less that 2, "
                          "quality must decreases to zero")

    def test_conjured_upd_quality_with_s_lt_0_q_0(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=-1, quality=0))
        conjured_item.update_quality()
        self.assertEquals(conjured_item.item.quality, 0,
                          "For Conjured Item, with negative sell_in, with quality equal to zero, "
                          "quality must not change")

    def test_conjured_upd_sell_in(self):
        conjured_item = ConjuredItem(Item(name="Conjured Mana Cake", sell_in=10, quality=20))
        conjured_item.update_sell_in()
        self.assertEquals(conjured_item.item.sell_in, 9, "For Conjured Item, "
                                                         "update sell_in must decrease sell_in by one")

    #  AgedBrie Item
    def test_aged_brie_udp_quality_with_qs_gt_0(self):
        aged_brie_item = AgedBrieItem(Item(name="Aged Brie", sell_in=2, quality=0))
        aged_brie_item.update_quality()
        self.assertEquals(aged_brie_item.item.quality, 1,
                          "For AgedBrie Item, with positive sell_in, quality must increase by one")

    def test_aged_brie_udp_quality_with_s_eq_0(self):
        aged_brie_item = AgedBrieItem(Item(name="Aged Brie", sell_in=0, quality=0))
        aged_brie_item.update_quality()
        self.assertEquals(aged_brie_item.item.quality, 1,
                          "For AgedBrie Item, with zero sell_in, quality must increase by one")

    def test_aged_brie_udp_quality_with_s_lt_0(self):
        aged_brie_item = AgedBrieItem(Item(name="Aged Brie", sell_in=-1, quality=0))
        aged_brie_item.update_quality()
        self.assertEquals(aged_brie_item.item.quality, 2,
                          "For AgedBrie Item, with zero sell_in, quality must increase by two")


if __name__ == '__main__':
    unittest.main()
