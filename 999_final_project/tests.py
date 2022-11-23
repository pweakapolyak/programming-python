import unittest
from triggers import *
from story import *
from datetime import timedelta
from filter import *

class ProblemSet5NewsStory(unittest.TestCase):
    def setUp(self):
        pass

    def testNewsStoryConstructor(self):
        story = NewsStory('', '', '', '', datetime.now())

    def testNewsStoryGetGuid(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_guid(), 'test guid')

    def testNewsStoryGetTitle(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_title(), 'test title')

    def testNewsStoryGetdescription(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_description(), 'test description')

    def testNewsStoryGetLink(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_link(), 'test link')

    def testNewsStoryGetTime(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(type(story.get_pubdate()), datetime)
        
class ProblemSet5(unittest.TestCase):
    def setUp(self):
        class TrueTrigger:
            def check_story(self, story): return True

        class FalseTrigger:
            def check_story(self, story): return False

        self.tt = TrueTrigger()
        self.tt2 = TrueTrigger()
        self.ft = FalseTrigger()
        self.ft2 = FalseTrigger()

    def test1TitleTrigger(self):
        cuddly    = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
        exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
        symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
        spaces    = NewsStory('', 'Did you see a purple     cow?', '', '', datetime.now())
        caps      = NewsStory('', 'The farmer owns a really PURPLE cow.', '', '', datetime.now())
        exact     = NewsStory('', 'purple cow', '', '', datetime.now())

        plural    = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
        separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
        brown     = NewsStory('', 'How now brown cow.', '' ,'', datetime.now())
        badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
        nospaces  = NewsStory('', 'purplecowpurplecowpurplecow', '', '', datetime.now())
        nothing   = NewsStory('', 'I like poison dart frogs.', '', '', datetime.now())

        s1 = TitleTrigger('PURPLE COW')
        s2  = TitleTrigger('purple cow')
        for trig in [s1, s2]:
            self.assertTrue(trig.check_story(cuddly), "TitleTrigger failed to fire when the phrase appeared in the title.")
            self.assertTrue(trig.check_story(exclaim), "TitleTrigger failed to fire when the words were separated by exclamation marks.")
            self.assertTrue(trig.check_story(symbols), "TitleTrigger failed to fire when the words were separated by assorted punctuation.")
            self.assertTrue(trig.check_story(spaces), "TitleTrigger failed to fire when the words were separated by multiple spaces.")
            self.assertTrue(trig.check_story(caps), "TitleTrigger failed to fire when the phrase appeared with both uppercase and lowercase letters.")
            self.assertTrue(trig.check_story(exact), "TitleTrigger failed to fire when the words in the phrase were the only words in the title.")
            
            self.assertFalse(trig.check_story(plural), "TitleTrigger fired when the words in the phrase were contained within other words.")
            self.assertFalse(trig.check_story(separate), "TitleTrigger fired when the words in the phrase were separated by other words.")
            self.assertFalse(trig.check_story(brown), "TitleTrigger fired when only part of the phrase was found.")
            self.assertFalse(trig.check_story(badorder), "TitleTrigger fired when the words in the phrase appeared out of order.")
            self.assertFalse(trig.check_story(nospaces), "TitleTrigger fired when words were not separated by spaces or punctuation.")
            self.assertFalse(trig.check_story(nothing), "TitleTrigger fired when none of the words in the phrase appeared.")

    def test2DescriptionTrigger(self):
        cuddly    = NewsStory('', '', 'The purple cow is soft and cuddly.', '', datetime.now())
        exclaim   = NewsStory('', '', 'Purple!!! Cow!!!', '', datetime.now())
        symbols   = NewsStory('', '', 'purple@#$%cow', '', datetime.now())
        spaces    = NewsStory('', '', 'Did you see a purple     cow?', '', datetime.now())
        caps      = NewsStory('', '', 'The farmer owns a really PURPLE cow.', '', datetime.now())
        exact     = NewsStory('', '', 'purple cow', '', datetime.now())

        plural    = NewsStory('', '', 'Purple cows are cool!', '', datetime.now())
        separate  = NewsStory('', '', 'The purple blob over there is cow.', '', datetime.now())
        brown     = NewsStory('', '', 'How now brown cow.', '', datetime.now())
        badorder  = NewsStory('', '', 'Cow!!! Purple!!!', '', datetime.now())
        nospaces  = NewsStory('', '', 'purplecowpurplecowpurplecow', '', datetime.now())
        nothing   = NewsStory('', '', 'I like poison dart frogs.', '', datetime.now())

        s1 = DescriptionTrigger('PURPLE COW')
        s2  = DescriptionTrigger('purple cow')
        for trig in [s1, s2]:
            self.assertTrue(trig.check_story(cuddly), "DescriptionTrigger failed to fire when the phrase appeared in the description.")
            self.assertTrue(trig.check_story(exclaim), "DescriptionTrigger failed to fire when the words were separated by exclamation marks.")
            self.assertTrue(trig.check_story(symbols), "DescriptionTrigger failed to fire when the words were separated by assorted punctuation.")
            self.assertTrue(trig.check_story(spaces), "DescriptionTrigger failed to fire when the words were separated by multiple spaces.")
            self.assertTrue(trig.check_story(caps), "DescriptionTrigger failed to fire when the phrase appeared with both uppercase and lowercase letters.")
            self.assertTrue(trig.check_story(exact), "DescriptionTrigger failed to fire when the words in the phrase were the only words in the description.")
            
            self.assertFalse(trig.check_story(plural), "DescriptionTrigger fired when the words in the phrase were contained within other words.")
            self.assertFalse(trig.check_story(separate), "DescriptionTrigger fired when the words in the phrase were separated by other words.")
            self.assertFalse(trig.check_story(brown), "DescriptionTrigger fired when only part of the phrase was found.")
            self.assertFalse(trig.check_story(badorder), "DescriptionTrigger fired when the words in the phrase appeared out of order.")
            self.assertFalse(trig.check_story(nospaces), "DescriptionTrigger fired when words were not separated by spaces or punctuation.")
            self.assertFalse(trig.check_story(nothing), "DescriptionTrigger fired when none of the words in the phrase appeared.")

    def test3BeforeAndAfterTrigger(self):

        dt = timedelta(seconds=5)
        now = datetime(2016, 10, 12, 23, 59, 59)
        ancient = NewsStory('', '', '', '', datetime(1987, 10, 15))
        just_now = NewsStory('', '', '', '', now - dt)
        in_a_bit = NewsStory('', '', '', '', now + dt)
        future = NewsStory('', '', '', '', datetime(2087, 10, 15))

        s1 = BeforeTrigger('12 Oct 2016 23:59:59')
        s2 = AfterTrigger('12 Oct 2016 23:59:59')

        self.assertTrue(s1.check_story(ancient), "BeforeTrigger failed to fire on news from long ago")
        self.assertTrue(s1.check_story(just_now), "BeforeTrigger failed to fire on news happened right before specified time")

        self.assertFalse(s1.check_story(in_a_bit), "BeforeTrigger fired to fire on news happened right after specified time")
        self.assertFalse(s1.check_story(future), "BeforeTrigger fired to fire on news from the future")

        self.assertFalse(s2.check_story(ancient), "AfterTrigger fired to fire on news from long ago")
        self.assertFalse(s2.check_story(just_now), "BeforeTrigger fired to fire on news happened right before specified time")

        self.assertTrue(s2.check_story(in_a_bit), "AfterTrigger failed to fire on news just after specified time")
        self.assertTrue(s2.check_story(future), "AfterTrigger failed to fire on news from long ago")

    def test4NotTrigger(self):
        n = NotTrigger(self.tt)
        b = NewsStory("guid", "title", "description", "link", datetime.now())

        self.assertFalse(n.check_story(b), "A NOT trigger applied to 'always true' DID NOT return false")

        y = NotTrigger(self.ft)
        self.assertTrue(y.check_story(b), "A NOT trigger applied to 'always false' DID NOT return true")

    def test5AndTrigger(self):
        yy = AndTrigger(self.tt, self.tt2)
        yn = AndTrigger(self.tt, self.ft)
        ny = AndTrigger(self.ft, self.tt)
        nn = AndTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "description", "link", datetime.now())

        self.assertTrue(yy.check_story(b), "AND of 'always true' and 'always true' should be true")
        self.assertFalse(yn.check_story(b), "AND of 'always true' and 'always false' should be false")
        self.assertFalse(ny.check_story(b), "AND of 'always false' and 'always true' should be false")
        self.assertFalse(nn.check_story(b), "AND of 'always false' and 'always false' should be false")

    def test6OrTrigger(self):
        yy = OrTrigger(self.tt, self.tt2)
        yn = OrTrigger(self.tt, self.ft)
        ny = OrTrigger(self.ft, self.tt)
        nn = OrTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "description", "link", datetime.now())

        self.assertTrue(yy.check_story(b), "OR of 'always true' and 'always true' should be true")
        self.assertTrue(yn.check_story(b), "OR of 'always true' and 'always false' should be true")
        self.assertTrue(ny.check_story(b), "OR of 'always false' and 'always true' should be true")
        self.assertFalse(nn.check_story(b), "OR of 'always false' and 'always false' should be false")

    def test7FilterStories(self):
        tt = TitleTrigger("New York City")
        a = NewsStory('', "asfd New York City asfdasdfasdf", '', '', datetime.now())
        b = NewsStory('', "asdfasfd new york city! asfdasdfasdf", '', '', datetime.now())
        noa = NewsStory('', "something somethingnew york city", '', '', datetime.now())
        nob = NewsStory('', "something something new york cities", '', '', datetime.now())

        st = DescriptionTrigger("New York City")
        a = NewsStory('', '', "asfd New York City asfdasdfasdf", '', datetime.now())
        b = NewsStory('', '', "asdfasfd new york city! asfdasdfasdf", '', datetime.now())
        noa = NewsStory('', '', "something somethingnew york city", '', datetime.now())
        nob = NewsStory('', '', "something something new york cities", '', datetime.now())

        triggers = [tt, st, self.tt, self.ft]
        stories = [a, b, noa, nob]
        filtered_stories = filter_stories(stories, triggers)
        for story in stories:
            self.assertTrue(story in filtered_stories)
        filtered_stories = filter_stories(stories, [self.ft])
        self.assertEqual(len(filtered_stories), 0)

    def test8FilterStories2(self):
        a = NewsStory('', "asfd New York City asfdasdfasdf", '', '', datetime.now())
        b = NewsStory('', "asdfasfd new york city! asfdasdfasdf", '', '', datetime.now())
        noa = NewsStory('', "something somethingnew york city", '', '', datetime.now())
        nob = NewsStory('', "something something new york cities", '', '', datetime.now())

        class MatchTrigger(Trigger):
            def __init__(self, story):
                self.story = story
            def check_story(self, story):
                return story == self.story
        triggers = [MatchTrigger(a), MatchTrigger(nob)]
        stories = [a, b, noa, nob]
        filtered_stories = filter_stories(stories, triggers)
        self.assertTrue(a in filtered_stories)
        self.assertTrue(nob in filtered_stories)
        self.assertEqual(2, len(filtered_stories))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProblemSet5NewsStory))
    suite.addTest(unittest.makeSuite(ProblemSet5))
    unittest.TextTestRunner(verbosity=2).run(suite)

