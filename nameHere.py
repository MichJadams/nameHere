from fpdf import FPDF
 
pdf = FPDF(format="letter")
pdf.add_page()
pdf.set_left_margin(20)
pdf.set_font("Arial", size=12)

#this is your personal information
YourName = "Michaela Adams"
YourPhone ="908-451-0751"
# HiringName="BestCompany Hiring Team"
# CompanyName ="BestCompany Inc."
# PointYouLike="supportive environment for continued education."
Signature="I hope to hear from you soon," 
additionPersonalInformation =""

HiringName=raw_input("The hiring team name: ")
CompanyName =raw_input("Enter the company name: ")
Position=raw_input("Enter the position you are applying for:")
PointYouLike=raw_input("Enter a point about the company you like. Finished the sentence 'In particular': ")


#change these to be three paragraphs for your cover letter 
Greeting="Hello "+HiringName+ ","
FirsParagraph="The technological challenges of working at your company caught my eye, but I am also drawn to your mission. I am recent bootcamp grad with a passion for JavaScript and writing sustainble code. I'm interested in working as a "+Position+" for "+CompanyName +". In particular "+PointYouLike+" ."  

SecondParagraph="I am a full Stack engineer with an eye towards rapid development and a knack for flexible problem solving. I love to code, and bring ideas to life. Through my previous positions I have developed finely honed communication skills, which I believe cannot be overstated in a development position. I have also spent a great deal of time code pairing while at Grace Hopper Academy." 

ThirdParagraph="My code speaks for itself, check out my github. https://github.com/MichJadams. Technologies touched: JavaScript, Node.js, React.js, SQL, CSS, HTML, webpack, babble,PostgreSQL, sequelize, Now, Git, Python and a little bit of Rust and Webassembly." 


pdf.cell(50, 50, txt=Greeting, ln=1, align="J")

pdf.multi_cell(w=175, h=10, txt = FirsParagraph,
border = 0, align = "J", fill = False)
pdf.cell(1,5,"",ln=1, align="J")

pdf.multi_cell(w=175, h=10, txt = SecondParagraph,
border = 0, align = "J", fill = False)
pdf.cell(1,5,"",ln=1, align="J")

pdf.multi_cell(w=175, h=10, txt = ThirdParagraph,
border = 0, align = "J", fill = False)

#adds space between paragraphs and your signature. Change the second param to effect height 
pdf.cell(1,15,"",ln=1, align="J")

pdf.cell(1,5,Signature,ln=1, align="J")
pdf.cell(1,5,YourName,ln=1, align="J")
pdf.cell(1,5,YourPhone,ln=1, align="J")

pdf.cell(1,5,additionPersonalInformation,ln=1, align="J")



# change this if you want to have a different naming format 
pdfName = YourName+"CoverLetter.pdf"
pdf.output(pdfName)
