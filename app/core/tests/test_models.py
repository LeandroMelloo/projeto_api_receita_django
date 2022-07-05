"""Teste Models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Teste Models"""

    def test_create_user_with_email_successful(self):
        """
        Teste de criação de um usuário com um email foi bem-sucedido
        """

        email = 'test@example.com'
        name = 'testname'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Teste se email está normalizado para novo usuário
        """

        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Teste que cria um usuário sem um email gera um ValueError
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '123456')

    def test_create_superuser(self):
        """
        Teste criando um superusuário
        """

        user = get_user_model().objects.create_superuser(
            'teste@exemplo.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
