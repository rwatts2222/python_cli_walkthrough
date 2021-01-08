class Item:
    def __init__(self, item_id, name, condition):  # create function with 3 parameters. self is a keyword referring to itself -- the class of Item.
        self.item_id = item_id    # these 3 lines assign variables that reach into Item class and pull out id, name, condition
        self.name = name
        self.condition = condition
        
    def __str__(self): #  Double underscores prevents variable being used outside this function.
        return f"Id:{self.item_id}\tName:{self.name}\tCondition:{self.condition}"  # returns id, name, condition of Item.  \t tabs over.



if __name__== "__main__":  # if this is the main file, do something
    item_one = Item(0, "book", "used")
    item_two = Item(1, "water bottle", "new")

    print(item_one.item_id)  # testing our Item class
    print(item_two)