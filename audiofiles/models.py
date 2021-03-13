from django.db import models

# Create your models here.
class Audio(models.Model):
    """
        This is the base class
        which will be inherited by the following audio files:
        Song, Podcast and Audiobook
    """
    # audio file type
    type = 'Audio'
    # db columns inherited by child classes.
    # title of the file
    title = models.CharField(max_length=100)
    # Duration/length of the audio (specified in seconds)
    duration_in_seconds = models.PositiveIntegerField()
    # Upload date for the file (auto-generated on creation)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    # list of the columns outlined above
    db_columns = ['type', 'id', 'title', 'duration_in_seconds', 'uploaded_on']
    
    def __str__(self):
        # returns a human-readable form of any record insertion
        return self.title
        
    class Meta:
        # sets its abstract field to true
        # to prevent the creation of this base model
        abstract = True

class Song(Audio):
    """
        Handles files of the song type.
        Accessible via the URL:
        audioserver/api/song/
    """
    type = 'Song'

class Podcast(Audio):
    """
        Handles files of the podcast type.
        Accessible via the URL:
        audioserver/api/podcast/
        Provides extra db columns.
    """
    type = 'Podcast'
    # db columns specific to this model
    # Host of the podcast
    host = models.CharField(max_length=100)
    # Participants (no more than 10)
    participants = models.CharField(
        max_length=1020,
        blank=True, null=True, default='',
        help_text = 'Ten participants at most: Demacate each name with a comma'
    )
    # db column aggregate
    db_columns = Audio.db_columns + ['host', 'participants']

class Audiobook(Audio):
    """
        Handles files of Audiobook type.
        Accessible via the URL:
        audioserver/api/song/
        Provides extra db columns.
    """
    type = 'Audiobook'
    # db columns specific to this model
    # Author of the book
    author = models.CharField(max_length=100)
    # The narrator
    narrator = models.CharField(max_length=100)
    # db column aggregate
    db_columns = Audio.db_columns + ['author', 'narrator']