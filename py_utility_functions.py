import traceback


class PyUtilityFunctions:

    @staticmethod
    def print_traceback():
        for line in traceback.format_stack():
            print(line.strip())
