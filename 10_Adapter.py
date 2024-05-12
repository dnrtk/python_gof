class Customer:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def show_customer_info(self):
        print("[id: {}] name: {}\temails: {}".format(self.id, self.name, self.email))

def get_customer(id) -> Customer | None:
    for customer in customers:
        if customer.id == id:
            return customer
    return None

customers = list()
customers.append(Customer(1, "hitorime", "hitorime@example.com"))
customers.append(Customer(2, "hutarime", "hutarime@example.com"))


class JsonAdapter:
    def __init__(self, json_str: str):
        import json
        self.customers = json.loads(json_str)

    def get_customer(self, id) -> Customer | None:
        for customer in self.customers:
            if customer["id"] == id:
                return Customer(
                    customer.get("id", -1),
                    customer.get("name", ""),
                    customer.get("email", ""),
                )
        return None

json_str = """
    [
        {"id": 3, "name": "sanninme", "email": "sanninme@example.com"},
        {"id": 4, "name": "yoninme", "email": "yoninme@example.com"}
    ]
"""


if __name__ == "__main__":
    # 通常のデータ取得
    customer = get_customer(1)
    customer.show_customer_info()

    # Adapterを用いたJSONからのデータ取得
    json_adapter = JsonAdapter(json_str)
    customer = json_adapter.get_customer(3)
    customer.show_customer_info()
