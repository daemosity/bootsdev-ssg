import unittest

from split_nodes_delimiter import contains_valid_delimiters

class TestGetFirstOccurringDelimiterIndices(unittest.TestCase):     
    def test_returns_false_if_delimiter_not_paired(self):
        text = "A * character"
        delimiter = "*"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = False
        self.assertEqual(result, expected_output)
    
    def test_returns_false_when_given_italic_delimiter_with_bold_markdown(self):
        text = "A **bold** word"
        delimiter = "_"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = False
        self.assertEqual(result, expected_output)
    
    def test_returns_false_when_incorrect_markdown(self):
        text = "A **bold_ word"
        delimiter = "_"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = False
        self.assertEqual(result, expected_output)
    
    def test_returns_false_when_incorrect_markdown(self):
        text = "A _bold** word"
        delimiter = "_"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = False
        self.assertEqual(result, expected_output)
    
    def test_returns_false_when_given_correct_bold_markdown_and_italic_delimiter(self):
        text = "A **bold** word"
        delimiter = "_"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = False
        self.assertEqual(result, expected_output)
    
    def test_returns_true_when_given_correct_bold_markdown_and_delimiter(self):
        text = "A **bold** word"
        delimiter = "**"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = True
        self.assertEqual(result, expected_output)

    def test_returns_true_when_given_correct_italic_markdown_and_delimiter(self):
        text = "A _italic_ word"
        delimiter = "_"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = True
        self.assertEqual(result, expected_output)

    def test_returns_true_when_given_correct_code_markdown_and_delimiter(self):
        text = "A `code` word"
        delimiter = "`"
        
        result = contains_valid_delimiters(text, delimiter)
        
        expected_output = True
        self.assertEqual(result, expected_output)