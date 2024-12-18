import flet as ft

def main(page: ft.Page):
    page.title = "To-Do App"
    page.scroll = "adaptive"

    tasks = []  # List to store tasks

    # Function to add a task
    def add_task(e):
        task_text = task_input.value.strip()
        if task_text:
            task = ft.Checkbox(label=task_text, value=False, on_change=update_task_status)
            tasks.append(task)
            task_list.controls.append(task)
            task_input.value = ""
            page.update()

    # Function to update the status of a task
    def update_task_status(e):
        completed_tasks = [task.label for task in tasks if task.value]
        status_label.value = f"Completed: {len(completed_tasks)} / {len(tasks)}"
        page.update()

    # UI Components
    task_input = ft.TextField(hint_text="Enter a task", expand=True)
    add_button = ft.ElevatedButton("Add", on_click=add_task)
    task_list = ft.Column()
    status_label = ft.Text("Completed: 0 / 0")

    # Layout
    page.add(
        ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        task_list,
        status_label,
    )

# Start the Flet app
ft.app(target=main)
