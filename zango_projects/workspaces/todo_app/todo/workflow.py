from ..packages.workflow.base.engine import WorkflowBase

from .models import Note


class TodoWorkflow(WorkflowBase):
    """
    Defines the workflow for managing todo items with various status transitions.

    This class inherits from WorkflowBase and implements a state machine for todo items,
    allowing transitions between different statuses such as in progress, completed, 
    on hold, and canceled.

    Attributes:
        status_transitions (list): A list of dictionaries defining possible status 
            transitions, including names, descriptions, and confirmation messages.

    Methods:
        progress_to_completed_done: Marks a todo item as completed.
        progress_to_hold_done: Puts a todo item on hold.
        hold_to_progress_done: Marks an on-hold todo item as in progress.
        progress_to_cancelled_done: Marks an in-progress todo item as canceled.
        hold_to_cancelled_done: Marks an on-hold todo item as canceled.

        Note:
            methods with name ending with '_done' after an status transitions name
            runs after that transition has been successfully completed. For example,
            In case of progress to completed transition, we have defined a method
            progress_to_completed_done which runs when we change the state of the
            item from in progress to completed. Inside progress_to_completed_done
            method, we have defined the changes that needs to be done on the note
            object at the database level.

    Meta:
        statuses (dict): Defines the available statuses with their corresponding 
            colors and labels.
        model: Specifies the model class (Note) this workflow is associated with.
        on_create_status (str): Defines the initial status for newly created todo items.

    Usage:
        This class is used to manage the lifecycle of todo items, providing methods
        to transition between different states and defining the visual representation
        of each status.
    
    Complete docs can be found here: https://www.zango.dev/docs/workflow/overview
    """
    status_transitions = [
        {
            "name": "progress_to_completed",
            "display_name": "Mark as completed",
            "description": "Mark this todo item as completed.",
            "from": "in_progress",
            "to": "completed",
            "confirmation_message": "Are you sure you want to mark this todo item as completed?",
        },
        {
            "name": "progress_to_hold",
            "from": "in_progress",
            "to": "on_hold",
            "display_name": "Put on hold",
            "description": "Put this todo item on hold.",
            "confirmation_message": "Are you sure you want to put this todo item on hold?",
        },
        {
            "name": "hold_to_progress",
            "from": "on_hold",
            "to": "in_progress",
            "display_name": "Mark as in progress",
            "description": "Mark this todo item as in progress.",
            "confirmation_message": "Are you sure you want to mark this todo item as in progress?",
        },
        {
            "name": "progress_to_canceled",
            "from": "in_progress",
            "to": "canceled",
            "display_name": "Mark as canceled",
            "description": "Mark this todo item as canceled.",
            "confirmation_message": "Are you sure you want to mark this todo item as canceled?",
        },
        {
            "name": "hold_to_canceled",
            "from": "on_hold",
            "to": "canceled",
            "display_name": "Mark as canceled",
            "description": "Mark this todo item as canceled.",
            "confirmation_message": "Are you sure you want to mark this todo item as canceled?",
        },
    ]


    def progress_to_completed_done(self, request, object_instance, transaction_obj):
        """
        Executes processing logic for the progress to completed status transition.

        Parameters:
            request (HttpRequest): The HTTP request object.
            object_instance (Patient): The instance of the Patient model.
            transaction_obj (TransactionModel): The associated transaction model object.
        """
        # Implement processing logic here
        object_instance.status = Note.COMPLETED
        object_instance.save()


    def progress_to_hold_done(self, request, object_instance, transaction_obj):
        """
        Executes processing logic for the progress to hold status transition.

        Parameters:
            request (HttpRequest): The HTTP request object.
            object_instance (Patient): The instance of the Patient model.
            transaction_obj (TransactionModel): The associated transaction model object.
        """
        # Implement processing logic here
        object_instance.status = Note.ON_HOLD
        object_instance.save()
    
    def hold_to_progress_done(self, request, object_instance, transaction_obj):
        """
        Executes processing logic for the hold to progress status transition.

        Parameters:
            request (HttpRequest): The HTTP request object.
            object_instance (Patient): The instance of the Patient model.
            transaction_obj (TransactionModel): The associated transaction model object.
        """
        # Implement processing logic here
        object_instance.status = Note.IN_PROGRESS
        object_instance.save()
    
    def progress_to_cancelled_done(self, request, object_instance, transaction_obj):
        """
        Executes processing logic for the progress to cancelled status transition.

        Parameters:
            request (HttpRequest): The HTTP request object.
            object_instance (Patient): The instance of the Patient model.
            transaction_obj (TransactionModel): The associated transaction model object.
        """
        # Implement processing logic here
        object_instance.status = Note.CANCELED
        object_instance.save()
    
    def hold_to_cancelled_done(self, request, object_instance, transaction_obj):
        """
        Executes processing logic for the hold to cancelled status transition.

        Parameters:
            request (HttpRequest): The HTTP request object.
            object_instance (Patient): The instance of the Patient model.
            transaction_obj (TransactionModel): The associated transaction model object.
        """
        # Implement processing logic here
        object_instance.status = Note.CANCELED
        object_instance.save()
    

    class Meta:
        statuses = {
            "in_progress": {
                "color": "#00857C",
                "label": "In Progress",
            },
            "completed": {
                "color": "#00FF00",
                "label": "Completed",
            },
            "on_hold": {
                "color": "#FFDB58",
                "label": "On hold",
            },
            "canceled": {
                "color": "#FF0000",
                "label": "Canceled",
            },
        }
        model = Note
        on_create_status = "in_progress"