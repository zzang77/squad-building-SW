from mplsoccer.pitch import Pitch, VerticalPitch
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

fig, ax = plt.subplots(1,2)

pitch = VerticalPitch(pitch_color='grass', line_color='white', stripe = True)
pitch.draw(ax[0])
ax[0].set_title("Squad Builder")

# ## 선수 위치 지정
# #GK
# ax[0].scatter(40, 3.3, c="white")
# #DF
# ax[0].scatter(10, 20, c="white")
# ax[0].scatter(30, 12, c="white")
# ax[0].scatter(50, 12, c="white")
# ax[0].scatter(70, 20, c="white")
# #MF
# ax[0].scatter(10, 50, c="white")
# ax[0].scatter(30, 42, c="white")
# ax[0].scatter(50, 42, c="white")
# ax[0].scatter(70, 50, c="white")
# #FW
# ax[0].scatter(30, 90, c="white")
# ax[0].scatter(50, 90, c="white")

## 사진 삽입
# iamge_path = "messi.png"
# img = Image.open(iamge_path)
# img_resized = img.resize((100, 100))
# ax[0].imshow(img_resized, extent=(10, 100, 10, 70), zorder=2)

# 선수 위치
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

# 선수 사진
# player_images = {
#     "GK": "messi.png",
#     "DF1": "messi.png",
#     "DF2": "messi.png",
#     "DF3": "messi.png",
#     "DF4": "messi.png",
#     "MF1": "messi.png",
#     "MF2": "messi.png",
#     "MF3": "messi.png",
#     "MF4": "messi.png",
#     "FW1": "messi.png",
#     "FW2": "messi.png"
# }

# #GK
# ax[0].text(40, 3.3, "GK", ha='center', va='center', color='black', fontsize=8)
# #DF
# ax[0].text(10, 15, "DF1", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(30, 7, "DF2", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(50, 7, "DF3", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(70, 15, "DF4", ha='center', va='center', color='black', fontsize=8)
# #MF
# ax[0].text(10, 45, "MF1", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(30, 37, "MF2", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(50, 37, "MF3", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(70, 45, "MF4", ha='center', va='center', color='black', fontsize=8)
# #FW
# ax[0].text(30, 85, "FW1", ha='center', va='center', color='black', fontsize=8)
# ax[0].text(50, 85, "FW2", ha='center', va='center', color='black', fontsize=8)

# 선수별로 이미지 삽입
# for player, pos in player_positions.items():
#     img = Image.open(player_images[player]).convert("RGBA")
#     #이미지 resize 화질 깨져서 삭제

#     # 이미지 위치
#     extent = (pos[0] - 5, pos[0] + 5, pos[1] +3 , pos[1] + 13)
#     ax[0].imshow(img, extent=extent, zorder=2)





# 선수 포지션 텍스트 추가 (선택 사항)
for player, pos in player_positions.items():
    ax[0].text(pos[0], pos[1], player, ha='center', va='center', color='black', fontsize=8)


pitch = Pitch(positional=True, label=True, axis= True, shade_middle=True)
pitch.draw(ax[1])
ax[1].set_title("Setting Football Tactics")

plt.show() 