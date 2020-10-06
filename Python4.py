class MenuItem:
    def info(self):
        return self.name+':￥'+str(self.price)

menu_item1=MenuItem()

menu_item1.name='サンドイッチ'
menu_item1.price=500

print(menu_item1.info())
menu_item1.info()


print(menu_item1.name)
print(menu_item1.price)


menu_item2=MenuItem()

menu_item2.name='チョコケーキ'
menu_item2.price=400

print(menu_item2.info())
menu_item2.info()

print(menu_item2.name)
print(menu_item2.price)
