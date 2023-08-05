DEFAULT_FILE_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1520
SYMBOL_SIZE = 300
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 0, 0

# Images
BG_IMAGE_PATH = "graphics/neon/0-bg.jpg"
GRID_IMAGE_PATH = "graphics/neon/grid.png"
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = "graphics/0/symbols"

# 5 Symbols
symbols = {
    'blackswan': f"{SYM_PATH}/blackswan.png",
    'whiteswan': f"{SYM_PATH}/whiteswan.png",
    'duck': f"{SYM_PATH}/duck.png",
    'fish': f"{SYM_PATH}/fish.png",
    'frog': f"{SYM_PATH}/frog.png"
}