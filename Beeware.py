import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def button_handler(widget):
    print("Butona Tıklandı!!")
    widget.text="Tıklandınız!"

class HelloWorldApp(toga.App):

    def startup(self):
        main_box=toga.Box(style=Pack(dirention=COLUMN, aligment=CENTER))

        button=toga.Button("Merhaba beeware!", on_press=button_handler, style=Pack(padding=10))

        main_box.add(button)

        self.main.window = toga.MainWindow(title=self.name)
        self.main.window = main_box
        self.main.window.show()

def main():
    return HelloWorldApp('Merhaba beeware', 'org.beeware.helloworld')

if __name__=='__main__':
    main().main_loop()   
