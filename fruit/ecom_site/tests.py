from django.test import TestCase
import requests 
from bs4 import BeautifulSoup
# Create your tests here.
 # URL of the page containing the communes list
def getcommunes(id):

    url = "https://apcsali-adrar.dz/communes/"+str(id)+"/wilaya"

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
    
print(getcommunes(5))    