def get_categories():
    return [{
        "id" : 1,
        "name" : "Mobile"
    },
    {
        "id": 2,
       "name": "Tablet"
        },
    {
            "id": 3,
            "name": "Laptop"
    }
    ]

def get_product(kw):
    pr = [{
        "id" : 1,
        "name": "Iphone 13",
        "price": 20000000,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoAESZE9KxrvCLQ_gbzI27ii-YCwCyOXTJc8uAnQP7f2VMC4XSWqYZIDKiiwPSqO7jgIU&usqp=CAU"
    },
    {
        "id": 2,
        "name": "Iphone 13",
        "price": 25000000,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoAESZE9KxrvCLQ_gbzI27ii-YCwCyOXTJc8uAnQP7f2VMC4XSWqYZIDKiiwPSqO7jgIU&usqp=CAU"
    },
    {
        "id": 3,
        "name": "Samsung galaxy A3",
        "price": 25000000,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoAESZE9KxrvCLQ_gbzI27ii-YCwCyOXTJc8uAnQP7f2VMC4XSWqYZIDKiiwPSqO7jgIU&usqp=CAU"
    }
    ]
    if kw:
        pr = [p for p in pr if p['name'].find(kw) >=0]
    return pr