from icon import build_icon

if __name__ == "__main__":
    build_icon(256).save(
        "app_icon.ico",
        sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )
