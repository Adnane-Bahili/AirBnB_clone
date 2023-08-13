#!/usr/bin/python3
"""Python Class CommandConsole for Airbnb Clone"""

import cmd
from datetime import datetime
import models
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """Contain the commmanns of ours console."""
    prompt = '(hbnb) '

    def precmd(self, line):
        return line.strip()

    def emptyline(self):
        """If line is empty don't do anything."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file. Exits the console."""
        return True

    def do_create(self, line):
        """Create un object instance."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[line]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
         based on class name and id."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy: Deletes an instance based on the class name and id."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances on the class name.
        If the class doesn't exist will print to the screen."""
        if len(line) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if line in k])

    def do_update(self, line):
        """Updates an instance based on the class name and id, by adding or
        updating attribute on json file."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
                                else:
                                    obj.save()
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """Count the number of instances of class."""
        if len(line) == 0:
            print(len([str(v) for v in models.storage.all().values()]))
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print(len([str(v) for k, v in models.storage.all().items()
                       if line in k]))

    def do_BaseModel(self, line):
        """Usage: cmd can be any of: all, show, update, destroy, or create."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'BaseModel', args]))

    def do_User(self, line):
        """Usage: User. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'User', args]))

    def do_State(self, line):
        """Usage: State. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'State', args]))

    def do_City(self, line):
        """Usage: City. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'City', args]))

    def do_Amenity(self, line):
        """Usage: Amenity. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Amenity', args]))

    def do_Place(self, line):
        """Usage: Place. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Place', args]))

    def do_Review(self, line):
        """Usage: Review. cmd."""
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Review', args]))


def parse(line):
    """Parse method-like command."""
    pattern = '\.([^.]+)\(|[\s,()]*([^(),]+)[\s,()]*'
    args = re.findall(pattern, line)
    cmd = args[0][0]
    try:
        args = args[1:]
    except IndexError:
        line = ''
    else:
        line = ' '.join(map(lambda x: x[1].strip('"'), args))
    return cmd, line


if __name__ == '__main__':
    """Loop"""
    HBNBCommand().cmdloop()
