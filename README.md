# nnip-assignment
In this assignment, I extracted the logic inside update_quality() method and introduced an Abstract class named **AbstractItem**
and also implemented that class with:

- NormalItem
- ConjuredItem
- SulfurasItem
- AgedBrieItem
- BackstagePassesItem

So regarding open-close principle, this new design enables us to easily add or remove a type of item from our code.
Also, we are now able to change the logic of one item of the code without making side effect on other items.
