from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Word, Section
from .forms import FormSection, FormWord
from accounts.models import User
import random


@login_required()
def home(request):
    sections = Section.objects.filter(user=request.user)
    context = {
        "sections": sections
    }
    return render(request, 'words/words_home.html', context)


@login_required()
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


@login_required()
def show_words(request, section_id):
    if 'score' in request.session:
        del request.session['score']
    words = Word.objects.filter(section=section_id)
    section = get_object_or_404(Section, id=section_id)
    context = {
        'words': words,
        'section': section
    }
    return render(request, 'words/words_show_words.html', context)


@login_required()
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


@login_required()
def delete_word(request, section_id, word_id):
    word = get_object_or_404(Word, id=word_id, section=section_id)
    word.delete()
    context = {
        'section_id': section_id
    }
    return redirect(request.META.get('HTTP_REFERER', '/'), context)
    # return redirect('show_words', context)


@login_required()
def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    section.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


'''
@login_required
def study_words(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    words = section.words.all()

    if not words:
        return redirect('show_words', section_id=section_id)

    random_word = random.choice(words)
    show_foreign = random.choice([True, False])

    if request.method == 'POST':
        user_input = request.POST.get('translation')
        correct_translation = (random_word.native_word if show_foreign else random_word.foreign_word).strip().lower()
        if user_input.strip().lower() == correct_translation:
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            request.session['score'] = 0

        return redirect('study_words', section_id=section_id)

    context = {
        'section': section,
        'random_word': random_word,
        'show_foreign': show_foreign,
        'score': request.session.get('score', 0)
    }

    return render(request, 'words/words_study_words.html', context)
'''


'''
def study_words(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    words = list(section.words.all())

    if not words:
        return render(request, 'words/study_words.html', {'section': section, 'score': 0, 'message': 'No words available in this section.'})

    random_word = random.choice(words)
    show_foreign = random.choice([True, False])

    if request.method == 'POST':
        translation = request.POST.get('translation')
        score = int(request.POST.get('score', 0))

        correct_translation = random_word.native_word if show_foreign else random_word.foreign_word

        if translation.lower().strip() == correct_translation.lower().strip():
            score += 1
            message = "Correct! Your score is now {}.".format(score)
        else:
            score = 0
            message = "Incorrect. The correct translation was '{}'. Your score has been reset.".format(correct_translation)

        return render(request, 'words/words_study_words.html', {
            'section': section,
            'random_word': random.choice(words),
            'show_foreign': random.choice([True, False]),
            'score': score,
            'message': message
        })

    return render(request, 'words/words_study_words.html', {
        'section': section,
        'random_word': random_word,
        'show_foreign': show_foreign,
        'score': 0,
        'message': ''
    })
'''


'''
@login_required
def study_words(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    words = section.words.all()

    if not words:
        return redirect('show_words', section_id=section_id)

    random_word = random.choice(words)
    show_foreign = random.choice([True, False])

    if request.method == 'POST':
        user_input = request.POST.get('translation')
        correct_translation = (random_word.native_word if show_foreign else random_word.foreign_word).strip().lower()
        if user_input.strip().lower() == correct_translation:
            request.session['score'] = request.session.get('score', 0) + 1
            message = f"Correct! Your score is now {request.session.get('score')}."
        else:
            request.session['score'] = 0
            message = f"Incorrect. The correct translation was '{correct_translation}'. Your score has been reset."
        context = {
            'message': message,
            'section_id': section_id
        }
        return render(request,'words/words_study_words.html', context)

    context = {
        'section': section,
        'random_word': random_word,
        'show_foreign': show_foreign,
        'score': request.session.get('score', 0),
    }

    return render(request, 'words/words_study_words.html', context)
'''


@login_required()
def study_words(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    words = list(section.words.all())

    if not words:
        return render(request, 'words/study_words.html',
                      {'section': section, 'score': 0, 'message': 'No words available in this section.'})

    if request.method == 'POST':
        translation = request.POST.get('translation')
        score = int(request.POST.get('score', 0))
        word_id = int(request.POST.get('word_id'))
        show_foreign = request.POST.get('show_foreign') == 'True'

        random_word = get_object_or_404(Word, id=word_id)
        correct_translation = random_word.native_word if show_foreign else random_word.foreign_word

        if translation.lower().strip() == correct_translation.lower().strip():
            score += 1
            message = f"Correct! Your score is now {score}."
        else:
            score = 0
            message = f"Incorrect '{translation}'. The correct translation was '{correct_translation}'. Your score has been reset."

        random_word = random.choice(words)
        show_foreign = random.choice([True, False])
    else:
        random_word = random.choice(words)
        show_foreign = random.choice([True, False])
        score = 0
        message = ''

    return render(request, 'words/words_study_words.html', {
        'section': section,
        'random_word': random_word,
        'show_foreign': show_foreign,
        'score': score,
        'message': message
    })
