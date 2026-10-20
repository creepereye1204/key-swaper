from PIL import Image, ImageDraw, ImageFont

BLUE = (45, 108, 223, 255)
ORANGE = (232, 83, 30, 255)
DARK = (40, 44, 52, 255)
WHITE = (255, 255, 255, 255)


def build_icon(size=256):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)

    split = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(split)
    sdraw.polygon([(0, 0), (size, 0), (0, size)], fill=BLUE)
    sdraw.polygon([(size, 0), (size, size), (0, size)], fill=ORANGE)

    img.paste(split, (0, 0), mask)

    draw = ImageDraw.Draw(img)
    border = max(2, size // 40)
    draw.ellipse((border, border, size - border, size - border), outline=WHITE, width=border)

    _draw_swap_glyph(draw, size / 2, size / 2, size * 0.28, max(3, size // 22))
    return img


def _draw_swap_glyph(draw, cx, cy, r, lw):
    span = r * 1.6
    y1 = cy - r * 0.4
    y2 = cy + r * 0.4
    x_left = cx - span / 2
    x_right = cx + span / 2
    head = lw * 2.2

    draw.line([(x_left, y1), (x_right - head, y1)], fill=WHITE, width=int(lw))
    draw.polygon(
        [(x_right, y1), (x_right - head, y1 - head * 0.7), (x_right - head, y1 + head * 0.7)],
        fill=WHITE,
    )

    draw.line([(x_right, y2), (x_left + head, y2)], fill=WHITE, width=int(lw))
    draw.polygon(
        [(x_left, y2), (x_left + head, y2 - head * 0.7), (x_left + head, y2 + head * 0.7)],
        fill=WHITE,
    )


def build_esc_icon(size=256):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    border = max(2, size // 40)
    radius = size // 5
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=DARK)
    draw.rounded_rectangle(
        (border, border, size - 1 - border, size - 1 - border),
        radius=radius - border,
        outline=ORANGE,
        width=border,
    )

    font = ImageFont.load_default(size=int(size * 0.34))
    draw.text((size / 2, size / 2), "ESC", font=font, fill=WHITE, anchor="mm")
    return img


if __name__ == "__main__":
    build_icon(256).save("icon_preview.png")
    build_esc_icon(256).save("esc_icon_preview.png")
