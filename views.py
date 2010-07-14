from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

def pygments(request, template_name="pygments/pygments.html"):
    if request.method == "POST":
        lang = request.POST.get('lang', 'python')
        code = request.POST.get('code', '')
        code = highlight(code, get_lexer_by_name(lang),HtmlFormatter(cssclass="pygments"))
        return HttpResponse(code)
    else:
        return render_to_response(template_name, {}
        , context_instance=RequestContext(request))