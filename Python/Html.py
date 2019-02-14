##Nathan Hinton.
##This is the Html file that contains all of the functions needed.

def table(self):
    self.text.insert(INSERT, """
<table>
<thead><!--Table Header-->
<th></th>
<th></th>
<th></th>
</thead>
<tbody><!--Table row 1-->
<td></td>
<td></td>
<td></td>
</tbody>
<tbody><!--Table row 2-->
<td></td>
<td></td>
<td></td>
</tbody>
<tbody><!--Table row 33-->
<td></td>
<td></td>
<td></td>
</tbody>
</table>
""")
def line(self):
    self.text.insert(INSERT, "<hr>")
def em(self):
    self.text.insert(INSERT, "<em></em>")
def address(self):
    self.text.insert(INSERT, "<address></address>")
def bold(self):
    self.text.insert(INSERT, "<b></b>")
def picture(self):
    self.text.insert(INSERT, "<img></img>")
def comment(self):
    self.text.insert(INSERT, "<!--  -->")
def list(self):
    self.text.insert(INSERT, """
<ul><caption></caption>
<li></li>
<li></li>
<li></li>
</ul>
""")
def a(self):
    self.text.insert(INSERT, "<a href=\"\"><a/>")
def p(self):
    self.text.insert(INSERT, "<p></p>")
def heading(self):
    self.text.insert(INSERT,"<h3></h3>")
