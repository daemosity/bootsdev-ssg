import unittest
import re

pattern = r"\n\n(?![\n\s\w]+?```$)"

class TestReSplit(unittest.TestCase):
    def test_returns_full_codeblock(self):
        md1 = """```
This is a code block
```
"""
        md2 = """
```
This is a code block
```
"""
        md3 = """
```
This is a code block
```"""
        
        out1 = list(filter(lambda x: not x.isspace(), re.split(pattern, md1.strip())))
        out3 = list(filter(lambda x: not x.isspace(), re.split(pattern, md3.strip())))
        out2 = list(filter(lambda x: not x.isspace(), re.split(pattern, md2.strip())))
        
        expected_output = ["""```
This is a code block
```"""]
        self.assertSequenceEqual(out1, expected_output)
        self.assertSequenceEqual(out2, expected_output)
        self.assertSequenceEqual(out3, expected_output)
        
    def test_splits_code_correctly(self):
        md1 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

```
This is a block of code
that continues on

and on after a newline
```

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        
        out1 = list(filter(lambda x: not x.isspace(), re.split(pattern, md1.strip(), flags = re.M | re.S)))

        
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """```
This is a block of code
that continues on

and on after a newline
```""",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertSequenceEqual(out1, expected_output)

    def test_splits_code_text2_correctly(self):
        md1 = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

```
This is a block of code, it has **bold** and _italic_ words that aren't changed.
```"""
        
        out1 = list(filter(lambda x: not x.isspace(), re.split(pattern, md1.strip(), flags = re.M | re.S)))

        
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            """```
This is a block of code, it has **bold** and _italic_ words that aren't changed.
```"""]
        self.assertSequenceEqual(out1, expected_output)