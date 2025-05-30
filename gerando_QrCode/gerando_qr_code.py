import qrcode
import os

base_dir = os.path.abspath(__file__)
diretorio_script = os.path.dirname(base_dir)

output_subdir_nome = "qrcodes_gerados"
output_path = os.path.join(diretorio_script, output_subdir_nome)

os.makedirs(output_path, exist_ok=True)
print(f"Salvando QRCodes em: {output_path}")

for i in range(1, 64):
    codigoQr = f"OVT-4114906-{i:06d}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(codigoQr)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join(output_path, f"{codigoQr}.png") # Salva no subdiretório
    img.save(file_path)
    print(f"Salvo: {file_path}")

for i in range(1, 64): 
    codigoQr = f"OVT-4112108-{i:06d}"

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

print("Processo concluído!")