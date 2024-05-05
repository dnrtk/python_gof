from abc import ABC, abstractmethod

# 抽象クラス
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def set_text(self, text: str):
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


# 具象クラス
class WindowsButton(Button):
    def click(self):
        print("Windowsボタンがクリックされました")

class MacButton(Button):
    def click(self):
        print("Macボタンがクリックされました")


class WindowsTextBox(TextBox):
    def __init__(self, text: str = ""):
        self._text = text

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str):
        self._text = "WindowsText: {}".format(text)

class MacTextBox(TextBox):
    def __init__(self, text: str = ""):
        self._text = text

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str):
        self._text = "MacText: {}".format(text)


# Windows用Factory
class WindowsFactory(AbstractFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        return WindowsTextBox()


# Mac用Factory
class MacFactory(AbstractFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_textbox(self) -> TextBox:
        return MacTextBox()


def CreateInstance(factory: AbstractFactory):
    print(factory.__class__)
    button = factory.create_button()
    button.click()

    textbox = factory.create_textbox()
    textbox.set_text("text message")
    print(textbox.get_text())
    print("")

if __name__ == "__main__":
    factory = WindowsFactory()
    CreateInstance(factory)

    factory = MacFactory()
    CreateInstance(factory)
