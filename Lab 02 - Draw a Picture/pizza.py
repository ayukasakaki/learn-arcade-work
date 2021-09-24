import arcade
arcade.open_window(600, 600, "Pizza")

arcade.set_background_color(arcade.csscolor.LIGHT_GREY)
arcade.start_render()
arcade.draw_triangle_filled(400, 600, 270, 320, 530, 320, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(400, 350, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(400, 409, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(380, 450, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(430, 457, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(325, 350, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(485, 350, 20, arcade.csscolor.BROWN)
arcade.draw_circle_filled(420, 500, 20, arcade.csscolor.BROWN)
arcade.draw_rectangle_filled(400, 320, 280, 40, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(410, 360, 20, 30, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(420, 460, 20, 30, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(410, 500, 20, 30, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(430, 390, 20, 30, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(380, 420, 20, 30, arcade.csscolor.GREEN)
arcade.draw_text("Pizza with Pepperoni and Small Green Bell Peppers Slices",
                 70, 230,
                 arcade.color.BLACK, 10)
arcade.finish_render()
arcade.run()