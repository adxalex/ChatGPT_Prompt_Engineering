from openai import OpenAI
from config import api_key
from IPython.display import display, HTML

parametros = """
The answer should respond with the following parameters:

- positive prompt: the first part of the text before "negative prompt"
- negative prompt: text with negative prompt
- Sampling steps: number between 0 - 200
- Width: number between 0 - 2048
- Height: number between 0 - 2048
- CFG Scale: number between 0 - 30
- Seed: number between 0 - 99999999999
"""

formato_respuesta = """The format should be JSON with the following keys: positive prompt, negative prompt, Sampling steps, Width, Height, CFG Scale, Seed"""

persona = """
A young woman with long, straight brown hair, fair skin, and large blue eyes with long eyelashes. She has well-defined, slightly arched dark brown eyebrows, a straight nose, and slightly full, well-defined lips. Her face is oval-shaped with soft, symmetrical lines. She is wearing sunglasses on her head
"""

pose = """
The photo is taken in natural daylight, with the light source coming from the front, slightly to the left, illuminating her face evenly. Her head is positioned straight towards the camera, making direct eye contact with a neutral expression. The background is softly blurred, focusing attention on her face.
"""

entrada = """ 
UHD, 8K, ultra detailed, a cinematic photograph of breathtaking cinematic photo HDR photo of A photo portrait of a mesmerizing lady with tightly coiled hair and clear skin, (golden blonde hair), (blue-green eyes), (large breasts, cleavage), (face portrait:1.5), natural light, rembrandt lighting scheme, (hyperrealism:1.2), (8K UHD:1.2), (photorealistic:1.2), shot with Nikon D750, detailed face, detailed hair, wearing a pink velvet choker, no glasses, and opaque white tights., ((photographed by Sports Illustrated)) . High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed . 35mm photograph, film, bokeh, professional, 4k, highly detailed . award-winning, professional, highly detailed, beautiful lighting, great composition
Negative prompt: (CyberRealistic_Negative_v3:1.3), bad-picture-chill-75v, epiCNegative, flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, ugly, deformed, noisy, blurry, distorted, grainy, ugly, deformed, noisy, blurry, NSFW
Steps: 45, CFG scale: 7, Sampler: DPM++ SDE, Seed: 1734565811, Size: 512x768, Model: cyberrealistic_v50, Version: v1.9.4, TI hashes: [object Object], Model hash: 0b20a3f2cd, Hires steps: 20, Hires sampler: DPM++ 2M SDE, Hires upscale: 2, Schedule type: Karras, Hires upscaler: 4x-UniScaleV2_Soft, ADetailer model: mediapipe_face_full, ADetailer prompt: [object Object], ADetailer version: 24.5.1, Denoising strength: 0.4, ADetailer mask blur: 4, ADetailer model 2nd: PitHandDetailer-v1-seg.pt, ADetailer model 3rd: deepfashion2_yolov8s-seg.pt, ADetailer model 4th: female_breast_v3.2.pt, Hires schedule type: Exponential, ADetailer confidence: 0.3, ADetailer prompt 2nd: [object Object], ADetailer prompt 3rd: [object Object], ADetailer prompt 4th: [object Object], ADetailer dilate erode: 4, ADetailer mask blur 2nd: 4, ADetailer mask blur 3rd: 4, ADetailer mask blur 4th: 4, ADetailer confidence 2nd: 0.3, ADetailer confidence 3rd: 0.3, ADetailer confidence 4th: 0.3, ADetailer inpaint padding: 32, ADetailer negative prompt: [object Object], ADetailer dilate erode 2nd: 4, ADetailer dilate erode 3rd: 4, ADetailer dilate erode 4th: 4, ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True, ADetailer inpaint padding 2nd: 32, ADetailer inpaint padding 3rd: 32, ADetailer inpaint padding 4th: 32, ADetailer negative prompt 2nd: [object Object], ADetailer negative prompt 3rd: [object Object], ADetailer negative prompt 4th: epiCPhoto-neg Realisian-Neg, ADetailer denoising strength 2nd: 0.4, ADetailer denoising strength 3rd: 0.4, ADetailer denoising strength 4th: 0.4, ADetailer inpaint only masked 2nd: True, ADetailer inpaint only masked 3rd: True, ADetailer inpaint only masked 4th: True, Clip skip: 2
"""

prompt = f"""
- With the following text you should respond with the {parametros} in the format {formato_respuesta}: {entrada}.
- On field "positive prompt" you must keep everything in parentheses
- On field "positive prompt" where you find physical description, I want that you replaced the physical description by {persona}, please do this in english. Remember that is important that you don't change the format of the positive prompt.
- On field "positive prompt" You must replace the descriptions of the photograph to the following descriptions {pose} please do this in english. Remember that is important that you don't change the format of the positive prompt.
"""
def enviar_prompt(promt):
    client = OpenAI(api_key=api_key)



    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"You should follow the instruction of {prompt}"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

print(enviar_prompt(prompt))

#display(HTML(enviar_prompt(prompt)))


