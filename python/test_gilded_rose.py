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


if __name__ == '__main__':
    unittest.main()
