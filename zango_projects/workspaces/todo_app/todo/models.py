from zango.apps.dynamic_models.models import DynamicModelBase
from django.db import models


class Note(DynamicModelBase):
    """
    Represents a Note in the db, inheriting from DynamicModelBase.

    This class defines the structure and behavior of Note objects, including
    their attributes and possible statuses.
    
    Attributes:
        COMPLETED (str): Constant representing the 'completed' status.
        IN_PROGRESS (str): Constant representing the 'in_progress' status.
        ON_HOLD (str): Constant representing the 'on_hold' status.
        CANCELED (str): Constant representing the 'canceled' status.

        NOTE_STATUS_CHOICES (list): A list of tuples defining the possible
                                    status choices for a Note.

    Fields:
        title (CharField): The title of the Note, limited to 100 characters.
        description (TextField): An optional description of the Note.
        status (CharField): The current status of the Note, chosen from
                            NOTE_STATUS_CHOICES. Defaults to IN_PROGRESS.

    Methods:
        __str__(): Returns a string representation of the Note, using its title.

    Usage:
        This model defines how a Note object will be stored in the database.
    """
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"

    NOTE_STATUS_CHOICES = [
        (COMPLETED, "Completed"),
        (IN_PROGRESS, "In progress"),
        (ON_HOLD, "On hold"),
        (CANCELED, "Canceled")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=NOTE_STATUS_CHOICES, default=IN_PROGRESS)

    def __str__(self):
        return self.title