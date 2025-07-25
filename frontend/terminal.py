from . import color
from .color import rgb

textline = list[tuple[str, rgb]]

def foreground_rgb(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"

def background_rgb(r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m"


class Terminal:
    def __init__(self):
        self.cursorX = 0
        self.cursorY = 0

    
    def move_cursor(self, x: int, y: int) -> None:
        print(f"\033[{y + 1};{x + 1}H", end='')
        self.cursorX = x
        self.cursorY = y

    def clear(self) -> None:
        print("\033[2J\033[H", end='')
        self.cursorX = self.cursorY = 0

    def bold(self):
        print("\033[1m", end='')

    def underline(self):
        print("\033[4m", end='')

    def hide_cursor(self):
        print("\033[?25l", end='')

    def show_cursor(self):
        print("\033[?25h", end='')

    def clear_style(self) -> None:
        print("\033[0m", end='')

    def new_line(self, reserve_x: bool = False) -> None:
        self.move_cursor(self.cursorX if reserve_x else 0, self.cursorY + 1)


    def print(self, text: str = '', x: int | None = None, y: int | None = None, foregr: rgb = (255, 255, 255), \
              backgr: rgb | None = None, bold = False, underline = False, end='\n') -> None:
        
        x = x if (x is not None) else self.cursorX
        y = y if (y is not None) else self.cursorY
        self.move_cursor(x, y)
        
        foregr_code = foreground_rgb(*foregr)
        backgr_code = background_rgb(*backgr) if (backgr is not None) else ''

        if bold:
            self.bold()
        if underline:
            self.underline()

        text += end

        print(f"{foregr_code}{backgr_code}{text}", end=end)

        lines: list[str] = text.split('\n')
        if len(lines) == 1:
            self.cursorX += len(lines[0])
        else:
            self.cursorY += len(lines) - 1
            self.cursorX = len(lines[-1])

        self.cursorX = max(0, self.cursorX)
        self.cursorY = max(0, self.cursorY)

        self.clear_style()
    

    def print_text_line(self, line: textline, x: int | None = None, y: int | None = None) -> None:
        x = x if (x is not None) else self.cursorX
        y = y if (y is not None) else self.cursorY
        self.move_cursor(x, y)
        for att in line:
            text, color = att
            self.print(text, foregr=color, end='')
        self.new_line()


    def input(self, prompt: str = "", x: int | None = None, y: int | None = None, \
              prompt_foregr: rgb = color.WHITE, prompt_backgr: rgb | None = None, \
              input_foregr : rgb = color.WHITE, input_backgr : rgb | None = None, \
              input_bold: bool = False, input_underline: bool = False) -> str:

        self.print(prompt, x, y, prompt_foregr, prompt_backgr, end='')

        foregr_code = foreground_rgb(*input_foregr)
        backgr_code = background_rgb(*input_backgr) if (input_backgr is not None) else ""
        bold_code = "\033[1m" if input_bold else ""
        underline_code = "\033[4m" if input_underline else ""

        print(f"{bold_code}{underline_code}{foregr_code}{backgr_code}", end='')
        answer = input()
        self.clear_style()
        self.new_line()
        return answer   