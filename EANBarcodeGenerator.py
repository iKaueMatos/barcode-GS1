import random
import os
from zipfile import ZipFile
from openpyxl import Workbook

class EANBarcodeGenerator:
    def __init__(self, company_code: str = None, product_code_length: int = 4):
        if company_code is None or not company_code.isdigit() or len(company_code) not in range(4, 8):
            raise ValueError("For EAN-13, the company code must be a numeric string with 4 to 7 digits.")
        self.company_code = company_code
        self.product_code_length = product_code_length
        self.prefix = "789"

    def generate_random_code(self, length: int = 12) -> str:
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

    def calculate_checksum(self, code: str) -> int:
        odd_sum = sum(int(code[i]) for i in range(0, 12, 2))
        even_sum = sum(int(code[i]) for i in range(1, 12, 2))
        total = odd_sum + even_sum * 3
        checksum = (10 - (total % 10)) % 10
        return checksum

    def generate_zpl(self, barcode_data: str, file_path: str) -> None:
        zpl_data = f"^XA\n^FO50,50^BY3\n^BCN,100,Y,N,N\n^FD{barcode_data}^FS\n^XZ"
        with open(file_path, "w") as zpl_file:
            zpl_file.write(zpl_data)

    def generate_barcode(self, generated_codes: set) -> str:
        while True:
            product_code = self.generate_random_code(self.product_code_length)
            partial_code = self.prefix + self.company_code + product_code
            full_code = partial_code + str(self.calculate_checksum(partial_code))

            if full_code not in generated_codes:
                generated_codes.add(full_code)
                return full_code

if __name__ == "__main__":
    try:
        company_code = "12345" # codigo que pode ser fornecido por meio de um registro na GS1 brasil
        product_code_length = 4
        output_dir = "barcodes"
        os.makedirs(output_dir, exist_ok=True)
        zip_file_path = "ean.zip"
        excel_file_path = os.path.join(output_dir, "ean.xlsx")

        generated_codes = set()

        wb = Workbook()
        ws = wb.active
        ws.title = "EAN Codes"
        ws.append(["Index", "EAN Code"])

        with ZipFile(zip_file_path, "w") as zipf:
            for i in range(2000):
                generator = EANBarcodeGenerator(company_code=company_code, product_code_length=product_code_length)
                full_code = generator.generate_barcode(generated_codes)

                zpl_filename = f"{full_code}.zpl"
                zpl_path = os.path.join(output_dir, zpl_filename)

                generator.generate_zpl(full_code, zpl_path)

                if os.path.exists(zpl_path):
                    zipf.write(zpl_path, os.path.basename(zpl_path))

                ws.append([i + 1, full_code])

        wb.save(excel_file_path)

        if os.path.exists(excel_file_path):
            zipf.write(excel_file_path, os.path.basename(excel_file_path))

        print(f"Generated 2000 ZPL files and saved them in {zip_file_path} and {excel_file_path}")
    except ValueError as e:
        print("Error:", e)
