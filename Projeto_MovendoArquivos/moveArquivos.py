import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

origem = r"E:\aOrigem"
destino = r"G:\nDestino"
log_path = r"C:\uDiretorioParaLogs" 

extensoes_imagem = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
    '.webp', '.heif', '.heic',
    '.raw', '.cr2', '.nef', '.arw', '.orf', '.rw2', '.sr2', '.dng', '.NEF'
}
extensoes_video = {
    '.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm',
    '.m4v', '.3gp', '.mts', '.m2ts', '.ts', '.vob', '.mpg', '.mpeg'
}
extensoes_midias = extensoes_imagem.union(extensoes_video)

os.makedirs(os.path.dirname(log_path), exist_ok=True)

with open(log_path, 'w', encoding='utf-8') as log_file:
    log_file.write(f"LOG DE TRANSFERÊNCIA - {datetime.now()}\n")
    log_file.write("-" * 60 + "\n")

def mover_arquivo(caminho_origem):
    try:
        if not os.path.isfile(caminho_origem):
            return

        ext = os.path.splitext(caminho_origem)[1].lower()
        if ext not in extensoes_midias:
            return

        caminho_relativo = os.path.relpath(os.path.dirname(caminho_origem), origem)
        destino_pasta = os.path.join(destino, caminho_relativo)

        os.makedirs(destino_pasta, exist_ok=True)

        nome_arquivo = os.path.basename(caminho_origem)
        caminho_destino = os.path.join(destino_pasta, nome_arquivo)

        base, ext_arquivo = os.path.splitext(nome_arquivo)
        contador = 1
        while os.path.exists(caminho_destino):
            caminho_destino = os.path.join(destino_pasta, f"{base}_{contador}{ext_arquivo}")
            contador += 1

        shutil.move(caminho_origem, caminho_destino)

        mensagem = f"[MOVIDO] {caminho_origem} -> {caminho_destino}"
        print(mensagem)
        with open(log_path, 'a', encoding='utf-8') as log_file:
            log_file.write(mensagem + '\n')

    except Exception as e:
        mensagem = f"[ERRO] {caminho_origem}: {e}"
        print(mensagem)
        with open(log_path, 'a', encoding='utf-8') as log_file:
            log_file.write(mensagem + '\n')

def remover_pastas_vazias(caminho):
    print("[LIMPANDO PASTAS VAZIAS]")
    for raiz, pastas, _ in os.walk(caminho, topdown=False):
        for pasta in pastas:
            pasta_completa = os.path.join(raiz, pasta)
            try:
                if not os.listdir(pasta_completa):
                    os.rmdir(pasta_completa)
                    mensagem = f"[REMOVIDA] Pasta vazia: {pasta_completa}"
                    print(mensagem)
                    with open(log_path, 'a', encoding='utf-8') as log_file:
                        log_file.write(mensagem + '\n')
            except Exception as e:
                mensagem = f"[ERRO] ao remover {pasta_completa}: {e}"
                print(mensagem)
                with open(log_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(mensagem + '\n')

def processar():
    print("[INICIANDO VARREDURA E TRANSFERÊNCIA]")
    arquivos_para_mover = []
    contador = 0

    for raiz, _, arquivos in os.walk(origem):
        for arquivo in arquivos:
            caminho = os.path.join(raiz, arquivo)
            arquivos_para_mover.append(caminho)

            contador += 1
            if contador % 500 == 0:
                print(f"[VARREDURA] {contador} arquivos verificados...")

    print(f"[TOTAL DE ARQUIVOS ANALISADOS]: {len(arquivos_para_mover)}")

    with ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(mover_arquivo, arquivos_para_mover)

    remover_pastas_vazias(origem)
    print("[PROCESSO CONCLUÍDO]")

processar()
