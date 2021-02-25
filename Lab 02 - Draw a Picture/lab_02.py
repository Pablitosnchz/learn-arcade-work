# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 700, "Drawing Example")

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)


arcade.start_render()

# Cesped
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


# Pies
# Izquierdo
arcade.draw_lrtb_rectangle_filled(325, 390, 220, 200, arcade.color.RED)
# Derecho
arcade.draw_lrtb_rectangle_filled(410, 475, 220, 200, arcade.color.RED)

# Contorno Pies
# Izquierdo
arcade.draw_rectangle_outline(357.5, 210, width=65, height=20, color=arcade.color.BLACK, border_width=3)
# Derecho
arcade.draw_rectangle_outline(442.5, 210, width=65, height=20, color=arcade.color.BLACK, border_width=3)


# Piernas
# Izquierda
arcade.draw_lrtb_rectangle_filled(335, 380, 315, 220, arcade.color.GRAY_BLUE)
# Derecha
arcade.draw_lrtb_rectangle_filled(420, 465, 315, 220, arcade.color.GRAY_BLUE)

# Contorno Piernas
# Izquierda
arcade.draw_rectangle_outline(357.5, 267.5, width=45, height=95, color=arcade.color.BLACK, border_width=3)
# Derecha
arcade.draw_rectangle_outline(442.5, 267.5, width=45, height=95, color=arcade.color.BLACK, border_width=3)


# Abdomen
arcade.draw_lrtb_rectangle_filled(320, 480, 400, 315, arcade.color.GRAY_BLUE)
# Contorno Abdomen
arcade.draw_rectangle_outline(400, 357.5, width=160, height=85, color=arcade.color.BLACK, border_width=3)


# Cuerpo
arcade.draw_triangle_filled(300, 325, 400, 265, 500, 325, arcade.color.GREEN)

# Contorno Cuerpo
arcade.draw_triangle_outline(300, 325, 400, 265, 500, 325, arcade.color.BLACK, border_width=2)

# Pectorales
# Izquierdo
arcade.draw_lrtb_rectangle_filled(300, 400, 500, 400, arcade.color.GRAY_BLUE)
# Derecho
arcade.draw_lrtb_rectangle_filled(400, 500, 500, 400, arcade.color.GRAY_BLUE)

# Contorno Pectorales
# Izquierdo
arcade.draw_rectangle_outline(350, 450, width=100, height=100, color=arcade.color.BLACK, border_width=3)
# Derecho
arcade.draw_rectangle_outline(450, 450, width=100, height=100, color=arcade.color.BLACK, border_width=3)


# Hombros
# Izquierdo
arcade.draw_lrtb_rectangle_filled(250, 300, 510, 460, arcade.color.YELLOW_GREEN)
# Derecho
arcade.draw_lrtb_rectangle_filled(500, 550, 510, 460, arcade.color.YELLOW_GREEN)

# Contorno Hombros
# Izquierdo
arcade.draw_rectangle_outline(275, 485, width=50, height=50, color=arcade.color.BLACK, border_width=3)
# Derecho
arcade.draw_rectangle_outline(525, 485, width=50, height=50, color=arcade.color.BLACK, border_width=3)

# Brazos
# Izquierdo
arcade.draw_lrtb_rectangle_filled(260, 290, 460, 350, arcade.color.GRAY_BLUE)
# Derecho
arcade.draw_lrtb_rectangle_filled(510, 540, 460, 350, arcade.color.GRAY_BLUE)

# Contorno Brazos
# Izquierdo
arcade.draw_rectangle_outline(275, 405, width=30, height=110, color=arcade.color.BLACK, border_width=3)
# Derecho
arcade.draw_rectangle_outline(525, 405, width=30, height=110, color=arcade.color.BLACK, border_width=3)

# Cuello
arcade.draw_lrtb_rectangle_filled(370, 430,510, 500, arcade.color.GRAY_BLUE)

#Contorno Cuello
arcade.draw_rectangle_outline(400, 505, width=60, height=10, color=arcade.color.BLACK, border_width=3)


# Cabeza
arcade.draw_lrtb_rectangle_filled(350, 450, 610, 510, arcade.color.GRAY_BLUE)

# Contorno Cabeza
arcade.draw_rectangle_outline(400, 560, width=100, height=100, color=arcade.color.BLACK, border_width=3)

# Ojos
# Derecho
arcade.draw_circle_filled(375,575,radius= 10,color= arcade.color.BLUEBERRY)
# Izquierdo
arcade.draw_circle_filled(425,575,radius= 10,color= arcade.color.BLUEBERRY)

# COntorno Ojos
# Izquierdo
arcade.draw_circle_outline(375,575,radius= 10,color= arcade.color.BLACK, border_width= 3)
arcade.draw_circle_outline(425,575,radius= 10,color= arcade.color.BLACK, border_width= 3)






arcade.finish_render()
arcade.run()
