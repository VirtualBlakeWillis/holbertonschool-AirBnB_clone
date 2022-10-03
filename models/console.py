#!/usr/bin/python3
import cmd
""" this is the model for the command interpreter """
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    """" This is the class for the interpreter """
    def do_quit(self, args):
        """ this quits the interpreter if user types quit"""
        quit()
    def do_EOF(self, args):
        """ exits interpreter if user inputs ctr+D """
        print()
        raise SystemExit
    def do_create(self, arg):
        """ creates new instance of BaseModel """
        if len(arg) < 0:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()