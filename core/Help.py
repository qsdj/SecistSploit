# coding:utf-8
from xml.sax.saxutils import escape
global_help = escape("""Global commands:
        help                        Print this help menu
        use <module>                Select a module for usage
        exec <shell command> <args> Execute a command in a shell
        search <search term>        Search for appropriate module
        exit                        Exit SecistSploit""")
module_help = escape("""Module commands:
        run                                 Run the selected module with the given options
        back                                De-select the current module
        set <option name> <option value>    Set an option for the selected module
        setg <option name> <option value>   Set an option for all of the modules
        unsetg <option name>                Unset option that was set globally
        show [info|options|devices]         Print information, options, or target devices for a module
        check                               Check if a given target is vulnerable to a selected module's exploit""")


