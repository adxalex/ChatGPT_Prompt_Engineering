from openai import OpenAI
from config import api_key
import panel as pn  # GUI
pn.extension()

# Inicializar el cliente OpenAI
client = OpenAI(api_key=api_key)

# Mensaje de contexto inicial
context = [{'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. 
You first greet the customer, then collect the order, 
and then ask if it's a pickup or delivery. 
You wait to collect the entire order, then summarize it and check for a final 
time if the customer wants to add anything else. 
If it's a delivery, you ask for an address. 
Finally you collect the payment.
Make sure to clarify all options, extras and sizes to uniquely 
identify the item from the menu.
You respond in a short, very conversational friendly style. 
The menu includes 
pepperoni pizza  12.95, 10.00, 7.00 
cheese pizza   10.95, 9.25, 6.50 
eggplant pizza   11.95, 9.75, 6.75 
fries 4.50, 3.50 
greek salad 7.25 
Toppings: 
extra cheese 2.00, 
mushrooms 1.50 
sausage 3.00 
canadian bacon 3.50 
AI sauce 1.50 
peppers 1.00 
Drinks: 
coke 3.00, 2.00, 1.00 
sprite 3.00, 2.00, 1.00 
bottled water 5.00 
"""}]

# Widgets de entrada y botón
inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

# Lista para almacenar los mensajes
panels = []

# Función para enviar y recibir mensajes de OpenAI
def enviar_prompt(prompt, messages):
    messages.append({'role': 'user', 'content': prompt})
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
    messages.append({'role': 'assistant', 'content': response})
    return response

# Función para manejar la interacción
def collect_messages(event):
    print("Button clicked")  # Mensaje de depuración
    user_input = inp.value
    response = enviar_prompt(user_input, context)
    panels.append(pn.pane.Markdown(f"**User:** {user_input}"))
    panels.append(pn.pane.Markdown(f"**OrderBot:** {response}"))
    inp.value = ''
    dashboard[-1] = pn.Column(*panels)  # Actualiza el panel con la conversación

# Vincular la función al botón
button_conversation.on_click(collect_messages)

# Crear el dashboard
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.Column(*panels, sizing_mode='stretch_both'),
)

dashboard.servable()
