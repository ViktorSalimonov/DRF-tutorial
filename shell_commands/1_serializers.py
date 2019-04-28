from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello world"\n')
snippet.save()

print """Translating the model instance into Python native datatypes."""
serializer = SnippetSerializer(snippet)
print "Serializer data:", serializer.data
# {'style': 'friendly', 'code': u'print("hello world")\n', 'id': 2, 'language': 'python', 'title': u''}

print """Rendering the data into json."""
content = JSONRenderer().render(serializer.data)
print "Content:", content
# {"id":2,"title":"","code":"print(\\"hello world\\")\\n","language":"python","style":"friendly"}'

print """Deserialization. Parsing a stream into Python native datatypes."""
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
print "Data:", data
# {u'style': u'friendly', u'code': u'print("hello world")\n', u'id': 2, u'language': u'python', u'title': u''}

print """Restoring those native datatypes into a fully populated object instance."""
serializer = SnippetSerializer(data=data)
print "Serializer is_valid:", serializer.is_valid()
# True
print "Serializer validated_data:", serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>

"""Serializing queryset instead of model instance. many=True flag for that."""
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print "Serializer data:", serializer.data
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]