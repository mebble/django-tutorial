from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request: HttpRequest):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        pass
