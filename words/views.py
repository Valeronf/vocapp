# yourappname/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Word, Theme
from .forms import WordForm, ThemeForm

def main_page(request):
    themes = Theme.objects.all()
    form = ThemeForm()

    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'words/theme_list.html', {'themes': themes, 'form': form})




def word_list(request, theme_id):
    theme = Theme.objects.get(pk=theme_id)
    words = Word.objects.filter(theme=theme)

    form = WordForm()

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.instance.theme = theme
            form.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'words/word_list.html', {'words': words, 'form': form, 'theme_id': theme_id, 'theme': theme})

#Delete, update for words
def delete_word(request, word_id):
    word = Word.objects.get(id=word_id)
    word.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def update_word(request, word_id, theme_id):
    print(theme_id)
    word = get_object_or_404(Word, id=word_id)
    print(f"Retrieved Word: {word}")
    form = WordForm(request.POST or None, instance=word)
    if form.is_valid():
        form.save()
        redirect_url = f'/{theme_id}/'
        print(redirect_url)
        return redirect(redirect_url)
    return render(request, 'words/update_word.html',{'form':form, 'word':word, 'theme_id':theme_id})


#Delete, update for list of theme(main page)
  
def delete_theme(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    theme.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def update_theme(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    form = ThemeForm(request.POST or None, instance=theme)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'words/update_theme.html',{'form':form, 'theme':theme})

