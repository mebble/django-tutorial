from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request: HttpRequest):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        parser = JSONParser()
        data = parser.parse(request)
        serializer = SnippetSerializer(data=data)  # [#]: Even if we pass 'id' in the request body, it will not use that id when creating the snippet. There must be some special fields in django that behave this way
        if not serializer.is_valid():
            return JsonResponse(status=400, data={"status": "failure", "errors": serializer.errors})
        snippet = Snippet(**serializer.validated_data)  # [#]: alternative: serializer.save() if we use ModelSerializer
        snippet.save()
        return JsonResponse(status=201, data={"status": "success"})

@csrf_exempt
def snippet_detail(request: HttpRequest, snippet_id):
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return JsonResponse(status=404, data={"status": "failure"})

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data) # [#] this merges the existing snippet and incoming data
        if not serializer.is_valid():
            return JsonResponse(status=400, data=serializer.errors)

        serializer.save()
        return JsonResponse(status=200, data=serializer.validated_data)
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
    else:
        serializer = SnippetSerializer(snippet)
        data = serializer.data
        return JsonResponse(status=200, data=data)
