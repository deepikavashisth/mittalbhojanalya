from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SubscribeForm
import urllib.parse

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        order_details = request.POST.get('order_details')

        # Format the message for WhatsApp
        message_text = f"📦 New Order!\n👤 Name: {name}\n📞 Phone: {phone}\n📝 Order: {order_details}"
        encoded_text = urllib.parse.quote(message_text)

        whatsapp_number = "919599090897"  

        whatsapp_link = f"https://wa.me/{whatsapp_number}?text={encoded_text}"

        # Redirect the user to WhatsApp
        return redirect(whatsapp_link)

    return render(request, 'order.html')


def ajax_subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'invalid_method'})


def index(request):
    menu_items = {
        'Momos': [
            {'name': 'Chilly Garlic Momos', 'price': '₹130', 'image': 'chilly_garlic_momos.jpg'}
        ],
        'Soup': [
            {'name': 'Veg Manchow Soup', 'price': '₹60', 'image': 'veg_manchow_soup.jpg'},
        ],
        'Burger': [
            {'name': 'Veg Burger', 'price': '₹40', 'image': 'veg_burger.jpg'}
        ],
        'Noodles': [
            {'name': 'Veg Singapuri Noodles', 'price': '₹100', 'image': 'veg_singapuri_noodles.jpg'},
            {'name': 'Hakka Noodles', 'price': '₹130', 'image': 'hakka_noodles.jpg'},
            {'name': 'Chilly Garlic Noodles', 'price': '₹130', 'image': 'chilly_garlic_noodles.jpg'}
        ],
        'Rice': [
            {'name': 'Mutter Pulao', 'price': '₹120', 'image': 'mutter_pulao.jpg'},
            {'name': 'Cheese Pulao', 'price': '₹140', 'image': 'cheese_pulao.jpg'}
        ],
        'Chilly': [
            {'name': 'Chilly Paneer', 'price': '₹220', 'image': 'chilly_paneer.jpg'},
            {'name': 'Honey Chilly Potato', 'price': '₹120', 'image': 'honey_chilly_potato.jpg'}
        ],
        'Manchurian': [
            {'name': 'Dry Manchurian', 'price': '₹150', 'image': 'dry_manchurian.jpg'},
            {'name': 'Gravy Manchurian', 'price': '₹180', 'image': 'gravy_manchurian.jpg'}
        ],
        'Sabji': [
            {'name': 'Shahi Paneer', 'price': '₹120/220', 'image': 'shahi_paneer.jpg'},
            {'name': 'Kadhai Paneer', 'price': '₹130/240', 'image': 'kadhai_paneer.jpg'},
            {'name': 'Paneer Butter Masala', 'price': '₹140/260', 'image': 'paneer_butter_masala.jpg'},
            {'name': 'Chana Masala', 'price': '₹100/180', 'image': 'chana_masala.jpg'},
            {'name': 'Mix Veg', 'price': '₹100/180', 'image': 'mix_veg.jpg'},
            {'name': 'Dum Aloo', 'price': '₹120/220', 'image': 'dum_aloo.jpg'},
            {'name': 'Dal Makhani', 'price': '₹100/180', 'image': 'dal_makhani.jpg'},
            {'name': 'Cheese Dal Makhani', 'price': '₹120/220', 'image': 'cheese_dal_makhani.jpg'},
            {'name': 'Dal Fry', 'price': '₹80/150', 'image': 'dal_fry.jpg'},
            {'name': 'Rajma', 'price': '₹80/150', 'image': 'rajma.jpg'},
            {'name': 'Amul Butter Dal Fry', 'price': '₹120/220', 'image': 'amul_dal_fry.jpg'},
            {'name': 'Sahi Chaap', 'price': '₹120/230', 'image': 'sahi_chaap.jpg'},
        ],
        'Tandoor & Paratha': [
            {'name': 'Garlic Naan', 'price': '₹60', 'image': 'garlic_naan.jpg'},
            {'name': 'Paneer Naan', 'price': '₹90', 'image': 'paneer_naan.jpg'},
            {'name': 'Stuff Naan', 'price': '₹80', 'image': 'stuffed_naan.jpg'},
            {'name': 'Aloo Naan', 'price': '₹55', 'image': 'aloo_naan.jpg'},
            {'name': 'Lachha Paratha', 'price': '₹35', 'image': 'lachha_paratha.jpg'},
            {'name': 'Aloo Paratha', 'price': '₹40', 'image': 'aloo_paratha.jpg'},
            {'name': 'Paneer Paratha', 'price': '₹80', 'image': 'paneer_paratha.jpg'},
            {'name': 'Pudina Paratha', 'price': '₹50', 'image': 'pudina_paratha.jpg'},
            {'name': 'Stuffed Paratha', 'price': '₹60', 'image': 'stuffed_paratha.jpg'},
        ],
        'Rayta & Salad': [
            {'name': 'Mix Rayta', 'price': '₹60/120', 'image': 'mix_rayta.jpg'},
            {'name': 'Green Salad', 'price': '₹100', 'image': 'green_salad.jpg'},
        ]
    }
    form = SubscribeForm()
    return render(request, 'index.html', {'menu_items': menu_items, 'form': form })

def menu(request):
    menu_items = {
        'Momos': [
            {'name': 'Veg Steam Momos', 'price': '₹80', 'image': 'veg_steam_momos.jpg'},
            {'name': 'Veg Fried Momos', 'price': '₹70/110', 'image': 'veg_fried_momos.jpg'},
            {'name': 'Chilly Garlic Momos', 'price': '₹80/130', 'image': 'chilly_garlic_momos.jpg'}
        ],
        'Soup': [
            {'name': 'Veg Manchow Soup', 'price': '₹60', 'image': 'veg_manchow_soup.jpg'},
            {'name': 'Veg Hot & Sour Soup', 'price': '₹60', 'image': 'veg_hot_sour_soup.jpg'}
        ],
        'Burger': [
            {'name': 'Veg Burger', 'price': '₹40', 'image': 'veg_burger.jpg'}
        ],
        'Noodles': [
            {'name': 'Veg Noodles', 'price': '₹60/100', 'image': 'veg_noodles.jpg'},
            {'name': 'Veg Singapuri Noodles', 'price': '₹70/110', 'image': 'veg_singapuri_noodles.jpg'},
            {'name': 'Hakka Noodles', 'price': '₹80/130', 'image': 'hakka_noodles.jpg'},
            {'name': 'Chilly Garlic Noodles', 'price': '₹80/130', 'image': 'chilly_garlic_noodles.jpg'}
        ],
        'Rice': [
            {'name': 'Plain Rice', 'price': '₹40/60', 'image': 'plain_rice.jpg'},
            {'name': 'Fried Rice', 'price': '₹60/100', 'image': 'fried_rice.jpg'},
            {'name': 'Jeera Rice', 'price': '₹60/100', 'image': 'jeera_rice.jpg'},
            {'name': 'Veg Pulao', 'price': '₹60/100', 'image': 'veg_pulao.jpg'},
            {'name': 'Mutter Pulao', 'price': '₹70/120', 'image': 'mutter_pulao.jpg'},
            {'name': 'Cheese Pulao', 'price': '₹80/140', 'image': 'cheese_pulao.jpg'}
        ],
        'Chilly': [
            {'name': 'Chilly Paneer', 'price': '₹220', 'image': 'chilly_paneer.jpg'},
            {'name': 'Chilly Potato', 'price': '₹70/100', 'image': 'chilly_potato.jpg'},
            {'name': 'Honey Chilly Potato', 'price': '₹80/120', 'image': 'honey_chilly_potato.jpg'}
        ],
        'Manchurian': [
            {'name': 'Dry Manchurian', 'price': '₹150', 'image': 'dry_manchurian.jpg'},
            {'name': 'Gravy Manchurian', 'price': '₹180', 'image': 'gravy_manchurian.jpg'}
        ],
        'Sabji': [
            {'name': 'Shahi Paneer', 'price': '₹120/220', 'image': 'shahi_paneer.jpg'},
            {'name': 'Mutter Paneer', 'price': '₹120/220', 'image': 'mutter_paneer.jpg'},
            {'name': 'Palak Paneer', 'price': '₹120/220', 'image': 'palak_paneer.jpg'},
            {'name': 'Kadhai Paneer', 'price': '₹130/240', 'image': 'kadhai_paneer.jpg'},
            {'name': 'Paneer Butter Masala', 'price': '₹140/260', 'image': 'paneer_butter_masala.jpg'},
            {'name': 'Paneer Bhurji', 'price': '₹150/280', 'image': 'paneer_bhurji.jpg'},
            {'name': 'Chana Masala', 'price': '₹100/180', 'image': 'chana_masala.jpg'},
            {'name': 'Mix Veg', 'price': '₹100/180', 'image': 'mix_veg.jpg'},
            {'name': 'Gobhi Aloo', 'price': '₹100/180', 'image': 'gobhi_aloo.jpg'},
            {'name': 'Jeera Aloo', 'price': '₹80/150', 'image': 'jeera_aloo.jpg'},
            {'name': 'Dum Aloo', 'price': '₹120/220', 'image': 'dum_aloo.jpg'},
            {'name': 'Stuffed Aloo', 'price': '₹140/260', 'image': 'stuffed_aloo.jpg'},
            {'name': 'Dal Makhani', 'price': '₹100/180', 'image': 'dal_makhani.jpg'},
            {'name': 'Cheese Dal Makhani', 'price': '₹120/220', 'image': 'cheese_dal_makhani.jpg'},
            {'name': 'Kadhi Pakora', 'price': '₹80/150', 'image': 'kadhi_pakora.jpg'},
            {'name': 'Dal Fry', 'price': '₹80/150', 'image': 'dal_fry.jpg'},
            {'name': 'Rajma', 'price': '₹80/150', 'image': 'rajma.jpg'},
            {'name': 'Amul Butter Dal Fry', 'price': '₹120/220', 'image': 'amul_dal_fry.jpg'},
            {'name': 'Sahi Chaap', 'price': '₹120/230', 'image': 'sahi_chaap.jpg'},
            {'name': 'Kadhai Chaap', 'price': '₹140/260', 'image': 'kadhai_chaap.jpg'},
            {'name': 'Butter Masala Chaap', 'price': '₹160/280', 'image': 'butter_masala_chaap.jpg'},
            {'name': 'Gobhi Masala', 'price': '₹110/200', 'image': 'gobhi_masala.jpg'}
        ],
        'Tandoor & Paratha': [
            {'name': 'Plain Roti', 'price': '₹10', 'image': 'plain_roti.jpg'},
            {'name': 'Butter Roti', 'price': '₹15', 'image': 'butter_roti.jpg'},
            {'name': 'Garlic Roti', 'price': '₹30', 'image': 'garlic_roti.jpg'},
            {'name': 'Onion Roti', 'price': '₹30', 'image': 'onion_roti.jpg'},
            {'name': 'Garlic Naan', 'price': '₹60', 'image': 'garlic_naan.jpg'},
            {'name': 'Butter Naan', 'price': '₹40', 'image': 'butter_naan.jpg'},
            {'name': 'Plain Naan', 'price': '₹35', 'image': 'plain_naan.jpg'},
            {'name': 'Paneer Naan', 'price': '₹90', 'image': 'paneer_naan.jpg'},
            {'name': 'Stuff Naan', 'price': '₹80', 'image': 'stuffed_naan.jpg'},
            {'name': 'Onion Naan', 'price': '₹65', 'image': 'onion_naan.jpg'},
            {'name': 'Aloo Naan', 'price': '₹55', 'image': 'aloo_naan.jpg'},
            {'name': 'Green Chilly Naan', 'price': '₹45', 'image': 'green_chilly_naan.jpg'},
            {'name': 'Masala Paratha', 'price': '₹60', 'image': 'masala_paratha.jpg'},
            {'name': 'Lachha Paratha', 'price': '₹35', 'image': 'lachha_paratha.jpg'},
            {'name': 'Aloo Paratha', 'price': '₹40', 'image': 'aloo_paratha.jpg'},
            {'name': 'Onion Paratha', 'price': '₹50', 'image': 'onion_paratha.jpg'},
            {'name': 'Paneer Paratha', 'price': '₹80', 'image': 'paneer_paratha.jpg'},
            {'name': 'Pudina Paratha', 'price': '₹50', 'image': 'pudina_paratha.jpg'},
            {'name': 'Red Chilly Paratha', 'price': '₹45', 'image': 'red_chilly_paratha.jpg'},
            {'name': 'Green Chilly Paratha', 'price': '₹45', 'image': 'green_chilly_paratha.jpg'},
            {'name': 'Stuffed Paratha', 'price': '₹60', 'image': 'stuffed_paratha.jpg'},
            {'name': 'Garlic Paratha', 'price': '₹50', 'image': 'garlic_paratha.jpg'}
        ],
        'Rayta & Salad': [
            {'name': 'Boondi Rayta', 'price': '₹60/120', 'image': 'boondi_rayta.jpg'},
            {'name': 'Mix Rayta', 'price': '₹60/120', 'image': 'mix_rayta.jpg'},
            {'name': 'Aloo Rayta', 'price': '₹60/120', 'image': 'aloo_rayta.jpg'},
            {'name': 'Green Salad', 'price': '₹100', 'image': 'green_salad.jpg'},
            {'name': 'Onion Salad', 'price': '₹100', 'image': 'onion_salad.jpg'}
        ],
        'Beverages & Cold Drink': [
            {'name': 'Cold Drink', 'price': 'MRP', 'image': 'cold_drink.jpg'},
            {'name': 'Ice Cream', 'price': 'MRP', 'image': 'ice_cream.jpg'}
        ],
    }
    return render(request, 'menu.html', {'menu_items': menu_items})


def about(request):
    return render(request, 'about.html')

def review(request):
    return render(request,'review.html')

