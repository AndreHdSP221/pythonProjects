import qrcode
import os
import time

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

class qrCode:
    def __init__(self, codigo_Item, nomePasta):
        self.codigo_Item = codigo_Item
        self.nomePasta = nomePasta
    
    def gerarCodigo(self, qtd_qr_code):
        base_dir = os.path.abspath(__file__) 
        diretorio_script = os.path.dirname(base_dir)

        output_path = os.path.join(diretorio_script, self.nomePasta)
        os.makedirs(output_path, exist_ok=True)
        print(f"Salvando QRCodes em: {output_path}")

        codigo = f'{self.codigo_Item}-'

        for i in range(1, qtd_qr_code + 1):  # Adicionei +1 para incluir o último
            codigoQr = f"{codigo}{i:06d}"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(codigoQr)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            file_path = os.path.join(output_path, f"{codigoQr}.png")
            img.save(file_path)
            print(f"Salvo: {file_path}")
        
        print("\n\nProcesso finalizado!")
        time.sleep(2)
        clear()        
