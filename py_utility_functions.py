import traceback


class PyUtilityFunctions:

    @staticmethod
    def print_traceback():
        for line in traceback.format_stack():
            print(line.strip())

    # region Python Program/Script Profiling and Performance Analysis

    def get_current_ram_usage(self):
        pass

    def get_current_cpu_usage(self):
        pass

    def get_current_disk_usage(self):
        pass

    def get_current_time_running(self):
        pass

    # endregion
