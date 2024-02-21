from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import JsonResponse
import requests 
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    context={'products':Product.objects.all()}
    return render(request,'pages/index.html',context)
def index_2(request):
    context={'products':Product.objects.all()}
    return render(request,'pages/index_2.html',context)
def about(request):
    return render(request,'pages/about.html')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
   
    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'total_price': total_price })
 
def add_to_cart(request, product_id):
     product = Product.objects.get(id=product_id)

     cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)
     cart_item.quantity += 1
     cart_item.save()
     
     return redirect('view_cart')
def decrease_cart_item(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    # next = request.POST.get('next', '/')   
    return redirect('view_cart')
def increase_cart_item(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)

    
    cart_item.quantity += 1
    cart_item.save()
    next = request.POST.get('next','/' )
    return redirect(next)
       
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
def contact(request):
    return render(request,'pages/contact.html')
def wiob():
    wilayat=[
        "أدرار",
        "الشلف",
        "الأغواط",
        "أم البواقي",
        "باتنة",
        "بجاية",
        "بسكرة",
        "بشار",
        "البليدة",
        "البويرة",
        "تمنراست",
        "تبسة",
        "تلمسان",
        "تيارت",
        "تيزي وزو",
        "الجزائر العاصمة",
        "الجلفة",
        "جيجل",
        "سطيف",
        "سعيدة",
        "سكيكدة",
        "سيدي بلعباس",
        "عنابة",
        "قالمة",
        "قسنطينة",
        "المدية",
        "مستغانم",
        "المسيلة",
        "معسكر",
        "ورقلة",
        "وهران",
        "البيض",
        "إليزي",
        "برج بوعريريج",
        "بومرداس",
        "الطارف",
        "تندوف",
        "تيسمسيلت",
        "الوادي",
        "خنشلة",
        "سوق أهراس",
        "تيبازة",
        "ميلة",
        "عين الدفلى",
        "النعامة",
        "عين تموشنت",
        "غرداية",
        "غليزان",
        "تيميمون",
        "برج باجي مختار",
        "أولاد جلال",
        "بني عباس",
        "عين صالح",
        "عين قزام",
        "تقرت",
        "جانت",
        "المغير",
        "المنيعة"
    ]
    # wilayyat= [Wilaya.objects.get_or_create(name=wilaya) for wilaya in wilayat]
    # Commune.objects.all().delete()
    i=0
    communes=[]
    for wilaya in wilayat:
        i=i+1
        wilayaobj,_=Wilaya.objects.get_or_create(name=wilaya)
        communes= getcommunes(i)
        for commune in communes:
            
            create,_ =Commune.objects.get_or_create(name=commune,wilaya=wilayaobj)
            
        
def getcommunes(id):
    url = "https://apcsali-adrar.dz/communes/"+str(id)+"/wilaya"

  

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the elements containing the communes list (based on the HTML structure of the page)
        # Adjust this part based on the structure of the page you are fetching data from
        """ commune_list=[(row.find_all('td')[2].get_text(),row.find_all('td')[4].get_text()[::-1])  for row in soup.find_all('tr') if len(row.find_all('td'))!=0]
        print(commune_list) """
        communes =[row.get_text() for row in soup.find_all('div',class_='contentRow-lesser frtxt')]
        return(communes)

    else:
        return("Failed to fetch data. Status code:", response.status_code)


def checkout(request,id):
    # wiob()
    if id!=0:
        product=Product.objects.get(id=id)
        total_price=product.price

    else:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    form=OrderForm()
    return render(request,'pages/checkout.html',{'total_price': total_price,'ordersform':form,'wilayat':Wilaya.objects.all()})
def error(request):
    return render(request,'pages/404.html')
def news(request):
    return render(request,'pages/news.html')
def shop(request):
    context={'products':Product.objects.all()}
    return render(request,'pages/shop.html',context)
def singlenews(request):
    return render(request,'pages/single-news.html')
def singleproduct(request,id):
    product_by_id=Product.objects.get(id=id)
    item=CartItem.objects.get_or_create( product=product_by_id,user=request.user)
    context={'products':Product.objects.all(),'id_product':product_by_id,'item':item}
    return render(request,'pages/single-product.html',context)
def get_communes(request):
    
    wilaya_id = request.GET.get('wilaya_id')
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values_list('id', 'name')
    data = list(communes)
    return JsonResponse(data, safe=False)