#!/usr/bin/python
import sys
import argparse


def handle_list_command():
    print('list called')
    pass


def handle_new_command(name):
    print('new called with {}'.format(name))
    pass


def handle_test_command():
    pass

command_handlers = {
    'list': handle_list_command,
    'new': handle_new_command,
    'test': handle_test_command,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='python dojo.py')
    subparsers = parser.add_subparsers(dest='command_name', help='List of commands')
    list_parser = subparsers.add_parser('list', help='List all available katas')
    new_parser = subparsers.add_parser('new', help='Create a directory')
    new_parser.add_argument('name', help='Kata name')
    test_parser = subparsers.add_parser('test', help='Run tests for your solution')

    ns = parser.parse_args(sys.argv[1:])
    handler = command_handlers.get(ns.command_name)
    if handler:
        command_args = {k: getattr(ns, k) for k in dir(ns) if not k.startswith('_') and k!='command_name'}
        handler(**command_args)
    else:
        parser.print_usage()
