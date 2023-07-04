
import unittest
from unittest.mock import MagicMock, patch
from tkinter import Tk, Canvas, Button, Scale
from paintApp import PaintApp

class TestPaintApp(unittest.TestCase):

    def setUp(self):
        self.app = PaintApp()

    # Test if the initial values of pen_color, eraser_color, and pen_size are set correctly
    def test_init_variables(self):
        self.assertEqual(self.app.pen_color, "black")
        self.assertEqual(self.app.eraser_color, "white")
        self.assertEqual(self.app.pen_size, 1)

    # Test if the correct number of color buttons are created for the color bar
    def test_createColorBar(self):
        color_button_count = sum(isinstance(child, Button) for child in self.app.grid_slaves())
        self.assertEqual(color_button_count, len(self.app.colorsTool))

    # Test if the pen color is changed when select_color() is called with a specific color
    def test_select_color(self):
        test_color = "#FF0000"
        self.app.select_color(test_color)
        self.assertEqual(self.app.pen_color, test_color)

    # Test if the eraser is activated by setting the pen color to the eraser color
    def test_eraser(self):
        self.app.eraser()
        self.assertEqual(self.app.pen_color, self.app.eraser_color)

    # Test if the canvas is cleared when the clear() function is called
    @patch("tkinter.Canvas.delete")
    def test_clear(self, mock_delete):
        self.app.clear()
        mock_delete.assert_called_once_with("all")

    # Test if an oval is drawn on the canvas when the paint() function is called with a mock event
    @patch("tkinter.Canvas.create_oval")
    def test_paint(self, mock_create_oval):
        event = MagicMock()
        event.x = 10
        event.y = 10

        self.app.paint(event)

        pen_size = self.app.pen_size_scale.get()
        mock_create_oval.assert_called_once_with(8, 8, 12, 12, fill=self.app.pen_color, outline=self.app.pen_color, width=pen_size)

if __name__ == "__main__":
    unittest.main()
