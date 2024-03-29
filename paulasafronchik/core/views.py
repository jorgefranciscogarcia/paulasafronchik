from django.shortcuts import render

html_cabecera = """
<h1>Paula Safronchik</h1>
<ul>
    <li> <a href="/contact/">Contacto</a> </li>
    <li> <a href="/portfolio/">Portfolio</a> </li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')
