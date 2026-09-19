# -*- coding: utf-8 -*-
"""Gera a arte de uma build em shared/art/: <p>-asc (medalhão 720), <p>-asc-bg (fundo desfocado 960), <p>-asc-sm (240) e as três da classe.

A ilustração da ascendência vem do poe2db (Art/2DArt/BaseClassIllustrations/<Nome>Ascendancy.webp); a da classe pode ser copiada de outra build da mesma classe.
Uso: python mkart.py <prefixo> <ilustracao-da-ascendencia> [<prefixo-da-classe-a-copiar> [cool]]"""
import os, shutil, sys
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "..", "..", "shared", "art")


def square(im):
    w, h = im.size
    s = min(w, h)
    return im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))


def vignette(size, inner=.62, outer=1.0):
    """Máscara radial: 255 até `inner` do raio, cai suavemente a 0 em `outer`."""
    m = Image.new("L", (size, size), 0)
    px = m.load()
    c = (size - 1) / 2
    for y in range(size):
        for x in range(size):
            d = (((x - c) ** 2 + (y - c) ** 2) ** .5) / c
            px[x, y] = 255 if d <= inner else 0 if d >= outer else int(255 * (1 - (d - inner) / (outer - inner)) ** 1.6)
    return m


def medallion(src, size):
    im = square(src).convert("RGB").resize((size, size), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    circle = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(circle).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    circle = circle.resize((size, size), Image.LANCZOS)
    edge = vignette(size, .80, 1.0)                       # escurece só a borda: moldura suave
    dark = ImageChops.multiply(im.convert("RGB"), Image.merge("RGB", (edge.point(lambda v: 90 + v * 165 // 255),) * 3))
    out = dark.convert("RGBA")
    out.putalpha(circle)
    return out


def backdrop(src, size):
    im = square(src).convert("RGB").resize((size, size), Image.LANCZOS).filter(ImageFilter.GaussianBlur(size / 90))
    im = ImageEnhance.Brightness(im).enhance(.78)
    mask = vignette(size, .70, .99)
    black = Image.new("RGB", (size, size), (0, 0, 0))
    return Image.composite(im, black, mask)


def main():
    p, fonte = sys.argv[1], sys.argv[2]
    src = Image.open(fonte)
    if len(sys.argv) > 4 and sys.argv[4] == "cool":              # variação de cor da mesma ilustração (gelo)
        r, g, bl = src.convert("RGB").split()
        src = Image.merge("RGB", (r.point(lambda v: int(v * .72)), g.point(lambda v: int(v * .96)), bl.point(lambda v: min(255, int(v * 1.14)))))
    medallion(src, 720).save(os.path.join(ART, f"{p}-asc.webp"), "WEBP", quality=88, method=6)
    backdrop(src, 960).save(os.path.join(ART, f"{p}-asc-bg.webp"), "WEBP", quality=80, method=6)
    medallion(src, 240).save(os.path.join(ART, f"{p}-asc-sm.webp"), "WEBP", quality=88, method=6)
    if len(sys.argv) > 3:
        for suf in ("class", "class-bg", "class-sm"):
            shutil.copyfile(os.path.join(ART, f"{sys.argv[3]}-{suf}.webp"), os.path.join(ART, f"{p}-{suf}.webp"))
    print("arte gerada:", sorted(f for f in os.listdir(ART) if f.startswith(p + "-")))


if __name__ == "__main__":
    main()
