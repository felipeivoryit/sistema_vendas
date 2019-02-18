import io
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML
from ..models import Funcionario

def pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(10, 800, 'Hello world.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def html_to_pdf_view(request):

    funcionarios = Funcionario.objects.all();

    html_string = render_to_string('pdf_template.html', {'funcionarios': funcionarios})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="funcionarios.pdf"'
        response.write(response)

    response.write(response)

    return response
