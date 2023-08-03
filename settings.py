DEFAULT_FILE_IMAGE_SIZE = (250, 250)
FPS = 120
HEIGHT = 1000
WIDTH = 1400
SYMBOL_SIZE = 250
START_X, START_Y = 0, -SYMBOL_SIZE
X_OFFSET, Y_OFFSET = 0, 0

# Images
BG_IMAGE_PATH = "graphics/neon/0-bg.jpg"
GAME_INDICIES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = "graphics/0/symbols"

# 5 Symbols
symbols = {
    'blackswan': f"{SYM_PATH}/blackswan.png",
    'whiteswan': f"{SYM_PATH}/whiteswan.png",
    'duck': f"{SYM_PATH}/duck.png",
    'fish': f"{SYM_PATH}/fish.png",
    'frog': f"{SYM_PATH}/frog.png"
}