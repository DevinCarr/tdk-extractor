from catalog_parser import PartNumberParser

class MLCC_Commercial_General_Parser(PartNumberParser):
    def __init__(self, part_number):
        super().__init__(part_number)
        self.voltage_map = {
            '0G': 4.0,
            '0J': 6.3,
            '1A': 10.0,
            '1C': 16.0,
            '1E': 25.0,
            '1V': 35.0,
            '1H': 50.0,
            '1N': 75.0
        }

    @staticmethod
    def valid(part_number):
        return part_number[0] == 'C'

    def catalog(self):
        return 'mlcc commercial general'

    def catalog_link(self):
        return 'https://product.tdk.com/info/en/catalog/datasheets/mlcc_commercial_general_en.pdf'

    def series(self):
        return self.part_number[0]

    def capacitance(self):
        """Nominal Capacitance in μF"""
        cap_code = self.part_number[10:13]
        if len(self.part_number) == 18:
            cap_code = self.part_number[9:12]
        if cap_code[1] == 'R':
            return float(cap_code[0]) + (0.1 * float(cap_code[2])) * (10.0 ** -6)
        else: 
            return (float(cap_code[0]) * 10.0 + float(cap_code[1])) * (10.0 ** int(cap_code[2])) * (10.0 ** -6)

    def package(self):
        """Package dimensions"""
        return self.part_number[1:5]

    def voltage(self):
        """Rated Voltage (DC)"""
        if len(self.part_number) == 18:
            return self.voltage_map[self.part_number[7:9]]
        else:
            return self.voltage_map[self.part_number[8:10]]

    