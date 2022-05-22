from django.db import models

from usr.models import Customers, CusRoot, CusGroup


class Subjects(models.Model):
    subject_name = models.CharField(max_length=30)
    culture = models.CharField(max_length=15)
    short_description = models.CharField(max_length=8)
    subject_for_level_name = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=10)
    entry_status = models.CharField(max_length=5)


class Topics(models.Model):
    topic_level_name = models.CharField(max_length=30)
    topic_level_value = models.CharField(max_length=30)
    fk_subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    topic_num_on_level = models.CharField(max_length=30)
    topic_name = models.CharField(max_length=20)
    creation_dt = models.DateField(max_length=26)
    tackles_total = models.CharField(max_length=20)
    tackles_failed = models.CharField(max_length=20)
    tough_scale = models.CharField(max_length=2)
    entry_status = models.CharField(max_length=15)


class Quests(models.Model):
    fk_topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    Description = models.CharField(max_length=200)
    correct_ans_desc = models.CharField(max_length=150)
    has_diag_flg = models.CharField(max_length=4)
    has_diag_url = models.CharField(max_length=50)
    has_more_ans_flg = models.CharField(max_length=2)
    reviewed_times = models.CharField(max_length=2)
    relates_to_other_que = models.CharField(max_length=2)
    relates_to_other_pos = models.CharField(max_length=2)
    review_sts = models.CharField(max_length=2)
    tackles_total = models.CharField(max_length=20)
    tackles_failed = models.CharField(max_length=20)
    tough_scale = models.CharField(max_length=2)
    marks_allocated = models.CharField(max_length=2)
    creation_dt = models.DateField(max_length=30)
    fk_created_usr = models.ForeignKey(Customers, on_delete=models.CASCADE)
    fk_creator_host_org = models.ForeignKey(CusRoot, on_delete=models.CASCADE)
    update_dt = models.DateField(max_length=30)
    fk_updater_by = models.CharField(max_length=30)
    fk_updater_host = models.CharField(max_length=30)


class QAnswers(models.Model):
    fk_que = models.ForeignKey(Quests, on_delete=models.CASCADE)
    ans_position = models.CharField(max_length=4)
    correct_flg = models.CharField(max_length=2)
    description = models.CharField(max_length=100)
    ans_is_diag_flg=models.CharField(max_length=2)
    ans_is_diag_url = models.CharField(max_length=50)


class ExamSet(models.Model):
    fk_cus_grp = models.ForeignKey(CusGroup, on_delete=models.CASCADE)
    fk_host_org = models.ForeignKey(CusRoot, on_delete=models.CASCADE)
    exam_set_name = models.CharField(max_length=30)
    max_papers = models.CharField(max_length=2)
    fk_exam_set_creator = models.ForeignKey(Customers, on_delete=models.CASCADE)
    create_timestamp = models.DateTimeField(max_length=20)
    expiry_timestamp = models.DateTimeField(max_length=30)
    active_flag = models.CharField(max_length=2)


class ExamPaper(models.Model):
    fk_exam_set = models.ForeignKey(ExamSet, on_delete=models.CASCADE)
    fk_subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    que_num_on_paper = models.CharField(max_length=2)
    max_ques_on_pp = models.CharField(max_length=2)
    quests_sn = models.ForeignKey(Quests, on_delete=models.CASCADE)
    fk_exam_pp_creator = models.ForeignKey(Customers, on_delete=models.CASCADE)
    create_timestamp = models.DateTimeField(max_length=20)
    expiry_timestamp = models.DateTimeField(max_length=30)
    active_flag = models.CharField(max_length=2)


class MarkedPapers(models.Model):
    fk_exam_set = models.ForeignKey(ExamSet, on_delete=models.CASCADE)
    fk_subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    fk_candidate_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    que_num_on_paper = models.CharField(max_length=2)
    max_ques_on_pp = models.CharField(max_length=2)
    quests_sn = models.ForeignKey(Quests, on_delete=models.CASCADE)
    answer_id_given = models.ForeignKey(QAnswers, on_delete=models.CASCADE)
    mark_result = models.CharField(max_length=1)
    marks_given = models.CharField(max_length=2)
    que_rated_flag = models.CharField(max_length=1)
    topic_rated_flag = models.CharField(max_length=1)




