from django.db import models

class WelcomeMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='registration_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Приветственное сообщение"
        

class RegistrationMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='registration_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Сообщение при регистрации"
        
class MainMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='registration_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Главное сообщение"
        
class CurriculumsMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Внеучебная деятельность"
        
class CurriculumsButtons(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    curriculums_message=models.ForeignKey(CurriculumsMessage,on_delete=models.CASCADE)
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='curriculumsbuttons_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Кнопки внеучебной деятельности"


class UnknownMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='registration_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Сообщение если неизвестная команда"