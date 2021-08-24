from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    # Этот клас сгенерит форму подобного типа, теги form следует добавлять в шаблоне
    #  <label for="your_name">Your name: </label>
    #  <input id="your_name" type="text" name="your_name" maxlength="100" required>
