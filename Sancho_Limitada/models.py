import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('sancho.db')
        self.create_productos_table()
        self.create_clientes_table()
        self.create_facturas_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_productos_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "productos" (
          codigo INTEGER PRIMARY KEY,
          categoria TEXT,
          nombre TEXT,
          precio INTEGER,
          cantidad INTEGER,
          estado boolean DEFAULT 0
        );
        """

        self.conn.execute(query)

    def create_clientes_table(self):

        query = """
                CREATE TABLE IF NOT EXISTS "clientes" (
                  cedula INTEGER PRIMARY KEY,
                  nombre TEXT,
                  direccion TEXT,
                  telefono INTEGER,
                  foto BLOB
                );
                """
        self.conn.execute(query)

    def create_facturas_table(self):
        query = """
                CREATE TABLE IF NOT EXISTS "facturas" (
                  codigo INTEGER PRIMARY KEY,
                  cliente INTEGER FOREIGNKEY REFERENCES clientes(cedula),
                  producto INTEGER FOREIGNKEY REFERENCES productos(codigo),
                  cantidad INTEGER,
                  fecha Date DEFAULT CURRENT_DATE,
                  valor_total INTEGER,
                  metodo_pago TEXT
                );
                """
        self.conn.execute(query)

class ProductModel:
    TABLENAME = "productos"

    def __init__(self):
        self.conn = sqlite3.connect('sancho.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND codigo={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print (params)
        query = f'insert into {self.TABLENAME} ' \
                f'(codigo, categoria, nombre, precio, cantidad) ' \
                f'values ("{params.get("codigo")}","{params.get("categoria")}",' \
                f'"{params.get("nombre")}","{params.get("precio")}","{params.get("cantidad")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"UPDATE {self.TABLENAME} " \
                f"SET estado =  {1} " \
                f"WHERE codigo = {item_id}"
        print (query)
        self.conn.execute(query)
        return self.list_items()

    def update(self, item_id, update_dict):
        """
        column: value
        cantidad: new cantidad
        """
        set_query = ", ".join([f'{column} = {value}'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE codigo = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT codigo, nombre, categoria, precio, cantidad, estado " \
                f"from {self.TABLENAME} WHERE estado != {1} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result

class ClientModel:
    TABLENAME = "clientes"

    def __init__(self):
        self.conn = sqlite3.connect('sancho.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND cedula={_id}"
        return self.list_items(where_clause)

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format to create a photo
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def create(self, params):
        print(params)
        foto = params.get("foto")
        empPhoto = self.convertToBinaryData(foto)
        query = f'insert into {self.TABLENAME} ' \
                f'(cedula, nombre, direccion, telefono, foto) ' \
                f'values ("{params.get("cedula")}","{params.get("nombre")}",' \
                f'"{params.get("direccion")}","{params.get("telefono")}","{empPhoto}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} " \
                f"WHERE cedula = {item_id}"
        print (query)
        self.conn.execute(query)
        return self.list_items()

    def update(self, item_id, update_dict):
        """
        column: value
        telefono: new telefono
        """
        set_query = ", ".join([f'{column} = {value}'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE cedula = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT cedula, nombre, direccion, telefono " \
                f"from {self.TABLENAME} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result


class BillModel:
    TABLENAME = "facturas"
    def __init__(self):
        self.conn = sqlite3.connect('sancho.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND codigo={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print(params)
        query = f'insert into {self.TABLENAME} ' \
                f'(codigo, cliente, producto, cantidad, valor_total, metodo_pago) ' \
                f'values ("{params.get("codigo")}","{params.get("cliente")}",' \
                f'"{params.get("producto")}","{params.get("cantidad")}","{params.get("valor_total")}", "{params.get("metodo_pago")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def update(self, item_id, update_dict):
        """
        column: value
        producto: new producto
        """
        set_query = ", ".join([f'{column} = {value}'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE codigo = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT codigo, cliente, producto, cantidad, valor_total, metodo_pago " \
                f"from {self.TABLENAME} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
