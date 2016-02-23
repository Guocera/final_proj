from django import forms

class PlanForm(forms.Form):
  name = forms.CharField(label="Plan name:", max_length=150)
  calories = forms.FloatField(label="Calories (kcal):")
  fat = forms.FloatField(label="Fat (g):", required=False)
  carbohydrates = forms.FloatField(label="Carbohydrates (g):", required=False)
  protein = forms.FloatField(label="Protein (g):", required=False)
  sat_fat = forms.FloatField(label="Saturated Fat (g):", required=False, widget=forms.HiddenInput())
  trans_fat = forms.FloatField(label="Trans Fat (g):", required=False, widget=forms.HiddenInput())
  mono_unsat_fat = forms.FloatField(label="Monounsaturated Fat (g):", required=False, widget=forms.HiddenInput())
  poly_unsat_fat = forms.FloatField(label="Polyunsaturated Fat (g):", required=False, widget=forms.HiddenInput())
  fiber = forms.FloatField(label="Fiber (g):", required=False, widget=forms.HiddenInput())
  sugar = forms.FloatField(label="Sugar (g):", required=False, widget=forms.HiddenInput())
  cholesterol = forms.FloatField(label="Cholesterol (mg):", required=False, widget=forms.HiddenInput())
  sodium = forms.FloatField(label="Sodium (mg):", required=False, widget=forms.HiddenInput())
  calcium = forms.FloatField(label="Calcium (mg):", required=False, widget=forms.HiddenInput())
  magnesium = forms.FloatField(label="Magnesium (mg):", required=False, widget=forms.HiddenInput())
  potassium = forms.FloatField(label="Potassium (mg):", required=False, widget=forms.HiddenInput())
  iron = forms.FloatField(label="Iron (mg):", required=False, widget=forms.HiddenInput())
  zinc = forms.FloatField(label="Zinc (mg):", required=False, widget=forms.HiddenInput())
  phosphorus = forms.FloatField(label="Phosphorus (mg):", required=False, widget=forms.HiddenInput())
  vit_a = forms.FloatField(label="Vitamin A (micro g):", required=False, widget=forms.HiddenInput())
  vit_c = forms.FloatField(label="Vitamin C (mg):", required=False, widget=forms.HiddenInput())
  thiamin = forms.FloatField(label="Thiamin (mg):", required=False, widget=forms.HiddenInput())
  riboflavin = forms.FloatField(label="Riboflavin (mg):", required=False, widget=forms.HiddenInput())
  niacin = forms.FloatField(label="Niacin (mg):", required=False, widget=forms.HiddenInput())
  vit_b6 = forms.FloatField(label="Vitamin B6 (mg):", required=False, widget=forms.HiddenInput())
  folic_acid = forms.FloatField(label="Folic Acid (micro g):", required=False, widget=forms.HiddenInput())
  vit_b12 = forms.FloatField(label="Vitamin B12 (micro g):", required=False, widget=forms.HiddenInput())
  vit_d = forms.FloatField(label="Vitamin D (micro g):", required=False, widget=forms.HiddenInput())
  vit_e = forms.FloatField(label="Vitamin E (mg):", required=False, widget=forms.HiddenInput())
  vit_k = forms.FloatField(label="Vitamin K (micro g):", required=False, widget=forms.HiddenInput())

class PopulateForm(forms.Form):
  terms = forms.CharField(
    label="Recipe terms:",
    max_length=150,
    widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'inputWarning'
    })
  )