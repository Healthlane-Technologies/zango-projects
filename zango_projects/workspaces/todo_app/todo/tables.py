
from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol

from .models import Note
from .forms import NoteForm

class TodoTable(ModelTable):
    """
    Defines a table representation for Todo items using the ModelTable base class.

    This class configures the display and behavior of a table that shows Todo items,
    including which fields to display, how they should be presented, and what actions
    can be performed on the table rows.

    Attributes:
        id (ModelCol): Configures the 'ID' column (sortable and searchable).
        title (ModelCol): Configures the 'Title' column (sortable and searchable).
        description (ModelCol): Configures the 'Description' column (sortable and searchable).
        status (ModelCol): Configures the 'Status' column (sortable).

    Class Attributes:
        table_actions (list): Defines actions that can be performed on the entire table.
                              Currently empty, indicating no table-wide actions.
        row_actions (list): Defines actions that can be performed on individual rows.
                            Currently includes an 'Edit' action using the NoteForm.

    Meta:
        model (Model): Specifies the model (Note) this table is based on.
        fields (list): Defines the fields from the model to be included in the table.
        row_selector (dict): Configures row selection behavior (currently disabled).

    The table allows sorting and searching on most columns, and provides an edit
    functionality for individual todo items through a form-based action.

    Complete docs can be found here: https://www.zango.dev/docs/crud/tables/overview
    """
    id = ModelCol(display_as='ID', sortable=True, searchable=True)
    title = ModelCol(display_as='Title', sortable=True, searchable=True)
    description = ModelCol(display_as='Description', sortable=True, searchable=True)
    status = ModelCol(display_as='Status', sortable=True)
    
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Note",
            "type": "form",
            "form": NoteForm,
        },
    ]

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'status']
        row_selector = {'enabled': False, 'multi': False}