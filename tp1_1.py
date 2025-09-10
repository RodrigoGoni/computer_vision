import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def white_patch(img: np.ndarray):

    # Convertir a float para los cálculos
    img_float = img.astype(np.float32)
    max_channel_value = np.max(img_float, axis=(0, 1))
    cantidad_de_desviaciones = 1.5
    correction_factors = np.ones(3, dtype=np.float32)
    # Se checkean los valores extremos y se usa una estrategia para corregirlos
    for i in range(len(max_channel_value)):
        if max_channel_value[i] < 1:
            correction_factors[i] = 255 / (np.mean(
                img_float[:, :, i]) - cantidad_de_desviaciones*np.std(img_float[:, :, i]))
        elif max_channel_value[i] > 254:
            correction_factors[i] = 255 / (np.mean(
                img_float[:, :, i]) + cantidad_de_desviaciones*np.std(img_float[:, :, i]))
        else:
            # Factores por canal BGR
            correction_factors[i] = 255.0 / \
                np.clip(max_channel_value[i], 1, 254)

    # Correccion

    corrected_img = img_float * correction_factors
    corrected_img = np.clip(corrected_img, 0, 255).astype(np.uint8)

    return corrected_img


BASE_IMG_FOLDERS = Path("Material_TPs/TP1/white_patch")
RESULTS_FOLDER = Path("results")
RESULTS_FOLDER.mkdir(exist_ok=True)

image_paths = list(BASE_IMG_FOLDERS.glob("*.png")) + \
    list(BASE_IMG_FOLDERS.glob("*.jpg"))
n_images = len(image_paths)

for img_path in image_paths:
    img = cv2.imread(str(img_path))
    if img is None:
        continue
    corrected_img = white_patch(img.copy())
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corrected_rgb = cv2.cvtColor(corrected_img, cv2.COLOR_BGR2RGB)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].imshow(img_rgb)
    axes[0].set_title(f"Original: {img_path.name}")
    axes[0].axis('off')

    axes[1].imshow(corrected_rgb)
    axes[1].set_title(f"White Patch: {img_path.name}")
    axes[1].axis('off')

    plt.tight_layout()

    # Guardar la figura en la carpeta results
    result_filename = RESULTS_FOLDER / f"{img_path.stem}_comparison.png"
    plt.savefig(result_filename, dpi=300, bbox_inches='tight')
    # plt.show()
