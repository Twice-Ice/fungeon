from pygame import Rect
SCREEN_SIZE = (1920, 1080)
SCREEN_RECT = Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
FPS = 120

def halfRound(val: float, n_digits: int = 0):
    val *= 10 ** n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10 ** n_digits if n_digits != 0 else int(result / 10)