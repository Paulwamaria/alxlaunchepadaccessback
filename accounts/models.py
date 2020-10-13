from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    """
    
    Returns a new user after legit registration credentials are provided.


    Args:
        BaseUserManager (class): An inbuild class in django for managing user accounts.

    Returns:
        User: returns and saves a user object in the database.
    """

    def create_user(self, email, firstName, lastName, password=None):
        if not email:
            raise ValueError("Users must have a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, firstName=firstName, lastName=lastName)

        user.set_password(password)
        user.save()
        return user

    # def create_superuser():
    #     pass


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    
    Validates registration data and instantiates the UserAccountManager


    Args:
        AbstractBaseUser (Inbuilt class): The inbuild classs for customizable models.
        PermissionsMixin ([type]): [description]

    Returns:
        Object: returns a user object.
    """
    email = models.EmailField(max_length=100, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        
        """
        
        Returns the object representation.
        Returns:
            email: Returns the email address of the requested user object.
        """
        return self.email
