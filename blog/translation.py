from modeltranslation.translator import translator , TranslationOptions , register
from .models import Blogs

class BlogsTranslationOptions(TranslationOptions):
    fields = ['description' ,]
translator.register(Blogs , TranslationOptions)
