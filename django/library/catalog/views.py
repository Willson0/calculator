from django.shortcuts import render

# Create your views here.
def book (request):
    context = {
        "book": 
        {
            "title": "Преступление и наказание",
            "author": "Достоевский",
            "year": 1823,
            "pages": 123,
            "rating": 4.3,
            "genres": ["роман", "классика", "психология"],
            "available": True,
        },
        "comments_count": 0,
    }
    return render(request, 'catalog/book_detail.html', context)