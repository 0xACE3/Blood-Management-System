from enum import Enum


class SupportedColors(Enum):
    RED           = (255, 000, 000)
    LIGHT_RED     = (255, 128, 128)
    DARK_RED      = (128, 000, 000)
    GREEN         = (000, 255, 000)
    LIGHT_GREEN   = (128, 255, 128)
    DARK_GREEN    = (000, 128, 000)
    BLUE          = (000, 000, 255)
    LIGHT_BLUE    = (128, 128, 255)
    DARK_BLUE     = (000, 000, 128)
    YELLOW        = (255, 255, 000)
    LIGHT_YELLOW  = (255, 255, 128)
    CYAN          = (000, 255, 255)
    LIGHT_CYAN    = (128, 255, 255)
    DARK_CYAN     = (000, 128, 128)
    DARK_YELLOW   = (128, 128, 000)
    MAGENTA       = (255, 000, 255)
    LIGHT_MAGENTA = (255, 128, 255)
    DARK_MAGENTA  = (128, 000, 128)
    WHITE         = (255, 255, 255)
    GRAY          = (128, 128, 128)
    BLACK         = (000, 000, 000)
    LIGHT_GRAY    = (192, 192, 192)
    DARK_GRAY     = (64,  64,   64)

    RESET = "\033[0m"






