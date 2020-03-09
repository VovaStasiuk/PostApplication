from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from ..utils import email_verification, additional_info


from rest_framework import serializers

User = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    new_password = serializers.CharField(
        required=False,
        write_only=True,
        allow_blank=True,
        allow_null=True,
    )
    new_password_confirm = serializers.CharField(
        required=False,
        write_only=True,
        allow_blank=True,
        allow_null=True,
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'new_password',
                  'new_password_confirm', )

    def create(self, validated_data):

        new_password = validated_data.pop('new_password', None)
        new_password_confirm = validated_data.pop('new_password_confirm', None)
        print(new_password)
        if not new_password or new_password != new_password_confirm:
            print(new_password, new_password_confirm)
            raise ValidationError('Password Confirmation Error')

        if not email_verification(validated_data['email']):
            raise ValidationError("Your email verification isn't successful")

        data = additional_info(validated_data['email'])
        if data:
            validated_data['first_name'] = data['givenName']
            validated_data['second_name'] = data['familyName']
        validated_data['password'] = make_password(new_password)
        instance = super().create(validated_data)
        instance.save()
        return instance
