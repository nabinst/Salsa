from django.shortcuts import render, get_object_or_404 ,redirect, reverse
from .models import Product, Comment
from .forms import CommentForm
# Create your views here.

def products_view(request):
    products = Product.objects.all()
    context ={
        'products': products,
    }
    return render(request, 'products.html',context)

def get_product(id):
    product = Product.objects.filter(id=id)
    if product.exists():
        return product[0]
    return None

def product_comment_post(request, id):
    post = get_object_or_404(Product, id=id)
    comments = post.comments.filter(active=True)
    #product = get_product(id)
    #new_comment = None
    # Comment posted

    comment_form = CommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            #comment_form.instance.product = comment_form.product
            # Create Comment object but don't save to database yet   
            #comment_form.instance.id = request.id
            comment_form.instance.product_name = Product.objects.get(id=id)
            #comment_form.instance.comments = comments

            #comment_form = comment_form.save(commit=False)
            # Assign the current post to the comment
            #new_comment.post = post
            # Save the comment tot he database
            comment_form.save()
            return redirect(reverse('post_comment_view', kwargs={'id': post.id}))
  
    context ={
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'product.html', context)