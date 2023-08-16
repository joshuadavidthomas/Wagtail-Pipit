from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create superuser if none exist

    Example:
        manage.py create_superuser_if_none_exists --user=admin --password=123
    """

    def add_arguments(self, parser):
        parser.add_argument("--user", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--email", default="admin@example.com")

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.exists():
            return

        username = options["user"]
        password = options["password"]
        email = options["email"]

        User.objects.create_superuser(  # type: ignore[attr-defined]
            username=username,
            password=password,
            email=email,
        )

        self.stdout.write('Local user "{}" was created'.format(username))
