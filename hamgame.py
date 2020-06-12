import arcade
from PIL import Image

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Example"

SPEED = 3

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.WHITE)
        self._time = 0
        self._maze = None
        self._path = None
        self._player = None
        self._is_transparent = False
        self._player_dir_list = []
        self._player_pos = None
        self._player_next_pos = None

        # self._maze_img = Image.open("/Users/claireharpel/PycharmProjects/hamiltongame/images/hammap1.png")
        # (width, height) = (800, 800)
        # self._maze_img = self._maze_img.resize((width, height))
        # self._maze_img.save("/Users/claireharpel/PycharmProjects/hamiltongame/images/hammap1.png")
        # # self._maze_img.show()

    def setup(self):
        self._maze = arcade.Sprite("/Users/claireharpel/PycharmProjects/hamiltongame/images/newmaze.png", scale= 0.25,
                                   center_x=400, center_y=400)
        self._player = arcade.Sprite("/Users/claireharpel/PycharmProjects/hamiltongame/images/transparentcircle2.png", scale=.007,
                                     center_x=400, center_y=790)
        self._path = arcade.Sprite("/Users/claireharpel/PycharmProjects/hamiltongame/images/hampath1.png", scale=.25,
                                   center_x=400, center_y=400)
        self._player_dir_list = [(-1, 0), (1, 0), (0,-1), (-1,0)]

    def on_draw(self):
        arcade.start_render()
        # self._path.draw()
        self._maze.draw()
        self._player.draw()

    def on_key_press(self, key, mod):
       if self._is_transparent:
            if key == arcade.key.LEFT:
                self._player.change_x = -SPEED
            elif key == arcade.key.RIGHT:
                self._player.change_x = +SPEED
            elif key == arcade.key.DOWN:
                self._player.change_y = -SPEED
            elif key == arcade.key.UP:
                self._player.change_y = +SPEED

    def on_key_release(self, key, mod):
        if key == arcade.key.LEFT:
            self._player.change_x = 0
        elif key == arcade.key.RIGHT:
            self._player.change_x = 0
        elif key == arcade.key.DOWN:
            self._player.change_y = 0
        elif key == arcade.key.UP:
            self._player.change_y = 0

    def on_update(self, time):
        self._time += time
        self._player.update()

        self._player_pos = self._player.position


        # print(arcade.get_pixel(player_pos[0] - 1, player_pos[1] - 1))
        if arcade.get_pixel(self._player_pos[0], self._player_pos[1]) == (255, 255, 255):
            self._is_transparent = True
        else:
            self._is_transparent = False
        # pixel_value = self._maze_img.getpixel(player_pos)
        # alpha = pixel_value[-1]
        # if alpha == 0:
        #     self._is_transparent = True
        #     arcade.set_background_color(arcade.csscolor.RED)
        # else:
        #     arcade.set_background_color(arcade.csscolor.LIGHT_GREY)
        #
        # self._player.update()

class StartPageView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = None

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_GREEN)
        self.background = arcade.Sprite("/Users/claireharpel/PycharmProjects/hamiltongame/images/startscreen.png", scale=0.4,
                               center_x=400, center_y=400)
    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        arcade.draw_text("WELCOME TO HAM MAPS", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLUEBERRY, font_size=50, anchor_x="center")
        arcade.draw_text("click to find your first class", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.BLUEBERRY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartPageView()
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    main()
