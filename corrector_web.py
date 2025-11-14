import gradio as gr
from spellchecker import SpellChecker

# Configurar SpellChecker para português europeu
spell = SpellChecker(language='pt')

# Palavras do português pré-1990
pre_1990_custom = {
    'facto', 'acto', 'óptimo', 'óptica', 'acção', 'educaçao', 'idéia'
}
spell.word_frequency.load_words(pre_1990_custom)

def corrigir_texto(texto):
    palavras = texto.split()
    resultado = ""

    for palavra in palavras:
        cor = "green"
        sugestao = ""
        # Se a palavra estiver errada
        if palavra.lower() not in spell and palavra.lower() not in pre_1990_custom:
            cor = "red"
            sugestao = f" (sugestão: {spell.correction(palavra)})"
        resultado += f'<span style="color:{cor}">{palavra}{sugestao}</span> '

    return resultado

# Criar interface Gradio
iface = gr.Interface(
    fn=corrigir_texto,
    inputs=gr.Textbox(lines=15, placeholder="Cole aqui o seu texto..."),
    outputs=gr.HTML(),
    title="Corrector Ortográfico Português Europeu (pré-1990)",
    description="Erros aparecem a vermelho com sugestão; palavras corretas a verde."
)

iface.launch()
