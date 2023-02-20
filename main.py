from lib import *


class Args:
    def __init__(self, guiself, args: tuple):
        self.args = args
        self.guiself = guiself
    
    def get(self, i: int):
        try:
            return self.args[i - 1]
        except IndexError:
            return None


class Gui(Tk):
    current_directory = getcwd()
    
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs) -> None:
        super().__init__(fg_color, **kwargs)
        
        self.title("GCMD")
        self.geometry("750x500")
        self.resizable(False, False)
        
        self.cmdLine = Entry(self, width=600, height=35, corner_radius=25, fg_color="#282828",
                             placeholder_text="Enter your command", font=("Arial", 15, "bold"))
        self.cmdLine.place(relx=.5, rely=.5, anchor="c")
        
        self.cd = Label(self, font=("Arial", 15, "bold"), text= \
                        f"CD: {self.current_directory}", corner_radius=25)
        self.cd.place(relx=.5, rely=.15, anchor="c")
        
        self.execute_btn = Button(self, font=("Arial", 15, "bold"), text="Execute CMD",
                                  corner_radius=25, fg_color="#282828", hover_color="#262626",
                                  command=self.execute_command)
        self.execute_btn.place(relx=.5, rely=.6, anchor="c")
        
        self.result_lbl = Label(self, font=("Arial", 15, "bold"), text="No Results",
                                corner_radius=25)
        self.result_lbl.place(relx=.5, rely=.7, anchor="c")
    
        
    def execute_command(self) -> None:
        name = self.cmdLine.get().split()[0]
        args = Args(self, tuple(self.cmdLine.get().split()[1:]))
        
        for cmd in listdir(f"{getcwd()}/cmd/"):
            if cmd[:-3] == name:
                exec(f"from cmd.{name} import _{name}; out = _{name}(args)")
                self.result_lbl.configure(text=f"Result: {locals()['out']}")
        

if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
