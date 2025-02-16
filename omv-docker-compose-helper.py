#!/bin/bash

# Version: 0.3.0

import argparse
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
        --env-file "{stack_folderpath}/{stack}.env" """

    if action == "show":
        cmd = cmd.strip()
        print(cmd)
        exit()

    cmd += f" {action}"

    # On lance en mode détaché et en supprimant les orphelins si on lance en up
    if action == "up":
        cmd += " --detach --remove-orphans"

    os.system(cmd)

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("action", help="up | down | stop | list | show | pull")
    argument_parser.add_argument("--stack", help="")
    argument_parser.add_argument('--ignore')
    args = argument_parser.parse_args()

    stacks = [
        stack_folder for stack_folder in os.listdir(STACKS_FOLDERPATH) 
        if os.path.isdir(os.path.join(STACKS_FOLDERPATH, stack_folder)) and
        not stack_folder.startswith(".")
    ]

    # Tri par ordre alphabétique
    stacks.sort()

    if args.ignore:
        ignore_list = args.ignore.split(",")

        for stack in ignore_list:
            if stack not in stacks:
                msg = f"Stack not found: {stack}"
                print(msg)
                exit()

        # Filtrage
        stacks = [stack for stack in stacks if stack not in ignore_list]

    if args.action == "list":
        msg = " ".join(stacks)
        msg = f"{msg}\n{len(stacks)} stacks"
        print(msg)
        exit()

    elif args.action not in ["up", "down", "stop", "show", "pull"]:
        argument_parser.print_help()
        exit()

    # Si on défini une stack unique
    if args.stack:
        execute_command(args.stack, args.action)
        exit()

    for stack_index, stack in enumerate(stacks):
        msg = f"\n[{stack_index+1}/{len(stacks)}] {stack}"
        print(msg)

        execute_command(stack, args.action)


if __name__ == "__main__":
    main()