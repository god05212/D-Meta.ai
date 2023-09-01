import os
import random
from PIL import Image

def merge_images(input_prefix, col_num, row_num, output_name):
    images = []
    for i in range(col_num * row_num):
        image_path = f"{input_prefix}_{i}.png"
        images.append(Image.open(image_path))

    # 랜덤 변환을 적용하여 이미지 병합
    merged_image = Image.new('RGB', (col_num * images[0].width, row_num * images[0].height))
    for row in range(row_num):
        for col in range(col_num):
            i = row * col_num + col
            img = images[i]

            # 랜덤 변환 적용
            if random.random() < 0.5:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            if random.random() < 0.5:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
            if random.random() < 0.5:
                img = img.rotate(90 * random.randint(0, 3))

            merged_image.paste(img, (col * img.width, row * img.height))

    merged_image.save(output_name)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("사용법: merge_image.py <input_prefix> <col_num> <row_num> <output_name>")
        sys.exit(1)

    input_prefix = sys.argv[1]
    col_num = int(sys.argv[2])
    row_num = int(sys.argv[3])
    output_name = sys.argv[4]

    merge_images(input_prefix, col_num, row_num, output_name)