import os
import math

class BarcodeLabelGenerator:
    def __init__(self):
        self.eans_and_skus = []

    def get_user_input(self):
        while True:
            ean = input("Digite o código EAN (ou 'sair' para terminar): ")
            if ean.lower() == 'sair':
                break
            sku = input("Digite o SKU para o código EAN: ")
            quantity = int(input("Digite a quantidade de etiquetas a serem geradas: "))
            self.eans_and_skus.append((ean, sku, quantity))

    def generate_zpl(self):
        zpl = "^XA^CI28\n"

        x_offset = 50  # Posição inicial no eixo X
        y_offset = 50  # Posição inicial no eixo Y
        width = 400    # Largura de cada etiqueta
        height = 200   # Altura de cada etiqueta

        max_columns = 2

        for ean, sku, quantity in self.eans_and_skus:
            for i in range(quantity):
                zpl += f"""
                ^LH{x_offset},{y_offset}
                ^FO50,20^BY2,,80^BEN,80,Y,N^FD{ean}^FS
                ^FO22,130^A0N,25,25^FDSKU: {sku}^FS
                """
                x_offset += width
                if x_offset >= width * max_columns + 50:
                    x_offset = 50
                    y_offset += height

        zpl += "^XZ"
        return zpl

    def print_zpl(self, zpl_code):
        print("ZPL Gerado:")
        print(zpl_code)

        zpl_file_path = "output.zpl"
        with open(zpl_file_path, "w") as zpl_file:
            zpl_file.write(zpl_code)
        print(f"Arquivo ZPL salvo em {zpl_file_path}")

def main():
    generator = BarcodeLabelGenerator()
    generator.get_user_input()
    zpl_code = generator.generate_zpl()
    generator.print_zpl(zpl_code)


if __name__ == "__main__":
    main()
