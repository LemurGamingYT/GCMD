from typing import Dict
from main import Args
from os import mkdir


def create_file(filename: str, *, content: str = None) -> None:
    with open(filename, "w") as fp:
        if content is not None:
            fp.write(content)


def create_directory(name: str, *, children: Dict[str, str] = None) -> None:
    try:
        mkdir(name)
    except FileExistsError:
        return "Directory already exists."
    
    for child in children:
        if "." not in child:
            mkdir(f"{name}/{child}")
            for child2 in children[child]:
                create_file(f"{name}/{child}/{child2}", content=children[child][child2])
        else:
            create_file(f"{name}/{child}", content=children[child])
    
    return "Created programming language base."


supported_languages = {
    "Python": {"main.py": """from sys import argv as _argv

def main(argv: list):
    print('Hello World!')

if __name__ == '__main__':
    main(_argv)
"""},
    
    "Java": {"out": {}, "lib": {}, "src": {"main.java": """public class Main {
    public static void main(String[] args) {
        System.out.println('Hello World!');
    }
}
"""}},
    
    "JavaScript" : {"main.js": "console.log('Hello World!')"},
    
    "C": {"include": {"main.h": "// header"}, "main.c": """#include <stdio.h>

int main(int argc, char *argv[]) {
    printf('Hello World!');
    return 0;
}
"""},
    
    "C++": {"include": {"main.hpp": "// header"}, "main.cpp": """#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
    cout << 'Hello World!' << endl;
    return 0;
}
"""}
}

def _setupProject(args: Args) -> str:
    programming_language = args.get(1)
    
    if programming_language not in supported_languages:
        return "Language not supported for 'setupProject' command."
    elif programming_language is None:
        return "An unknown error occurred."
    
    name = args.get(2)
    
    if name is None:
        return "An unknown error occurred."
    
    return create_directory(f"{args.guiself.current_directory}/{name}",
                     children=supported_languages[programming_language])
