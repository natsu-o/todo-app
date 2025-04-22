tasks = []

def show_menu():
    print("\n=== ToDoリスト ===")
    print("1. タスクを追加")
    print("2. タスクを表示")
    print("3. タスクを削除")
    print("4. 終了")

def add_task():
    task = input("追加するタスクを入力してください: ")
    tasks.append(task)
    print(f"「{task}」を追加しました。")

def show_tasks():
    if not tasks:
        print("タスクはまだありません。")
    else:
        print("\n【現在のタスク】")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("削除するタスクの番号を入力してください: "))
            removed = tasks.pop(num - 1)
            print(f"「{removed}」を削除しました。")
        except (ValueError, IndexError):
            print("正しい番号を入力してください。")

while True:
    show_menu()
    choice = input("操作を選んでください（1-4）: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("終了します。お疲れさまでした！")
        break
    else:
        print("無効な選択です。1〜4を入力してください。")
