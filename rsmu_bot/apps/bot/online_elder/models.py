from django.db import models

# Онлайн Староста главное сообщение
class ElderMessage(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='eldermessage_img',blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Сообщение Онлайн Старосты"
#Кнопки к главному сообщению онлайн старосты.
class ElderMessageButtons(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    elder_message=models.ForeignKey(ElderMessage,on_delete=models.CASCADE)
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='eldermessagebuttons_img',blank=True)
    link=models.CharField(max_length=400,blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))

    def __str__(self):
        return f'{self.title}'
    
    def get_sub_buttons(self):
        sub_buttons = self.subeldermessagebuttons_set.all()
        return sub_buttons if sub_buttons.exists() else False
    
    def get_active(self):
        return ElderMessageButtons.objects.get(state=ElderMessageButtons.MESSAGE_STATES["A"][0],title="Отчисление")
    
    class Meta:
        verbose_name = "Кнопки к сообщению онлайн старосты --- Темы"

class SubElderMessageButtons(models.Model):
    MESSAGE_STATES= {
        "A": "Активно",
        "N": "Неактивно"
    }
    eldermessagebutton=models.ForeignKey(ElderMessageButtons,on_delete=models.CASCADE)
    title=models.CharField(max_length=400)
    message=models.TextField(max_length=4000)
    image=models.ImageField(upload_to='subeldermessagebuttons_img',blank=True)
    link=models.CharField(max_length=400,blank=True)
    state=models.CharField(max_length=1,choices=list(MESSAGE_STATES.items()))

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Кнопки к Подтемам"