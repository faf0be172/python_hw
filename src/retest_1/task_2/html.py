from contextlib import contextmanager


class HTMLElement:
    def __init__(self, tag_name, level=0):
        self.level = level
        self.tag_name = tag_name
        self.parent = None
        self.children = []


class HTMLTag(HTMLElement):
    def __init__(self, tag_name, level=0):
        super().__init__(tag_name, level)

    @contextmanager
    def execute_tag(self, document):
        document.doc += "  " * self.level + f"<{self.tag_name}>"
        if self.children:
            document.doc += "\n"
        yield self
        if self.children:
            document.doc += "  " * self.level + f"</{self.tag_name}>\n"
        else:
            document.doc += f"</{self.tag_name}>\n"


class HTMLString(HTMLElement):
    def __init__(self, tag_name, inner_text='', level=0):
        super().__init__(tag_name, level)
        self.innerText = inner_text

    @contextmanager
    def execute_tag(self, document):
        document.doc += "  " * self.level + f"<{self.tag_name}>{self.innerText}</{self.tag_name}>\n"
        yield self


class HTML:
    def __init__(self):
        self.root = HTMLTag(tag_name="html")
        self.current_tag = self.root
        self.doc = ""

    def _add_tag(self, tag_name):
        tag = HTMLTag(tag_name=tag_name, level=self.current_tag.level + 1)
        tag.parent = self.current_tag
        self.current_tag.children.append(tag)
        copy = tag.parent
        self.current_tag = tag
        yield self
        self.current_tag = copy

    @contextmanager
    def body(self):
        yield from self._add_tag("body")

    @contextmanager
    def div(self):
        yield from self._add_tag("div")

    def p(self, inner_text=''):
        p_tag = HTMLString(tag_name="p", inner_text=inner_text, level=self.current_tag.level + 1)
        p_tag.parent = self.current_tag
        self.current_tag.children.append(p_tag)

    def generate(self):
        def dfs(node):
            with node.execute_tag(self) as tag:
                for child in tag.children:
                    dfs(child)

        dfs(self.root)
        return self.doc


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p("Первая строка.")
            html.p("Вторая строка.")
        with html.div():
            html.p("Третья строка.")
print(html.generate())
