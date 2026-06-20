# -*- coding: utf-8 -*-
"""CodeAlpha Task 1 """



import gradio as gr
from deep_translator import GoogleTranslator


langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
language_names = [lang.capitalize() for lang in langs_dict.keys()]

# 2. Translation logic (The Engine)
def translate_text(text, source_lang, target_lang):
    if not text.strip():
        return "⚠️ Please enter some text to translate."

    try:

        src = "auto" if source_lang == "Auto Detect" else source_lang.lower()
        tgt = target_lang.lower()

        # Translation process
        translator = GoogleTranslator(source=src, target=tgt)
        result = translator.translate(text)
        return result

    except Exception as e:
        return f"❌ Translation Error: {str(e)}"

# 3. Gradio Interface (The UI)
source_options = ["Auto Detect"] + language_names

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌍 Universal AI Translator")
    gr.Markdown("Translate your text instantly into over 100 languages!")

    with gr.Row():
        # Left Side: Input
        with gr.Column():
            source_language = gr.Dropdown(choices=source_options, value="Auto Detect", label="Source Language")
            input_text = gr.Textbox(lines=5, placeholder="Type your text here...", label="Text to Translate")
            translate_btn = gr.Button("Translate ✨", variant="primary")

        # Right Side: Output
        with gr.Column():
            target_language = gr.Dropdown(choices=language_names, value="Tamil", label="Target Language")
            output_text = gr.Textbox(lines=5, label="Translated Text", interactive=False)

    # Button click event
    translate_btn.click(
        fn=translate_text,
        inputs=[input_text, source_language, target_language],
        outputs=output_text
    )

demo.launch(share=True)