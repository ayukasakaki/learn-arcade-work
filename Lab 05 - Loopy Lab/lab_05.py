import arcade
arcade.open_window(600, 600, "Turtle")

arcade.set_background_color(arcade.csscolor.DARK_CYAN)
arcade.start_render()
arcade.draw_arc_filled(300, 380, 60, 100, arcade.csscolor.LIGHT_GREEN, 0, 180)
arcade.draw_ellipse_filled(300, 350, 200, 30, arcade.csscolor.LIGHT_GREEN)
arcade.draw_ellipse_filled(300, 250, 200, 30, arcade.csscolor.LIGHT_GREEN)
arcade.draw_ellipse_filled(300, 200, 20, 30, arcade.csscolor.LIGHT_GREEN)
arcade.draw_ellipse_filled(300, 300, 150, 200, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(300, 250, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(310, 270, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(290, 270, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(300, 290, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(310, 310, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(290, 310, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(290, 310, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(300, 330, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(290, 350, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(310, 350, 10, arcade.csscolor.LIGHT_GREEN)
arcade.draw_circle_filled(center_x=300,
                          center_y=370,
                          radius=10,
                          color=arcade.csscolor.LIGHT_GREEN)
arcade.draw_text("Stephen the Turtle",
                 150, 130,
                 arcade.color.BLACK, 24)
arcade.finish_render()


arcade.run()
