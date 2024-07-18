from django.db import models
from rsmu_bot.apps.bot.users.models import BotUser
from PIL import Image
from PIL.ExifTags import TAGS

class PollsImage(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='polls_images/')
    file_size = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    color_mode = models.CharField(max_length=20, null=True, blank=True)
    bit_depth = models.IntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)
    author_creator = models.CharField(max_length=255, null=True, blank=True)
    copyright = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    poll_number = models.IntegerField()
    state = models.CharField(max_length=20, choices=[
        ('uploaded', 'Uploaded'),
        ('in_processing', 'In Processing'),
        ('processed', 'Processed'),
        ('good', 'Good'),
        ('bad','Bad'),
    ])

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            self.file_size = self.image.size
            self.width, self.height = img.size
            self.color_mode = img.mode
            # Extract metadata
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == 'DateTimeOriginal':
                        self.creation_date = value
                    elif tag_name == 'DateTime':
                        self.modification_date = value
                    elif tag_name == 'Artist':
                        self.author_creator = value
                    elif tag_name == 'Copyright':
                        self.copyright = value
                    elif tag_name == 'ImageDescription':
                        self.description = value

        super(PollsImage, self).save(*args, **kwargs)

    def __str__(self):
        return f'Изображение пользователя с id {self.user} и состоянием {self.state}'

    class Meta:
        verbose_name = "Скрины опросников"