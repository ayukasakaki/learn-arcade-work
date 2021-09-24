import arcade
arcade.open_window(600, 600, "Drawing")
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
arcade.start_render()
# Draw ground and sky
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.color.SAND)
arcade.draw_lrtb_rectangle_filled(0, 600, 400, 200, arcade.color.LIGHT_PINK)
arcade.draw_lrtb_rectangle_filled(0, 600, 500, 300, arcade.color.ORANGE)
arcade.draw_lrtb_rectangle_filled(0, 600, 600, 400, arcade.color.DARK_ORANGE)
arcade.draw_lrtb_rectangle_filled(0, 600, 700, 500, arcade.color.LIGHT_CARMINE_PINK)
# Drawing a tree
arcade.draw_rectangle_filled(100, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(100, 270, 60, 80, arcade.csscolor.DARK_GREEN)
# Drawing the sun
arcade.draw_arc_filled(300, 200, 110, 100, arcade.csscolor.YELLOW, 0, 180)
# Drawing the other trees
arcade.draw_rectangle_filled(200, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 270, 60, 80, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(400, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(400, 270, 60, 80, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(550, 270, 60, 80, arcade.csscolor.DARK_GREEN)
# Drawing the sign
arcade.draw_rectangle_filled(100, 50, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(100, 100, 170, 70, arcade.color.SIENNA)
arcade.draw_rectangle_filled(100, 100, 170, 60, arcade.csscolor.SIENNA)
# Drawing the text
arcade.draw_text("Welcome to TEXAS",
                 30, 100,
                 arcade.color.BLACK, 12)
arcade.finish_render()
arcade.run()

