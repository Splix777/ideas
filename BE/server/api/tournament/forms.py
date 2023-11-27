from typing import Any
from django import forms
from .models import Tournament, Match, Round
from api.userauth.models import CustomUser as User

class TournamentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TournamentForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['type'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['round'].required = False
        self.fields['winner'].required = False
        self.fields['players'].required = False
        self.fields['observers'].required = False

    class Meta:
        model = Tournament
        fields = [
            'name',
            'type',
            'start_date', 
            'end_date',
            'round',
            'winner',
            'players',
            'observers'
            ]
        
class MatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['tournament'].required = False
        self.fields['round'].required = False
        self.fields['player1'].required = False
        self.fields['player2'].required = False
        self.fields['winner'].required = False
        self.fields['loser'].required = False
        self.fields['status'].required = False
        self.fields['game'].required = False

    class Meta:
        model = Match
        fields = [
            'tournament',
            'round',
            'player1',
            'player2',
            'winner',
            'loser',
            'status',
            'game'
            ]
        
class RoundForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoundForm, self).__init__(*args, **kwargs)
        self.fields['tournament'].required = False
        self.fields['round_number'].required = False
        self.fields['matches'].required = False

    class Meta:
        model = Round
        fields = [
            'tournament',
            'round_number',
            'matches',
            ]
        
class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False
        self.fields['email'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['is_staff'].required = False
        self.fields['is_active'].required = False
        self.fields['is_superuser'].required = False
        self.fields['date_joined'].required = False
        self.fields['last_login'].required = False
        self.fields['groups'].required = False
        self.fields['user_permissions'].required = False

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name', 
            'last_name',
            'is_staff',
            'is_active',
            'is_superuser',
            'date_joined',
            'last_login',
            'groups',
            'user_permissions'
            ]