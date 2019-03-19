# To Do: Put piece on lower later

import sys
sys.path.append("../pygame-cdkk")
from cdkkPyGameApp import *
from cdkkSpriteExtra import *

### --------------------------------------------------

class Manager_TestSprite(SpriteManager):
    def __init__(self, name = "Test PyGame App Manager"):
        super().__init__(name)
        self._highlight = 0
        self._highlight_on = True
        cell_size = 40

        self._board1 = Sprite_BoardGame_Board(name="Board1")
        self._board1.setup_grid(cell_size, 8, EventManager.gc_event("Board1"))
        self._board1.rect.topleft = (40,40)
        self.add(self._board1)

        self._board2 = Sprite_BoardGame_Board(name="Board2", style={"fillcolour":"green", "altcolour":None, "outlinecolour":"black", "outlinewidth":2})
        self._board2.setup_grid(cell_size, 8, EventManager.gc_event("Board2"))
        self._board2.rect.topleft = (400,50)
        self.add(self._board2)

        self._board3 = Sprite_BoardGame_Board(name="Board3", style={"fillcolour":None, "altcolour":None, "fillimage":"board.png", "outlinecolour":None})
        self._board3.setup_grid(cell_size, 8)
        self._board3.rect.topleft = (800,50)
        self.add(self._board3)

        self._piece1 = Sprite_BoardGame_Piece("Piece1", self._board3, style={"fillcolour":"red4"})
        self.add(self._piece1)
        self._piece2 = Sprite_BoardGame_Piece("Piece2", self._board3, col=3, style={"fillcolour":"yellow2", "piecemargin":10})
        self.add(self._piece2)

    def event(self, e):
        dealt_with = super().event(e)
        if not dealt_with and e.type == EVENT_GAME_CONTROL:
            if e.action == "Board1":
                x, y = e.pos
                col, row = self._board1.find_cell(x, y)
                print("Board 1: {0}, {1}".format(col, row))
                dealt_with = True
            elif e.action == "Board2":
                x, y = e.pos
                col, row = self._board2.find_cell(x, y)
                print("Board 2: {0}, {1}".format(col, row))
                dealt_with = True
            elif e.action == "Highlight":
                self._board1.highlight_cells([(self._highlight, self._highlight)], self._highlight_on)
                self._board2.highlight_cells([(7-self._highlight, self._highlight)], self._highlight_on)
                if self._highlight == 7:
                    self._highlight_on = not self._highlight_on
                self._highlight = (self._highlight + 1) % 8
                dealt_with = True
        return dealt_with
        

### --------------------------------------------------

class TestPyGameApp(PyGameApp):
    def init(self):
        super().init((1200, 600))
        pygame.display.set_caption("Test cdkkSpriteExtra")
        self.background_fill = "burlywood"
        self.add_sprite_mgr(Manager_TestSprite())
        self.event_mgr.keyboard_event(pygame.K_q, "Quit")
        self.event_mgr.keyboard_event(pygame.K_h, "Highlight")

### --------------------------------------------------

theApp = TestPyGameApp()
theApp.execute()
