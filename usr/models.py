from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Packages(models.Model):
    pack_name = models.CharField(max_length=30)
    max_cus_1 = models.CharField(max_length=15)
    max_cus_2 = models.CharField(max_length=5)
    max_groups = models.CharField(max_length=10)
    pay_curr = models.CharField(max_length=5)
    payable_amount = models.CharField(max_length=13)
    pay_duration = models.CharField(max_length=10)
    description = models.CharField(max_length=50)


class CusRoot(models.Model):
    org_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    contact_cus = models.CharField(max_length=20)
    creation_dt = models.DateField(max_length=26)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    entry_status = models.CharField(max_length=30)
    org_type = models.CharField(max_length=30)
    org_status = models.CharField(max_length=30)
    fk_pack_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    sales_rep_id = models.CharField(max_length=30)


class CusRootSub(models.Model):
    fk_root_cus = models.ForeignKey(CusRoot, on_delete=models.CASCADE)
    sub_ref_id = models.CharField(max_length=30)
    fiscal_year = models.CharField(max_length=4)
    curr_month = models.CharField(max_length=2)
    sub_status = models.CharField(max_length=2)
    created_by = models.CharField(max_length=20)
    creation_dt = models.DateField(max_length=30)
    updated_by = models.CharField(max_length=20)
    update_dt = models.DateField(max_length=30)


class CusRootTrx(models.Model):
    sub_ref_id = models.CharField(max_length=30)
    fiscal_year = models.CharField(max_length=4)
    curr_month = models.CharField(max_length=2)
    sub_status = models.CharField(max_length=2)
    created_by = models.CharField(max_length=20)
    creation_dt = models.DateField(max_length=30)
    updated_by = models.CharField(max_length=20)
    update_dt = models.DateField(max_length=30)


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=30)
    creation_dt = models.DateField(max_length=30)
    kyc_flag = models.CharField(max_length=1)
    has_doc_type = models.CharField(max_length=1)
    has_doc_value = models.CharField(max_length=26)
    has_org_type = models.CharField(max_length=2)
    has_org_value = models.ForeignKey(CusRoot, on_delete=models.CASCADE)
    has_class_code = models.CharField(max_length=10)
    has_other_class_flg = models.CharField(max_length=2)
    entry_status = models.CharField(max_length=2)
    cus_type = models.CharField(max_length=2)
    cus_status = models.CharField(max_length=2)
    has_badge = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Customers.objects.create(user=instance)
        instance.profile.save()


class CusGroup(models.Model):
    grp_name = models.CharField(max_length=30)
    grp_type = models.CharField(max_length=30)
    grp_level_name = models.CharField(max_length=30)
    grp_level_value = models.CharField(max_length=30)
    fk_cus_root = models.ForeignKey(CusRoot, on_delete=models.CASCADE)
    fk_cus_created_grp = models.CharField(max_length=30)
    grp_create_dt = models.DateField(max_length=30)
    grp_expire_dt = models.DateField(max_length=30)
    entry_status = models.CharField(max_length=30)


class CusRelates(models.Model):
    child_cus = models.ManyToManyField(Customers)
    parent_cus = models.ManyToManyField(CusRoot)
    rel_type = models.CharField(max_length=20)
    create_timestamp = models.DateTimeField(max_length=20)
    expiry_timestamp = models.DateTimeField(max_length=30)
    entry_status = models.CharField(max_length=2)
