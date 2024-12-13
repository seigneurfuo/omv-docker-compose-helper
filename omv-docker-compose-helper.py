#!/bin/bash

# Version: 0.1.1

import argparse
import os

STACKS_FOLDERPATH = "/docker"

def main(args):
    stacks = [
        stack_folder for stack_folder in os.listdir(STACKS_FOLDERPATH) 
        if os.path.isdir(os.path.join(STACKS_FOLDERPATH, stack_folder))
    ]

    stacks_count = len(stacks)
    for stack_index, stack in enumerate(stacks):
        stack_folderpath = os.path.join(STACKS_FOLDERPATH, stack)
        stack_yml = os.path.join(stack_folderpath, f"{stack}.yml")

        if not os.path.isfile(stack_yml):
            continue

        msg = f"\n[{stack_index+1}/{stacks_count}] {stack}: {stack_yml}"
        print(msg)

        cmd = f"""/usr/bin/docker compose --file "{stack_folderpath}/{stack}.yml" \
            --file "{stack_folderpath}/compose.override.yml" \
            --env-file "{STACKS_FOLDERPATH}/global.env" \
            --env-file "{stack_folderpath}/{stack}.env" {args.action}"""

        # On lance en mode détaché si on lance en up
        if args.action == "up":
            cmd += " -d"

        os.system(cmd)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("action", help="up | down")
    args = argument_parser.parse_args()

    if args.action not in ["up", "down"]:
        argument_parser.print_help()
        exit()

    main(args)