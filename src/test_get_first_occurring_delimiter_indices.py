import unittest

from split_nodes_delimiter import get_paired_delimiter_indices

class TestGetFirstOccurringDelimiterIndices(unittest.TestCase):     
    def test_returns_same_idx_only_one_italic_character_match(self):
        text = "A * character"
        delimiter = "*"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = (2, 2)
        self.assertEqual(result, expected_output)
    
    def test_returns_same_idx_if_only_one_bold_character_match(self):
        text = "A ** character"
        delimiter = "**"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = (2, 2)
        self.assertEqual(result, expected_output)
    
    def test_does_not_return_same_index_if_delimiter_is_italic_and_markdown_is_bold(self):
        text = "A ** character"
        delimiter = "_"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = None
        self.assertEqual(result, expected_output)
    
    def test_returns_None_if_there_is_no_match(self):
        text = "A ** character"
        delimiter = "`"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = None
        self.assertEqual(result, expected_output)
    
    def test_returns_same_index_if_delimiter_is_at_end_of_string(self):
        text = "A **"
        delimiter = "**"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = (2,2)
        self.assertEqual(result, expected_output)
    
    def test_returns_same_index_if_delimiter_is_at_end_of_string(self):
        text = "A _"
        delimiter = "_"
        
        result = get_paired_delimiter_indices(delimiter, text)
        
        expected_output = (2,2)
        self.assertEqual(result, expected_output)