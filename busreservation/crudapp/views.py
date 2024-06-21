from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crudapp.models import Reservation

def index(request):
    obj = Reservation.objects.filter(delete_flag=False).all()
    return render(request, "index.html",{"object":obj})

@csrf_exempt
def save(request):
    if request.method == "POST":
    #if request.method == "POST" and request.is_ajax():
        fullname = request.POST.get('fullname')
        emailID = request.POST.get('emailID')
        phoneno = request.POST.get('phoneno')
        depart = request.POST.get('depart')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        seats = request.POST.get('seats')
        preference = request.POST.get('preference')

        new_record = Reservation.objects.create(
            full_name=fullname, email=emailID, phone=phoneno, departure_city=depart,
            destination_city=destination, date_of_journey=date, time_of_departure=time,
            number_of_seats=seats, seat_preference=preference
        )

        return JsonResponse({
            'success': True,
            'id': new_record.id,
            'fullname': new_record.full_name,
            'emailID': new_record.email,
            'phoneno':new_record.phone,
            'depart':new_record.departure_city,
            'destination':new_record.destination_city,
            'date':new_record.date_of_journey,
        })
    
    return JsonResponse({'success': False})

def fetch_reservations(request):
    #reservations = Reservation.objects.all().values()
    reservations = Reservation.objects.filter(delete_flag=False).values(
        'id', 'full_name', 'email', 'phone', 'departure_city', 'destination_city', 'date_of_journey'
    )
    reservations_list = list(reservations)  # Convert QuerySet to list
    return JsonResponse({'reservations': reservations_list})

def delete_record(request):
    if request.method == 'POST':
        record_id = request.POST.get('id')
        try:
            record = get_object_or_404(Reservation, id=record_id)
            record.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def update_record(request):
    if request.method == "GET":
        record_id = request.GET.get('id')
        fullname = request.GET.get('fullname')
        emailID = request.GET.get('emailID')
        phoneno = request.GET.get('phoneno')
        depart = request.GET.get('depart')
        destination = request.GET.get('destination')
        date = request.GET.get('date')

        try:
            Reservation.objects.filter(id=record_id).update(
            full_name = fullname,
            email = emailID,
            phone = phoneno,
            departure_city = depart,
            destination_city = destination,
            date_of_journey = date)

            return JsonResponse({'success': True})
        except Reservation.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Reservation not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})