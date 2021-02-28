import unittest

from barky import Option,get_new_bookmark_data,get_option_choice,option_choice_is_valid,get_user_input
import commands

class MyTestCase(unittest.TestCase):
    def test_get_user_input(self,label='Title'):
        #dict = {'Title': 'aaa'}
        self.assertEqual('aaa', get_user_input(label))


    def test_get_option_choice(self):
        options = {
            "A": Option(
                "Add a bookmark",
                commands.AddBookmarkCommand(),
                prep_call=get_new_bookmark_data,
            ),
        }
        chosen_option = get_option_choice(options)
        self.assertEqual(options["A"], chosen_option)



if __name__ == '__main__':
    unittest.main()
