from django import template
from django.template import Context, Template, Node


TEMPLATE = """
<iframe src="http://www.slideshare.net/slideshow/embed_code/{{ id }}"
        width="427"
        height="356"
        frameborder="0"
        marginwidth="0"
        marginheight="0"
        scrolling="no"
        allowfullscreen>
</iframe>
"""


def do_slideshare(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
    return SlideShareNode(id_, doc)


class SlideShareNode(Node):
    def __init__(self, id_, doc):
        self.id = template.Variable(id_)
        self.doc = template.Variable(doc)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        try:
            actual_doc = self.doc.resolve(context)
        except template.VariableDoesNotExist:
            actual_doc = self.doc

        t = Template(TEMPLATE)
        c = Context({'id': actual_id, 'doc': actual_doc}, autoescape=context.autoescape)
        return t.render(c)


register = template.Library()
register.tag('slideshare', do_slideshare)