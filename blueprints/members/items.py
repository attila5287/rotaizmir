import numpy as np
import initFunctionsForClassItem 
from initFunctionsForClassItem import (randGen_itemState,
randGen_itemType,
randGen_itemBasePrice,
dictItemState_init,
dictItemType_init,
randGen_itemID,
labelMaker,
dictItemIcon_init,
randGen_itemIcon,
randGen_itemTitle
)
# description from another file
from descGenForClassItem import randGen_itemDesc


class Item:
    """ GENERATES HOUSE MARKET ITEMS WITH STATE, TYPE, BASE PRICE(RND0)-,ITEM ID AND PRICE-INDEX-LABEL(KEY FOR DB). CREATE AS AN OBJECT THUS WEB-INTERFACE WITH JINJA2,  
    AND UPLOADING TO MONGODB DATABASE THRU ITERABLE OBJS"""
    def __init__(self,
                 itemState='',
                 itemType='',
                 itemBasePrice='',
                 itemID='',
                 priceIndexLabel ='',
                 itemIconNo ='',
                 itemTitle='',
                 itemDesc='', 
                 **kwargs):
        super().__init__(**kwargs)
        self.itemState = randGen_itemState()
        self.itemType = randGen_itemType()
        self.itemBasePrice = randGen_itemBasePrice()
        self.itemID = randGen_itemID(self.itemState,self.itemType)
        self.priceIndexLabel = labelMaker(self.itemState,self.itemType)
        self.itemIconNo = randGen_itemIcon(self.itemType)
        self.itemTitle = randGen_itemTitle(self.itemType,self.itemState)
        self.itemDesc = randGen_itemDesc()
    
    def display(self):
        """ TESTING CODE LOCALLY BEFORE FLASK-HEROKU-APP
        PRINTS OUT ALL PROPERTIES BEING GENERATED
        """
        # print(" - $ - $  - # -REGROPOLY- # - $  - $ - ")
        print("itemState         | {}".format(self.itemState))
        print("itemType          | {}".format(self.itemType))
        print("itemBasePrice     | $ {:,.0f}".format(self.itemBasePrice))
        print("itemID            | {}".format(self.itemID))
        print("priceIndexLabel   | {}".format(self.priceIndexLabel))
        print("itemIconNo        | {}".format(self.itemIconNo[-7:]))
        print("itemTitle         | {}".format(self.itemTitle))
        print("itemDesc          | {}".format(self.itemDesc))
        print()
        return None
    
        

# ============================================================
# ============================================================
# ============================================================

# a = Item()
# a.display()
