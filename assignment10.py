class ShoppingCart():
    def __init__(self,Product_Name,Quantity,Price):
        self.Product_Name=Product_Name
        self.Quantity=Quantity
        self.Price=Price

    def TotalCost(self):
        return self.Quantity * self.Price

    def DisplayBill(self):
        print("----- Shopping Bill -----")
        print("Product Name:", self.Product_Name)
        print("Quantity:", self.Quantity)
        print("Price per Item:", self.Price)
        print("Total Cost:", self.TotalCost())

c =ShoppingCart("laptop",2,50000)
c.DisplayBill()

    