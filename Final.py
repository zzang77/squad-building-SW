import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch, VerticalPitch
from matplotlib.widgets import TextBox
from PIL import Image
import numpy as np
from functools import partial

# 이미지 파일 선택(Thinker)
def upload_image(player_name):
    root = tk.Tk()
    root.withdraw()
    root.update()
    file_path = filedialog.askopenfilename(title=f"Select Image for {player_name}", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
    return file_path

# 선수 포지션션
player_positions = {
    "GK": (40, 3.3),
    "DF1": (10, 25),
    "DF2": (30, 20),
    "DF3": (50, 20),
    "DF4": (70, 25),
    "MF1": (10, 60),
    "MF2": (30, 52),
    "MF3": (50, 52),
    "MF4": (70, 60),
    "FW1": (30, 90),
    "FW2": (50, 90)
}

# 선수 이미지 업로드
player_images = {}
for player in player_positions:
    img_path = upload_image(player)
    if img_path:
        player_images[player] = img_path
    else:
        player_images[player] = None
# 이미지 resize 제거(사진 화질 깨짐짐)

# 기본 설정(설정창 크기기)
fig, ax = plt.subplots(1, 3, figsize=(14, 7))

# 스쿼드 메이커 배경 그리기(축구장) - 1
pitch = VerticalPitch(pitch_color='grass', line_color='white', stripe=True)
pitch.draw(ax[0])
ax[0].set_title("Squad Builder")

# 텍스트 변경(딕셔너리)
player_texts = {player: player for player in player_positions}

# 선수별로 이미지 삽입 및 텍스트 추가
for player, pos in player_positions.items():
    if player_images[player]:
        try:
            img = Image.open(player_images[player])
            extent = (pos[0] - 5, pos[0] + 5, pos[1] + 3, pos[1] + 13) # 이미지 좌표 설정정
            ax[0].imshow(img, extent=extent, zorder=2) #zorder 표시 순서
        except Exception as e:
            print(f"Error loading image for {player}: {e}")

    ax[0].text(pos[0], pos[1], player_texts[player], ha='center', va='center', color='black', fontsize=8, zorder=3)

# TextBox 설정정
text_boxes = {}
textbox_start_x = 0.75  # figure 내 위치(오른쪽)

def submit(text, player):
    player_texts[player] = text
    for txt in ax[0].texts:
        if txt.get_text() == player:
            txt.set_text(text)
            break
    plt.draw()

for idx, (player, pos) in enumerate(player_positions.items()):
    textbox_ax = fig.add_axes([textbox_start_x, 0.9 - (idx * 0.08), 0.1, 0.05])
    text_box = TextBox(textbox_ax, label=player, initial=player, label_pad=0.05)
    text_boxes[player] = text_box
    text_box.on_submit(partial(submit, player=player))

# 스쿼드 메이커 배경 그리기(축구장) - 1
pitch2 = Pitch(positional=True, label=True, axis=True, shade_middle=True)
pitch2.draw(ax[1])
ax[1].set_title("Setting Football Tactics")

ax[2].axis('off')

plt.show()
