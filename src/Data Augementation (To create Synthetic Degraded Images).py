from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import random
import os

def add_noise(img, level):
    np_img = np.array(img)
    noise_scale = {'light': 25, 'medium': 50, 'heavy': 75}[level]
    noise = np.random.normal(loc=0, scale=noise_scale, size=np_img.shape)
    np_img = np.clip(np_img + noise, 0, 255)
    return Image.fromarray(np_img.astype('uint8'))

def random_erasing(img, level):
    draw = ImageDraw.Draw(img)
    num_shapes = {'small': 1, 'medium': 2}[level]
    max_area = 0.5 * img.width * img.height

    erased_area = 0
    while erased_area < max_area:
        shape = random.choice(['rectangle', 'ellipse'])
        x = random.randint(0, img.width)
        y = random.randint(0, img.height)
        w = random.randint(int(0.05 * img.width), int(0.3 * img.width))
        h = random.randint(int(0.05 * img.height), int(0.3 * img.height))
        if shape == 'rectangle':
            draw.rectangle([x, y, x + w, y + h], fill=0)
        elif shape == 'ellipse':
            draw.ellipse([x, y, x + w, y + h], fill=0)
        erased_area += w * h
        if erased_area > max_area:
            break
    return img

def blur_image(img, level):
    radius = {'light': 1, 'medium': 3, 'heavy': 5}[level]
    return img.filter(ImageFilter.GaussianBlur(radius))

def apply_transformations(img_path):
    img = Image.open(img_path).convert('L')
    synthetic_images = []
    noise_levels = ['light', 'medium', 'heavy']
    erasure_levels = ['small', 'medium']
    blur_levels = ['light', 'medium', 'heavy']

    # Apply individual transformations
    for level in noise_levels:
        synthetic_images.append(add_noise(img.copy(), level))
    for level in erasure_levels:
        synthetic_images.extend([random_erasing(img.copy(), level) for _ in range(3)])  # Ensure enough samples
    for level in blur_levels:
        synthetic_images.append(blur_image(img.copy(), level))

    # Apply combinations of degradations
    combinations = [
        ('noise', 'blur'),
        ('blur', 'erasure'),
        ('noise', 'erasure'),
        ('noise', 'blur', 'erasure'),
    ]

    for combo in combinations:
        for _ in range(2):  # Generate multiple images per combination
            img_copy = img.copy()
            for degradation in combo:
                if degradation == 'noise':
                    img_copy = add_noise(img_copy, random.choice(noise_levels))
                elif degradation == 'blur':
                    img_copy = blur_image(img_copy, random.choice(blur_levels))
                elif degradation == 'erasure':
                    img_copy = random_erasing(img_copy, random.choice(erasure_levels))
            synthetic_images.append(img_copy)

    return synthetic_images

# Loop through all files in the input folder and apply transformations
input_folder = 'medieval_sinhala'
output_folder = 'test_synthetic_medieval_sinhala4'

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        img_path = os.path.join(input_folder, filename)
        try:
            synthetic_images = apply_transformations(img_path)
            image_name = filename[:-4]  # Removes the '.jpg' from filename

            # Save the synthetic images
            for i, synthetic_img in enumerate(synthetic_images):
                synthetic_img.save(os.path.join(output_folder, f'{image_name}_synthetic_image_{i}.jpg'))
            print(f"Processed {filename} successfully.")
        except Exception as e:
            print(f"Failed to process {filename}: {str(e)}")
