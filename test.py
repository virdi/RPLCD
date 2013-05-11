# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import RPIO
from RPLCD import CharLCD, Alignment, CursorMode, ShiftMode


RPIO.setwarnings(False)


lcd = CharLCD()

lcd.setup()
raw_input('Display should be blank. ')

lcd.cursor_mode = CursorMode.blink
raw_input('The cursor should now blink. ')

lcd.cursor_mode = CursorMode.line
raw_input('The cursor should now be a line. ')

lcd.write_string('Hello world!')
raw_input('"Hello world!" should be on the LCD. ')

lcd.cursor_pos = (1, 0)
lcd.write_string('2')
lcd.cursor_pos = (2, 0)
lcd.write_string('3')
lcd.cursor_pos = (3, 0)
lcd.write_string('4')
raw_input('Lines 2, 3 and 4 should now be labelled with the right numbers. ')

lcd.clear()
raw_input('Display should now be clear, cursor should be at initial position. ')

lcd.cursor_pos = (0, 5)
lcd.write_string('12345')
raw_input('The string should have a left offset of 5 characters. ')

lcd.write_shift_mode = ShiftMode.display
lcd.cursor_pos = (1, 5)
lcd.write_string('12345')
raw_input('Both strings should now be at column 0. ')

lcd.write_shift_mode = ShiftMode.cursor
lcd.cursor_pos = (2, 5)
lcd.write_string(lcd.write_shift_mode.name)
raw_input('The string "cursor" should now be on the third row, column 0. ')

lcd.home()
raw_input('Cursor should now be at initial position. Everything should be shifted to the right by 5 characters. ')

lcd.display_enabled = False
raw_input('Display should now be blank. ')

lcd.clear()
lcd.write_string('Eggs, Ham, Bacon')
lcd.cursor_pos = (1, 0)
lcd.write_string('and Spam')
lcd.display_enabled = True
raw_input('Display should now show "Eggs, Ham, Bacon and Spam". ')

lcd.shift_display(4)
raw_input('Text should now be shifted to the right by 4 characters. ')
lcd.shift_display(-4)
raw_input('Shift should now be reverted. ')

lcd.text_align_mode = Alignment.right
lcd.write_string(' Spam')
raw_input('The word "Spam" should now be inverted. ')

lcd.text_align_mode = Alignment.left
lcd.write_string(' Wurscht')
raw_input('The word "mapS" should now be replaced with "Wurscht". ')

print('Test done.')


#lcd.close()
