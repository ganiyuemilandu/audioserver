from django.test import TestCase
from .models import Song, Podcast, Audiobook

# Create your tests here.

class SongTestCase(TestCase):
    # Song database test
    model = Song
    def setUp(self):
        self.model.objects.create(
            title=self.model.type,
            duration_in_seconds=1000
        )
    def test_song_content(self):
        data = self.model.objects.get(id=1)
        title = f'{data.title}'
        self.assertEqual(title, self.model.type)
        self.assertEqual(data.duration_in_seconds, 1000)

class PodcastTestCase(TestCase):
    # Podcast database test
    model = Podcast
    def setUp(self):
        self.model.objects.create(
            title=self.model.type,
            duration_in_seconds=1000,
            host='Ganiyu',
        )
    def test_podcast_content(self):
        data = self.model.objects.get(id=1)
        title = f'{data.title}'
        duration = data.duration_in_seconds
        host = f'{data.host}'
        self.assertEqual(title, self.model.type)
        self.assertEqual(duration, 1000)
        self.assertEqual(host, 'Ganiyu')

class AudiobookTestCase(TestCase):
    # Audiobook database test
    model = Audiobook
    def setUp(self):
        self.model.objects.create(
            title=self.model.type,
            duration_in_seconds=1000,
            author='Ganiyu',
            narrator='Emilandu'
        )
    def test_podcast_content(self):
        data = self.model.objects.get(id=1)
        title = f'{data.title}'
        duration = data.duration_in_seconds
        author = f'{data.author}'
        narrator = f'{data.narrator}'
        self.assertEqual(title, self.model.type)
        self.assertEqual(duration, 1000)
        self.assertEqual(author, 'Ganiyu')
        self.assertEqual(narrator, 'Emilandu')
