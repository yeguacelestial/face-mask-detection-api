import tensorflow as tf
import tflite_runtime.interpreter as tflite

import numpy as np

from PIL import Image

from urllib import request

MODEL_URL = 'https://github.com/yeguacelestial/face-mask-detection-api/raw/main/mask_classifier.tflite'

print("[*] Downloading model...")
urllib.request.urlretrieve(MODEL_URL, 'mask_classifier.tflite')

print("[+] Done.")

# Load TFLite model and allocate tensors
interpreter = tflite.Interpreter(model_path='mask_classifier.tflite')
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

floating_model = input_details[0]['dtype'] == np.float32

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]


def predict_mask_on_img(img_path):
    img = Image.open(img_path).resize((width, height))

    input_data = np.expand_dims(img, axis=0)

    if floating_model:
        input_data = (np.float32(input_data) - 127.5) / 127.5

    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    results = np.squeeze(output_data)
    scalar_result = int(round(np.asscalar(results)))

    print(f"\n[***] OUTPUT: {output_data}")

    if scalar_result:
        print(f"[-] No se detectó una mascara en {img_path}: {scalar_result}")
        return False, scalar_result

    else:
        print(f"[+] Se detecto una mascara en {img_path}: {scalar_result}")
        return True, scalar_result