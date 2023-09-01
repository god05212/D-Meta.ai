# 이미지 처리 스크립트
이 저장소에는 이미지 처리를 위한 두 개의 Python 스크립트인 `cut_image.py`와 `merge_image.py`가 포함되어 있습니다. 이 스크립트는 이미지를 잘라내고 합치는 작업을 수행하며, 각각의 하위 이미지에 대해 랜덤한 변환을 적용합니다.

## cut_image.py
`cut_image.py`는 입력 이미지를 작은 하위 이미지로 자르고, 각 하위 이미지에 대해 랜덤한 변환(미러링, 뒤집기, 90도 회전)을 적용합니다.

### 사용법
```bash
python cut_image.py <input_image> <col_num> <row_num> <output_prefix>
```

- input_image: 입력 이미지의 경로.
- col_num: 이미지를 자를 열 수.
- row_num: 이미지를 자를 행 수.
- output_prefix: 하위 이미지 파일명의 접두사.

## merge_image.py
merge_image.py는 cut_image.py로 생성된 하위 이미지 집합을 가져와 각 하위 이미지에 대해 랜덤한 변환을 적용한 후 이들을 합쳐 최종 이미지를 생성합니다.

### 사용법
```bash
python merge_image.py <input_prefix> <col_num> <row_num> <output_name>
```

- input_prefix: cut_image.py의 출력 파일명 접두사.
- col_num: 하위 이미지 그리드의 열 수.
- row_num: 하위 이미지 그리드의 행 수.
- output_name: 출력 병합 이미지의 이름.

## 테스트 자동화
테스트 자동화를 위해 test_automation.sh 스크립트를 사용할 수 있습니다. 이 스크립트는 cut_image.py와 merge_image.py를 예제 매개변수로 실행합니다.

### 사용법
```bash
./test_automation.sh
```

참고: 스크립트를 실행하기 전에 Python 및 필요한 라이브러리(PIL)가 설치되어 있는지 확인하십시오.

이것은 단순한 예시이며, 실제 프로젝트에 맞게 조정이 필요할 수 있습니다. 배포하기 전에 충분한 테스트를 수행하십시오.
