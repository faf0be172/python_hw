from src.retest_1.task_2.html import HTML


def test_empty_doc():
    html = HTML()
    assert html.generate() == "<html></html>\n"


def test_sample():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p("Первая строка.")
                html.p("Вторая строка.")
            with html.div():
                html.p("Третья строка.")

    assert (
        html.generate()
        == "<html>\n"
        + "  <body>\n"
        + "    <div>\n"
        + "      <div>\n"
        + "        <p>Первая строка.</p>\n"
        + "        <p>Вторая строка.</p>\n"
        + "      </div>\n"
        + "      <div>\n"
        + "        <p>Третья строка.</p>\n"
        + "      </div>\n"
        + "    </div>\n"
        + "  </body>\n"
        + "</html>\n"
    )
