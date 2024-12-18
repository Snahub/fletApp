from flet import *

def main(page: Page):

    page.title = 'Telecom Cambodia'
    # Set background color
    page.bgcolor = colors.BLUE_400 # Blue background
    page.vertical_alignment = MainAxisAlignment.CENTER  # Center vertically
    page.horizontal_alignment = CrossAxisAlignment.CENTER 

    # Image widget
    image = Image(
        src="asset\images\logo-tc1.png",
        width=200,        
        height=150,
        fit=ImageFit.CONTAIN  # Fit image nicely
    )
    text = Text(
        value="Welcome to Telecom Cambodia",  
        size=20,                       
        color=colors.WHITE,          
        weight=FontWeight.BOLD,     
    )
    # Place image using Column or Stack layout
    content = Column(
        controls=[
            Container(content=image, padding=10),  # Centered image
            Container(content=text, alignment=alignment.center),   # Centered text
        ],
        alignment=MainAxisAlignment.CENTER,            # Vertically center the content
        horizontal_alignment=CrossAxisAlignment.CENTER # Horizontally center the content
    )
    page.add(content)
    page.update()

app(target=main)
