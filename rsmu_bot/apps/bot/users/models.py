from django.db import models
import re

class StudentRaw(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    third_name=models.CharField(max_length=100)
    snils=models.CharField(max_length=11)
    
    
    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.snils}"

class BotUser(models.Model):
    COURSES={
        '1':'Первый курс',
        '2':'Второй курс',
        '3':'Третий курс',
        '4':'Четвертый курс',
        '5':'Пятый курс',
        '6':'Шестой курс'
    }
    first_name=models.CharField(max_length=100,blank=True)
    second_name=models.CharField(max_length=100,blank=True)
    third_name=models.CharField(max_length=100,blank=True)
    snils=models.CharField(max_length=11,blank=True)
    is_auth=models.BooleanField(default=False)
    course=models.CharField(max_length=1,choices=COURSES,blank=True)
    user_id=models.PositiveBigIntegerField(unique=True,blank=True)
    
        
    def snils_authenticate(self, input_snils):
        if re.match(r'^\d{11}$',input_snils):
            try: 
                studentraw = StudentRaw.objects.get(snils=input_snils)
                if input_snils == studentraw.snils:
                    self.snils = input_snils
                    self.first_name = studentraw.first_name
                    self.second_name = studentraw.second_name
                    self.third_name = studentraw.third_name
                    self.is_auth = True
                    self.save()
                    return "Success"
            except Exception as e:
                print(f'Error occured: {e}')
                if str(e) == "StudentRaw matching query does not exist.":
                    return "DoesNotExist"
        else:
            return "FormatError"
        
    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.snils}"
                

        
        
        
    
    
    