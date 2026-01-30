from repositories.TodoRepository import TodoRepository

class TodoSortService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def sort_by_title(self):
        self.repository.data.sort(key=lambda t: t.title.lower())

    def sort_by_status(self):
        self.repository.data.sort(key=lambda t: t.is_finished)
