#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi



def build_page(text_area_content):
    header = "<h1>Web Caesar</h1>"
    rot_label = "<label>Rotate by:</label>"
    message_label = "<label>Enter a message:</label>"
    br = "<br>"

    text_area= "<textarea name='message'>" + text_area_content + "</textarea>"
    rotation = "<input type='number' name='rotation'></input>"
    submit = "<input type='submit'/>"

    form = ("<form method='post'>"
            + rot_label + br + rotation + br + br
            + message_label + br + text_area + br + br
            + submit + "</form>")

    content = header + form

    return content



class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(content)


    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotation")

        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)

        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
