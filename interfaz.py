##----------------------------------------IMPORTS------------------------------------------------------
import chatbot as bot
import gradio as gr

#----------------------------------------VARIABLES------------------------------------------------------


#----------------------------------------FUNCIONES------------------------------------------------------


#----------------------------------------PROGRAMA------------------------------------------------------
bot.respuestas()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")