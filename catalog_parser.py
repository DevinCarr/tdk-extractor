class PartNumberParser:
    def __init__(self, part_number):
        self.part_number = part_number

    def link(self):
        return 'https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=' + self.part_number

    def catalog(self):
        return None

    def catalog_link(self):
        return None

    def series(self):
        return None
    
    def row_output(self):
        return [self.link(), self.part_number, str(self.capacitance()), str(self.package()), str(self.voltage())]

    def capacitance(self):
        return None

    def package(self):
        return None

    def voltage(self):
        return None