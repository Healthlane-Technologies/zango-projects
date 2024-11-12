from ..packages.crud.forms import BaseForm
from ..packages.crud.form_fields import ModelField

from .models import Note

class NoteForm(BaseForm):
    """
    Defines a form for creating and editing Note objects.

    This class inherits from BaseForm and provides a user interface for inputting
    or modifying Note data. It includes fields for the title and description of a Note.

    Attributes:
        title (ModelField): A field for entering the title of the Note.
            It is marked as required and includes a placeholder and error message.
        description (ModelField): A field for entering the description of the Note.
            It is also required and includes a placeholder and error message.

    Meta:
        title (str): Specifies the title of the form as "Notes".
        model (Model): Associates this form with the Note model.

    The form ensures that both title and description are provided by the user
    when creating or editing a Note, with clear placeholders and error messages
    to guide user input.

    Complete docs can be found here: https://www.zango.dev/docs/crud/forms/overview
    """
    title = ModelField(placeholder="Enter Title ", required=True, required_msg="This field is required.")
    description = ModelField(placeholder="Enter description", required=True, required_msg="This field is required.")

    class Meta:
        title = "Notes"
        model = Note