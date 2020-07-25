# Create your views here.
import datetime

from django.http import HttpResponse


def dummy_catalog(request, book_id):
    now = datetime.datetime.now()
    html = f"""
        <html>
            <p>Book catalog id: {book_id}. Timestamp: {now}</p>
        </html>"""
    return HttpResponse(html)
