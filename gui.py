import tkinter as tk

class gui_c():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Waka Ama")
        self.current_frame = None
        self.show_HomeScreen()

    def show_HomeScreen(self):
        # Define and display your Home Screen here
        if self.current_frame:
            self.current_frame.destroy()  # Destroy current frame if exists
        self.current_frame = tk.Frame(self.root)
        # Add widgets (labels, buttons, etc.) to self.current_frame
        # Example:
        label = tk.Label(self.current_frame, text="Welcome to Waka Ama App!")
        label.pack()
        self.current_frame.pack()

    def show_SelectYearScreen(self):
        # Define and display your Select Year Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Select Year Screen
        self.current_frame.pack()

    def show_ErrorScreen(self):
        # Define and display your Error Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Error Screen
        self.current_frame.pack()

    def show_LoadingScreen(self):
        # Define and display your Loading Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Loading Screen
        self.current_frame.pack()

    def show_ExitConfirmation(self):
        # Define and display your Exit Confirmation Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Exit Confirmation Screen
        self.current_frame.pack()

    def show_HelpScreen(self):
        # Define and display your Help Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Help Screen
        self.current_frame.pack()

    def show_Successful_SaveResultsScreen(self):
        # Define and display your Successful Save Results Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Successful Save Results Screen
        self.current_frame.pack()

    def show_LogsScreen(self):
        # Define and display your Logs Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Logs Screen
        self.current_frame.pack()

    def show_ResultsScreen(self):
        # Define and display your Results Screen here
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        # Add widgets for Results Screen
        self.current_frame.pack()
