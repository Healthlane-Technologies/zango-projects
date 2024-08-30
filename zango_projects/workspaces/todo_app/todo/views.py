from ..packages.crud.base import BaseCrudView
from .tables import TodoTable
from .forms import NoteForm
from .workflow import TodoWorkflow
\
class TodoCrudView(BaseCrudView):
    """
    Defines a CRUD (Create, Read, Update, Delete) view for managing Todo items.

    This class inherits from BaseCrudView and provides a user interface for interacting
    with Todo items, including viewing a list of items, adding new items, and managing
    existing ones.

    Attributes:
        page_title (str): The title displayed at the top of the page, set to "Todo list".
        add_btn_title (str): The text displayed on the button for adding new items, 
                             set to "New todo item".
        table (TodoTable): The table configuration used to display the list of Todo items.
        form (NoteForm): The form used for creating and editing Todo items.
        workflow (TodoWorkflow): The workflow that manages the state transitions of Todo items.

    Methods:
        display_add_button_check(request): Determines whether to display the 'Add' button.
                                           Currently always returns True, but can be customized
                                           with specific logic.

    This view combines the TodoTable for displaying items, the NoteForm for adding/editing items,
    and the TodoWorkflow for managing item states, providing a complete interface for
    Todo item management.

    Complete docs can be found here: https://www.zango.dev/docs/crud/category/crud-view
    """
    page_title = "Todo list"
    add_btn_title = "New todo item"
    table = TodoTable
    form = NoteForm
    workflow = TodoWorkflow

    def display_add_button_check(self, request):
        # Add your logic here
        return True