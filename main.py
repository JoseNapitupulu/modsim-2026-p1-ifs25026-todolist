from repositories.TodoRepository import TodoRepository
from services.TodoService import TodoService
from services.TodoSearchService import TodoSearchService
from services.TodoSortService import TodoSortService
from views.TodoView import TodoView

def main():
    todo_repository = TodoRepository()
    todo_service = TodoService(todo_repository)
    todo_view = TodoView(todo_service)

    todo_view.show_todos()

if __name__ == "__main__":
    main()
