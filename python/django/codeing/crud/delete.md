### Delete
```python
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Employees.objects.get(id = book_id)
    except Employees.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
```