import os
from mistune import BlockLexer, BlockGrammar

d = os.path.basename(os.getcwd())


def headers():
    print("---")
    print("layout : post")
    print("category : articles")
    print("title : ! '{}'".format(d))
    print("description : ")
    print("tags : []")
    print("---")
    print("")


with open('talk.md') as f:
    text = f.read()

    slides = [[]]
    tokens = BlockLexer(BlockGrammar())(text)
    for token in tokens:
        if token.get('type') == 'paragraph' and token.get('text').startswith('^'):
            slides[-1].append(token.get('text').lstrip('^ '))
        if token.get('type') == 'hrule':
            slides.append([])

    headers()

    print("<table>")
    for i, slide in enumerate(slides, 1):
        print(f'  <tr><td><a href="#{i}"><img class="slide" src="/assets/images/{d}/{i}.png"></i></td><td>')
        print("    <p>")
        print("\n    </p><p>\n    ".join(slide))
        print("    </p>")
        print("  </td></tr>")
    print("</table>")
