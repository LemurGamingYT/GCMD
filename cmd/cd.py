from main import Args


def _cd(args: Args) -> str:
    new = args.get(1)
    
    if new is None:
        return "An unknown error occurred."
    
    args.guiself.current_directory = new
    args.guiself.cd.configure(text=f"CD: {new}")
    
    return "Command Executed successfully."
