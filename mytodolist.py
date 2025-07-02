import json
import os
import argparse

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task: {title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        status = "\u2713" if task.get("done") else " "
        print(f"{i}. [{status}] {task.get('title')}")


def complete_task(index):
    tasks = load_tasks()
    idx = index - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print(f"Completed task: {tasks[idx]['title']}")
    else:
        print("Task index out of range.")


def delete_task(index):
    tasks = load_tasks()
    idx = index - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Task index out of range.")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Todo List")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title")

    sub.add_parser("list", help="List tasks")

    p_done = sub.add_parser("done", help="Mark task as completed")
    p_done.add_argument("index", type=int)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("index", type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list" or args.command is None:
        list_tasks()
    elif args.command == "done":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
