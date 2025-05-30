### Models.py
```pyhton
from django.db import models

# Create your models here.
class Countries(models.Model):
    shortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

class States(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()


class Cities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()
```

### Urls.py
```python
urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/fetch-states', views.fetchState, name ='fetch_states'),
    path('ajax/fetch-city', views.fetchCity, name ='fetch_city'),
]
```
### view.py
```python
from django.template import loader
from .models import Countries, States, Cities
from django.core import serializers
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
	# return HttpResponse('first page')
	# return render(request, 'index.html')
	mydata = Countries.objects.all()
	template = loader.get_template('index.html')
	context = {
		'countries': mydata,
	}
	return HttpResponse(template.render(context, request))
	# return render(request, 'index.html', context)

def fetchState(request):
	if request.method == "POST":
		countryId = request.POST.get('country_id')
		stateData = States.objects.filter(country_id=countryId)
		state_data = [{'id': state.id, 'name': state.name} for state in stateData]
		# serialized_states = serializers.serialize('json', stateData)
		return JsonResponse({'states': state_data})
	# return HttpResponse(stateData)



def fetchCity(request):
	stateId = request.POST.get('state_id')
	cityData = Cities.objects.filter(state_id=stateId)
	city_data = [{'id': city.id, 'name': city.name} for city in cityData]
	return JsonResponse({'city': city_data})
```

### Html
```python
<select name="country" class="form-control" id="country-dropdown">
<option value="">-- Select Country --</option>
{% for country in countries %}
    <option value="{{ country.id }}">{{ country.name }}</option>
{% endfor %}
</select>

<select id="state-dropdown" class="form-control">
<option value="">-- Select State --</option>
</select>

<select name="city" class="form-control" id="city-dropdown">
<option value="">-- Select City --</option>
</select>

<script type="text/javascript">
$("document").ready( function () {

  $('#country-dropdown').on('change', function() {
      var country_id = this.value;
      $.ajax({
          url: "{% url 'fetch_states' %}",
          type: "POST",
          headers: {
              'X-CSRFToken': '{{ csrf_token }}'
          },
          data: {
              country_id: country_id
          },
          cache: false,
          success: function(result) {
            $("#state-dropdown").empty();
            $('#state-dropdown').html('<option value="">-- Select State --</option>');
            $.each(result.states, function(index, item) {
              $("#state-dropdown").append('<option value="' + item.id + '">' + item.name + '</option>');
            });            
          },
          error: function(error) {
              console.log('Error:', error);
          }
      });
  });

  $('#state-dropdown').on('change', function() {
    var state_id = this.value;
    $.ajax({
        url: "{% url 'fetch_city' %}",
        type: "POST",
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
        data: {
            state_id: state_id
        },
        cache: false,
        success: function(result) {
          $("#city-dropdown").empty();
          $('#city-dropdown').html('<option value="">-- Select City --</option>');
          $.each(result.city, function(index, item) {
            $("#city-dropdown").append('<option value="' + item.id + '">' + item.name + '</option>');
          });            
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
  });


}); 

</script>
```