# Importar las bibliotecas necesarias
import curses
import time

# Establecer la ventana de curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Variables para la pintura
last_x, last_y = 0, 0
drawing = False

# Función para dibujar un punto en la pantalla
def draw_point(x, y):
    stdscr.addch(y, x, '*')

# Evento de movimiento del cursor
while True:
    c = stdscr.getch()
    if c == curses.KEY_MOUSE:
        x, y, _, _ = curses.getmouse()
        if drawing:
            draw_point(x, y)
        last_x, last_y = x, y
    elif c == curses.KEY_LEFT:
        drawing = False
    elif c == curses.KEY_RIGHT:
        drawing = True

# Liberar la ventana de curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
