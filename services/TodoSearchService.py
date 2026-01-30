from repositories.TodoRepository import TodoRepository

class TodoSearchService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def search_by_title(self, keyword: str):
        keyword = keyword.lower()
        results = [
            todo for todo in self.repository.get_all_todos()
            if keyword in todo.title.lower()
        ]

        if not results:
            print("[!] Todo tidak ditemukan.")
            return

        print("Hasil pencarian:")
        for todo in results:
            print(todo)
