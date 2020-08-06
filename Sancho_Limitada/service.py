from models import ProductModel, ClientModel, BillModel


class ProductService:
    def __init__(self):
        self.model = ProductModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response

class ClientService:
    def __init__(self):
        self.model = ClientModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response

class BillService:
    def __init__(self):
        self.model = BillModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def list(self):
        response = self.model.list_items()
        return response