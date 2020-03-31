from upload import *

if __name__ == "__main__":
    upload = Upload(use_display=False, headless=True, width=1920, height=1080)
    upload.all(file_types=[FileType.png, FileType.jpg], sleep_interval=1)
    print("[DONE]")