from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,  password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    phone_regex = RegexValidator(regex=r'^[+]{1}[0-9]{12}$', message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")
    mobile = models.CharField(_("mobile"), unique=True,validators=[phone_regex], max_length=13)
    first_name = models.CharField(_("first name") , max_length=60 , null=True)
    last_name = models.CharField(_("last name") , max_length=60, null=True)
    image = models.ImageField(_("avatar"), upload_to='user/avatars', blank=True, )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['full_name']
    objects = UserManager()

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the user full_name.
        """
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    


class Address(models.Model):
    user = models.ForeignKey(User,related_name='address', verbose_name=_("User") 
                            ,on_delete=models.CASCADE)
    city = models.CharField(_("city"), max_length=60, null=False , blank=False )
    street = models.CharField(_("street"), max_length=60, )
    allay = models.CharField(_("allay"), max_length=60,  )
    zip_code = models.IntegerField(_("zip code"), null=False , blank=False )
    

class Shop(models.Model):
    user = models.ForeignKey(User,related_name='shop', verbose_name=_("User") 
                        ,on_delete=models.CASCADE)
    name = models.CharField(_("name") , max_length=120)
    discription = models.TextField(_("discription"), max_length=400)
    image = models.ImageField(_("avatar"), upload_to='shop/logo', blank=True, )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

