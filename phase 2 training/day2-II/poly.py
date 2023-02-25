class vijayawada():
    def placename(self):
        print("vijaywada")
    def student(self):
        print("yes-bza")
    def which_year(self):
        print("3rd")
class hyd():
    def placename(self):
        print("hyderabad")
    def student(self):
        print("yes-hyd")
    def which_year(self):
        print("3rd")
bza=vijayawada()
hyd=hyd()
for details in (bza,hyd):
    details.placename()
    details.student()
    details.which_year()
