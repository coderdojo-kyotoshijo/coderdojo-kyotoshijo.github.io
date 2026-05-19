"""
OGP画像 (ogp.png 1200x630) 生成スクリプト

タグライン・URLなどを変更した場合は本ファイルを編集して再実行:
    python3 generate-ogp.py

実行には Pillow と、システムに以下のフォントが必要:
- /usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf  (日本語)
- /usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf    (英字 Bold)
- /usr/share/fonts/truetype/lato/Lato-Medium.ttf             (英字 Regular)

Mac/Windows で実行する場合は、フォントパスを各環境の日本語/英字フォントに書き換えてください。
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

JP_FONT      = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"
EN_FONT_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
EN_FONT_REG  = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(__file__), "ogp.png")

img = Image.new("RGB", (W, H), "#1F3A5F")
draw = ImageDraw.Draw(img)
top, btm = (0x1F,0x3A,0x5F), (0x0F,0x23,0x40)
for y in range(H):
    t = y/H
    draw.line([(0,y),(W,y)], fill=(int(top[0]*(1-t)+btm[0]*t),
                                   int(top[1]*(1-t)+btm[1]*t),
                                   int(top[2]*(1-t)+btm[2]*t)))

glow = Image.new("RGBA", (W,H), (0,0,0,0))
gd = ImageDraw.Draw(glow)
cx, cy, r0 = int(W*0.85), int(H*0.18), 480
for r in range(r0, 0, -4):
    a = int(50*(1-r/r0)**2)
    if a > 0: gd.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(243,154,75,a))
img.paste(glow, (0,0), glow)
draw = ImageDraw.Draw(img)

LX, LY, LS = 96, 196, 220
mark = Image.new("RGB", (LS,LS), (0,0,0))
md = ImageDraw.Draw(mark)
for y in range(LS):
    t = y/LS
    md.line([(0,y),(LS,y)], fill=(int(0x2A*(1-t)+0x14*t),
                                  int(0x4A*(1-t)+0x29*t),
                                  int(0x75*(1-t)+0x44*t)))
mask = Image.new("L", (LS, LS), 0)
ImageDraw.Draw(mask).rounded_rectangle([0,0,LS,LS], radius=40, fill=255)
img.paste(mark, (LX, LY), mask)

draw = ImageDraw.Draw(img)
draw.line([(LX+40, LY+60),  (LX+22, LY+110), (LX+40, LY+160)],  fill="#F39A4B", width=7)
draw.line([(LX+180, LY+60), (LX+198, LY+110),(LX+180, LY+160)], fill="#F39A4B", width=7)
draw.ellipse([LX+172-11, LY+46-11, LX+172+11, LY+46+11], fill="#F39A4B")

font_nin = ImageFont.truetype(JP_FONT, 110)
bbox = draw.textbbox((0,0), "忍", font=font_nin)
tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
draw.text((LX + (LS-tw)/2 - bbox[0], LY + (LS-th)/2 - bbox[1] + 4),
          "忍", fill="white", font=font_nin)

font_brand_en = ImageFont.truetype(EN_FONT_BOLD, 42)
font_title_jp = ImageFont.truetype(JP_FONT,     104)
font_tag_jp   = ImageFont.truetype(JP_FONT,     30)
font_sub_jp   = ImageFont.truetype(JP_FONT,     22)
font_sub_en   = ImageFont.truetype(EN_FONT_REG, 22)
font_url_en   = ImageFont.truetype(EN_FONT_REG, 22)
font_side_jp  = ImageFont.truetype(JP_FONT,     22)
font_side_en  = ImageFont.truetype(EN_FONT_REG, 22)

x0 = 356
draw.text((x0, 222), "CoderDojo",                                   fill=(255,255,255,230), font=font_brand_en)
draw.text((x0, 282), "京都四条",                                     fill="white",            font=font_title_jp)
draw.text((x0, 416), "京都市下京区の子ども向けプログラミング道場", fill="#FFD6A8",         font=font_tag_jp)

sub_en = "Scratch / micro:bit / Web / Python"
sub_jp = " など、自分のペースで「つくる」を学べます。"
y = 466
draw.text((x0, y), sub_en, fill=(220,225,235,200), font=font_sub_en)
en_w = draw.textlength(sub_en, font=font_sub_en)
draw.text((x0+en_w, y), sub_jp, fill=(220,225,235,200), font=font_sub_jp)

draw.line([(96, 540), (W-96, 540)], fill=(243,154,75,100), width=2)
draw.text((96, 560), "coderdojo-kyoto-shijo.github.io", fill="#FFD6A8", font=font_url_en)

color = (207,217,230,255)
parts = [
    ("7",   font_side_en),
    ("〜",  font_side_jp),
    ("17",  font_side_en),
    ("歳・参加無料・月", font_side_jp),
    ("1",   font_side_en),
    ("回 日曜午後",   font_side_jp),
]
total_w = sum(draw.textlength(t, font=f) for t,f in parts)
xx = W - 96 - total_w
yy = 560
for t, f in parts:
    draw.text((xx, yy), t, fill=color, font=f)
    xx += draw.textlength(t, font=f)

img.save(OUT, optimize=True)
print(f"Saved: {OUT}  ({img.size})")
