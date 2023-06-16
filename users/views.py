from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Views for users app.
def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display a blank form
		form = UserCreationForm()
	else:
		# Process completed form
		form = UserCreationForm(data=request.POST)

		# If there are no errors in the form, save data entered...
		# to the database and log the user in. 
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('pibloggers:index')

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'registration/register.html', context)