import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = \
    (board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7)
keyboard.row_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.INSERT, KC.HOME, KC.PGUP, KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
    KC.DELETE, KC.END, KC.PGDOWN, KC.KP_7, KC.KP_8, KC.KP_9, KC.NO,
    KC.NO, KC.NO, KC.NO, KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_PLUS,
    KC.NO, KC.UP, KC.NO, KC.KP_1, KC.KP_2, KC.KP_3, KC.NO,
    KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.KP_0, KC.KP_DOT, KC.KP_ENTER]
]

#keyboard.debug_enabled = True
if __name__ == '__main__':
    keyboard.go()
