#!/bin/bash

# Version: 0.2.0

import argparse
from ast import arg
import os

STACKS_FOLDERPATH = "/docker"

def execute_command(stack, action):
    stack_folderpath = os.path.join(STACKS_FOLDERPATH, stack)
    stack_yml = os.path.join(stack_folderpath, f"{stack}.yml")

    if not os.path.isfile(stack_yml):
        return

    msg = f"Stack path: {stack_yml}"
    print(msg)

    cmd = f"""/usr/bin/docker compose --file "{stack_folderpath}/{stack}.yml" \
        --file "{stack_folderpath}/compose.override.yml" \
        --env-file "{STACKS_FOLDERPATH}/global.env" \
        --env-file "{stack_folderpath}/{stack}.env" {action}"""

    # On lance en mode détaché si on lance en up
    if action == "up":
        cmd += " -d"

    os.system(cmd)

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("action", help="up | down | list")
    argument_parser.add_argument("--stack", help="")
    args = argument_parser.parse_args()

    stacks = [
        stack_folder for stack_folder in os.listdir(STACKS_FOLDERPATH) 
        if os.path.isdir(os.path.join(STACKS_FOLDERPATH, stack_folder)) and
        not stack_folder.startswith(".")
    ]

    # Tri par ordre alphabétique
    stacks.sort()

    if args.action == "list":
        msg = " ".join(stacks)
        print(msg)
        exit()

    elif args.action not in ["up", "down"]:
        argument_parser.print_help()
        exit()

    # Si on défini une stack unique
    if args.stack:
        execute_command(args.stack, args.action)
        exit()


    stacks_count = len(stacks)
    for stack_index, stack in enumerate(stacks):
        msg = f"\n[{stack_index+1}/{stacks_count}] {stack}"
        print(msg)

        execute_command(stack, args.action)


if __name__ == "__main__":
    main()