from django.db import models

class Project(models.Model):
    # Creation_date = models.DateTimeField('Date', auto_now_add=True)
    Project_name = models.TextField(max_length=255)
    Project_desc = models.TextField(max_length=3500)
    Project_img = models.ImageField()
    Skills = models.TextField(max_length=140, default='SOME STRING')
    Project_no = models.TextField(max_length=140, default='SOME STRING')
    # class Meta:
    #     ordering = ('creation_date',)


    def __repr__(self):
        Project_name = self.Project_name.replace(" ", "-")
        return Project_name


