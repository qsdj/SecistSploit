#!/usr/bin/env python
# encoding: utf-8
import threading
import sys
import collections
import warnings
from prompt_toolkit import print_formatted_text, HTML
from weakref import WeakKeyDictionary
from xml.sax.saxutils import escape

try:
    import queue
except ImportError:  # For compatible with Python 2.x
    import Queue as queue
PrinterQueue = queue.Queue()
ThreadOutputStream = WeakKeyDictionary()
PrintResource = collections.namedtuple("PrintResource", ["text", "sep", "end", "file", "thread"])


class PrinterThread(threading.Thread):
    def __init__(self):
        super(PrinterThread, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            text, sep, end, _file, thread = PrinterQueue.get()
            print_formatted_text(text, sep=sep, end=end, file=_file)
            PrinterQueue.task_done()


def print_table(headers, *args, **kwargs) -> None:
    """ Print table.

    example:
    Name            Current setting     Description
    ----            ---------------     -----------
    option_name     value               description
    foo             bar                 baz
    foo             bar                 baz

    :param headers: Headers names ex.('Name, 'Current setting', 'Description')
    :param args: table values, each element representing one line ex. ('option_name', 'value', 'description), ...
    :param kwargs: 'extra_fill' space between columns, 'header_separator' character to separate headers from content
    :return:
    """
    extra_fill = kwargs.get("extra_fill", 5)
    headers_separator = kwargs.get("header_separator", "-")
    if not all(map(lambda x: len(x) == len(headers), args)):
        print_error("Headers and table rows tuples should be the same length.")
        return

    def custom_len(x):
        try:
            return len(x)
        except TypeError:
            return 0

    fill = []
    headers_line = '   '
    headers_separator_line = '   '
    for index, header in enumerate(headers):
        column = [custom_len(arg) for arg in args]
        column.append(len(header))
        current_line_fill = max(column) + extra_fill
        fill.append(current_line_fill)
        headers_line = "".join((headers_line, "{header:<{fill}}".format(header=header, fill=current_line_fill)))
        headers_separator_line = "".join((headers_separator_line,
                                          "{:<>{}}".format(headers_separator * len(header), current_line_fill)))
    print_info()
    print_info(headers_line)
    print_info(headers_separator_line)
    for arg in args:
        content_line = "   "
        for index, element in enumerate(arg):
            content_line = "".join((content_line, "{:<{}}".format(element, fill[index])))
        print_info(content_line)
    print_info()


def print_order_dict(dictionary, order=None) -> None:
    """ Pretty dict print.
    Pretty printing dictionary in specific order. (as in 'show info' command)
    Keys not mentioned in *order* parameter will be printed in random order.
    ex. print_order_dict({'name': John, 'sex': 'male', "hobby": ["rugby", "golf"]}, ('sex', 'name'))

    Sex:
    male
    Name:
    John
    Hobby:
    - rugby
    - golf
    """
    order = order or ()

    def pretty_print(title, body):
        print_info("\n{}:".format(title.capitalize()))
        if not isinstance(body, str):
            for value in body:
                print_info("- ", value)
        else:
            print_info(body)

    keys = list(dictionary.keys())
    for element in order:
        try:
            key = keys.pop(keys.index(element))
            values = dictionary[key]
        except (KeyError, ValueError):
            pass
        else:
            pretty_print(element, values)
    for rest_key in keys:
        pretty_print(rest_key, dictionary[rest_key])


def color_print(string: str, color: str ='', *args, **kwargs ) -> None:
    if not kwargs.pop("verbose", True):
        return
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    thread = threading.current_thread()
    string = escape(string)
    try:
        _file = ThreadOutputStream.get(thread, ())[-1]
    except IndexError:
        _file = kwargs.get("file", sys.stdout)
    text = HTML("<p fg='{color}'>{text}</p>".format(color=color,\
                                                    text=string))
    PrinterQueue.put(PrintResource(text=text, sep=sep, end=end, file=_file, thread=thread))


def color_blue(string: str) -> str:
    """ Returns string colored with blue
    :param str string:
    :return str:
    """
    return color_print(string, 'blue')


def color_green(string: str) -> str:
    """ Returns string colored with green
    :param str string:
    :return str:
    """
    return color_print(string, 'green')



def color_red(string: str) -> str:
    """ Returns string colored with red
    :param str string:
    :return str:
    """
    return color_print(string, 'red')


print_error = color_red

print_success = color_blue

print_status = color_green

print_info = color_print



