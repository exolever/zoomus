import unittest

from mock import patch

from zoomus import components


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DeleteTestCase))
    return suite


class DeleteTestCase(unittest.TestCase):

    def setUp(self):
        self.component = components.recording.RecordingComponent(
            base_uri="http://foo.com",
            config={
                'api_key': 'KEY',
                'api_secret': 'SECRET'
            }
        )

    def test_can_delete(self):
        with patch.object(components.base.BaseComponent, 'post_request',
                          return_value=True) as mock_post_request:

            self.component.delete(meeting_id='ID')

            mock_post_request.assert_called_with(
                "/recording/delete",
                params={
                    'meeting_id': 'ID'
                }
            )

    def test_requires_id(self):
        with self.assertRaises(ValueError) as context:
            self.component.delete()
            self.assertEqual(
                context.exception.message, "'meeting_id' must be set")


if __name__ == '__main__':
    unittest.main()
