"""Class for directory listing"""
import datetime
import os
import sys


class Listing:
    """Listing class"""
    @classmethod
    def print_help(cls):
        """
        Help section, print the correct usage of script
        :return: None
        """
        helpfile = open('help.txt', 'r')
        lines = helpfile.readlines()
        helpfile.close()

        for line in lines:
            print(line.strip('\n'))

    @classmethod
    def get_argument(cls):
        """
        Gets command line argument
        :returns: Argument passed as string
        """
        try:
            argument = sys.argv[1]
            # if the argument is help, then print help
            if argument == "help":
                cls.print_help()
                sys.exit(0)
            return argument
        except IndexError:
            cls.print_help()
            sys.exit(0)

    @classmethod
    def list_directory(cls):
        """This function is used to list the directory contents"""
        try:
            # get directory path
            directory_path = cls.get_argument()
            # Change directory to required directory
            os.chdir(directory_path)
            # list out the contents of the directory
            directory_contents = os.listdir(directory_path)
            print('count =', len(directory_contents))
            for content in directory_contents:
                # Stats of the directory content
                contentstat = os.stat(content)
                # Creation date of file/Directory
                creationdate = datetime.datetime.fromtimestamp(
                    contentstat.st_birthtime).strftime('%d %b %Y %H:%M:%S')
                if os.path.isdir(content):
                    print(u'{:<60} {:<5} {:<10}'.format(content, 'D', '-'), creationdate)
                else:
                    # Size of file
                    contentsize = str(contentstat.st_size) + ' KB'
                    print(u'{:<60} {:<5} {:<10}'.format(content, 'F', contentsize), creationdate)
        except FileNotFoundError:
            print("Directory not found")
            cls.print_help()


if __name__ == "__main__":
    Listing().list_directory()
