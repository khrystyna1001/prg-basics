shopping_list = 'shopping_list.txt'

def add_product(file_name, product_name):
    with open(file_name,'a') as content:
        content.write(product_name)
        content.write(' ')

product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break 
    else:
        add_product(shopping_list, product)