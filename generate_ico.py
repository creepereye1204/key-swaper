from icon import build_esc_icon, build_icon

ICO_SIZES = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

if __name__ == "__main__":
    build_icon(256).save("app_icon.ico", sizes=ICO_SIZES)
    build_esc_icon(256).save("esc_icon.ico", sizes=ICO_SIZES)
