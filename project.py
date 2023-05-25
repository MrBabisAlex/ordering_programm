import sqlite3
import sys
from tabulate import tabulate


def main():
    dicts = {}
    keys = ["Type", "Name", "Price"]
    values = []
    if len(sys.argv) != 2:
        sys.exit(
            'print("Usage project.py --insert, --delete, --update, --examine, --order")'
        )
    mode = sys.argv[1]

    match mode:
        case "insert":
            j = 0
            if len(sys.argv) == 2:
                for i in range(len(keys)):
                    data = input(f"Add {keys[j]}: ")
                    values.append(data)
                    dicts[keys[i]] = values[i]
                    j += 1
                insert_product(dicts["Type"], dicts["Name"], dicts["Price"])

        case "delete":
            if len(sys.argv) == 2 and sys.argv[1] == "delete":
                product = input("Enter product name to delete: ")
                delete_product(product)

        case "update":
            j = 0
            if len(sys.argv) == 2 and sys.argv[1] == "update":
                product = input("Product to update: ")
                if not product.isalpha():
                    sys.exit('Incorrect Value')
                for i in range(len(keys)):
                    data = input(f"Add {keys[j]}: ")
                    values.append(data)
                    dicts[keys[i]] = values[i]
                    j += 1
                update_product(product, dicts["Type"], dicts["Name"], dicts["Price"])

        case "examine":
            product = input("Enter Product to examine: ")
            product_list = see_product(product)
            if product_list == [] and product != "all":
                print("Product not in batabase")
            elif product == "all":
                menu = see_all_products()
                print(
                    tabulate(
                        menu, headers=["Type", "Name", "Price"], tablefmt="outline"
                    )
                )
            else:
                print(
                    tabulate(
                        product_list,
                        headers=["Type", "Name", "Price"],
                        tablefmt="outline",
                    )
                )

        case "order":
            give_order()

        case _:
            print("Command not recognized")
            print("Usage project.py --insert, --delete, --update")


def insert_product(food, name, price):
    try:
        if food.isalpha() and name.isalpha() and price.isdecimal():
            price = int(price)
            conn = sqlite3.connect("menu.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO products VALUES(?, ?, ?)", (food, name, price))
            conn.commit()
            conn.close()
        else:
            raise AttributeError
    except ValueError:
        sys.exit('Incorrect Value')


def delete_product(name):
    try:
        if name.isalpha():
            conn = sqlite3.connect("menu.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM products WHERE food = ?", (name,))
            conn.commit()
            conn.close()
        else:
            raise AttributeError
    except ValueError:
        sys.exit('Incorrect Value')



def update_product(food, new_food, new_name, new_price):
        try:
            if new_food.isalpha() and new_name.isalpha() and new_price.isdecimal():
                new_price = int(new_price)
                conn = sqlite3.connect("menu.db")
                cur = conn.cursor()
                cur.execute(
                    "UPDATE products SET food = ?, name = ?, price = ? WHERE food = ?",
                    (
                        new_food,
                        new_name,
                        new_price,
                        food,
                    ),
                )
                conn.commit()
                conn.close()
            else:
                raise AttributeError
        except ValueError:
            sys.exit('Incorrect Value')



def see_product(name):
    try:
        if name.isalpha():
            conn = sqlite3.connect("menu.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM products WHERE food = ?", (name,))
            product = cur.fetchall()
            conn.commit()
            conn.close()
            return product
        else:
            raise AttributeError
    except ValueError:
        sys.exit('Incorrect Value')


def see_all_products():
    conn = sqlite3.connect("menu.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    product = cur.fetchall()
    conn.commit()
    conn.close()
    return product


def give_order():
    print("Enter product or finish to exit!")
    order = []
    total = 0
    k = 0
    while True:
        product = input("Select product: ")
        order_product = see_product(product)
        if product == "finish":
            break
        elif order_product != []:
            quantity = input("Select Quantity: ")
            new_order = []
            for i in order_product:
                for j in i:
                    new_order.append(j)
            new_order.append(quantity)
            order.append(new_order)
            k += 1
            total += new_order[2] * int(quantity)
            continue
        else:
            print("Product not in list")
            continue
    print("Would you like to print the order?")
    answer = input("Y/N? ")
    answer = answer.upper().strip()
    if answer == "Y":
        print_order(order, total)
    else:
        print(
            tabulate(
                order,
                headers=["Type", "Name", "Price", "Quantity"],
                tablefmt="outline",
                numalign="left",
                showindex="always",
            )
        )
        print(f"total:  {total} $")


def print_order(order, total):
    with open("order.txt", "w") as file1:
        file1.writelines(
            tabulate(
                order,
                headers=["Type", "Name", "Price", "Quantity"],
                tablefmt="outline",
                numalign="left",
                showindex="always",
            )
        )
        file1.write("\n")
        file1.write(f"total:  {total} $")


if __name__ == "__main__":
    main()
