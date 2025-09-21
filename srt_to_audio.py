# -*- coding: utf-8 -*-

"""
Script para converter um arquivo de legenda SRT em um arquivo de áudio MP3 com voz masculina.

Dependências:
- edge-tts: para usar as vozes neurais da Microsoft Edge.
- pysrt: para analisar (parse) arquivos de legenda .srt.
- asyncio: para rodar a biblioteca edge-tts.

**IMPORTANTE**: Este script requer uma conexão ativa com a internet para funcionar.

Como usar:
python srt_to_audio.py <caminho_para_o_arquivo.srt>
"""

import sys
import os
import asyncio
import edge_tts
import pysrt
from tqdm import tqdm

# --- CONFIGURAÇÃO DA VOZ ---
# Escolha a voz masculina para o áudio.
# Outras opções para português do Brasil: "pt-BR-AntonioNeural"
VOICE = "pt-BR-FabioNeural"

async def main(caminho_arquivo_srt: str):
    """
    Função principal que lê o SRT e o converte para áudio.
    """
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.exists(caminho_arquivo_srt):
            print(f"Erro: O arquivo '{caminho_arquivo_srt}' não foi encontrado.")
            return

        print(f"Abrindo o arquivo de legenda: {caminho_arquivo_srt}")
        legendas = pysrt.open(caminho_arquivo_srt, encoding='utf-8')

        # Concatena todo o texto das legendas em uma única string
        texto_completo = " ".join(legenda.text.replace('\n', ' ').strip() for legenda in legendas)

        if not texto_completo:
            print("Aviso: O arquivo de legenda parece estar vazio.")
            return

        print(f"\nTexto extraído com sucesso. Usando a voz: {VOICE}")
        print("Iniciando a conversão para áudio (isso pode levar um tempo)...")
        
        caminho_base = os.path.splitext(caminho_arquivo_srt)[0]
        caminho_arquivo_mp3 = f"{caminho_base}.mp3"
        
        # Cria o objeto de comunicação com o serviço TTS
        communicate = edge_tts.Communicate(texto_completo, VOICE)

        # Salva o áudio no arquivo de saída
        # Como edge-tts não oferece um callback de progresso nativo para o save,
        # exibimos uma mensagem de que o processo está em andamento.
        await communicate.save(caminho_arquivo_mp3)

        print(f"\nConversão concluída! Áudio salvo em: {caminho_arquivo_mp3}")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado durante o processo: {e}")
        print("Verifique sua conexão com a internet e se o nome da voz está correto.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso incorreto.")
        print(f"Execute: python {sys.argv[0]} <caminho_para_o_arquivo.srt>")
        sys.exit(1)

    caminho_srt_fornecido = sys.argv[1].strip().strip("'\"")

    if not caminho_srt_fornecido.lower().endswith('.srt'):
        print(f"Erro: O arquivo '{caminho_srt_fornecido}' não é um arquivo .srt válido.")
        sys.exit(1)

    # Executa a função assíncrona 'main'
    asyncio.run(main(caminho_srt_fornecido))


