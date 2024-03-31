# check_commit_msg.py
import re
import sys


def main(commit_msg_filepath):
    pattern = r"^(bug|feature|enhancement|hotfix|doc)\(\d+\): .+"
    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read().strip()
        if not re.match(pattern, commit_msg):
            print(
                "Commit message does not follow the required format: "
                + "'<type>(<issue_number>): <commit message>'"
            )
            print(
                "Where <type> can be one of: "
                + "bug, feature, enhancement, hotfix, doc."
            )
            return 1
    return 0


if __name__ == "__main__":
    exit(main(sys.argv[1]))
