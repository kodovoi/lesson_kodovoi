from PIL import Image, ImageFilter, ImageEnhance

# Открытие изображения
image_path = 'input_image.jpg'
image = Image.open(image_path)

# Изменение размера изображения
new_size = (800, 600)
resized_image = image.resize(new_size)

# Применение эффектов
# 1. Чёрно-белое изображение
black_and_white_image = resized_image.convert('L')

# 2. Размытие
blurred_image = black_and_white_image.filter(ImageFilter.BLUR)

# 3. Увеличение контрастности
enhancer = ImageEnhance.Contrast(blurred_image)
enhanced_image = enhancer.enhance(2.0)

# Сохранение изображения в другом формате
output_path = 'output_image.png'
enhanced_image.save(output_path, 'PNG')

print(f"Изображение сохранено как {output_path}")
