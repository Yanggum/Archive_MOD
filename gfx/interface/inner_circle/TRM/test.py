from PIL import Image
import os

# === 설정 ===
input_path = "nagisa_faction_J_bar.tga"          # 원본 이미지
output_dir = "split_frames"   # 저장 폴더
frames = 100                      # 총 분할 수

# 출력 폴더 생성
os.makedirs(output_dir, exist_ok=True)

# 원본 로드
img = Image.open(input_path).convert("RGBA")
width, height = img.size

# 1단계: 가로 100배의 초장형 이미지 생성
final_width = width * frames
long_img = Image.new("RGBA", (final_width, height))

for i in range(frames):
    progress = (i + 1) / frames
    crop_width = int(width * progress)
    cropped = img.crop((0, 0, crop_width, height))
    long_img.paste(cropped, (i * width, 0))

# 2단계: 100등분해서 .tga로 저장
segment_width = width
base_name = os.path.splitext(os.path.basename(input_path))[0]

for i in range(frames):
    left = i * segment_width
    right = left + segment_width
    segment = long_img.crop((left, 0, right, height))

    output_path = os.path.join(output_dir, f"{base_name}_{i+1}.tga")
    segment.save(output_path, format="TGA")

print(f"✅ {frames}개의 .tga 파일이 {output_dir}/ 에 저장되었습니다.")
