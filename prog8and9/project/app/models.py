from django.db import models
from django.forms import ModelForm

# Meeting Model
class Meeting(models.Model):
    meeting_code = models.CharField(max_length=100)
    meeting_dt = models.DateField(auto_now_add=True)
    meeting_subject = models.CharField(max_length=100)
    meeting_np = models.IntegerField()

    def __str__(self):
        return f"{self.meeting_code} - {self.meeting_subject}"

# Course Model
class Course(models.Model):
    course_code = models.CharField(max_length=40)
    course_name = models.CharField(max_length=100)
    course_credits = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.course_name

# Student Model
class Student(models.Model):
    student_usn = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_sem = models.IntegerField()
    enrolment = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.student_name} ({self.student_usn})"

# Project Model
class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptopic = models.CharField(max_length=200)
    plangauges = models.CharField(max_length=200)
    pduration = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.ptopic}"

# Project Registration Form
class ProjectReg(ModelForm):
    required_css_class = "required"

    class Meta:
        model = Project
        fields = ['student', 'ptopic', 'plangauges', 'pduration']
