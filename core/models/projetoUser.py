from django.db import models
from .user import User
from .projeto import Projeto

class UserProjeto(models.Model):
    client_user = models.ForeignKey(User, related_name="client_projects", on_delete=models.CASCADE)
    freelancer_user = models.ForeignKey(User, related_name="freelancer_projects", on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, related_name="user_projects", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User Projeto"
        verbose_name_plural = "User Projetos"
        unique_together = ["client_user", "freelancer_user", "projeto"]

    def __str__(self):
        return f"UserProjeto - Client: {self.client_user.username}, Freelancer: {self.freelancer_user.username}, Projeto: {self.projeto.titulo}"
