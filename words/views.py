from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Word, Section
from .forms import FormSection, FormWord
from accounts.models import User


@login_required
def home(request):
    sections = Section.objects.filter(user=request.user)
    context = {
        "sections": sections
    }
    return render(request, 'words/words_home.html', context)


@login_required
def create_section(request):
    form = FormSection()
    if request.method == 'POST':
        form = FormSection(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.user = request.user
            form.save()
            return redirect('home')
    context = {
        "form": form,
    }
    return render(request, 'words/words_new_section.html', context)


@login_required
def show_words(request, section_id):
    words = Word.objects.filter(section=section_id)
    section = get_object_or_404(Section, id=section_id)
    context = {
        'words': words,
        'section': section
    }
    return render(request, 'words/words_show_words.html', context)


@login_required
def create_words(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    context = {
        'section': section,
    }
    if request.method == "POST":
        foreign_word = request.POST.get('foreign_word')
        native_word = request.POST.get('native_word')
        if foreign_word and native_word:
            new_word = Word.objects.create(foreign_word=foreign_word, native_word=native_word, section=section)
            new_word.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'words/words_new_words.html', context)


@login_required
def delete_word(request, section_id, word_id):
    word = get_object_or_404(Word, id=word_id, section=section_id)
    word.delete()
    context = {
        'section_id': section_id
    }
    return redirect(request.META.get('HTTP_REFERER', '/'), context)
    # return redirect('show_words', context)


@login_required
def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    section.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def learn_word(request):
    pass
