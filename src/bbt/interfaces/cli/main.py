"""Main CLI entry point for bbt."""

import argparse
import sys

from bbt.interfaces.cli.transition import cmd_record, cmd_show
from bbt.interfaces.cli.closeout import cmd_closeout


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bbt",
        description="Big Brain Time — Joint Cognitive Control & Continuity System",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # bbt closeout
    closeout_parser = subparsers.add_parser("closeout", help="Conversational voice/chat closeout workflow")
    closeout_parser.add_argument(
        "--project", "-p", default=".", help="Path to project directory (default: current dir)"
    )
    closeout_parser.add_argument("--dump", "-d", default="", help="Raw voice or chat dump text")
    closeout_parser.add_argument(
        "--non-interactive", action="store_true", help="Skip interactive prompts"
    )
    closeout_parser.add_argument(
        "--accept", action="store_true", help="Explicitly accept proposal in non-interactive mode"
    )
    closeout_parser.add_argument(
        "--proposal-only", action="store_true", help="Emit proposal card without prompting for acceptance"
    )

    # bbt transition
    trans_parser = subparsers.add_parser("transition", help="Manage project continuity transitions")
    trans_subparsers = trans_parser.add_subparsers(dest="subcommand", help="Transition action")

    # bbt transition show
    show_parser = trans_subparsers.add_parser("show", help="Compile and display Re-entry Pack")
    show_parser.add_argument(
        "--project", "-p", default=".", help="Path to project directory (default: current dir)"
    )

    # bbt transition record
    rec_parser = trans_subparsers.add_parser("record", help="Record a new project transition")
    rec_parser.add_argument(
        "--project", "-p", default=".", help="Path to project directory (default: current dir)"
    )
    rec_parser.add_argument("--stop-point", "-s", default="", help="Where work stopped")
    rec_parser.add_argument("--next-action", "-n", default="", help="Next physical action")
    rec_parser.add_argument("--purpose", default="", help="Session purpose")
    rec_parser.add_argument("--material-changes", "-c", default="", help="Comma separated material changes")
    rec_parser.add_argument("--open-loops", default="", help="Comma separated open loops")
    rec_parser.add_argument(
        "--non-interactive", action="store_true", help="Skip interactive confirmation prompts"
    )
    rec_parser.add_argument(
        "--accept", action="store_true", help="Explicitly accept proposal in non-interactive mode"
    )

    args = parser.parse_args()

    if args.command == "closeout":
        cmd_closeout(
            project_path=args.project,
            dump=args.dump,
            interactive=not args.non_interactive,
            accept=args.accept,
            proposal_only=args.proposal_only,
        )
    elif args.command == "transition":
        if args.subcommand == "show":
            cmd_show(args.project)
        elif args.subcommand == "record":
            cmd_record(
                project_path=args.project,
                stop_point=args.stop_point,
                next_action=args.next_action,
                purpose=args.purpose,
                material_changes=args.material_changes,
                open_loops=args.open_loops,
                interactive=not args.non_interactive,
                accept=args.accept,
            )
        else:
            trans_parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
