# Menu and ordering programm
>#### Video Demo:  <https://youtu.be/axpAujd-qtg>
>#### Description: My final project for *the CS50's indroduction to programming with Python* is a databased ordering system in which the user can organise the menu of a shop and also print orders

---

## Table of contents:
+ Introduction
+ Technologies
+ Installation
+ Usage
+ Roadmap
+ Room for Improvement

---

## Introduction:
As my final project i choose to create a simple ordering system, in order to make use of the technologies and also the topics included in this course.

---

## Technologies:
+ sqlite3
+ tabulate

---

## Installation:
When i started this project i had to install tabulate library from [HERE](https://pypi.org/project/tabulate/)

---

## Usage:
The Usage is pretty straight forward. The user has 5 options 'insert, delete, update, examine and order'. If the user selects the examine option he is able to examine either one element or every element on database by entering the word 'all'. After order is selected the user is able to output a txt file saved in current location simply by entering 'Y' when he's prompted.

---

## Roadmap:
Before i start my project i draw exactly what i wanted on paper. I decided what the project is all about, how it would work and how many functions should be made. After that my first concerne was to create the actual database. The first 3 options handle the database part of the code where the user is able to insert,update or delete a product.

```
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

```

The 2 other options help the user to take an order or examine a product

```
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

```

## Room for Improvement:

  + Future ideas for my project:
    + add a user table on database to give admin access to users

  + TODO
    + add date and time to orders
    + add history

## Acknowledgment

Special thanks to professor Davis J. Malan, Doug Loyd, Brian Yu and everyone on CS50 staff who made this awesome course available for everyone

