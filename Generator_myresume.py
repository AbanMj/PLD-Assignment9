from fpdf import FPDF
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

#json file8

import json
JSONfileinfos = open('myresume.json', 'r')
JSONfile = JSONfileinfos.read()
file = json.loads(JSONfile)

pdf.image ('border1.png', 0, -10, 250 )
pdf.set_font ('arial', '',  2)
pdf.cell(100,32,"                ", ln= True,)
pdf.image ('profile2.png', 140, 23, 45 )

pdf.set_font ('arial', 'B',  20)
pdf.cell (150,5, file [0] ['Name'], ln=True, )
pdf.set_font ('arial', 'I',  12)
pdf.cell (140,5, file [0] ['Address'], ln=True,)
pdf.set_font ('arial', 'I',  12)
pdf.cell (150,5, file [0] ['Email'], ln=True, )
pdf.set_font ('arial', 'I',  12)
pdf.cell (150,5, file [0] ['Cellphone'], ln=True,)


#Obj.
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'OBJECTIVE', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Objective1'], ln=True)
pdf.cell(50,4, file [0] ['Objective2'], ln=True,)

#PI
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'PERSONAL INFORMATION', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Birthday'], ln=True,)
pdf.cell(50,4, file [0] ['Birthplace'], ln=True,)
pdf.cell(50,4, file [0] ['Gender'], ln=True,)
pdf.cell(50,4, file [0] ['Nationality'], ln=True,)
pdf.cell(50,4, file [0] ['Status'], ln=True,)
pdf.cell(50,4, file [0] ['Height'], ln=True,)
pdf.cell(50,4, file [0] ['Weight'], ln=True,)

#EB
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'EDUCATIONAL BACKGROUND', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Elementary'], ln=True,)
pdf.cell(50,4, file [0] ['Junior High School'], ln=True,)
pdf.cell(50,4, file [0] ['Senior High School'], ln=True,)
pdf.cell(50,4, file [0] ['College'], ln=True,)

#Achievement
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'ACHIEVEMENTS', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Achievement1'], ln=True,)
pdf.cell(50,4, file [0] ['Achievement2'], ln=True,)
pdf.cell(50,4, file [0] ['Achievement3'], ln=True,)
pdf.cell(50,4, file [0] ['Achievement4'], ln=True,)

#skill
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'SKILLS', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Skill1'], ln=True,)
pdf.cell(50,4, file [0] ['Skill2'], ln=True,)
pdf.cell(50,4, file [0] ['Skill3'], ln=True,)
pdf.cell(50,4, file [0] ['Skill4'], ln=True,)
pdf.cell(50,4, file [0] ['Skill5'], ln=True,)
pdf.cell(50,4, file [0] ['Skill6'], ln=True,)

#CR
pdf.set_font ('arial', 'B',  14)
pdf.set_text_color (r= 255, g= 128, b= 128)
pdf.cell (120,10, 'CHARACTER REFERENCE', ln=True)
pdf.set_font ('arial', '',  12)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(50,4, file [0] ['Character Reference1'], ln=True,)
pdf.set_font ('arial', 'I',  10)
pdf.cell(50,4, file [0] ['Reference 1'], ln=True,)
pdf.set_font ('arial', '',  12)
pdf.cell(50,4, file [0] ['Character Reference2'], ln=True,)
pdf.set_font ('arial', 'I',  10)
pdf.cell(50,4, file [0] ['Reference 2'], ln=True,)


pdf.set_font ('arial', 'I',  10)
pdf.cell(70, 10, file [0] ['Certify'],ln= True)

pdf.set_font ('arial', 'U', 12)
pdf.cell(350,7, file [0] ['Name'], ln= True, align='C')
pdf.set_font ('arial', '', 12)
pdf.cell(350,3, file [0] ['Applicant'], ln=True, align='C')

pdf.image ('border.png', 0, 253, 250 )

pdf.output ('ABAN_MARY_JOY.pdf')