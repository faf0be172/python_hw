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
    def execute_tag(self):
        print('  ' * self.level + f'<{self.tag_name}>', end='')
        if self.children:
            print()
        yield self
        if self.children:
            print('  ' * self.level + f'</{self.tag_name}>')
        else:
            print(f'</{self.tag_name}>')


class HTMLString(HTMLElement):
    def __init__(self, tag_name, inner_text='', level=0):
        super().__init__(tag_name, level)
        self.innerText = inner_text

    @contextmanager
    def execute_tag(self):
        print('  ' * self.level + f'<{self.tag_name}>{self.innerText}</{self.tag_name}>')
        yield self


class HTML:
    def __init__(self):
        self.root = HTMLTag(tag_name='html')
        self.current_tag = self.root

    @contextmanager
    def body(self):
        body_tag = HTMLTag(tag_name='body', level=self.current_tag.level + 1)
        body_tag.parent = self.current_tag
        self.current_tag.children.append(body_tag)
        copy = body_tag.parent
        self.current_tag = body_tag
        yield self
        self.current_tag = copy

    @contextmanager
    def div(self):
        div_tag = HTMLTag(tag_name='div', level=self.current_tag.level + 1)
        div_tag.parent = self.current_tag
        self.current_tag.children.append(div_tag)
        copy = div_tag.parent
        self.current_tag = div_tag
        yield self
        self.current_tag = copy

    def p(self, inner_text=''):
        p_tag = HTMLString(tag_name='p', inner_text=inner_text, level=self.current_tag.level + 1)
        p_tag.parent = self.current_tag
        self.current_tag.children.append(p_tag)

    def generate(self):
        def dfs(node):
            with node.execute_tag() as tag:
                for child in tag.children:
                    dfs(child)

        dfs(self.root)


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p("Первая строка.")
            html.p("Вторая строка.")
        with html.div():
            html.p("Третья строка.")
html.generate()
