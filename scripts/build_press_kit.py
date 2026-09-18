from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

OUT=Path("assets/presse/kit-presse-arthur-nicolas.pdf")
OUT.parent.mkdir(parents=True,exist_ok=True)

serif="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
serif_b="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
sans="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
sans_b="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
for name,path in [("Serif",serif),("SerifB",serif_b),("Sans",sans),("SansB",sans_b)]:
    if Path(path).exists():
        pdfmetrics.registerFont(TTFont(name,path))

BG=colors.HexColor("#08090c")
WINE=colors.HexColor("#721a2d")
TEXT=colors.HexColor("#17171b")
MUTED=colors.HexColor("#65616a")
PAPER=colors.HexColor("#f5f2ed")

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=20*mm,bottomMargin=18*mm,
                      title="Kit presse - Arthur Nicolas",author="Arthur Nicolas")

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="Eyebrow",fontName="SansB",fontSize=8,leading=10,textColor=WINE,spaceAfter=7,textTransform="uppercase"))
styles.add(ParagraphStyle(name="TitleBig",fontName="SerifB",fontSize=34,leading=36,textColor=TEXT,spaceAfter=10))
styles.add(ParagraphStyle(name="PressTitle",fontName="SerifB",fontSize=24,leading=27,textColor=TEXT,spaceAfter=10))
styles.add(ParagraphStyle(name="PressSub",fontName="Serif",fontSize=14,leading=19,textColor=MUTED,spaceAfter=12))
styles.add(ParagraphStyle(name="Body2",fontName="Sans",fontSize=9.6,leading=14,textColor=TEXT,spaceAfter=9))
styles.add(ParagraphStyle(name="Small2",fontName="Sans",fontSize=8.2,leading=11.5,textColor=MUTED,spaceAfter=6))
styles.add(ParagraphStyle(name="Quote2",fontName="Serif",fontSize=15,leading=20,textColor=TEXT,leftIndent=10,borderColor=WINE,borderWidth=1.3,borderPadding=8,spaceBefore=8,spaceAfter=14))

def page(canvas,doc):
    canvas.saveState()
    w,h=A4
    canvas.setFillColor(WINE); canvas.rect(0,h-7*mm,w,7*mm,fill=1,stroke=0)
    canvas.setFillColor(MUTED); canvas.setFont("Sans",7.5)
    canvas.drawString(18*mm,9*mm,"Arthur Nicolas · Kit presse")
    canvas.drawRightString(w-18*mm,9*mm,f"{doc.page}")
    canvas.restoreState()

story=[]
story += [
    Paragraph("KIT PRESSE · 2026",styles["Eyebrow"]),
    Paragraph("Arthur Nicolas",styles["TitleBig"]),
    Paragraph("Auteur · dark fantasy urbaine · thriller gothique",styles["PressSub"])
]
cover=Image("assets/requiem-cover.jpg",width=53*mm,height=79*mm)
author=Image("assets/photos/arthur-author-ravenscrow.jpg",width=78*mm,height=66*mm)
table=Table([[cover,author]],colWidths=[60*mm,90*mm])
table.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ALIGN",(0,0),(-1,-1),"CENTER"),
                           ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
story += [table,Spacer(1,8*mm)]
story += [
    Paragraph("À PROPOS",styles["Eyebrow"]),
    Paragraph("Auteur et animateur originaire des Alpes-de-Haute-Provence, Arthur Nicolas écrit des récits sombres, visuels et atmosphériques dans lesquels le fantastique révèle des failles humaines concrètes : deuil, culpabilité, colère, solidarité, pouvoir et mémoire.",styles["Body2"]),
    Paragraph("Passionné par le cinéma, l'horreur, la photographie et la musique, il construit ses romans comme des espaces où l'ambiance reste indissociable des choix moraux. Après <i>Interpolis</i>, publié aux Éditions du Net en 2025, il développe <i>La Saga des Ombres</i>. Il anime également <i>Dans l'Ombre des Livres</i>, un podcast consacré aux parcours d'auteurs et à la réalité du monde éditorial.",styles["Body2"]),
    Spacer(1,2*mm),
    Paragraph("<b>Contact auteur & presse</b> · arthur.ncls@icloud.com",styles["Body2"]),
    Paragraph("<b>Contact podcast</b> · danslombredeslivres@gmail.com",styles["Body2"]),
    Paragraph("Instagram · @artncls_auteur · Site · https://arthurncls.github.io/",styles["Small2"]),
    PageBreak()
]

story += [
    Paragraph("REQUIEM",styles["Eyebrow"]),
    Paragraph("La Saga des Ombres · Tome I",styles["PressTitle"]),
    Paragraph("Dark fantasy urbaine gothique · thriller fantastique adulte",styles["PressSub"]),
]
facts=[
    ["Édition","Indépendante révisée · 16 juillet 2026"],
    ["Format","374 pages · 34 chapitres"],
    ["ISBN","979 8198698017"],
    ["Cycle","4 volumes · trajectoire complète"],
    ["Cadre","Ravenscrow, ville fictive des West Midlands · 2022"],
]
ft=Table(facts,colWidths=[34*mm,120*mm])
ft.setStyle(TableStyle([("FONTNAME",(0,0),(0,-1),"SansB"),("FONTNAME",(1,0),(1,-1),"Sans"),
                        ("FONTSIZE",(0,0),(-1,-1),8.8),("TEXTCOLOR",(0,0),(0,-1),WINE),
                        ("TEXTCOLOR",(1,0),(1,-1),TEXT),("BOTTOMPADDING",(0,0),(-1,-1),6),
                        ("TOPPADDING",(0,0),(-1,-1),6),("LINEBELOW",(0,0),(-1,-1),0.25,colors.HexColor("#d8d3d0"))]))
story += [ft,Spacer(1,7*mm)]
story += [
    Paragraph("PRÉSENTATION",styles["Eyebrow"]),
    Paragraph("Dix ans après le meurtre de ses parents, Thomas Gray, justicier spectral né d'un pacte infernal, enquête avec la journaliste Stella Frost sur des crimes qui relient la pègre, la mairie et les fondations occultes de Ravenscrow, jusqu'à découvrir que l'entité qu'il traque, la ville qu'il veut sauver et la puissance qu'il porte appartiennent au même piège.",styles["Body2"]),
    Paragraph("« Un thriller gothique qui bascule progressivement dans la dark fantasy, l'horreur cosmique et l'apocalypse, sans perdre son moteur intime : la relation entre Thomas et Stella. »",styles["Quote2"]),
    Paragraph("REPÈRES",styles["Eyebrow"]),
    Paragraph("<b>Atmosphère :</b> sombre, pluvieuse, viscérale, mélancolique et cinématographique.",styles["Body2"]),
    Paragraph("<b>Références de ton :</b> <i>The Batman</i> pour la ville malade et le justicier ambivalent ; <i>Se7en</i> pour la logique rituelle ; <i>Sleepy Hollow</i> pour l'atmosphère gothique.",styles["Body2"]),
    Paragraph("<b>Contenus sensibles :</b> violence graphique, meurtres rituels, profanations religieuses, deuil, trauma, coercition, fanatisme politique et religieux, langage soutenu.",styles["Small2"]),
    PageBreak()
]

sign=Image("assets/photos/arthur-signing-ravenscrow.jpg",width=72*mm,height=72*mm)
pod=Image("assets/photos/podcast-dans-ombre-livres.jpg",width=72*mm,height=72*mm)
media_table=Table([[sign,pod]],colWidths=[78*mm,78*mm])
media_table.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
story += [
    Paragraph("MÉDIAS · RENCONTRES · PODCAST",styles["Eyebrow"]),
    Paragraph("Au-delà des pages",styles["PressTitle"]),
    media_table,Spacer(1,7*mm),
    Paragraph("<b>Dans l'Ombre des Livres</b> explore les parcours d'auteurs et la réalité du monde éditorial : publication, rémunération, visibilité, premiers romans, maisons d'édition et coulisses du livre.",styles["Body2"]),
    Paragraph("<b>BFM DICI · 2 octobre 2025</b> — entretien télévisé autour du parcours d'auteur et de l'univers de <i>Ravenscrow</i>.<br/><link href='https://www.dailymotion.com/video/x9rkasw' color='#721a2d'>Voir l'interview sur Dailymotion</link>",styles["Body2"]),
    Paragraph("<b>Rencontres sélectionnées :</b> E.Leclerc Gap (29 novembre 2025), Intermarché Saint-Pons (23 mai 2026), Librairie de la Presse à Digne-les-Bains (4 juillet 2026).",styles["Body2"]),
    Spacer(1,3*mm),
    Paragraph("POUR LES PROFESSIONNELS",styles["Eyebrow"]),
    Paragraph("Interviews, dédicaces, tables rondes, salons, interventions et échanges autour de l'écriture, de la dark fantasy et de la réalité du monde du livre.",styles["Body2"]),
    Paragraph("<b>Contact auteur & presse :</b> arthur.ncls@icloud.com",styles["Body2"]),
    Paragraph("<b>Contact podcast :</b> danslombredeslivres@gmail.com",styles["Body2"]),
    Paragraph("Visuels HD et informations complémentaires : https://arthurncls.github.io/presse.html",styles["Small2"]),
]

doc.build(story,onFirstPage=page,onLaterPages=page)
print(OUT)
