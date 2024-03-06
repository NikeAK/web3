from core import Core


class App:
    def __init__(self) -> None:
        self.__core = Core()
        
    def run(self):
        self.__core.initialize()

if __name__ == "__main__":
    app = App()
    app.run()

