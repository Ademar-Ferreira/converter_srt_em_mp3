# Conversor de Legendas SRT para Áudio 🎧

Este é um script em Python que converte arquivos de legenda no formato .srt para arquivos de áudio .mp3. O projeto utiliza o serviço de conversão de texto em fala (TTS) da Microsoft Edge, que oferece vozes neurais de alta qualidade e som natural.

✨ Recursos
- Conversão Simples: Transforma um arquivo .srt completo em um único áudio .mp3
- Vozes de Alta Qualidade: Utiliza vozes neurais realistas (a voz masculina "Fábio" é o padrão)
- Interface de Linha de Comando: Fácil de usar através de qualquer terminal
- Customizável: A voz pode ser facilmente alterada editando uma única linha no script

⚙️ Pré-requisitos
Antes de começar, garanta que você tenha os seguintes itens instalados em seu sistema:
- Python 3.7+
- Uma conexão ativa com a internet, pois o script se conecta ao serviço da Microsoft para gerar o áudio

🚀 Como Usar

1. Clone o Repositório
Primeiro, clone este repositório para a sua máquina usando o comando git clone.

2. Instale as Dependências
Instale as bibliotecas Python necessárias com o seguinte comando:
pip install edge-tts pysrt tqdm

3. Execute o Script
Agora você está pronto para converter suas legendas! Execute o script srt_to_audio.py passando o caminho do seu arquivo .srt como argumento.

Exemplo de uso:
python srt_to_audio.py "C:\Users\SeuNome\Downloads\minha-legenda.srt"

O arquivo de áudio (.mp3) será gerado e salvo no mesmo diretório do arquivo de legenda original.

🎛️ Como Customizar a Voz
Você pode facilmente alterar a voz usada na narração:

1. Abra o arquivo srt_to_audio.py em um editor de código ou texto
2. Encontre a variável VOICE no topo do arquivo:

# --- CONFIGURAÇÃO DA VOZ ---
# Escolha a voz masculina para o áudio.
# Outras opções para português do Brasil: "pt-BR-AntonioNeural"
VOICE = "pt-BR-FabioNeural"

3. Altere o valor da variável VOICE para qualquer outra voz suportada. Por exemplo, para usar a voz feminina "Francisca", troque para:
VOICE = "pt-BR-FranciscaNeural"

Para ver a lista completa de vozes disponíveis, consulte a documentação oficial de vozes da Microsoft.