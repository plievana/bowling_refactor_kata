from game import Game


class TestBowlingGame:
    __slots__ = ('_g')

    def setup(self):
        print("setup")
        self._g = Game();

    def _roll_many(self, n: int, pins: int):
        for i in range(0, n):
            self._g.roll(pins)

    def _roll_spare(self):
        self._g.roll(5)
        self._g.roll(5)
    
    def _roll_strike(self):
        self._g.roll(10)
  
    def test_gutter_game(self):
        self._roll_many(20, 0)
        assert 0 == self._g.score()
  
    def test_all_ones(self):
        self._roll_many(20,1)
        assert 20 == self._g.score()

    def test_one_spare(self):
        self._roll_spare()
        self._g.roll(3)
        self._roll_many(17,0)
        assert 16 == self._g.score()

    def test_one_strike(self):
        self._g.roll(10)  # strike
        self._g.roll(3)
        self._g.roll(4)
        self._roll_many(16, 0)
        assert 24 == self._g.score()

    def test_perfect_game(self):
        self._roll_many(12,10)
        assert 300 == self._g.score()
