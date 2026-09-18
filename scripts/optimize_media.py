from PIL import Image, ImageOps, ImageDraw, ImageFont
from pathlib import Path

def webp(src, dst, max_width, quality=84):
    im=Image.open(src).convert("RGB")
    if im.width > max_width:
        h=round(im.height*max_width/im.width)
        im=im.resize((max_width,h), Image.Resampling.LANCZOS)
    Path(dst).parent.mkdir(parents=True,exist_ok=True)
    im.save(dst,"WEBP",quality=quality,method=6)

webp("assets/requiem-cover.jpg","assets/books/requiem.webp",900,86)
webp("/tmp/interpolis.jpg","assets/books/interpolis.webp",900,86)
webp("assets/photos/arthur-author-ravenscrow.jpg","assets/photos/arthur-author-ravenscrow.webp",1100,82)
webp("assets/photos/arthur-reading-ravenscrow.jpg","assets/photos/arthur-reading-ravenscrow.webp",1200,82)
webp("assets/photos/arthur-signing-ravenscrow.jpg","assets/photos/arthur-signing-ravenscrow.webp",1200,82)
webp("assets/photos/podcast-dans-ombre-livres.jpg","assets/photos/podcast-dans-ombre-livres.webp",1000,84)

canvas=Image.new("RGB",(1200,630),(8,9,12))
cover=Image.open("assets/requiem-cover.jpg").convert("RGB")
cover=ImageOps.fit(cover,(330,500),method=Image.Resampling.LANCZOS)
canvas.paste(cover,(90,65))
draw=ImageDraw.Draw(canvas)
serif="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
serif_b="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
sans="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
try:
    f1=ImageFont.truetype(serif_b,64)
    f2=ImageFont.truetype(serif,34)
    f3=ImageFont.truetype(sans,21)
except Exception:
    f1=f2=f3=ImageFont.load_default()
draw.text((485,150),"Arthur Nicolas",font=f1,fill=(242,239,233))
draw.text((488,245),"Auteur de dark fantasy",font=f2,fill=(199,189,192))
draw.text((488,295),"urbaine et thriller gothique",font=f2,fill=(199,189,192))
draw.rectangle((488,365,840,369),fill=(114,26,45))
draw.text((488,405),"REQUIEM · LA SAGA DES OMBRES",font=f3,fill=(210,205,207))
draw.text((488,452),"arthurncls.github.io",font=f3,fill=(150,145,151))
canvas.save("assets/social/arthur-nicolas-og.jpg","JPEG",quality=88,optimize=True)
