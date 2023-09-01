import os
import random
from PIL import Image

def cut_image(input_image, col_num, row_num, output_prefix):
    # 입력 이미지 로드
    img = Image.open(input_image)
    width, height = img.size

    # 하위 이미지 크기 계산
    sub_width = width // col_num
    sub_height = height // row_num

    # 크기 조정이 필요한 경우 수행
    if sub_width < 2 or sub_height < 2:
        sub_width = max(sub_width, 2)
        sub_height = max(sub_height, 2)
        img = img.resize((sub_width * col_num, sub_height * row_num))

    # 하위 이미지 자르고 처리
    sub_images = []
    for row in range(row_num):
        for col in range(col_num):
            left = col * sub_width
            upper = row * sub_height
            right = left + sub_width
            lower = upper + sub_height
            sub_img = img.crop((left, upper, right, lower))

            # 랜덤 변환 적용
            if random.random() < 0.5:
                sub_img = sub_img.transpose(Image.FLIP_LEFT_RIGHT)
            if random.random() < 0.5:
                sub_img = sub_img.transpose(Image.FLIP_TOP_BOTTOM)
            if random.random() < 0.5:
                sub_img = sub_img.rotate(90 * random.randint(0, 3))

            sub_images.append(sub_img)

    # 하위 이미지 저장
    for i, sub_img in enumerate(sub_images):
        output_name = f"{output_prefix}_{i}.png"
        sub_img.save(output_name)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("사용법: cut_image.py <input_image> <col_num> <row_num> <output_prefix>")
        sys.exit(1)

    input_image = sys.argv[1]
    col_num = int(sys.argv[2])
    row_num = int(sys.argv[3])
    output_prefix = sys.argv[4]

    cut_image(input_image, col_num, row_num, output_prefix)