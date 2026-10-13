from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


output = Path(__file__).with_name("resumo_projeto_facul.pdf")
repository_url = "https://github.com/Lavoyer/Facul.git"

with PdfPages(output) as pdf:
    figure = plt.figure(figsize=(8.27, 11.69), facecolor="#f7f4ee")
    figure.text(
        0.10,
        0.90,
        "Sistematiza\u00e7\u00e3o - M\u00e9todos Matem\u00e1ticos",
        fontsize=23,
        fontweight="bold",
        color="#17324d",
    )
    figure.text(
        0.10,
        0.855,
        "Do sinal ao espectro: um analisador e filtro de sinais",
        fontsize=13,
        color="#9a4d2d",
    )
    figure.text(0.10, 0.78, "Reposit\u00f3rio Git", fontsize=11, fontweight="bold", color="#17324d")
    figure.text(
        0.10,
        0.745,
        repository_url,
        fontsize=11,
        color="#1769aa",
        url=repository_url,
    )
    figure.text(0.10, 0.65, "Resumo", fontsize=15, fontweight="bold", color="#17324d")
    summary = (
        "Este projeto aplica ferramentas de M\u00e9todos Matem\u00e1ticos ao processamento\n"
        "de um acorde musical L\u00e1 maior (A3 + C#4 + E4), contaminado por um zumbido\n"
        "de rede de 60 Hz e por ru\u00eddo branco. O notebook acompanha a transforma\u00e7\u00e3o\n"
        "do sinal no dom\u00ednio do tempo para sua representa\u00e7\u00e3o espectral e retorna\n"
        "ao dom\u00ednio do tempo depois da filtragem."
    )
    figure.text(0.10, 0.59, summary, fontsize=11, color="#252525", linespacing=1.65)
    figure.text(0.10, 0.43, "Etapas principais", fontsize=15, fontweight="bold", color="#17324d")
    stages = (
        "1. S\u00e9rie de Fourier: aproxima\u00e7\u00e3o de uma onda quadrada e observa\u00e7\u00e3o do fen\u00f4meno de Gibbs.\n"
        "2. FFT e espectro: identifica\u00e7\u00e3o das componentes de frequ\u00eancia do acorde e dos ru\u00eddos.\n"
        "3. Filtragem: aplica\u00e7\u00e3o de filtros e FFT inversa para recuperar um sinal mais limpo.\n"
        "4. Laplace: estudo de H(s), polos e zeros para interpretar o comportamento dos filtros."
    )
    figure.text(0.10, 0.35, stages, fontsize=10.5, color="#252525", linespacing=1.8)
    figure.text(0.10, 0.17, "Tecnologias: Python, NumPy, SciPy, Matplotlib, Pandas e SymPy.", fontsize=10, color="#555555")
    figure.text(0.10, 0.12, "Arquivos de áudio e notebook estão disponíveis no repositório.", fontsize=10, color="#555555")
    figure.text(0.10, 0.06, "Gerado em 13/10/2026", fontsize=8.5, color="#777777")
    pdf.savefig(figure, bbox_inches="tight")
    plt.close(figure)

print(output)