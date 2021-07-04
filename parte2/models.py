from django.db import models


# Create your models here.


class Contacto(models.Model):
    nome = models.CharField(max_length=20)
    apelido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    telefone = models.CharField(max_length=9)
    ano_nascimento = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} {self.apelido}"


class Quiz(models.Model):
    question1 = models.IntegerField("How many teams race in Formula 1?")
    question2 = models.IntegerField("How many championships has Lewis Hamilton won?")
    question3 = models.IntegerField("Which Team has won the most championships? - 1 -> Mercedez  2 -> Ferrari  3 -> Williams")
    question4 = models.IntegerField("For which team does Nicholas Latifi race for? - 1 -> Williams  2 -> Ferrari  3 -> Red Bull")
    question5 = models.IntegerField("What color is the Ferrari car? - 1 -> Blue  2 -> Red  3-> Green")
    question6 = models.IntegerField("Where is the location of Haas's base? - 1 -> USA  2-> Italy  3-> Germany")
    question7 = models.IntegerField("How many drivers race in a F1 race?")
    question8 = models.IntegerField("How many drivers are from Europe?")
    question9 = models.IntegerField("Who is the oldest driver? - 1 -> Fernando Alonso  2-> Yuki Tsunoda 3-> Kimi Raikkonen ")
    question10 = models.IntegerField("Who is Sebastian Vettel's teammate? - 1 -> Kimi Raikkonen  2-> Lance Stroll 3-> Charles Leclerc")

    def __str__(self):
        return "Quiz"


class Comments(models.Model):
    question1 = models.IntegerField("From 1 to 10 how would you rate the level of clarity in the questions presented in the quizz section of this website?", max_length=10)
    question2 = models.IntegerField("From 1 to 10 how would you rate the level of rigor in the questions presented in the quizz section of this website?", max_length=10)
    question3 = models.IntegerField("Reagarding the website itself how would you qualify(from 1 to 10) the level of precision regarding the information displayed?", max_length=10)
    question4 = models.CharField("Do you think this website covers a wide range of topics related to F1?", max_length=120)
    question5 = models.CharField("Do you believe this website focused on important details about F1. How focused would you say it was from 1 to 10 ?", max_length=120)
    question6 = models.CharField("How useful do you think this website was?", max_length=120)
    question7 = models.CharField("Does this website make sense, as in, the various parts make sense as a whole? Please give us your opinion?", max_length=120)
    question8 = models.CharField("As amazing as this site is i'm sure there are ways we can improve it further. Please give us your ideas on how to improve it?", max_length=120)

    def __str__(self):
        return "Quiz"



