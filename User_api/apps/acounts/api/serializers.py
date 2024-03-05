from rest_framework import serializers

from ..models import User


class Userserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=13, min_length=9, required=True) 
    date_birth = serializers.DateField(required=True)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=65, min_length=8, write_only=True)

    def validate(self, data):
        password2 = data.pop('password2', None)

        if password2:
            if data['password'] != password2:
                raise serializers.ValidationError('As senhas não são iguais')

        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        User_obj = self.Meta.model(**validated_data)
        User_obj.set_password(password)
        User_obj.save()
        
        return User_obj
    

    
    
    
    class Meta:
        model = User
        fields  = (
            'id',
            'name',
            'email',
            'phone',
            'date_birth',
            'password',
            'password2',
            'cretaed_at',
            'updated_at'
        )