class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, galon):
        if str(galon.idGalon) not in self.carrito.keys():
            self.carrito[str(galon.idGalon)] = {
                "idGalon": str(galon.idGalon),
                "marca": galon.marca.nombreMarca,  # Usar nombreMarca
                "cantidad": 1,
                "precio": str(galon.precio),
                "total": galon.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == str(galon.idGalon):
                    value["cantidad"] += 1
                    value["total"] += galon.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, galon):
        id = str(galon.idGalon)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, galon):
        for key, value in self.carrito.items():
            if key == str(galon.idGalon):
                value["cantidad"] -= 1
                value["total"] -= galon.precio
                if value["cantidad"] < 1:
                    self.eliminar(galon)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}